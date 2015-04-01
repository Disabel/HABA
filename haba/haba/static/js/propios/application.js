 $(document).ready(function() {
	  $('.add-banking').click(function(ev){
	    ev.preventDefault();
	    var count = $('.banking').children().length;;    
	    var tmplMarkup = $('#banking-template').html();
	    var compiledTmpl = _.template(tmplMarkup);
	    $('div.banking').append(compiledTmpl({ id : count }));
	    // update form count
	    $('#id_banking-TOTAL_FORMS').attr('value', count+1);
	    // DatePicker
	    $( ".bankingdate" ).datepicker({
  		changeYear: true
		});
	  });  
	  $('.add-education').click(function(ev){
	    ev.preventDefault();
	    var count = $('.education').children().length;;    
	    var tmplMarkup = $('#education-template').html();
	    var compiledTmpl = _.template(tmplMarkup);
	    $('div.education').append(compiledTmpl({ id : count }));
	    // update form count
	    $('#id_education-TOTAL_FORMS').attr('value', count+1);
	  }); 	
		removeParent = function(e) {
    		$(e).parent().remove();
		}
  });