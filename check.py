import pickle

with open('models/svc.pkl', 'rb') as model_file:
    svc = pickle.load(model_file)
print("Model loaded successfully!")
