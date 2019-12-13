$(document).ready(function() {
    //alert("here");
    $('textarea.wysiwyg-editor').wysiwygEditor();

});

function submit_mail(){
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();


    let data = $('textarea.wysiwyg-editor').val();
    var email = $('#txtSearch').val();
    email = email.split(',');
    let temp = Array();
    for (i of email){
        temp.push(i.toString().trim());
    }
    temp.pop();
    alert(data);
    $.ajax({
        url: '/mailer/email_manager',
        type: 'POST',
        data:{
            'csrfmiddlewaretoken':csrftoken,
            'data': data,
            'email': JSON.stringify(temp)
        },
        error: function () {
            alert('Could not connect to server...');
        },
        success: function(response_ds) {
            alert(response_ds);
        }
    });
}

function searchOpen() {
    var search = $('#txtSearch').val();
    let temp = search.split(',');
    let s_data = temp[temp.length-1].toString().trim();
    //  console.log(s_data);
    var data = {
        search: s_data

    };
    $.ajax({
        url: '/mailer/search.json',
        data: data,
        dataType: 'jsonp',
        jsonp: 'callback',
        jsonpCallback: 'searchResult'
    });
}

function split( val ) {
    return val.split( /,\s*/ );
}
function extractLast( term ) {
    return split( term ).pop();
}

function searchResult(data) {
    console.log(data);
    $( "#txtSearch" ).autocomplete ({
        minLength: 0,
        source: function( request, response) {
            // delegate back to autocomplete, but extract the last term
            response( $.ui.autocomplete.filter(
                data, extractLast( request.term ) ) );
        },
        focus: function() {
            // prevent value inserted on focus
            return false;
        },
        select: function( event, ui ) {
            var terms = split( this.value );
            // remove the current input
            terms.pop();
            // add the selected item
            terms.push( ui.item.value );
            // add placeholder to get the comma-and-space at the end
            terms.push( "" );
            this.value = terms.join( ", " );
            return false;
        }
    });
}