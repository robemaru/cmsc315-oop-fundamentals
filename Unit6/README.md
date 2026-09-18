
## Unit 6 Discussion: Dictionaries as Hash Tables

## Overview
This assignment used Python dictionaries to demonstrate hash table behavior. I created a restaurant reservation system in which each reservation ID was used as a key and the reservation information was stored as the value.

## Learning Objectives
The program demonstrated the following concepts:
* Inserting key-value pairs
* Retrieving values using keys
* Updating existing values
* Removing entries
* Testing edge cases
* Understanding hashing and collisions
* Applying a dictionary to a real-world scenario

## Real-World Scenario
I used a restaurant reservation system as the real-world application. Each reservation had a unique reservation ID such as R101 or R102. The reservation ID acted as the dictionary key, while the customer's name, reservation time, and table assignment were stored as the value.

This scenario demonstrated why a hash-table structure was useful. A restaurant could quickly look up a reservation when a customer provided a reservation ID.

## Program Operations

## Insert Operations
I created an empty dictionary and added five reservation key-value pairs. Each reservation ID became a key, and the reservation information became the corresponding value.

The dictionary behaved like a hash table because Python used hashing to determine how keys were stored and retrieved.

## Lookup Operations
I retrieved two existing reservations by using their reservation IDs as keys. The get() method returned the value associated with each key.

Dictionary lookups had an average time complexity of O(1), which made them efficient for retrieving reservation information.

## Update Operations
I updated the reservation associated with R103.

When an existing key received a new value, the previous value was replaced while the key remained in the dictionary.

## Delete Operations
I removed reservation R105 using the pop() method.

The key-value pair was removed from the dictionary, and the remaining reservations stayed available.

## Edge Cases
I tested several edge cases:
* Missing key lookup: Looking up R999 with get() returned None instead of causing a program error.
* Updating a missing key: Assigning a value to R999 created a new key-value pair.
* Deleting a missing key: I checked whether R888 existed before attempting to delete it, so the program handled the missing key safely.
* Empty dictionary: I created an empty dictionary to demonstrate that the structure could contain zero entries.

## Hashing and Collisions
A hash table used a hash function to determine where a key should be stored. A collision occurred when different keys mapped to the same hash location.

Python dictionaries handled collisions internally. The program therefore did not need to manually implement a collision-resolution method.

Collision resolution could affect performance because many collisions could require additional work to locate the correct value. A well-designed hash table minimized collisions and maintained efficient operations.

## Efficiency and Memory
Python dictionary insertion, lookup, and deletion were O(1) on average. This made dictionaries useful when fast access to data was needed.

The dictionary required more memory as more key-value pairs were added. Therefore, memory usage grew with the number of stored reservations.

## Reflection
While completing this assignment, I learned how Python dictionaries could be used to demonstrate the behavior of hash tables. I practiced inserting, looking up, updating, and deleting key-value pairs. I also learned that dictionary keys were hashed so that values could be retrieved efficiently.

One challenge was understanding how to safely handle keys that did not exist. I overcame this by using the get() method for lookups and checking whether a key existed before deleting it. I also tested what happened when a value was assigned to a new key.

Hash tables used hashing to map keys to storage locations. A collision occurred when two keys mapped to the same location. Python handled collision resolution internally. Hash tables improved efficiency because common operations such as lookup, insertion, and deletion had an average time complexity of O(1). As more entries were stored, the dictionary required additional memory.

## GitHub Repository
https://github.com/robemaru/cmsc315-oop-fundamentals/tree/main/Unit6
```

***
