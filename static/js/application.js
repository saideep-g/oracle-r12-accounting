
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
	$ ('.sidebar').toggle();
	if($('.sidebar').css('display') == 'none') {

		$(".main").attr("class", "col-sm-9 col-sm-offset-0 col-md-12 col-md-offset-0 main");
	} else {
		$(".main").attr("class", "col-sm-8 col-sm-offset-3 col-md-9 col-md-offset-3 main");
	}

});
// Scripts to open Screenshot Modal
$('#pe-accrual-btn').click(function(event) {
	$('#period-end-accrual-modal').modal('show');
});

$('#allow-recon-accting-btn').click(function(event) {
	$('#when-pymt-clrs-modal').modal('show');
});
