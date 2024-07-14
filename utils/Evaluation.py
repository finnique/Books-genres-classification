import random
import pandas as pd

# Evaluation for multi-class classification
genre_list = ['fantasy', 'thriller', 'science', 'history', 'horror', 'crime', 'romance', 'psychology', 'sports', 'travel']

# generate random predictions
def random_pred(labels, genre_list):
    # randomly assign elements from list as predictions
    pred = [random.choice(genre_list) for label in range(len(labels))]
    
    return pred

'''
FUNCTION: count_pred()
input: 
    labels: gold labels
    pred: predictions
    genre_list: list of all genre in dataset
output: 
    count_pred_dict: return TP, FP, FN for each class as a nested dictionary
'''
def count_pred(labels, pred, genre_list):
    count_pred_dict = {}

    # calculate precision for each genre
    for genre in genre_list:
        # initialize counters
        TP = 0
        FP = 0
        FN = 0
        # initialized inner dict
        temp_dict = {}

        # counting
        for x, y in zip(labels, pred):
           if x == genre and x == y:
               TP += 1
           if y == genre and x != y:
               FP += 1
           if x == genre and y != x:
               FN += 1

        # create temp_dict based on counts of each genre
        temp_dict.update({"TP" : TP, "FP" : FP, "FN" : FN})
        # update count_pred_dict
        count_pred_dict.update({ genre : temp_dict})

    return count_pred_dict

def precision_byclass(count_pred_dict):
# precision = TP (class A) / TP (class A) + FP (class A)
    precision_class = {}

    for key in count_pred_dict.keys():
        # retrieve counts for each genre
        TP = count_pred_dict[key]["TP"]
        FP = count_pred_dict[key]["FP"]

        # calculate precision for each genre
        if TP + FP == 0:
            precision = None
        else:
            precision = round(TP / (TP + FP), 2)

        # update dict
        precision_class.update({key : precision})

    return precision_class

def recall_byclass(count_pred_dict):
 # recall = TP (class A) / TP (class A) + FN (class A)
    recall_class = {}

    for key in count_pred_dict.keys():
        # retrieve counts for each genre
        TP = count_pred_dict[key]["TP"]
        FN = count_pred_dict[key]["FN"]

        # calculate precision for each genre
        if TP + FN == 0:
            recall = None
        else:
            recall = round(TP / (TP + FN), 2)

        # update dict
        recall_class.update({key : recall})
        
    return recall_class

def f1_byclass(precision_class, recall_class):
    f1_class = {}

    for key in recall_class.keys():
        recall = recall_class[key]
        precision = precision_class[key]
        f1_score = (2 * precision * recall) / (precision + recall)

        # update dict
        f1_class.update({key : round(f1_score, 2)})
    
        
    return f1_class  


# loading data
# df = pd.read_csv("data/data.csv")

# # loading labels
# labels = df["genre"]

# print(len(labels))

# labels = ['fantasy', 'fantasy', 'fantasy', 'thriller', 'science', 'history', 'horror']
# pred = ['fantasy', 'fantasy', 'fantasy', 'fantasy', 'fantasy', 'fantasy', 'fantasy']

# print(count_pred(labels, labels, genre_list))

# counts = count_pred(labels, random_pred(labels, genre_list), genre_list)

# pre = precision_byclass(counts)
# rec = recall_byclass(counts)
# f1 = f1_byclass(pre, rec)

# print(pre)
# print(rec)
# print(f1)


