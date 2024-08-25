import pandas as pd
import joblib

pickle_file_path = 'modelo/predicao_surprise.pkl'
pipeline = joblib.load(pickle_file_path)

def predict(df):
    ''' Recebe um dataframe com as respostas'''
    result = pipeline.predict_proba(df)
    top_indices  = result[0].argsort()[-5:][::-1]
    produtos_recomendados = pipeline.classes_[top_indices]
    return produtos_recomendados
