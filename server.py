from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/<string:page_name>")
def dynamic_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as db_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db_file.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as db_file2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data )
            return render_template('thankyou.html', useremail = data['email'])
        except:
            return 'couldn\'t save to the database'
    else:
        return 'something went wrong'



# @app.route("/index.html")
# def homepage_index():
#     return render_template('index.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/components.html")
# def components():
#     return render_template('components.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/blog")
# def blog():
#     return "<p>Are you reading this blog?</p>"

# @app.route("/blog/2020/dogs")
# def blog2():
#     return "<p>This is my blog post.</p>"