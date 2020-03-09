from flask import request
from app import app



@app.route( "/api/submit", methods=[ "POST" ] )
def submit():

    #check if the request contains JSON
    if request.is_json:
        return "test"

    return "hello"



#@app.route('/summary')
#def summary():
 #   data = make_summary()
 #   response = app.response_class(
  #      response=json.dumps(data),
   #     status=200,
    #    mimetype='application/json'
    #)
    #return response