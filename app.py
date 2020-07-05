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
	
	features = [float(x) for x in request.form.values()]
	final_feature 	= [np.array(features)]
	prediction 		= model.predict(final_feature)
	if prediction[0] == 1:
		output = "Purchase"
	else:
		output = "Not Purchase"
	return render_template('index.html', output={"output":output,"params":features})

#Main driver function
if __name__ == '__main__':
	app.run(debug=True)
