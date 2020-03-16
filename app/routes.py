from flask import make_response
from flask import request

from app import app
from app.Controllers.routes_controller import RoutesController


@app.route( "/api/authorize", methods=[ "POST" ] )
def authorize():
    """this will authorize user ---> not implemented, will just return a random token
    :return: will return user token
    """
    response = None

    #check if we have request that contains JSON
    if request.is_json:
        content = request.json

        response_data = RoutesController.getRemoteClientToken( content[ "username" ] )

        #check if we have an error
        if "error" in response_data:
            response = make_response( response_data, 404 )
        else:
            response = make_response( response_data, 200 )
    else:
        response = make_response( { "error":"Only JSON supported" }, 400 )

    return response
#===========================================end of function definition



@app.route( "/api/NewUser", methods=[ "POST" ] )
def createNewUser():
    """This function will create a new user
    :return: will return new user details
    """
    response = None

    #check if we have request that contains JSON
    if request.is_json:
        content = request.json
        return make_response( RoutesController.createNewClient( content[ "username" ] ), 200 )

    return make_response( { "error":"Only JSON supported" }, 400 )
#===========================================end of function definition



@app.route( "/api/submit", methods=[ "POST" ] )
def submit():
    """this will submit message, the  message can be either email of sms
    :return:
    """
    response = None
    response_data = None

    #check if the request contains JSON
    if request.is_json:
        content = request.json
        client_token = content[ "token" ];
        message = content[ "message" ]

        #check if we have sms request
        if str.lower( content[ "type" ] ) == "sms":
            response_data = RoutesController.createSMS( content["contact_number"], message, client_token )
        #check if we have email
        elif str.lower( content[ "type" ] ) == "email":
            response_data = RoutesController.createEmail( content[ "contact_email" ], message, client_token )
        else:
            return make_response( { "error":"message type not supported" }, 404 )

        #check if we have an error
        if "error" in response_data:
            return make_response( response_data, 404 )
    else:
        return make_response( { "error": "Only JSON is supported" }, 400 )

    return make_response( response_data, 200 )
#===========================================end of function definition



@app.route( "/api/message/<message_id>", methods=[ "POST" ] )
def getMessage( message_id ):
    response = None

    #check if the request contains json
    if request.is_json:
        content = request.json
        client_token = content[ "token" ]
        message_type = content[ "type" ]

        return make_response( RoutesController.getMessage( message_id, client_token, message_type ), 200 )
#===========================================end of function definition
