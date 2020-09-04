from django import forms


class CourseraForm(forms.Form):
    text = forms.CharField(label='Отзыв', min_length=2, max_length=39)
    grade = forms.IntegerField(label='Grade', max_value=10)
    image = forms.FileField(label='Image', required=False)

    def clean_text(self):
        if 'abc' not in self.cleaned_data['text']:
            raise forms.ValidationError('Not found the correct data, sorry')


