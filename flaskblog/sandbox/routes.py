from flask import abort, flash, request, render_template, redirect, url_for, Blueprint
from flaskblog.sandbox.forms import CalculatorForm

sandbox = Blueprint('sandbox', __name__)


@sandbox.route("/sandbox/play", methods=['GET', 'POST'])
def simple_calculator():
    form = CalculatorForm()
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        num3 = num1 + num2
        flash("{} + {} = {}".format(num1, num2, num3), "success")
        return redirect(url_for('sandbox.simple_calculator'))
    return render_template("sandbox.html", form=form)


# https://www.tutorialspoint.com/flask/flask_sending_form_data_to_template.htm
# https://stackoverflow.com/questions/51006831/adding-two-numbers-in-flask

# This one might be the most relevant
# https://stackoverflow.com/questions/52343833/flask-how-to-update-div-after-processing-form-inputs

# Example of a data science flask app
# https://github.com/kayschulz/travel_destination_recommendation

