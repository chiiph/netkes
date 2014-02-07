$(function() {

    // Workings for the modal wrapper and widgets

    $('#add-widget').click(function(){
        $('.modal-wrapper').show().css('height', $(document).height());
    });

    $('#option-add-user button').click(function(){
            $('.widget-add-user-option').hide();
            $('.widget-add-user').show();
    });

    $('h2.page-header .actions').click(function() {
        $('.widget-add-user').hide()
        $('.widget-add-user-option').show();
        $('.modal-wrapper').hide();
    });

    //Auto Tooltips
    $('td').each(function(){
        if($(this).text()){
            if(this.offsetWidth < this.scrollWidth){
                $(this).attr('title', $(this).text());
            }
        }
    });

    //Loader for the login page
    $('#login').mouseup(function() {
        $(this).replaceWith("<img src='/static/blue_mgnt/img/loader.gif' style='float:right; margin-right:40px'/>");
        $('#log_in').submit();
    });


    // Controller for hide/show in details
    if($('toggle-controller')){
        $('.widget-overview').hide()
        $('.toggle-controller > span').html('<i class="ss-icon">&#x002B;</i> See');
        $('.toggle-controller').click(function(){
            var curr_widget = $(this).parent().next('.widget-overview');
            curr_widget.toggle();
            $('span', this).html(curr_widget.is(':visible') ? '<i class="ss-icon">&#x002D;</i> Hide' : '<i class="ss-icon">&#x002B;</i> See');
        });
    }

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
});
