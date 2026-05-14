import joblib 

def func_joblib(model): 
    model= joblib.dump(model,"model.joblib")
    return model 
