from django import forms

class P2PForm(forms.Form):
    ITEM_TYPES = ( ('Expense','Expense'), ('Inventory','Inventory'))
    YES_OR_NO = ((True, 'Yes'), (False, 'No'))
    item_type = forms.ChoiceField( label = 'Item Type' ,initial='Expense',
        choices=ITEM_TYPES, 
        widget = forms.Select(  attrs={'class': 'form-control'}))
    
    period_end_accrual = forms.ChoiceField(label = 'Period End Accrual',  initial=False, required= False, 
        choices= YES_OR_NO,
        widget = forms.Select (attrs={'class': 'form-control'}, 
                                                       ))
    allow_recon_accounting =  forms.ChoiceField(label = 'Allow Reconciliation Accounting',  initial=False, required= False, 
        choices= YES_OR_NO, 
        widget = forms.Select( attrs={'class': 'form-control'}  ))
