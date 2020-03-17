from random import seed
from random import randint
import datetime

from app import db

seed( 0 )

class RemoteClient( db.Model ):
    """This will hold remote client"""

    __tablename__ = "RemoteClient"
    __table_args__ = {'extend_existing': True}

    #this is table row ID
    id = db.Column( db.Integer, primary_key=True )

    username = db.Column( db.String, index=True, unique=True )

    #this is client token
    client_token = db.Column( db.String, index=True )

    def __init__( self, usernameP ):
        """this is the class constructor
        :param usernameP: this is the token that will identify the client
        """
        self.client_token = self.__generateToken()
        self.username = usernameP
        db.session.add( self )

    def __generateToken( self ):
        """this will generate a token
        :return: randomly generated string
        """
        token_string = ""

        #generate token
        for _ in range(40):
            token_string = token_string + str( randint( 0, 9 ) )

        return token_string

    @staticmethod
    def getRemoteClientRecord( client_tokenP ):
        """this will get a client record based on token
        :param client_tokenP: this is the token of client
        :return: client record will be returned
        """
        return RemoteClient.query.filter_by( client_token=client_tokenP ).first()

    @staticmethod
    def getRemoteClientByUsername( usernameP ):
        """this will get client by username
        :param usernameP: this is client user name
        :return: client record will be returned
        """
        return RemoteClient.query.filter_by( username=usernameP ).first()
#===========================================end of class definition



class SMS( db.Model ):
    """This will hold the sms object"""

    __tablename__ = "SMS"
    __table_args__ = {'extend_existing': True}

    #this is table row ID
    id = db.Column( db.Integer, primary_key=True )

    #this is the contact number with width of 30 to accommodate international numbers
    contact_number = db.Column( db.String, index=True )

    # this is the message id
    message_content = db.Column( db.String )

    #this is the remote client
    remote_client_id = db.Column( db.Integer, db.ForeignKey( "RemoteClient.id" ) )

    # this is the transaction datetime
    transaction_datetime = db.Column( db.DateTime )


    def __init__( self, contact_numberP, remote_client_idP, message_contentP ):
        """this is the class constructor
        :param contact_numberP: this is the number the sms will be sent to
        :param remote_client_idP: this is the remote client that is sending the sms
        :param message_contentP: this is the message content
        """
        self.contact_number = contact_numberP
        self.remote_client_id = remote_client_idP
        self.message_content = message_contentP
        self.transaction_datetime = getCurrentDateTime()

        db.session.add( self )

    @staticmethod
    def getSMSByContactNumber( contact_numberP ):
        """this will get all smses sent to a given number
        :param contact_numberP: this is the contact number
        :return: list of smses will be returned
        """
        return SMS.query.filter_by( contact_number = contact_numberP ).all()

    @staticmethod
    def getSMSByClient( client_idP ):
        """this will get all smses sent by a client
        :param client_idP: this is the client ID
        :return: list of smses will be returned
        """
        return SMS.query.filter_by( remote_client_id = client_idP ).all()

    @staticmethod
    def getSMSByID( sms_idP ):
        """this will get an sms record by ID
        :param sms_idP: this is the ID of the sms
        :return: sms object will be returned
        """
        return SMS.query.filter_by( id = sms_idP ).first()

    @staticmethod
    def getRecentlySentSMS( sms_idP, client_idP ):
        """this will get the recently sent sms
        :param sms_idP: this is the sms id number
        :param client_idP: this is the client token
        :return: will return sms details
        """
        return SMS.query.filter( SMS.id == sms_idP ).filter( SMS.remote_client_id == client_idP ).first()
#===========================================end of class definition



class Email( db.Model ):
    """This class will hold the email object
    """

    __tablename__ = "Email"
    __table_args__ = {'extend_existing': True}

    #this is table row ID
    id = db.Column( db.Integer, primary_key=True )

    #this is the contact email address
    contact_email_address = db.Column( db.String, index=True )

    # this is the message content
    message_content = db.Column(db.String)

    #this is the remote client
    remote_client_id = db.Column( db.Integer, db.ForeignKey( "RemoteClient.id" ) )

    #this is the transaction datetime
    transaction_datetime = db.Column( db.DateTime )


    def __init__( self, contact_email_addressP, remote_client_idP, message_contentP ):
        """this is the class constructor
        :param contact_email_addressP: this is the contact email address
        :param remote_client_idP: this is remote client id
        :param message_contentP: this is the message content
        """
        self.contact_email_address = contact_email_addressP
        self.remote_client_id = remote_client_idP
        self.message_content = message_contentP
        self.transaction_datetime = getCurrentDateTime()

        db.session.add( self )

    @staticmethod
    def getEmailByAddress( email_addressP ):
        """this will get all emails sent to a given address
        :param email_addressP: this is the contact email address
        :return: list of email records will be returned
        """
        return Email.query.filter_by( contact_email_address = email_addressP ).all()

    @staticmethod
    def getEmailByClient( client_idP ):
        """this will get all emails sent by given client
        :param client_idP: this is the Id of the client
        :return: list of email records will be returned
        """
        return Email.query.filter_by( remote_client_id = client_idP ).all()

    @staticmethod
    def getEmailById( email_idP ):
        """this will get email by Id
        :param email_idP: this is the Id of the email record
        :return: email record will be returned
        """
        return Email.query.filter_by( id = email_idP ).first()

    @staticmethod
    def getRecentlySentEmail(email_idP, client_idP):
        """this will get the recently sent email
        :param email_idP: this is the sms id number
        :param client_idP: this is the client token
        :return: will return sms details
        """
        return Email.query.filter(Email.id == email_idP).filter(Email.remote_client_id == client_idP).first()
#===========================================end of class definition



def getCurrentDateTime():
    """This will get the current datetime
    :return: datetime string will be returned
    """
    return datetime.datetime.now()



def commitToDatabase():
    """this function will commit records to database
    :return:
    """
    db.session.commit()




