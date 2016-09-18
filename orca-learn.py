from flask import Flask, request, jsonify
import log
import random
import os
app = Flask(__name__)

@app.route('/classify', methods=['GET'])
def classify():
	log.function('classify')
	
	token = request.args['token']
	keywords = request.args['keywords']

	log.info('TOKEN: ' + token)
	log.info('KEYWORDS: ' + keywords)

	# Check for a null token or keyword
	if(not token):
		return jsonify({'message':'No token given'}), 400
	if(not keywords):
		return jsonify({'message':'No keywords given'}), 400


	# Then, See if the token is valid
	if(token != os.environ.APP_TOKEN):
		return jsonify({'message':'Invalid token'}), 401

	# Now we can do the classification
	results = [
		{ '1':80, '2':5, '3':5, '4':5, '5':5 },
		{ '1':5, '2':80, '3':5, '4':5, '5':5 },
		{ '1':5, '2':5, '3':80, '4':5, '5':5 },
		{ '1':5, '2':5, '3':5, '4':80, '5':5 },
		{ '1':5, '2':5, '3':5, '4':5, '5':80 },
	]

	return jsonify(random.choice(results))