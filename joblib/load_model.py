import joblib

#load a model
loaded_model = joblib.load(open('dib_79.pkl', 'rb'))

pred = loaded_model.predict([[10,20,30,40,50,10,20,10]])

if pred[0] == 1:
    print('the person is diabetic')
else:
    print('the person is not diabetic')