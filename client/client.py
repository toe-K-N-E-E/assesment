

from Utils.request_menu import RequestMenu

def showMenu():
    """this will render the menu
    :return: nothing will be return
    """
    print( "1. Create New User" )
    print( "2. Authorize" )
    print( "3. Send SMS" )
    print( "4. Send Email" )
    print( "5. Get Recently Sent Message" )
    print( "6. Exit" )
#======================================end of function definition



def main():
    """this is main function for client
    :return: nothing to return
    """

    run = True

    while run:
        showMenu()
        choice = input( "Enter your choice 1-6: " )
        print( "" )

        #check if we creating a new user
        if choice == "1":
            print( "Creating New User" )
            new_username = input( "Enter new username: " )
            RequestMenu.createNewUser( new_username )           #this function will set token on creation so authentication not required
        #check if we authorizing
        elif choice == "2":
            print( "Authorize User" )
            username = input( "Enter username for authorization: " )
            RequestMenu.authorize( username )
        #check if we sending an sms
        elif choice == "3":
            print( "Send an SMS" )
            contact_number = input( "Enter Phone Number: " )
            message_content = input( "Enter SMS: " )
            RequestMenu.sendMessage( contact_number, message_content, "sms" )
        #check if we sending an email
        elif choice == "4":
            print( "Send an Email" )
            contact_email = input( "Enter Email Address: " )
            message_content = input( "Enter Email Content: " )
            RequestMenu.sendMessage( contact_email, message_content, "email" )
        #check if we request info about previously sent message
        elif choice == "5":
            print( "Previously Sent Message" )
            RequestMenu.getRecentMessageDetails()
        #check if we terminating program
        elif choice == "6":
            run = False


if __name__ == "__main__":
    main()              # run main
