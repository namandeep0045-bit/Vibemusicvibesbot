# ==============================================================================
# preload.py - Background Track Preload Manager
# ==============================================================================

import asyncio
from pathlib import Path
from typing import Dict, Set

from VibeMusicBot import logger


class PreloadManager:
    """Manages background preloading of upcoming tracks in queue."""
    
    def __init__(self):
        """Initialize the preload manager."""
        self._preload_tasks: Dict[int, Set[asyncio.Task]] = {}
        self._preloading: Dict[int, Set[str]] = {}
    
    async def start_preload(self, chat_id: int, count: int = 2) -> None:
        """Start preloading upcoming tracks for a chat."""
        from VibeMusicBot import queue, yt
        
        upcoming_tracks = queue.peek_next(chat_id, count)
        
        if not upcoming_tracks:
            return
        
        if chat_id not in self._preload_tasks:
            self._preload_tasks[chat_id] = set()
        if chat_id not in self._preloading:
            self._preloading[chat_id] = set()
        
        for track in upcoming_tracks:
            if queue.is_downloaded(track):
                continue
            
            track_id = getattr(track, 'id', None)
            if not track_id or track_id in self._preloading[chat_id]:
                continue
            
            self._preloading[chat_id].add(track_id)
            
            task = asyncio.create_task(self._preload_track(chat_id, track))
            self._preload_tasks[chat_id].add(task)
            
            task.add_done_callback(
                lambda t, cid=chat_id: self._cleanup_task(cid, t)
            )
    
    async def _preload_track(self, chat_id: int, track) -> None:
        """Preload a single track in the background."""
        from VibeMusicBot import yt
        
        try:
            track_id = track.id
            is_live = getattr(track, 'is_live', False)
            
            file_path = await yt.download(
                track_id,
                is_live=is_live,
                video=getattr(track, "video", False),
            )
            
            if file_path:
                track.file_path = file_path
        
        except asyncio.CancelledError:
            raise
        
        except Exception as e:
            logger.error(f"❌ Error preloading track {track.id} for chat {chat_id}: {e}")
        
        finally:
            if chat_id in self._preloading and track.id in self._preloading[chat_id]:
                self._preloading[chat_id].remove(track.id)
    
    async def cancel_preload(self, chat_id: int) -> None:
        """Cancel all active preload tasks for a chat."""
        if chat_id not in self._preload_tasks:
            return
        
        tasks = self._preload_tasks[chat_id].copy()
        
        for task in tasks:
            if not task.done():
                task.cancel()
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        
        self._preload_tasks[chat_id].clear()
        if chat_id in self._preloading:
            self._preloading[chat_id].clear()
    
    def _cleanup_task(self, chat_id: int, task: asyncio.Task) -> None:
        """Clean up completed task from tracking."""
        if chat_id in self._preload_tasks:
            self._preload_tasks[chat_id].discard(task)