
import re
from django.core.exceptions import ValidationError
from projetoSolidario.models import Empresa
from django import forms



class EmpresaForm(forms.ModelForm):



    class Meta:
        model = Empresa
        fields = (
            'razao_social', 'nome_fantasia', 'cnpj',
            'telefone', 'email',
        )

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        
        # Garantir que telefone seja uma string
        if not isinstance(telefone, str) or re.search(r'[a-zA-Z]', telefone):
            self.add_error(
                'telefone',
                ValidationError(
                    'O Telefone não deve conter letras',
                    code='invalid'
                )
            )
        return telefone
    

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
    
    # Garantir que cnpj seja uma string e contenha apenas números, pontos e barras
        if not isinstance(cnpj, str) or not re.match(r'^[\d./-]+$', cnpj):
            self.add_error(
            'cnpj',
            ValidationError(
                'O CNPJ deve conter apenas números, pontos e barras',
                code='invalid'
            )
        )
        return cnpj