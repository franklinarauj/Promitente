from django import forms
from app.models import TB_Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = TB_Cliente
        fields = "__all__"

class AtualizarClienteForm(forms.ModelForm):

    class Meta:
        model = TB_Cliente
        fields = ['nome', 'email', 'telefone']
