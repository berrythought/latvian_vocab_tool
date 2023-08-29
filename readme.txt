To use:

1. Enter text in Latvian in the file 'enter_text.txt'
2. Run the code in vocab_tool_v3. This will output the formatted text and a graph to show how reading comprehension is changing over time.
3. The text will be outputted in a word document called 'output'. Any 'new' words that appear in the text for the first time will be highlighted in bold. 
4. The CSVs will save the results of the searches from Letonika, so that it won't be necessary to search it again if the same word appears some time in a future text. It is recommended not to touch these files.

Potential improvements:
1. The code will struggle with certain letters that are not found in the Latvian/English alphabet. This should be easy to fix.
2. Certain words considered 'base words' by Letonika are not generally given their own entries in a dictionary. e.g. 'likdams' is shown as a separate base word to 'likt', but these are not worth learning separately. 