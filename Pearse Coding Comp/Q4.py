def Solution():
    # We will use a for loop to handle up to 20 pairs of words
    for _ in range(20):
        word1, word2 = input().split()

        # Find the shortest word length to compare
        min_len = min(len(word1), len(word2))

        # Check each character position
        for i in range(min_len):
            if word1[i] != word2[i]:
                # Output the first mismatched characters
                print(word1[i], word2[i])
                return

        # If the words match for the minimum length, check for extra characters
        if len(word1) < len(word2):
            print("_", word2[min_len])  # Missing character in word1
            return
        elif len(word1) > len(word2):
            print(word1[min_len], "_")  # Missing character in word2
            return

Solution()