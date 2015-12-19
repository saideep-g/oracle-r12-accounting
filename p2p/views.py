# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.shortcuts import render
from p2p.forms import P2PForm

# Create your views here.
# Create your views here.
def p2p_accounting(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = P2PForm(request.POST)
        if form.is_valid(): # All validation rules pass
            item_type_val = form.cleaned_data ['item_type']

            period_end_accrual_val = form.cleaned_data ['period_end_accrual']
            allow_recon_accounting = form.cleaned_data ['allow_recon_accounting']
            # setting period end accrual as a Boolean
            if  period_end_accrual_val== 'True':
                period_end_accrual_val = True
            else:
                period_end_accrual_val = False

            # setting allow recon accounting as a Boolean
            if  allow_recon_accounting == 'True':
                allow_recon_accounting  = True
            else:
                allow_recon_accounting  = False


        else:
            #this is fallback and usually not used since we are using 'Choices' in our form
            item_type_val ='Expense'
            allow_recon_accounting = False
            period_end_accrual_val =False
    else:
        #Initial load when the request != POST (e.g. GET)
        form=P2PForm()
        #setting form variables to default values for a != POST (e.g. GET request)
        item_type_val ='Expense'
        period_end_accrual_val =False
        allow_recon_accounting = False

    print(period_end_accrual_val)
    receipt_accting=  tuple(field for field in p2p_accting_list if ( field['accounting_entry']=='PO Receipt' and
                                                            field['item_type']==item_type_val and
                                                            field['period_end_accrual']== period_end_accrual_val
                                                            ) )
    deliver_accting = (field for field in p2p_accting_list  if ( field['accounting_entry']=='PO Deliver' and
                                                            field['item_type']==item_type_val
                                                            ) )
    invoice_accting = (field for field in p2p_accting_list if (field['accounting_entry']=='AP Invoice' and
                                                            field ['period_end_accrual']==period_end_accrual_val
                                                            ) )
    payment_accting = (field for field in p2p_accting_list  if (field['accounting_entry']=='AP Payment' and
                                                            field ['allow_recon_accounting']==allow_recon_accounting
                                                            ) )
    recon_accting = tuple(field for field in p2p_accting_list  if (field['accounting_entry']=='AP Payment Reco' and
                                                            field ['allow_recon_accounting']==allow_recon_accounting
                                                            ) )
     #list_accounting =  (d for d in list_accounting_expense if d['accounting_entry']=='PO Receipt' )
    return render(request, 'p2p/p2p_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting,
        'ap_invoice_accting':invoice_accting, 'ap_payment_accting':payment_accting,
        'ap_payment_recon_accting': recon_accting,'form': form})



p2p_accting_list = [
  {
    "id":1,
    "dr_cr":"DEBIT",
    "account_description":"Receiving Inventory A/c",
    "accounting_entry":"PO Receipt",
    "item_type":"Expense",
    "stream":"P2P",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":2,
    "dr_cr":"CREDIT",
    "account_description":"AP Accrual A/c",
    "accounting_entry":"PO Receipt",
    "item_type":"Expense",
    "stream":"P2P",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":3,
    "dr_cr":"DEBIT",
    "account_description":"Expense/PO Charge A/c",
    "accounting_entry":"PO Deliver",
    "item_type":"Expense",
    "stream":"P2P",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":4,
    "dr_cr":"CREDIT",
    "account_description":"Receiving Inventory A/c",
    "accounting_entry":"PO Deliver",
    "item_type":"Expense",
    "stream":"P2P",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":5,
    "dr_cr":"DEBIT",
    "account_description":"Receiving Inventory A/c",
    "accounting_entry":"PO Receipt",
    "item_type":"Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":6,
    "dr_cr":"CREDIT",
    "account_description":"AP Accrual A/c",
    "accounting_entry":"PO Receipt",
    "item_type":"Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":7,
    "dr_cr":"DEBIT",
    "account_description":"Inventory Material A/c",
    "accounting_entry":"PO Deliver",
    "item_type":"Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":8,
    "dr_cr":"CREDIT",
    "account_description":"Receiving Inventory A/c",
    "accounting_entry":"PO Deliver",
    "item_type":"Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":9,
    "dr_cr":"DEBIT",
    "account_description":"AP Accrual A/c",
    "accounting_entry":"AP Invoice",
    "item_type":"Expense / Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":10,
    "dr_cr":"CREDIT",
    "account_description":"AP Liability A/c",
    "accounting_entry":"AP Invoice",
    "item_type":"Expense / Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":11,
    "dr_cr":"DEBIT",
    "account_description":"Cash/Bank A/c",
    "accounting_entry":"AP Payment",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":12,
    "dr_cr":"CREDIT",
    "account_description":"AP Liability A/c",
    "accounting_entry":"AP Payment",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":13,
    "dr_cr":"DEBIT",
    "account_description":"Expense/PO Charge A/c",
    "accounting_entry":"AP Invoice",
    "item_type":"Expense",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":1
  },
  {
    "id":14,
    "dr_cr":"CREDIT",
    "account_description":"AP Liability",
    "accounting_entry":"AP Invoice",
    "item_type":"Expense",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":1
  },
  {
    "id":15,
    "dr_cr":"DEBIT",
    "account_description":"Cash/Bank A/c",
    "accounting_entry":"AP Payment Reco",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":1,
    "period_end_accrual":0
  },
  {
    "id":16,
    "dr_cr":"CREDIT",
    "account_description":"Cash Clearing A/c",
    "accounting_entry":"AP Payment Reco",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":1,
    "period_end_accrual":0
  },
  {
    "id":17,
    "dr_cr":"DEBIT",
    "account_description":"AP Liability A/c",
    "accounting_entry":"AP Payment",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":1,
    "period_end_accrual":0
  },
  {
    "id":18,
    "dr_cr":"CREDIT",
    "account_description":"Cash Clearing A/c",
    "accounting_entry":"AP Payment",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":1,
    "period_end_accrual":0
  }
]
