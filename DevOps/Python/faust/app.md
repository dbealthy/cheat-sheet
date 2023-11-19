### App constructor arguments
- id unique identifier of application. Applications with the same id are considered to be in the same consumer group
- datadir - The directory in which this instance stores the data used by local tables, etc
- tabledir - The directory in which this instance stores local table data
- debug - Use in development to expose sensor information endpoint.
- broker_credentials - Specify the authentication mechanism to use when connecting to the broker.
  SASL Authentication 
  app = faust.App(
    broker_credentials=faust.SASLCredentials(
        username='x',
        password='y',
    ))
- processing_guarantee - The processing guarantee that should be used. Possible values are “at_least_once” (default) and “exactly_once”.
	  Note that by default exactly-once processing requires a cluster of at least three brokers what is the recommended setting for production. For development you can change this, by adjusting broker setting transaction.state.log.replication.factor to the number of brokers you want to use.
	  
- stream_buffer_maxsize - This setting control back pressure to streams and agents reading from streams.
	If set to 4096 (default) this means that an agent can only keep at most 4096 unprocessed items in the stream buffer.
	
	Essentially this will limit the number of messages a stream can “prefetch”.


## @app.agent() 
Define a new stream processor
``` python
@app.agent()
async def myagent(stream):
    """Example agent."""
    async for value in stream:
        print(f'MYAGENT RECEIVED -- {value!r}')
        yield value
```

No topic was passed to the agent decorator, so an anonymous topic will be created for it

## @app.task() 
Define a new support task

``` python
@app.task()
async def mytask():
    print('APP STARTED AND OPERATIONAL')
```

The task will be started when the app starts, by scheduling it as an [`asyncio.Task`](https://docs.python.org/dev/library/asyncio-task.html#asyncio.Task "(in Python v3.13)") on the event loop. It will only be started once the app is fully operational, meaning it has started consuming messages from Kafka.


## @app.timer()
Define a new periodic task
``` python
@app.timer(30.0)
async def my_periodic_task():
    print('THIRTY SECONDS PASSED')
```
Use the timer() decorator to define an asynchronous periodic task that runs every 30.0 seconds:


## @app.page()
Define a new Web View
``` python
@app.page('/path/to/view/')
async def myview(web, request):
    print(f'FOO PARAM: {request.query["foo"]}')
```

## @app.command()
Define a new command-line command
``` python
@app.command()
async def example():
    """This docstring is used as the command help in --help."""
    print('RUNNING EXAMPLE COMMAND')
```

## @app.service()
Define a new service

``` python
import faust
from mode import Service

app = faust.App('service-example')

@app.service
class MyService(Service):

    async def on_start(self):
        print('MYSERVICE IS STARTING')

    async def on_stop(self):
        print('MYSERVICE IS STOPPING')

    @Service.task
    async def _background_task(self):
        while not self.should_stop:
            print('BACKGROUND TASK WAKE UP')
            await self.sleep(1.0)

if __name__ == '__main__':
    app.main()
```

The `service()` decorator adds a custom `mode.Service` class as a dependency of the app.

### What is a Service?

A service is something that can be started and stopped, and Faust is built out of many such services.

The mode library was extracted out of Faust for being generally useful, and Faust uses this library as a dependency.

Examples of classes that are services in Faust include: the App, a stream, an agent, a table, the TableManager, the Conductor, and just about everything that is started and stopped is.

Services can also have background tasks, or execute in an OS thread.

### Concurrency and parallel execution
- Setting agent concurrency sets the number of async agents running within the same processing instance. But it applies a restriction to tables so that they can't be modified in a stream processed in async manner.
- Running multiple worker instances and setting multiple topic partitions allows for actual parallelization and auto scaling capabilities. Upscaling for sure and downscaling not sure.



### Terms
- “agent” – A named group of actors processing a stream.
- “actor” – An individual agent instance.

