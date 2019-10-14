from django import forms

class MessageForm(forms.Form):
    
    
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Write Your Message Here!"
        })
    )
    
