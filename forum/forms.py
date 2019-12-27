from django import forms


class ProjectSubmitForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Project Title'
        }),
        max_length=100,
        label="Project Title",
        required=True,
    )
    subtitle = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subtitle for the project'
        }),
        max_length=500,
        label="Subtitle",
        required=True
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Project Proposal',
            'rows': 20,
        }),
        label="Project Intro",
        required=True
    )
    img1 = forms.ImageField(
        allow_empty_file=False,
        label="Project Image 1",
        required=True,
    )
    img2 = forms.ImageField(
        allow_empty_file=False,
        label="Project Image 2",
        required=True,
    )
    img3 = forms.ImageField(
        allow_empty_file=False,
        label="Project Image 3",
        required=True,
    )
