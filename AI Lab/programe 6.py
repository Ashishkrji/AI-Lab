#Python script for tokenizing text data.

import re
text = "Python is easy to learn, and fun to use!"
tokens = re.findall(r'\b\w+\b', text)
print("Tokens:", tokens)
