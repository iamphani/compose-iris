import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "False", 1: "True"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "volume": d.volume,
            "difficulty": d.difficulty,
            "time_estimator": d.time_estimator,
            "unique_operators": d.unique_operators,
            "unique_operands":d.unique_operands,
            "total_operators":d.total_operators,
            "total_operands":d.total_operands,
            "is_defect": d.is_defect
        
        }
        for d in data
    ]

    return processed
