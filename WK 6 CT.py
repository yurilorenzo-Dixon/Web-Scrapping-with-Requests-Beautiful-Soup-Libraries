# Import required libraries
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import re

# Download stopwords (only need to run once)
nltk.download('stopwords')

# Step 1: Get the webpage content
url = "https://www.python.org"
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract text from the page
text = soup.get_text(separator=' ')

# Step 4: Clean the text
text = text.lower()
text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation and numbers

# Step 5: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in text.split() if word not in stop_words]

cleaned_text = ' '.join(filtered_words)

# Step 6: Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)

# Step 7: Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud from python.org Webpage", fontsize=14)
plt.show()

# Optional: Save the image
wordcloud.to_file("python_org_wordcloud.png")
