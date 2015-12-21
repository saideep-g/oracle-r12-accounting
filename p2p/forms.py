from django import forms

class P2PForm(forms.Form):
    ITEM_TYPES = ( ('Expense','Expense'), ('Inventory','Inventory'))
    YES_OR_NO = ((True, 'Yes'), (False, 'No'))
    PERIOD_END_ACCRUAL = (('At Receipt', 'At Receipt'), ('Period End','Period End'))

    item_type = forms.ChoiceField( label = 'Item Type' ,initial='Expense',
        choices=ITEM_TYPES,
        widget = forms.Select(  attrs={'class': 'form-control'}))

    period_end_accrual = forms.ChoiceField(label = 'Period End Accrual',  initial='At Receipt', required= False,
        choices= PERIOD_END_ACCRUAL,
        widget = forms.Select (attrs={'class': 'form-control'},
                                                       ))
    allow_recon_accounting =  forms.ChoiceField(label = 'Accounting - When Payment Clears',  initial=False, required= False,
        choices= YES_OR_NO,
        widget = forms.Select( attrs={'class': 'form-control'}  ))
