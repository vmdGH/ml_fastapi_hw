import pandas as pd
import pickle

def f(x):
    return float(str(x).split(' ')[0])

def open_and_scale(data):
    with open('scaler_data/standard_scaler.pkl', 'rb') as scaler_file:
        loaded_scaler = pickle.load(scaler_file)
    with open('scaler_data/columns_scale.pkl', 'rb') as columns_file:
        loaded_columns = pickle.load(columns_file)
    data[loaded_columns] = pd.DataFrame(loaded_scaler.transform(data[loaded_columns]), columns=loaded_columns)
    return data

def open_and_encode(data):
    with open('encoder_data/one_hot_encoder.pkl', 'rb') as ohe_file:
        loaded_ohe = pickle.load(ohe_file)
    with open('encoder_data/columns_encode.pkl', 'rb') as columns_file:
        loaded_columns = pickle.load(columns_file)
    data_encoded = pd.DataFrame(loaded_ohe.transform(data[loaded_columns]).toarray(), columns=loaded_ohe.get_feature_names_out(loaded_columns))
    result_df = pd.concat([data, data_encoded], axis=1)
    data_encoded = result_df.drop(columns=loaded_columns)
    return data_encoded

def preproces(data):
    data_1 = data.drop(columns=['torque', 'name'])
    data_1.loc[:, 'mileage'] = data_1['mileage'].apply(f)
    data_1.loc[:, 'engine'] = data_1['engine'].apply(f)
    data_1.loc[:, 'max_power'] = data_1['max_power'].apply(f)
    data_1['seats'] = data_1['seats'].astype('int')
    data_1['engine'] = data_1['engine'].astype('int')
    data_scaled = open_and_scale(data_1)
    data_scaled_encoded = open_and_encode(data_scaled)
    return data_scaled_encoded

def fitted_model():
    with open('fitted_model/best_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model
