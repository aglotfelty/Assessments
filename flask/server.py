from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/')
def index():
    """Home page."""

    return render_template("index.html")


@app.route('/application-form')
def apply_here():
    """Application page"""

    jobs=['Software Engineer', 'QA Engineer', 'Product Manager']
    return render_template("application-form.html", job_options=jobs)


@app.route('/application-success', methods=['POST'])
def finish_form():
    """Application response form"""
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    preformatted_salary = str(request.form.get("salary"))
    formatted_salary = ''
    for char in preformatted_salary:
        if char != ',':
            formatted_salary += char
    salary = formatted_salary
    job_title = request.form.get("job")

    return render_template("application-response.html",
                            first_name=first_name,
                            last_name=last_name,
                            salary=salary,
                            job_title=job_title
                           )

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
