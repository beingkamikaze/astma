import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
class WordCloudGeneration:
 def preprocessing(self, data):
 # convert all words to lowercase
 data = [item.lower() for item in data]
 # load the stop_words of english
 stop_words = set(stopwords.words('english'))
 # concatenate all the data with spaces.
 paragraph = ' '.join(data)
 # tokenize the paragraph using the inbuilt tokenizer
 word_tokens = word_tokenize(paragraph) 
 # filter words present in stopwords list 
 preprocessed_data = ' '.join([word for word in word_tokens if not word in stop_words])
 print("\n Preprocessed Data: " ,preprocessed_data)
 return preprocessed_data
 def create_word_cloud(self, final_data):
 # initiate WordCloud object with parameters width, height, maximum font size and background 
color
 # call the generate method of WordCloud class to generate an image
 wordcloud = WordCloud(width=1600, height=800, max_font_size=200, 
background_color="black").generate(final_data)
 # plt the image generated by WordCloud class
 plt.figure(figsize=(12,10))
 plt.imshow(wordcloud)
 plt.axis("off")
 plt.show()
wordcloud_generator = WordCloudGeneration()
# you may uncomment the following line to use custom input
# input_text = input("Enter the text here: ")
input_text = 'These datasets are used for machine-learning research and have been cited in peerreviewed academic journals. Datasets are an integral part of the field of machine learning. Major 
advances in this field can result from advances in learning algorithms (such as deep learning), 
computer hardware, and, less-intuitively, the availability of high-quality training datasets.[1] Highquality labeled training datasets for supervised and semi-supervised machine learning algorithms are 
usually difficult and expensive to produce because of the large amount of time needed to label the 
data. Although they do not need to be labeled, high-quality datasets for unsupervised learning can 
also be difficult and costly to produce.'
input_text = input_text.split('.')
clean_data = wordcloud_generator.preprocessing(input_text)
wordcloud_generator.create_word_cloud(clean_data)
