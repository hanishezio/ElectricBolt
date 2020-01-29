from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
import psycopg2


# Create your views here.
def arealoc(request):
    return render(request,'arealoc.html') 

def annanagar(request):
        hostname = 'localhost'
        username = 'postgres'
        password = '1234'
        database = 'electricbolt'
        

        # Simple routine to run a query on a database and print the results:
        def doQuery( conn ) :
            cur = conn.cursor()
            print("a")

            cur.execute( "SELECT email FROM public.register_registration WHERE location LIKE '%Annanagar%';" )
            count=0          
            
            for email in cur.fetchall() :

                subject = 'Regarding Total Power Cut '
                message = ' Hi,Tommorrow is Total Power Cut from 9.00 AM to 5.00 pm in your area '
                email_from = settings.EMAIL_HOST_USER
                recipient_list = email    
                send_mail( subject, message, email_from, recipient_list )
                count=count+1
                if count ==4:
                    break


        print ("Using psycopg2…")
        import psycopg2
        myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        doQuery( myConnection )
        myConnection.close()

        # print ("Using PyGreSQL…")
        # import pgdb
        # myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
        # doQuery( myConnection )
        # myConnection.close()
    

        return render(request, 'mail.html')

def theppakulam(request):
        hostname = 'localhost'
        username = 'postgres'
        password = '1234'
        database = 'electricbolt'
        

        # Simple routine to run a query on a database and print the results:
        def doQuery( conn ) :
            cur = conn.cursor()
            print("a")

            cur.execute( "SELECT email FROM public.register_registration WHERE location LIKE '%Theppakulam%';" )
            count=0          
            
            for email in cur.fetchall() :

                subject = 'Regarding Total Power Cut'
                message = ' Hi,Tommorrow is Total Power Cut from 9.00 AM to 5.00 pm in your area '
                email_from = settings.EMAIL_HOST_USER
                recipient_list = email    
                send_mail( subject, message, email_from, recipient_list )
                count=count+1
                if count ==4:
                    break


        print ("Using psycopg2…")
        import psycopg2
        myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        doQuery( myConnection )
        myConnection.close()

        # print ("Using PyGreSQL…")
        # import pgdb
        # myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
        # doQuery( myConnection )
        # myConnection.close()
    

        return render(request, 'mail.html') 


def villapuram(request):
        hostname = 'localhost'
        username = 'postgres'
        password = '1234'
        database = 'electricbolt'
        

        # Simple routine to run a query on a database and print the results:
        def doQuery( conn ) :
            cur = conn.cursor()
            print("a")

            cur.execute( "SELECT email FROM public.register_registration WHERE location LIKE '%Villapuram%';" )
            count=0          
            
            for email in cur.fetchall() :

                subject = 'Regarding Total Power Cut'
                message = ' Hi,Tommorrow is Total Power Cut from 9.00 AM to 5.00 pm in your area '
                email_from = settings.EMAIL_HOST_USER
                recipient_list = email    
                send_mail( subject, message, email_from, recipient_list )
                count=count+1
                if count ==4:
                    break


        print ("Using psycopg2…")
        import psycopg2
        myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        doQuery( myConnection )
        myConnection.close()

        # print ("Using PyGreSQL…")
        # import pgdb
        # myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
        # doQuery( myConnection )
        # myConnection.close()
    

        return render(request, 'mail.html')

