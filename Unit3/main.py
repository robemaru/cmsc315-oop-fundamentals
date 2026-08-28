"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # The insert() operation places the value at the requested index.
    # Existing elements at and after the index shift to the right.
    # Inserting near the beginning can require O(n) time because
    # many elements may need to be shifted.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Check that the index is valid before deleting.
    if index < 0 or index >= len(lst):
        return None

    # Save the value before removing it.
    removed_value = lst[index]

    # Deleting an element causes later elements to shift left.
    del lst[index]

    return removed_value


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # A list search is a linear search because elements are checked
    # one at a time from the beginning until the value is found.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # -1 means the requested value was not found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Real-world scenario: a student uses a list to organize course tasks.
    tasks = ["Read chapter", "Complete quiz", "Submit assignment"]

    print("Original list:", tasks)

    # Insert a task at the beginning.
    insert_at(tasks, 0, "Check announcements")
    print("After beginning insertion:", tasks)

    # Insert a task in the middle.
    insert_at(tasks, 2, "Watch lecture")
    print("After middle insertion:", tasks)

    # Insert a task at the end.
    insert_at(tasks, len(tasks), "Review notes")
    print("After end insertion:", tasks)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Delete the first task.
    removed = delete_at(tasks, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", tasks)

    # Delete a task from the middle.
    middle_index = len(tasks) // 2
    removed = delete_at(tasks, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", tasks)

    # Delete the last task.
    removed = delete_at(tasks, len(tasks) - 1)
    print("Removed from end:", removed)
    print("Updated list:", tasks)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a value that still exists in the list.
    search_result = search_value(tasks, "Complete quiz")
    print("Search for 'Complete quiz': index", search_result)

    # Search for a value that does not exist.
    search_result = search_value(tasks, "Study for exam")
    print("Search for 'Study for exam': index", search_result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Try to delete an invalid index.
    invalid_delete = delete_at(tasks, 100)
    print("Delete using invalid index:", invalid_delete)

    # Edge case 2: Search for a value that is not in the list.
    missing_search = search_value(tasks, "Nonexistent task")
    print("Search for missing value:", missing_search)

    # Edge case 3: Insert into an empty list.
    empty_tasks = []
    insert_at(empty_tasks, 0, "New task")
    print("Insert into empty list:", empty_tasks)


if __name__ == "__main__":
    main()
