from mf_performance_details import mf_performance
from flask import Flask,jsonify,request
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)


@app.route('/')
def welcome():
    return "Forcaster HomePage"

@app.route('/predict',methods=["Get"])
def popularity_based_recommendation():
    mf_perform=mf_performance()
    return mf_perform.performance_based_recommendation(load_cache=False)

if __name__=='__main__':    
    # print(predict('LUPIN',30))
    app.run(host='0.0.0.0',port=8000)
