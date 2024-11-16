# General Syntax: list[start:stop:step]
def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Start with the first string as the prefix
    prefix = strs[0]

    # Compare the prefix with each string in the array
    for string in strs[1:]:
        # Shorten the prefix until it matches the start of the current string
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]

        # If the prefix becomes empty, there is no common prefix
        if not prefix:
            return ""

    return prefix


# Example usage:
strings = ["flower", "flow", "flight"]
print(longestCommonPrefix(strings))  # Output: "fl"

strings = ["dog", "racecar", "car"]
print(longestCommonPrefix(strings))  # Output: ""
