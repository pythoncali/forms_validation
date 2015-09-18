from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length=200, widget=forms.Textarea, required=True)

    def clean_message(self):
        message = self.cleaned_data['message']
        if 'I Love DjangoCali' not in message:
            raise forms.ValidationError("What's wrong with you!!!")

        return message

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.split()) > 2:
            raise forms.ValidationError("Your name is weird!!!")

        return name

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get("name", '')
        message = cleaned_data.get("message", '')

        if len(name.split())==1 and 'i got 2 names' in message:
            # Only do something if both fields are valid so far.
            raise forms.ValidationError(
                "I know you are lying!!!"
            )