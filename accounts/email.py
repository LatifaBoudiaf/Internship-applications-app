from django.core.mail import send_mail

def send_account_details_email(user_email, username, password):
    subject = 'Your Account Credentials'
    message = 'Username:'+{username}+'Password:'+{password}  
    from_email = 'latifa.boudiaf@univ-constantine2.dz'
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
