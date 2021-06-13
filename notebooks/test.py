import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
model = joblib.load(open('rf.pkl', 'rb'))
data = pd.read_csv('/home/arun/Documents/mlwebapp/data/digit-recognizer/train.csv')


X = data.drop('label',axis=1)
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
                                                random_state=1)

x = X_train.to_numpy()

x1 = x[45]



topred = np.array(x1)[np.newaxis, :] 

pred = model.predict(topred)

print("prediction ",  str(pred[0]))