``` python 
transfer_counts = app.Table(
    'transfer_counts',
    default=int,
    key_type=str,
    value_type=int,
)
```

*Tables are not accassable by agents other than the one that created the table. So it should be used to store application state*

A table is a **distributed in-memory dictionary**, backed by a Kafka changelog topic used for persistence and fault-tolerance. We can replay the changelog upon network failure and node restarts, allowing us to rebuild the state of the table as it was before the fault.

## Can't modify tables from outside of stream
You cannot modify a table outside of a stream operation; this means that you can only mutate the table from within an `async for event in stream:` block. We require this to align the table’s partitions with the stream’s, and to ensure the source topic partitions are correctly rebalanced to a different worker upon failure, along with any necessary table partitions.

## Changelog
Every modification to a table has a corresponding changelog update, the changelog is used to recover data after a failure.

We store the changelog in Kafka as a topic and use log compaction to only keep the _most recent value for a key in the log_. Kafka periodically compacts the table, to ensure the log does not grow beyond the number of keys in the table.

In production the RocksDB store **allows for almost instantaneous recovery of tables**: a worker only needs to retrieve updates missed since last time the instance was up.


## Concurrency and tables

Concurrent agents are **not allowed to modify tables**: an exception is raised if this is attempted.

They are, however, allowed to read from tables.