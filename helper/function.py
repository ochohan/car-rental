from flask import Flask, render_template, request, redirect, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime
from decouple import config

SENDGRID_API_KEY = config('SENDGRID_API_KEY')


def send_email(email, subject, html_content):
    try:
        message = Mail(
            from_email='noreply.adelaide.cars@gmail.com',  
            to_emails=email,
            subject=subject,
            html_content=html_content
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return True  
    except Exception as e:
        flash(f'Error sending email: {str(e)}', 'error')
        return False  

        
def calculate_days_between(start_date, end_date):
    date_format = "%Y-%m-%d"
    start_datetime = datetime.strptime(start_date, date_format)
    end_datetime = datetime.strptime(end_date, date_format)
    delta = end_datetime - start_datetime
    return delta.days

if __name__ == "__main__":
    app.run()
