import schedule
import time
import threading

class FileOrganizerScheduler:
    def __init__(self, organizer_instance, folder_path_getter, interval_getter, status_logger):
        self.organizer = organizer_instance
        self.folder_path_getter = folder_path_getter
        self.interval_getter = interval_getter
        self.status_logger = status_logger
        self._job = None
        self._scheduler_thread = None
        self._running = False

    def _organize_job(self):
        folder_path = self.folder_path_getter()
        if folder_path:
            self.status_logger("Running scheduled organization...")
            message, log_entries = self.organizer.organize_folder(folder_path)
            self.status_logger(message)
            for entry in log_entries:
                self.status_logger(entry)
        else:
            self.status_logger("Scheduled organization skipped: No folder selected.")

    def start_scheduler(self):
        self.stop_scheduler()
        interval = self.interval_getter()
        if interval > 0:
            self.status_logger(f"Scheduling organization every {interval} minutes.")
            self._job = schedule.every(interval).minutes.do(self._organize_job)
            self._running = True
            self._scheduler_thread = threading.Thread(target=self._run_schedule)
            self._scheduler_thread.daemon = True
            self._scheduler_thread.start()
        else:
            self.status_logger("Auto-organize is disabled.")

    def stop_scheduler(self):
        if self._running:
            self.status_logger("Stopping existing scheduler...")
            schedule.clear()
            self._running = False
            if self._scheduler_thread and self._scheduler_thread.is_alive():
                # A more robust way to stop the thread might be needed for production
                # For now, clearing schedule and relying on daemon thread exit
                pass
            self._scheduler_thread = None

    def _run_schedule(self):
        while self._running:
            schedule.run_pending()
            time.sleep(1)

    def __del__(self):
        self.stop_scheduler()