from app import db




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