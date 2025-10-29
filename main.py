# 🧠 Your Task: Tokenize the story from 'story.txt' using NLTK's sent_tokenize and word_tokenize functions

# Make sure required NLTK resources are available
import re
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# 1. Open and read the story text
text_file = open("./story.txt")
file_val = text_file.read()


# 2. (Optional) Remove any unwanted characters using re.sub
# For example: remove extra whitespace or punctuation symbols
clean_story = re.sub(r'\s+', " ", file_val).strip()  # Keep common sentence characters

# 3. Tokenize the story into sentences
# TODO: Replace the line below with a call to sent_tokenize
sentences = sent_tokenize(clean_story)
# print(sentences)

# 4. Tokenize the story into words
# TODO: Replace the line below with a call to word_tokenize
words = word_tokenize(clean_story)
# 5. Print results
print("=== Sentences ===")
print(sentences)
print("\n=== Words ===")
print(words)
print(f'Number of Words: {len(words)}')
print(f'Number of Sentences: {len(sentences)}')
