import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import defaultdict

nltk.download('stopwords')

stopwords = set(stopwords.words('english'))

ps = PorterStemmer()

with open('wikipedia.xml', 'r', encoding='utf-8') as file:
    data = file.read()


pages = re.findall(r'<page>(.*?)</page>', data, re.DOTALL)

