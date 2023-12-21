from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, IntegerField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm, CSRFProtect
from app.main.models import Supplier

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
  

class AddRoleForm(FlaskForm):
    name = StringField('Role Name', validators=[DataRequired()])
    submit = SubmitField('Add Role')

class EditUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=15)])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    password = StringField('Password')  # You may want to change this to a PasswordField for security
    # Add more fields as needed

    submit = SubmitField('Save Changes')

class AddProductCategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Add Category')

class AddSupplierForm(FlaskForm):
    supplier_id = StringField('Supplier ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    contact_person = StringField('Contact Person', validators=[DataRequired()])
    contact_email = StringField('Contact Email', validators=[DataRequired()])
    contact_phone = StringField('Contact Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Add Supplier')

class AddProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    brand = StringField('Brand')
    unit_price = FloatField('Unit Price', validators=[DataRequired()])
    unit_measurement = StringField('Unit of Measurement')
    quantity_in_stock = IntegerField('Quantity in Stock', validators=[DataRequired()])
    discount_percentage = FloatField('Discount Percentage')
    promotional_tag = StringField('Promotional Tag')
    nutritional_information = TextAreaField('Nutritional Information')
    country_of_origin = StringField('Country of Origin')
    supplier = SelectField('Supplier', coerce=int, validators=[DataRequired()])
    date_added = DateField('Date Added to Inventory', validators=[DataRequired()])
    submit = SubmitField('Add Product')