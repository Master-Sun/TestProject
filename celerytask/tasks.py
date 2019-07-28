from celery.task import Task
import time


class TestTask(Task):
    # 任务名，定时任务会用到
    name = "test-task"

    def run(self, *args, **kwargs):
        print("任务开始...")
        print("args=%s, kwargs=%s" % (args, kwargs))
        time.sleep(4)
        print("任务结束...")

# 定时任务
class BeatTask(Task):
    # 任务名
    name = "beat-task"

    def run(self, *args, **kwargs):
        print("任务开始...")
        print("当前时间：", time.time())
        print("任务结束...")
