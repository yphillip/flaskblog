from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField


class CalculatorForm(FlaskForm):
    num1 = IntegerField("First integer")
    num2 = IntegerField("Second integer")
    submit = SubmitField("Perform addition!")
