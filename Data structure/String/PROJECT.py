# string_word_counter_project.py
# Author: Sanjog Don
# Description: Simple Word Counter using String Operations

text = input("Enter a sentence:\n").lower().strip()

# Split into words
words = text .split()
total_words = len(words)
unique_words = set(words)
longest_word = max(words, key=len)

print("\n📊 RESULT 📊")
print(f"Total Words: {total_words}")
print(f"Unique Words: {len(unique_words)}")
print(f"Longest Word: {longest_word}")
print("\nWord Frequency:")
for word in unique_words:
    print(f"{word}: {words.count(word)}")
print("\nThank you for using the Word Counter!")