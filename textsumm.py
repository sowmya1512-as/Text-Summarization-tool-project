import re

# Input text
text = """Artificial Intelligence is transforming the world. 
It is used in healthcare, education, and finance. 
AI helps automate tasks and improves efficiency. 
However, there are concerns about job loss and ethics. 
AI continues to grow rapidly in many industries."""

print("🔹 Original Text:\n")
print(text)

# Step 1: Split into sentences
sentences = re.split(r'[.!?]', text)

# Step 2: Word frequency
word_freq = {}
for word in text.lower().split():
    word = re.sub(r'[^\w]', '', word)
    if word != "":
        word_freq[word] = word_freq.get(word, 0) + 1

# Step 3: Score sentences
sentence_scores = {}
for sentence in sentences:
    for word in sentence.lower().split():
        word = re.sub(r'[^\w]', '', word)
        if word in word_freq:
            sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

# Step 4: Get top 2 sentences
summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

# Step 5: Print summary
print("\n🔹 Summary:\n")
for s in summary_sentences:
    print(s.strip())
