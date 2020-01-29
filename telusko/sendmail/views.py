from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render,redirect
import psycopg2







# Create your views here.
# def mail(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['shkgroups08@gmail.com',]    
#     send_mail( subject, message, email_from, recipient_list )
       
        

#     return render(request, 'mail.html')


	
def mail(request):
        # hostname = 'localhost'
        # username = 'postgres'
        # password = '1234'
        # database = 'electricbolt'
        

        # # Simple routine to run a query on a database and print the results:
        # def doQuery( conn ) :
        #     cur = conn.cursor()

        #     cur.execute( "select auth_user.email,location_location.location from auth_user inner join location_location on auth_user.id = location_location.id;" )
        #     count=0
            
        #     for email in cur.fetchall() :

        #         subject = 'Thank you for registering to our site'
        #         message = ' it  means a world to us '
        #         email_from = settings.EMAIL_HOST_USER
        #         recipient_list = email    
        #         send_mail( subject, message, email_from, recipient_list )
        #         count=count+1
        #         if count ==4:
        #             break


        # print ("Using psycopg2…")
        # import psycopg2
        # myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        # doQuery( myConnection )
        # myConnection.close()

        # # print ("Using PyGreSQL…")
        # # import pgdb
        # # myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
        # # doQuery( myConnection )
        # # myConnection.close()
    

        return render(request, 'mail.html')

def homepage(request):          
    return redirect('home')