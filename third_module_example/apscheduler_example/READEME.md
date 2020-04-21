# APScheduler框架

[参考链接](https://mp.weixin.qq.com/s/LkLErqNgZEtMg2D1YiJMZQ)

## 一、APScheduler简介
APScheduler（Advanced Python Scheduler）是一个轻量级的Python定时任务调度框架（Python库）。APScheduler有三个内置的调度系统，其中包括：
- cron式调度（可选开始/结束时间）
- 基于间隔的执行（以偶数间隔运行作业，也可以选择开始/结束时间）
- 一次性延迟执行任务（在指定的日期/时间内运行作业一次）

### 支持的后端存储作业

APScheduler可以任意混合和匹配调度系统和作业存储的后端，其中支持后端存储作业包括：

- Memory
- SQLAlchemy
- MongoDB
- Redis
- RethinkDB
- ZooKeeper

### 集成的Python框架

APScheduler内继承了几个常见的Python框架：

- asyncio
- gevent
- tornado
- qt

## 三、APScheduler组件

APScheduler共有4种组件，分别是：

- 触发器（trigger），触发器中包含调度逻辑，每个作业都有自己的触发器来决定下次运行时间。除了它们自己初始配置以外，触发器完全是无状态的。
- 作业存储器（job store），存储被调度的作业，默认的作业存储器只是简单地把作业保存在内存中，其他的作业存储器则是将作业保存在数据库中，当作业被保存在一个持久化的作业存储器中的时候，该作业的数据会被序列化，并在加载时被反序列化，需要说明的是，作业存储器不能共享调度器。
- 执行器（executor），处理作业的运行，通常通过在作业中提交指定的可调用对象到一个线程或者进程池来进行，当作业完成时，执行器会将通知调度器。
- 调度器（scheduler），配置作业存储器和执行器可以在调度器中完成。例如添加、修改、移除作业，根据不同的应用场景，可以选择不同的调度器，可选的将在下一小节展示。

### 各组件简介

#### 调度器

- BlockingScheduler : 当调度器是你应用中唯一要运行的东西时。
- BackgroundScheduler : 当你没有运行任何其他框架并希望调度器在你应用的后台执行时使用（充电桩即使用此种方式）。
- AsyncIOScheduler : 当你的程序使用了asyncio（一个异步框架）的时候使用。
- GeventScheduler : 当你的程序使用了gevent（高性能的Python并发框架）的时候使用。
- TornadoScheduler : 当你的程序基于Tornado（一个web框架）的时候使用。
- TwistedScheduler : 当你的程序使用了Twisted（一个异步框架）的时候使用
- QtScheduler : 如果你的应用是一个Qt应用的时候可以使用。

#### 作业存储器

如果你的应用在每次启动的时候都会重新创建作业，那么使用默认的作业存储器（MemoryJobStore）即可，但是如果你需要在调度器重启或者应用程序奔溃的情况下任然保留作业，你应该根据你的应用环境来选择具体的作业存储器。例如：使用Mongo或者SQLAlchemy JobStore （用于支持大多数RDBMS）

#### 执行器

对执行器的选择取决于你使用上面哪些框架，大多数情况下，使用默认的ThreadPoolExecutor已经能够满足需求。如果你的应用涉及到CPU密集型操作，你可以考虑使用ProcessPoolExecutor来使用更多的CPU核心。你也可以同时使用两者，将ProcessPoolExecutor作为第二执行器。

#### 触发器

当你调度作业的时候，你需要为这个作业选择一个触发器，用来描述这个作业何时被触发，APScheduler有三种内置的触发器类型：

- date 一次性指定日期
- interval 在某个时间范围内间隔多长时间执行一次
- cron 和Linux crontab格式兼容，最为强大

## 四、使用
当你需要调度作业的时候，你需要为这个作业选择一个触发器，用来描述该作业将在何时被触发，APScheduler有3中内置的触发器类型：

- 新建一个调度器（scheduler）
- 添加一个调度任务（job store)
- 运行调度任务

### 添加任务

有两种方式可以添加一个新的作业：

- add_job来添加作业
- 装饰器模式添加作业

#### 指定时间执行任务，只执行一次

```python
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def job2(text):
    print('job2', datetime.datetime.now(), text)
scheduler = BlockingScheduler()
scheduler.add_job(job2, 'date', run_date=datetime.datetime(2020, 2, 25, 19, 5, 6), args=['text'], id='job2')
scheduler.start()
```
