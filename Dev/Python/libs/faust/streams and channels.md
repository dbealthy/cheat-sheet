Faust agents iterate over streams, and streams iterate over channels.

A channel is a construct used to send and receive messages, then we have the “topic”, which is a named-channel backed by a Kafka topic.

Streams read from channels (either a local-channel or a topic).

`Agent` <–> `Stream` <–> `Channel`

Topics are named-channels backed by a transport (to use e.g. Kafka topics):

`Agent` <–> `Stream` <–> `Topic` <–> `Transport` <–> aiokafka

Faust defines these layers of abstraction so that agents can send and receive messages using more than one type of transport.

Topics are highly Kafka specific, while channels are not. That makes channels more natural to subclass should you require a different means of communication, for example using [RabbitMQ](http://rabbitmq.com/) (AMQP), [Stomp](https://stomp.github.io/), [MQTT](http://mqtt.org/), [NSQ](http://nsq.io/), [ZeroMQ](http://zeromq.org/), etc.
## Channels

A **channel** is a buffer/queue used to send and receive messages. This buffer could exist in-memory in the local process only, or transmit serialized messages over the network.

You can create channels manually and read/write from them:

``` python
async def main():
    channel = app.channel()

    await channel.put(1)

    async for event in channel:
        print(event.value)
        # the channel is infinite so we break after first event
        break
```