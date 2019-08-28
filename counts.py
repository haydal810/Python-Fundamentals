def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("And") == 3, "Not True"
assert count_upper_case("AAd") == 2, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"

print("All the tests passed")