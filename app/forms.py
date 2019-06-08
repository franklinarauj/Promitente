from django import forms
from app.models import TB_Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = TB_Cliente
        fields = "__all__"

        # widgets = {
        #     'cpf' : forms.CharField(attrs={'class': 'cpf_class'}),
        # }

    # def __init__(self, *args, **kwargs):
    #     super(ClienteForm, self).__init__(*args, **kwargs)
    #     self.fields["__all__"].widget.attrs.update({'class': 'myfieldclass'})