class Solution(object):
    def lengthOfLongestSubstring(self, s):
        characters = []
        result = 0

        for char in s:
            if char in characters:
                duplicate_index = characters.index(char)
                characters = characters[duplicate_index + 1:]

            characters.append(char)
            result = max(result, len(characters))

        return result