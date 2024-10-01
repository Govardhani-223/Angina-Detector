from flask import Flask,request
import pickle

with open('model.pkl','rb') as model:
    ai=pickle.load(model)

app = Flask(__name__)

@app.route('/predict',methods=['GET','POST'])
def predict():
    bpm= float(request.args.get('bpm'))
    result = ai.predict([[bpm]])[0]
    return result




if(__name__=="__main__"):
    app.run(host='0.0.0.0',port=2000)