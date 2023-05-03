from django.forms import ModelForm, DateInput
from delta.models import Cadastro


# Create the form class.
class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ["date", "produto", "solicitante", "seguradora", "carro_rebocado", "cor", "placa", "sinistro", "tot_km", "valor", "cliente", "telefone", "de", "para"]
        widgets = {
            'date': DateInput(attrs={'placeholder': 'AAAA-MM-DD'})
        }