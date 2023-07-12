import nltk
from textblob import TextBlob


def analyze(inpt):
    # insert user input to a text variable and replace sentence

    blob1 = TextBlob(str(inpt))#"Random jumble. with punctuation and spaces . hate words and love words.")

    my_list = []
    my_list2 = []

    # stores polarity and subjectivity of each sentence in a list

    for sentence in blob1.sentences:
        my_list.append(sentence.sentiment.polarity)
        my_list2.append(sentence.sentiment.subjectivity)


    x = my_list
    y = my_list2

    average_x = round(sum(x)/len(x) * 100, 2)
    average_y = round(sum(y)/len(y) * 100, 2)
    indicator = "Positive"
    meme = average_x

    if (average_x < 0):
        indicator = "Negative"
        meme = meme * -1


    return average_x, average_y, indicator, meme


# example blob for testing
# output = polarity = -0.8 and subjectivity = 0.9

#blob2 = TextBlob("I hate Donald Trump")

#print(format(blob2.sentiment))

