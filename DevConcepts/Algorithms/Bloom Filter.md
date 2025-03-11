Source: https://en.wikipedia.org/wiki/Bloom_filter

**Bloom filter** is a space-efficient probabilistic data structure.  that is used to test whether an element is a member of a set. Query returns either "possibly in set" or "definitely not in set". Elements can be added to the set, but not removed (though this can be addressed with the counting Bloom filter variant); the more items added, the larger the probability of false positives.

## Space and time advantages

It requires **9.6 bits** to store for each entry in order to get results with about 1% probability of false positive. This might be reduced by a factory of ten, by increasing the number of bits up to 14.4.

the time needed either to add items or to check whether an item is in the set is a fixed constant, **O(k)**, completely independent of the number of items already in the set

## Features
- Lookups are independent and can be parallelized.
- Tiny space usage (14.4 bits for entry)
- Fixed time complexity O(k) *k - number of hash functions*



## Alternatives
- Cuckoo filter - https://en.wikipedia.org/wiki/Cuckoo_filter