class Solution:

  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
  
    char_counts = [0] * 26

    for char in magazine:
      char_counts[ord(char) - ord('a')] += 1

    for char in ransomNote:
      index = ord(char) - ord('a')
      char_counts[index] -= 1

      if char_counts[index] < 0:
        return False

    return True