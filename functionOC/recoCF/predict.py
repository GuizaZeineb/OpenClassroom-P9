import os
import json
import pickle
import numpy as np
import implicit


def initialize_model():
    workdir = "/Users/zeineb/lab9"
    chemin = workdir + "/files"

    #-----Load sparse_user_item matrix
    with open(os.path.join(chemin,"sparse_user_item.pkl"), "rb") as f:
            loaded_sparse_user_item = pickle.load(f)
    print("loaded_sparse_user_item done")

    #-----Load best model CF
    with open(os.path.join(chemin,"CF_model.pkl"), "rb") as f:
            loaded_model = pickle.load(f)
    print("loaded_model done")

    return loaded_model, loaded_sparse_user_item

#------------------------------
# CREATE USER RECOMMENDATIONS
#------------------------------

def implicit_recommendation(model, sparse_user_item, user_id):
    
    
    # Use the implicit recommender.
    print ("start recommendation dans implicit recommendations")
    recommended = model.recommend(user_id, sparse_user_item)
    implicit_articles = []

    # Get artist names from ids
    for item in recommended:
        idx, score = item
        implicit_articles.append(int(idx)) # cast to int necessary to make it work on json
    
    # to remove duplicated from implicit_articles 
    result = [] 
    [result.append(int(x)) for x in implicit_articles if x not in result]
    
    return result[:5] #implicit_articles[:5] #result[:5]

def predict_reco_CF(userId):
    print("Start predict.py, userId ", userId, type(userId)), 
    model, sparse_user_item = initialize_model()
    return implicit_recommendation(model, sparse_user_item, userId)
