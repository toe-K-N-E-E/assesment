import datetime
from app import db



class TransactionEmail( db.Model ):
    """This will be a single email transaction"""

    #this is the transaction ID
    id = db.Column( db.Integer, primary_key=True )

    #this is the client token
    client_token = db.Column( db.String, index=True )

    #this is the email address
    email_address = db.Column( db.String  )

    #this is the transaction datetime
    transaction_datetime = db.Column( db.DateTime )

    def __init__( self, client_tokenP, email_addressP ):
        """class constructor that will add timestamp
        :param client_tokenP:
        :param email_addressP:
        """
        self.client_token =client_tokenP
        self.email_address = email_addressP
        self.transaction_datetime = getCurrentDateTime()




class TransactionSMS( db.Model ):
    """This will be a single sms transaction"""

    #this is the transaction ID
    id = db.Column( db.Integer, primary_key=True )

    #this is the client token
    client_token = db.Column( db.String, index=True )

    #this is the contact number
    contact_number = db.Column( db.String )

    #this is the transaction datetime
    transaction_datetime = db.Column( db.DateTime )

    def __init__( self, client_tokenP, contact_numberP ):
        """class constructor that will add timestamp
        :param client_tokenP: this is the client ID
        :param contact_numberP: this is the cell number sms will be sent to
        """
        self.client_token =client_tokenP
        self.contact_number = contact_numberP
        self.transaction_datetime = getCurrentDateTime()




class RemoteClient( db.Model ):
    """This will hold remote client"""

    #this is table row ID
    id = db.Column( db.Integer, primary_key=True )

    #this is client token
    client_token = db.Column( db.String, index=True )




class SMS( db.Model ):
    """This will hold the sms object"""

    #this is table row ID
    id = db.Column( db.Integer, primary_key=True )

    #this is the contact number with width of 30 to accommodate international numbers
    contact_number = db.Column( db.String, index=True )

    #this is the message id
    message_id = db.Column( db.Integer, db.ForeignKey( "message.id" ), unique=True )




class Email( db.Model ):
    """This class will hold the email object
    """

    #this is table row ID
    id = db.Column( db.Integer, primary_key=True )

    #this is the contact email address
    contact_email_address = db.Column( db.String, index=True )

    #this is the message id
    message_id = db.Column( db.Integer, db.ForeignKey( "message.id" ), unique=True )




class Message( db.Model ):
    """This class will hold the message content for both SMS and Email messages
    """

    id = db.Column( db.Integer, primary_key=True )

    #this is the message content
    content = db.Column( db.String )




def getCurrentDateTime():
    """This will get the current datetime
    :return: datetime string will be returned
    """
    now = datetime.now()
    return now.strftime( "%d/%m/%Y %H:%M:%S" )

