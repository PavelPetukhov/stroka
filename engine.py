import time
import threading
import queue

from molva.common import stroka_logging

class Engine:
    def __init__(self, cfg):
        self.cfg = cfg
        self.is_active = True

        self.user_active_commands = queue.Queue()
        self.logger = stroka_logging.getLogger()

    def _run_user_command(self):
        while True:
            while not self.user_active_commands.empty():
                print(self.user_active_commands.get())
                time.sleep(2)

    def _get_user_command(self):
        while True:
            user_cmd = input()
            self.user_active_commands.put(user_cmd)

    def run(self):
        self.logger.info("Engine started")
        t1 = threading.Thread(target=self._run_user_command)
        t2 = threading.Thread(target=self._get_user_command)
        t1.start()
        t2.start()
