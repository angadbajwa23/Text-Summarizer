#importing libraries
import pandas as pd
import numpy as np
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import re

#Input data
data="""They become high in calories, high in cholesterol, low in healthy nutrients, high in sodium mineral, high in sugar, starch, unhealthy fat, lack of protein and lack of dietary fibers.
Processed and junk foods are the means of rapid and unhealthy weight gain and negatively impact the whole body throughout the life.
Junk foods tastes good and looks good however do not fulfil the healthy calorie requirement of the body.
It is found according to the Centres for Disease Control and Prevention that Kids and children eating junk food are more prone to the type-2 diabetes.
Eating junk food daily lead us to the nutritional deficiencies in the body because it is lack of essential nutrients, vitamins, iron, minerals and dietary fibers.
It increases risk of cardiovascular diseases because it is rich in saturated fat, sodium and bad cholesterol.
High sodium and bad cholesterol diet increases blood pressure and overloads the heart functioning.
One who like junk food develop more risk to put on extra weight and become fatter and unhealthier.
Junk foods contain high level carbohydrate which spike blood sugar level and make person more lethargic, sleepy and less active and alert.
For instance, foods like French fries, burgers, candy, and cookies, all have high amounts of sugar and fats."""

#Preprocessing

def preprocess(words):
    
    # Word Tokenization
    words=word_tokenize(data)
    
    # Removing special characters
    words= [re.sub('[^a-zA-Z]','',_) for _ in words]
    words= [word for word in words if word!='']
    
    # Eliminating the stopwords
    words=[word for word in words if word not in set(stopwords.words("english"))]
    
    # Lowercase
    words = [word.lower() for word in words]
    
    
    return words




# Creating the Frequency Table

def frequency_table(words):
    
    freq_table={}
    
    for word in words:
        if word in freq_table:
            freq_table[word]+=1
            
        else:
            freq_table[word]=1
            
    return freq_table
        
        

# Sentence Tokenization and sentence value

def sentence_table(data):
    
    sentences = sent_tokenize(data)
    
    sentence_value = {}
    
    for sentence in sentences:
        for word,freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence]+=freq
                else:
                    sentence_value[sentence]= freq

    return sentence_value    




words=preprocess(data)
#print(words) #To print the words in the input data after preprocessing

freq_table=frequency_table(words)

# To print the word frequency table
"""
print("{:<20} {:<20}".format('Word','Frequency'))
for word, freq in freq_table.items():
    print("{:<20} {:<20} ".format(word,freq))
"""

sentence_value = sentence_table(data)
# To print sentence value table
"""
print("{:<10} {:<10}".format('Sentence','-  Frequency'))
for sentence, freq in sentence_value.items():
    print("{:<20} {:<5} ".format(sentence,freq))
"""

# Calculating average score of all the sentences in the input data
total=0
count=0
for sentence,sentence_freq in sentence_value.items():
    total+=sentence_freq
    count+=1

average=total/count
print(average)


# Considering only those sentences which have a score greater than the average score
summary=""
for sentence,sentence_freq in sentence_value.items():
    if sentence_freq>average:
        summary+=" "+sentence   

print(summary)