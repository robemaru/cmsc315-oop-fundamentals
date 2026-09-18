"""
==================================================
UNIT 6 DISCUSSION: Python Dictionaries as
Hash Tables
==================================================

INSTRUCTIONS:
In this activity, I worked with Python dictionaries
to simulate the behavior of a hash table.

I modified the provided starter code to demonstrate
common operations and explain key hash table concepts.

I followed all TODO prompts in the code and kept the
TODO prompts in place. The output clearly documented
what the program did at each step.

Real-world scenario:
The program simulated a restaurant reservation system.
Each reservation ID was used as a key, and the
reservation information was stored as the value.
"""

def main():
    print("==== UNIT 6: DICTIONARIES AS HASH TABLES ====")

    # ============================================================
    # TODO (Student): CREATE A HASH TABLE
    # ============================================================
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how the
    #    dictionary behaves like a hash table.
    # 4. Display the contents of the dictionary.

    reservations = {}

    reservations["R101"] = "Alice - 7:00 PM - Table 4"
    reservations["R102"] = "Brian - 7:30 PM - Table 2"
    reservations["R103"] = "Carlos - 8:00 PM - Table 6"
    reservations["R104"] = "Diana - 8:30 PM - Table 1"
    reservations["R105"] = "Emma - 9:00 PM - Table 5"

    # The dictionary behaved like a hash table because each key
    # was hashed to determine where its value was stored.
    # Keys provided fast average-time access to reservation data.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    print("Reservations after insertion:")
    for key, value in reservations.items():
        print(f"{key}: {value}")

    # ============================================================
    # TODO (Student): LOOKUP OPERATIONS
    # ============================================================
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to
    #    explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # The first lookup used the reservation ID as the key and
    # returned the value associated with that key.
    lookup_one = reservations.get("R102")
    print(f"Lookup R102: {lookup_one}")

    # The second lookup performed the same operation for another
    # existing key and returned its reservation information.
    lookup_two = reservations.get("R104")
    print(f"Lookup R104: {lookup_two}")

    # ============================================================
    # TODO (Student): UPDATE OPERATIONS
    # ============================================================
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when
    #    an existing key is assigned a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print("Before update:")
    print(f"R103: {reservations['R103']}")

    # Assigning a new value to an existing key replaced the
    # previous value while keeping the same key.
    reservations["R103"] = "Carlos - 8:15 PM - Table 8"

    print("After update:")
    print(f"R103: {reservations['R103']}")

    # ============================================================
    # TODO (Student): DELETE OPERATIONS
    # ============================================================
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when
    #    a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("Before deletion:")
    print(reservations)

    # The pop method removed the selected key and its associated
    # value from the dictionary.
    removed_reservation = reservations.pop("R105")

    print(f"Removed R105: {removed_reservation}")
    print("After deletion:")
    print(reservations)

    # ============================================================
    # TODO (Student): EDGE CASES
    # ============================================================
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: A lookup for a missing key returned None when
    # the get() method was used, so the program did not crash.
    missing_lookup = reservations.get("R999")
    print(f"Missing lookup R999: {missing_lookup}")
    print("Explanation: get() safely returned None because R999 did not exist.")

    # Edge case 2: Updating a missing key created a new key-value
    # pair instead of causing an error.
    reservations["R999"] = "Walk-in Guest - 9:30 PM - Table 3"
    print(f"After updating missing key R999: {reservations['R999']}")
    print("Explanation: assigning a value to a new key added that entry.")

    # Edge case 3: Deleting a missing key was handled safely by
    # checking whether the key existed before calling pop().
    missing_key = "R888"
    if missing_key in reservations:
        reservations.pop(missing_key)
        print(f"{missing_key} was deleted.")
    else:
        print(f"Safe delete: {missing_key} was not found, so no deletion occurred.")

    # Edge case 4: An empty dictionary was tested to show that
    # a hash-table-based structure could start with no entries.
    empty_reservations = {}
    print(f"Empty dictionary: {empty_reservations}")
    print("Explanation: an empty dictionary contained no key-value pairs.")

    # Hash table collision explanation:
    # A collision could occur when two keys produced the same
    # hash location. Python dictionaries handled collisions
    # internally, so the program did not need to implement
    # collision resolution manually.

    print("\n=== HASH TABLE SUMMARY ===")
    print("Python dictionaries used keys to retrieve values efficiently.")
    print("Average dictionary lookup, insertion, and deletion were O(1).")
    print("Hash collisions were handled internally by Python.")
    print(f"Final reservation count: {len(reservations)}")


if __name__ == "__main__":
    main()
