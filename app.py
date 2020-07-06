from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home(): 
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	
	
	return 1#render_template('index.html', output={"output":output,"params":features})

#Main driver function
if __name__ == '__main__':
	app.run(debug=True)
