from flask import (Flask, render_template, url_for, request, redirect)
import csv

app = Flask(__name__)


@app.route('/') #Root Route
def home_page():
    return render_template('./index.html')

@app.route('/<string:page_name>') #Root Route
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET']) #Root Route
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'Failure to save to the database!'

        # return 'Email form submitted!'
        # sender_email = request.form['email']
        # subject = request.form['subject']
        # message = request.form['message']
        # return f"""sender_email: {sender_email}
        #  subject: {subject}
        #  message: {message}
        # """

    return 'Email content not found!'

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data ["subject"]
        message = data ["message"]
        output = f"\n{email},{subject},{message}"
        file = database.write(output)

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csv_database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(csv_database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

if __name__ == "__main__":
    app.run(debug=True, port=8080)