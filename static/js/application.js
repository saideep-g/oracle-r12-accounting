
$("#form_filter").submit(function() {
      if ($('#id_item_type').val() == 'Inventory'  & $('#id_period_end_accrual').val()=='True') {
        //$('#error_message').text ('For an Inventory Item, we cannot enable "Period-end Accrual"');
        $('#myModal').modal('show');
        return false;

      }
      else {    
        
        return true;
      }
    });

$( document ).ready(function() {
  ga('send', 'pageview', location.pathname);        
    });