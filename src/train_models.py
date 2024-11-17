from sklearn.ensemble import RandomForestClassifier
import pickle
def train_model(data):
    model = RandomForestClassifier()
    model.fit(data[['sensor_id', 'value']], data['target'])
    with open('models/predictive_model.pkl', 'wb') as file:
        pickle.dump(model, file)
