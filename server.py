from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
import subprocess
from forms import ContactForm

app = Flask(__name__)

app.secret_key = 'your_secret_key_here'

# Mailtrap configuration for testing
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525  # You can also use 2525 or 25
app.config['MAIL_USERNAME'] = '2b74c9db1ccf2b'
app.config['MAIL_PASSWORD'] = '28058a12059d57'  # Replace with your actual password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/blog')
def blog():
  return render_template('/blog/index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        #name = request.form['name']
        #email = request.form['email']
        #message = request.form['message']
        #subject = request.form['subject']

        name = form.name.data
        email = form.email.data
        message = form.message.data
        subject = form.subject.data

        # Validate form data
        if not name or not email or not message or not subject:
            flash('All fields are required!')
            return redirect(url_for('contact'))

        # Compose email
        msg = Message(subject='Contact Form Submission',
                      sender=email,
                      recipients=['wonderfullycreatedbooks@gmail.com'],
                      body=f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")

        # Send email
        mail.send(msg)
        flash('Thank you for your message!')
        return redirect(url_for('contact'))
    return render_template('/contact/index.html')

@app.route('/digitalart')
def digitalart():
  return render_template('/digitalart/index.html')

@app.route('/digitalart/portraits')
def portraits():
  return render_template('/digitalart/portraits/index.html')

@app.route('/digitalart/prints')
def prints():
  return render_template('/digitalart/prints/index.html')

@app.route('/poetry')
def poetry():
  return render_template('/poetry/index.html')

@app.route('/about/ourstory')
def ourstory():
  return render_template('/about/ourstory/index.html')

if __name__ == '__main__':
  app.run(debug=True)
