from flask import Flask, jsonify
from flask import request
import joblib 
import pandas as pd
import numpy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



def simulate_product(data):
  data_test=[];
  gender=0;
  age=data['age'];
  price=data['price'];
  pre_product=data['previousProduct'];
  sale=0;



  #Convert gender
  if(data['gender']== 'Male'):
    gender=1;
  if(data['sale']=='Yes'):
    sale=1;

  data_row=[gender,age,pre_product,price,sale];
  data_test.append(data_row);
  for x in range(6):
    if(x%2==0):
      age=data['age']+ x*8;
      price=data['price']+ x*5;
      pre_product=data['previousProduct'] +x;
    else:
      pre_product=data['previousProduct'] -x;
      age=data['age']- x*5;
      price=data['price']- x*2;

    data_row=[gender,age,pre_product,price,sale];
    data_test.append(data_row);

  print(data_test)

  return data_test;



# function to get unique values
def unique(list1):
  
    # initialize a null list
    unique_list = []
      
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list;


@app.route('/json-example')
def json_example():
    return 'JSON Object Example'
@app.route('/recomentdations',methods=['GET', 'POST'])
def recomendation_product():

  #samples_to_predict=[[1,22,21,109,1],[1,16,35,50,1]]
  print(request.json)
  samples_to_predict=simulate_product(request.json)
  samples_to_predict.append([1,16,35,50,1]);
  samples_to_predict.append([1,22,21,109,1]);
  #print(type(samples_to_predict))
  value=model_predict.predict(numpy.array(samples_to_predict))
  #print(type(value))
  result=unique(value.tolist());
  return jsonify({'prediction': result});

if __name__ == '__main__':
  model_predict = joblib.load('recomendation_model.sav')
  app.run(host='0.0.0.0', port=5001)