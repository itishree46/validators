from django import forms

def validate_for_n(value):
    if value[0]=='n':
        raise forms.ValidationError('name start with n')
def check_len(value):
    if len(value)<4:
        raise forms.ValidationError('name is too short')

class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[validate_for_n])
    age=forms.IntegerField()
    email=forms.EmailField(max_length=100)
    reemail=forms.EmailField(max_length=100)

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reemail']
        if e!=r:
            raise forms.ValidationError('email is not matched')
