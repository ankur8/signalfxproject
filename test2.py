from flask import Flask
from flask import jsonify
from flask import json
from flask import request, Response
import requests
#import signalfx
import time
import os
app = Flask(__name__)


@app.route("/process", methods=['POST','GET'])
def process():
	#TOKEN = os.environ['SIGNALFX_API_TOKEN']
	#sfx = signalfx.SignalFx(ingest_endpoint='https://ingest.{REALM}.signalfx.com')
	#ingest = sfx.ingest('ORG_TOKEN')
	
	if request.method == 'GET':
		return "Event send service running fine"
	
	data=request.get_json()
	id=data['id']
	description=data['description']
	sjson={"id":id,"description":description}
	myToken = 'TOKEN'
	myurl='http://localhost:4000/end'
	#myUrl = 'https://ingest.{REALM}.signalfx.com/v2/event'
	#head = {'Content-type': 'application/json','Authorization': 'token {}'.format(myToken)}
	head= {'Content-type': 'application/json'}
	r = requests.post(myurl, json=sjson,headers=head)
	if r.status_code == 200:
		print(r.status_code)
	return (r.text)
	
	


#############(Section-2) To use sinalfx library ################
'''with signalfx.SignalFx(ingest_endpoint='https://ingest.{REALM}.signalfx.com').ingest('PASSEDTOKEN') as sfx:
    sfx.send_event(
        event_type='ec2altert',
	category='USER_DEFINED',
        dimensions={
            'id': id,
            'description': description},
	timestamp=time.time()*1000)
'''
###################################END Section - 2)#######################


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"),debug=True)




