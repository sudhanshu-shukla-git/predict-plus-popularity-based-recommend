from mf_performance_details import mf_performance
from mf_popularity_details import mf_popularity
from user_content_based_mf import content_based_recommend
from user_scoring_model import user_score
from flask import Flask,jsonify,request
# from flasgger import Swagger

app=Flask(__name__)
# Swagger(app)


@app.route('/')
def welcome():
    return "Predict Plus Mutual Fund Recommender"

@app.route('/performance_based',methods=["Get"])
def performace_based_recommendation():
    
    mf_category=request.args.get("mf_category")
    mf_sub_category=request.args.get("mf_sub_category")
    risk=request.args.get("risk")
    top_n=int(request.args.get("top_n"))
    load_cache=bool(request.args.get("load_cache"))
    
    mf_perform=mf_performance()
    return mf_perform.performance_based_recommendation(mf_category,mf_sub_category,risk,top_n,load_cache)

@app.route('/popularity_based',methods=["GET"])
def popularity_based_recommendation():
    
    mf_category=request.args.get("mf_category")
    mf_sub_category=request.args.get("mf_sub_category")
    risk=request.args.get("risk")
    if request.args.get("top_n") is not None:
        top_n=int(request.args.get("top_n"))
    else :
        top_n=5
    load_cache=bool(request.args.get("load_cache"))

    print(mf_category,mf_sub_category,risk,top_n,load_cache)

    mf_popular=mf_popularity()
    return mf_popular.performance_based_recommendation(mf_category)


@app.route('/user_score', methods=['POST'])
def user_score_details():
  data = request.get_json()
  
  score=user_score()
  return score.get_scoring_result(data)


@app.route('/content_based', methods=['POST'])
def content_based_mf_recommend():
  data = request.get_json()
  
  content_recommend=content_based_recommend()
  return content_recommend.content_based_recommendation(data)


if __name__=='__main__':    
    app.run(host='0.0.0.0',port=8000,debug=False)
