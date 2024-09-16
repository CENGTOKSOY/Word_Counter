import pandas as pd
import re

file_path = 'excel_file.xlsx'
df = pd.read_excel(file_path)

captions = df['G'][1:961]
all_words = []
for caption in captions:

    words = re.findall(r'\b\w+\b', str(caption).lower())
    all_words.extend(words)


unique_words = set(all_words)
unique_word_count = len(unique_words)

print(f"Different word count: {unique_word_count} ")