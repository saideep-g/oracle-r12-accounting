
$("#form_filter").submit(function() {
      if ($('#id_item_type').val() == 'Inventory'  & $('#id_period_end_accrual').val()=='Period End') {
        //$('#error_message').text ('For an Inventory Item, we cannot enable "Period-end Accrual"');
        $('#myModal').modal('show');
        return false;

      }
      else {
        return true;
      }
    });

$("#add-field").click(function() {
        $('#add-field-form').toggle(100)
    });


// Adding fields based on choices selected
$ ('#add-field-form-btn').click(function(event) {

    // check which journal source field is checked
    if ($("#journal-source").is(':checked')) {
        $('.jrnl-source-field').show();
    } else {
        $('.jrnl-source-field').hide();
    }
    // check which journal source field is checked
    if ($("#defaults-from").is(':checked')) {
        $('.defaults-from-field').show();
    } else {
        $('.defaults-from-field').hide();
    }
    if ($("#accting-class").is(':checked')) {
        $('.accting-class-field').show();
    } else {
        $('.accting-class-field').hide();
    }
});

// Toggle Sidebar and increase width of main accordingly
$('.sidebar-toggle').click(function(event) {
    /* Act on the event */
    console.log ($(".sidebar").attr('display'));
    toogleSidebar();

});

function toogleSidebar (event){
    $ ('.sidebar').toggle();
    if($('.sidebar').css('display') == 'none') {

        $(".main").attr("class", "col-sm-9 col-sm-offset-0 col-md-12 col-md-offset-0 main");
    } else {
        $(".main").attr("class", "col-sm-8 col-sm-offset-3 col-md-9 col-md-offset-3 main");
    }

}
// Scripts to open Screenshot Modal
$('#pe-accrual-btn').click(function(event) {
    $('#period-end-accrual-modal').modal('show');
});

$('#allow-recon-accting-btn').click(function(event) {
    $('#when-pymt-clrs-modal').modal('show');
});

$('#item-type-btn').click(function(event) {
    $('#item-type-modal').modal('show');
});


//Events related to Invoice Price Variance
$('#ipv-update-accting').click(function(event) {
    updateAmt();
        });
//Updating Invoice Amt
$('#invoice-price'). keyup(function(event) {
    inv_price= $('#invoice-price').val() 
    inv_qty= $('#invoice-qty').val() 
     $('#invoice-amount').val (inv_price*inv_qty)
     updateAmt();
     if (inv_price<0) {       
                     $.notify("Negative Invoice price?? Anyways, we left it there so that you can play around!!", "info");
            }
});

$(function() {
    if (window.location.pathname == '/invoice_price_variance_accounting/') {
        $('.jrnl-amount, .jrnl-amount-field').show();
        updateAmt();
        toogleSidebar();
    }

});

// Calculating IPV and Amts based on the values in the scenario
    function updateAmt() {//get the values
    invoice_amount= $('#invoice-amount').val()
    receipt_amount = $('#receipt-amount').val()
    po_amount =$('#po-amount').val() 
    inv_qty = $('#invoice-qty').val() 
    po_price = $('#po-price').val() 
    inv_price= $('#invoice-price').val() 
    ipv_amount = (po_price - inv_price) * inv_qty
    //Updating IPV Amount
    ipv_row = $("tr:contains('Invoice Price Variance A/c')").filter (function(){
                            return $(this).children ('td.jrnl-source-field').text().trim()== 'Payables';
                        })
     if (ipv_amount <0) {
        $('#ipv-amount').text('$ ' + ipv_amount).removeClass('label-success').addClass('label-danger');
        ipv_row.children("td.jrnl-amount").text(ipv_amount*-1);
        ipv_row.children("td.debit-credit").text('DEBIT');

    } else{ 
        $('#ipv-amount').text('$ ' + ipv_amount).addClass('label-success').removeClass('label-danger');

        ipv_row.children("td.jrnl-amount").text(ipv_amount);
        ipv_row.children("td.debit-credit").text('CREDIT');

    }
    //Updating Amount of accounting entries
    $("tr:contains('AP Liability A/c')").children("td.jrnl-amount").text(invoice_amount);
    $("tr:contains('Cash/Bank A/c')").children("td.jrnl-amount").text(invoice_amount);
    $("tr:contains('Receiving Inventory A/c')").children("td.jrnl-amount").text(receipt_amount);
    $("tr:contains('Expense AP Accrual A/c')").filter (function(){
            return $(this).children ('td.jrnl-source-field').text().trim()== 'Payables';
        }).children("td.jrnl-amount").text(inv_qty*po_price);
    $("tr:contains('Expense AP Accrual A/c')").filter (function(){
            return $(this).children ('td.jrnl-source-field').text().trim()== 'Cost Management';
        }).children("td.jrnl-amount").text(receipt_amount);      
       $("tr:contains('Expense/PO Charge A/c')").filter (function(){
            return $(this).children ('td.jrnl-source-field').text().trim()== 'Cost Management';
        }).children("td.jrnl-amount").text(receipt_amount);     

}

/*$(function() {
    console.log($('#invoice-amount').val())
    invoice_amount= $('#invoice-amount').val()
    $("tr:contains('Receiving Inventory A/c')").children("td.jrnl-amount").css('color','blue').text(100);
    accrual = $("tr:contains('Expense AP Accrual A/c')");

    $(accrual).filter (function(){
        
       // return ($(this).children ('td').first().text()== 'DEBIT') ; //this worked
       return ($(this).children ('td.jrnl-source-field').text().trim()== 'Payables') ; 
    }).css('color','red').children("td.jrnl-amount").text(invoice_amount);
    //$('tr:has(td:nth-child(1):contains("DEBIT"))‌​').css('color','red') ;
    console.log ( $('tr:has(td:nth-child(1):contains("DEBIT"))‌​').css('color','red'));

    $('#ipv-update-accting').click(function(event) {
        console.log ( $('tr:has(td:nth-child(2):contains("Receiving Inventory A/c")):has(td:nth-child(1):contains("Debit"))‌​').children("td.jrnl-amount"));
        //$("tr:contains('Receiving Inventory A/c')").children("td.jrnl-amount").css('color','red').text('9') ;
        //$("tr:contains('Receiving Inventory A/c'):contains ('DEBIT')").children("td.jrnl-amount").css('color','red').text('20') ;
        //$('tr:has(td:nth-child(2):contains("Receiving Inventory A/c")):has(td:nth-child(1):contains("DEBIT"))‌​').
        //children("td.jrnl-amount").text ('20');
    });    
});*/