import json
import requests


class RequestMenu( object ):

    __host_url = host_url = "http://127.0.0.1:5000"                     #change this is server URL

    #this is the authorization endpoint
    __authorize_endpoint = "/api/authorize"

    #this is the user create endpoint
    __user_create_endpoint = "/api/NewUser"

    #this is the submit endpoint
    __submit_endpoint = "/api/submit"

    #this endpoint will return the message
    __get_message_endpoint = "/api/message"

    #this is client token
    __client_token = None

    #this is the username
    __username = ""

    #this sill hold the most recently sent message ID
    __last_sent_id = ""

    #this is the last send message type
    __last_sent_type = ""

    @staticmethod
    def authorize( usernameP ):
        """the function will authorize a user
        :param usernameP: this is the username
        :return: will return the new data
        """
        request_data = { "username":usernameP }
        json_response = RequestMenu.__executeRequest( request_data, RequestMenu.__authorize_endpoint )

        RequestMenu.__username = usernameP
        RequestMenu.__client_token = json_response[ "client_token" ]

        print( "Authorized\n" )
    #=======================================end of function definition



    @staticmethod
    def createNewUser( usernameP ):
        """this function will create a new user
        :param usernameP: this is the username of user
        :return: will return the new user data
        """
        request_data = { "username": usernameP }
        json_response = RequestMenu.__executeRequest( request_data, RequestMenu.__user_create_endpoint )

        RequestMenu.__username = usernameP
        RequestMenu.__client_token = json_response[ "client_token" ]

        print( "User Created\n" )
    #=======================================end of function definition



    @staticmethod
    def sendMessage( contactP, contentP, message_typeP ):
        """this function will submit email or sms message
        :param contactP: this is the email address or sms number
        :param contentP: this is the email or sms content
        :param message_typeP: this is the message type( can be sms or email )
        """
        #check if user is not authorized
        if RequestMenu.__client_token is None:
            print( "Authorization Required" )
            return

        #this is our request data
        request_data = { "token":RequestMenu.__client_token,
                         "type":message_typeP,
                         "message":contentP }

        #check if we have sms
        if message_typeP == "sms":
            request_data[ "contact_number" ] = contactP
        #check if we have email
        elif message_typeP == "email":
            request_data[ "contact_email" ] = contactP
        else:
            print(  "ERROR: Invalid message type --- can only be sms or email")
            return

        json_response = RequestMenu.__executeRequest( request_data, RequestMenu.__submit_endpoint )
        RequestMenu.__last_sent_id = json_response["id"]
        RequestMenu.__last_sent_type = message_typeP

        print( "Message Sent\n" )
    #=======================================end of function definition



    @staticmethod
    def getRecentMessageDetails():
        """this will get the recently sent message
        :return: N/A
        """

        # check if user is not authorized
        if RequestMenu.__client_token is None:
            print("Authorization Required")
            return

        request_data = { "token":RequestMenu.__client_token,
                         "type":RequestMenu.__last_sent_type }

        json_response = RequestMenu.__executeRequest( request_data, RequestMenu.__get_message_endpoint + "/" + str( RequestMenu.__last_sent_id ) )

        print( "====================" )

        #check if we have email type
        if RequestMenu.__last_sent_type == "email":
            print( "Email Address: " + json_response[ "contact_email" ] )
        #check if we have contact number
        elif RequestMenu.__last_sent_type == "sms":
            print( "Contact Number: " + json_response[ "contact_number" ] )

        print( "Message Content: " + json_response[ "message_content" ] + "\n" )
    #=======================================end of function definition



    @staticmethod
    def __executeRequest( request_dataP, api_endpointP):
        """this will create the request data
        :param request_dataP: this is the data we are sending
        :param api_endpointP: this is the api endpoint
        :return: json data will be returned
        """
        response = requests.post(RequestMenu.__host_url + api_endpointP, data=json.dumps( request_dataP ), headers={"content-type": "application/json"})
        return response.json()
    #=======================================end of function definition





