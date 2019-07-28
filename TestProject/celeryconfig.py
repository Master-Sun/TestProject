from datetime import timedelta

import djcelery
djcelery.setup_loader()

BROKER_BACKEND = "redis"
BROKER_URL = 'redis://119.3.4.159:6379/1'
CELERY_RESULT_BACKEND = 'redis://119.3.4.159:6379/2'

# 设置任务队列，区分不同的任务类型
CELERY_QUEUES = {
    "beat_tasks": {
        "exchange": "beat_tasks",
        "exchange_type": "direct",
        "binding_key": "beat_tasks",
    },
    "work_queue": {
        "exchange": "work_queue",
        "exchange_type": "direct",
        "binding_key": "work_queue",
    },

}

# 指定默认使用的任务队列
CELERY_DEFAULT_QUEUE = "work_queue"

# 注册任务：对应celerytask应用下的tasks文件中的类
CELERY_IMPORTS = (
    "celerytask.tasks",
)

# 有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发的worker数量
CELERYD_CONCURRENCY = 4

# 任务失败时允许重试
CELERY_ACKS_LATE = True

# 设置每个worker最多执行100个任务，之后会被销毁，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大运行时间，超时时会被终止
CELERYD_TASK_TIME_LIMIT = 12 * 30

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'beat-task',
        'schedule': timedelta(seconds=5),
        # 'args': (2, 6),
        'options': {    # 设置使用的任务队列
            'queue': 'beat_tasks',
        }
    }
}
