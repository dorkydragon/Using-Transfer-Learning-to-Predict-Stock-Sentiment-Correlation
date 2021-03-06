from pre_processing import Pre_Processing
from textblob import TextBlob                         #You have to download textblob

class TextBlob_Polarity:
     def __init__(self):
    
        self.feature_list=[]            #list of features that will be returned

     def get_feature(self,doc_list):
        
            for doc in doc_list:
                 doc_blob=TextBlob(doc.text)

                 if doc_blob.sentiment.polarity >0.1:       #the textblob object has a function that calculate the positivity or negativity(polarity) of a piece of text
                    self.feature_list.append(1)
                 else:
                    self.feature_list.append(0)
            
            return self.feature_list

     def get_polarity(self, headlines_list):
         headlines = []
         for headline in headlines_list:
             refined = TextBlob(headline)
             polarity = refined.sentiment.polarity
             headlines.append(polarity)
         average = sum(headlines)/len(headlines)
         return average



    



















 