##Note
1. I did not manage to implement the client due to time constraints and loadshedding
2. Having worked mostly on cloud platforms and worked in a place where authentication was already implemented, I havent implemented authentication. But can learn how to do that
3. For now the token will be placed inside the request body

FLASK_APP=microblog.py

##setup
1. install python 3.8 ( install pycharm as this was written and tested on pycharm )
2. ensure venv is active
3. install flask ( pip install flask )
4. install flask SQLAlchemy ( pip install flask-sqlalchemy )
5. install flask Migrate ( pip install flask-migrate )
6. this app will run using SQLite by defualt, in the file "app/__init__.py" comment out the SQLite "SQLALCHEMY_DATABASE_URI" and uncomment
   the MYSQL "SQLALCHEMY_DATABASE_URI"
7. export "FLASK_APP=main.py" on linux or "set FLASK_APP=main.py" on windows 
7. run the migration script( flask db migrate )
8. apply changes to database( flask db upgrade )
9. run using Flask server ( flask run )

#API
1. /api/authorize:

    -Post
    
    -Body:
        
        { "username":"john@vmail.me" }
    
    -Response:
        
        { "id":client_record.id, "client_token":client_record.client_token }
    
    -description:
        
        This end point will return a token to the client when a username is given. Have'nt implemented Authentication as 
        cloud platforms handle this part, but can learn how to do it. In this case when a new username is sent to this endpoint
        a new client record is added to the database and a token is generated and returned to the client, client must save the token
        for later requests
        
2. /api/submit
    
    -Post
    
    -Body( SMS ):
        
        { "token":client_token, "type":"sms", "message":"some message", "contact_number":"0821234567"}
        
    -Body( Email ):
        
        { "token":client_token, "type":"email", "message":"some message", "contact_email":"my@mail.com"}
        
    -Response( SMS ):
        
        { "id":sms.id, "remote_client_id":sms.remote_client_id, "contact_number":sms.contact_number }
        
    -Response( Email ):
        
        { "id":email.id, "remote_client_id":email.remote_client_id, "contact_email_address":email.contact_email_address }
     
    -description
        
        This will create either an email or sms record, it will also relate the client that requested the sms or email 
        
3. /api/message/<id>
    
    -Post
    
    -Body( SMS ):
    
        { "token":client_token, "type":"sms" }
        
    -Body( Email ):
        
        { "token":client_token, "type":"email" }
        
    -Response( SMS ):
        
        { "contact_number": "07212122111", "message_content": "hello world" }
        
    -Response( Email ):
        
        { "contact_email_address":"c@c.c", "message_content":"hello world" }
        
    -description
        
        This will return the details of either the sms or email message that is being requested