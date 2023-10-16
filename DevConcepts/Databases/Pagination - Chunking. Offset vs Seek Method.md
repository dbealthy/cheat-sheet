## Offset Pagination
- Simple
- Requires order by for consistency
- Becomes quite slow with larger offset values, because in order to reach a high offset from a result set, all previous records have to be skipped and counted.
  
### Example
Page 1:
```SQL
SELECT first_name, last_name, score
FROM players`
WHERE game_id = 42
ORDER BY score DESC
LIMIT 10;
```
Page 10 000
```SQL
SELECT first_name, last_name, score
FROM players`
WHERE game_id = 42
ORDER BY score DESC
LIMIT 10
OFFSET 100000;
```
Even if the tuple `(game_id, score)` is indexed, we’ll have to actually traverse the whole index in order to count how many records we’ve already skipped.

## SQL Seek Method or Keyset Pagination

- Much faster. The Seek Method does not skip records before an OFFSET, but it skips records until the last record previously fetched.
- Requires non-ambiguous order by for consistency.

### Example
``` SQL
SELECT player_id, first_name, last_name, score
FROM players
WHERE game_id = 42
-- assuming 15 is Jack Harris's player_id
AND (score, player_id) < (949, 15)
ORDER BY score DESC, player_id DESC
LIMIT 10;
```


> NOTE: If there is no **ORDER BY clause that uniquely identifies each row**. Some rows may get lost when using Seek Method, because our filtering depends on that ordering.

> NOTE: If columns used in ORDER BY clause are nullable be cautious. `NULLS FIRST` and `NULLS LAST` might apply and further complicate the “seek predicate”.

### Performance comparison
RED - Offset Pagination
GREEN - Seek Method Pagination

![[Pasted image 20230927101535.png]]