### collections.Counter(list) 
- returns a dict where key is a element of the list and value is the number of occurancies in the list.

Methods:
.most_common(number) - returns number of most common items



### collections.OrderedDict
Preserves the order the keys were inserted.
- If value changes by key. The position remains the same
- Deletion and re-insertion will put the value to the back of OrderedDict
- Often used for cache implementations
