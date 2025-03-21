
from django.shortcuts import render, redirect


def send_welcome_email(user):
    html_message = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Welcome to NyumbaChap</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }}
            .container {{ background: white; padding: 20px; border-radius: 10px; text-align: center; }}
            .btn {{ display: inline-block; background: #007BFF; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🎉 Welcome {user.username}!</h2>
            <p>Thank you for registering at NyumbaChap. To complete your profile, click below:</p>
            <a href="https://nyumbachap.com/edit_profile/" class="btn">Complete Your Profile</a>
            <p>If you have any issues, feel free to contact us.</p>
        </div>
    </body>
    </html>
    """

    send_html_email("Welcome to NyumbaChap!", user.email, html_message)
