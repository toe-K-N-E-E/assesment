from app.models import Email
from app.models import RemoteClient
from app.models import SMS
from app.models import commitToDatabase

import json


class RoutesController( object ):

    @staticmethod
    def createNewClient( usernameP ):
        """this will create a new client
        :param usernameP: this is the name of the user
        :return: will return user ID and token
        """
        client_record = RemoteClient.getRemoteClientByUsername( usernameP )

        #check if we have none
        if client_record is None:
            client_record = RemoteClient( usernameP )
            commitToDatabase()

        return json.dumps( { "id":client_record.id, "client_token":client_record.client_token } )
#===========================================end of function definition



    @staticmethod
    def getRemoteClientToken( usernameP ):
        """this will get the client token
        :param usernameP: this is the client username
        :return: will return client token
        """
        client_record = RemoteClient.getRemoteClientByUsername( usernameP )

        #check if we have None
        if client_record is None:
            return json.dumps( { "error":"user not found" } )

        return json.dumps( { "id":client_record.id, "client_token":client_record.client_token } )
#===========================================end of function definition



    @staticmethod
    def createSMS( contact_numberP, message_contentP, client_tokenP ):
        """this will create an SMS
        :param contact_numberP: this is the contact number
        :param message_contentP: this is the message content
        :param client_tokenP: this is the user token
        :return: will return details of sms record
        """
        client_record = RemoteClient.getRemoteClientRecord( client_tokenP )

        #check if we don't have client record
        if client_record is None:
            return json.dumps( { "error":"user not found" } )

        sms = SMS( contact_numberP, client_record.id, message_contentP )

        commitToDatabase()

        return json.dumps( { "id":sms.id, "remote_client_id":sms.remote_client_id, "contact_number":sms.contact_number } )
#===========================================end of function definition



    @staticmethod
    def createEmail( contact_email_addressP, message_contentP, client_tokenP ):
        """this will create a new email
        :param contact_email_addressP: this is the email address of the contact
        :param message_contentP: this is the message content
        :param client_tokenP: this is the user token
        :return: will return details of the email record
        """
        client_record = RemoteClient.getRemoteClientRecord( client_tokenP )

        # check if we dont have client record
        if client_record is None:
            return json.dumps( { "error": "user not found" } )

        email = Email( contact_email_addressP, client_record.id, message_contentP )

        commitToDatabase()

        return json.dumps( { "id":email.id, "remote_client_id":email.remote_client_id, "contact_email_address":email.contact_email_address } )
#===========================================end of function definition



    @staticmethod
    def getMessage( record_idP, client_tokenP, message_typeP ):
        """this will return sent message
        :param record_idP: this is the record id of sms or email
        :param client_tokenP: this is the user token
        :param message_typeP: this is the message type
        :return: will return result
        """
        client_record = RemoteClient.getRemoteClientRecord( client_tokenP )
        record = None
        result_dict = {}

        #check if we have nothing
        if client_record is None:
            return json.dumps( { "error":"user not found" } )

        #check if sms is being requested
        if message_typeP == "sms":
            record = SMS.getRecentlySentSMS( record_idP, client_record.id )

            #check if we have nothing
            if record is None:
                return json.dumps({"error": "no match found"})

            result_dict[ "contact_number" ] = record.contact_number
        #check if email is being requested
        elif message_typeP == "email":
            record = Email.getRecentlySentEmail( record_idP, client_record.id )

            # check if we have nothing
            if record is None:
                return json.dumps({"error": "no match found"})

            result_dict[ "contact_email" ] = record.contact_email_address
        else:
            return json.dumps( { "error":"unknown message type" } )

        result_dict[ "message_content" ] = record.message_content

        return json.dumps( result_dict )
#===========================================end of class definition