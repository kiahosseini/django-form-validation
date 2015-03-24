# django-form-validation
This django apps provide 2 base forms for you that handle proper attributes in your Django form's fields to be used in jQuery Validation plugin
* * *

## Installation
```bash 
python setup.py install
```

## Usage
> simply make your forms inherit from form_validation's base forms

```python
from form_validation.forms import BaseForm, BaseModelForm
from djago import forms


class ContactForm(BaseForm):
    name = forms.CharField(label='Name')
    subject = forms.CharField(label='Name')
    message = forms.TextField(label='Message')
    email = forms.EmailField(label='Email')
    
cf = ContactForm()
print cf

"""
must print something like:
<tr class="required"><th><label for="id_name">Name:</label></th><td><input id="id_name" name="name" required="True" type="text" /></td></tr>
<tr class="required"><th><label for="id_subject">Name:</label></th><td><input id="id_subject" name="subject" required="True" type="text" /></td></tr>
<tr class="required"><th><label for="id_message">Message:</label></th><td><textarea cols="40" id="id_message" name="message" required="True" rows="10">
</textarea></td></tr>
<tr class="required"><th><label for="id_email">Email:</label></th><td><input email="True" id="id_email" name="email" required="True" type="email" /></td></tr>

"""
```