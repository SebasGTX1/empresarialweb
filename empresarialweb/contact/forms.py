from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Write your name'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Write your email'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label='Content', required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3,
               'placeholder': 'Write your message'}
    ), min_length=5, max_length=1000)
