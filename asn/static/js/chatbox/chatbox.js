console.clear();

// shitty js not for use, just don`t look)

$(document).ready(
    function() {
        $(".body").niceScroll({
            cursorcolor: "rgba(0,0,0,0.5)",
            cursorborder: "none",
					  zindex: 99999
        });
    }
);

$("body").getNiceScroll().hide();

// $(window).on('keydown', function(e) {
//   if (e.which == 13) {
//     sendMess();
//     return false;
//   }
// });
    
count = 0
function sendMess(msg) {
    d = new Date();
    m = d.getMinutes();
    // msg = $('.sending-message textarea').val();
    var height = $('.body')[0].scrollHeight;
    if ($.trim(msg) == '') {
        return false;
    }
    $('<div class="u-message"><p>' + msg + '</p></div>').appendTo($('#rg_chat')).hide().show("fast");
    $('.body').animate({scrollTop:$('figure').offset().top}, 'slow');

// function sendMess(msg) {

    // console.log(msg);
    // var d = new Date();
    //
    // var m = d.getMinutes();
    // // msg = $('.sending-message textarea').val();
    // var height = $('.body')[0].scrollHeight;
    // count++;
    // var s = msg;
    // var s = $('<div class="u-message" id="id_"'+count+'><p>' + msg + '</p></div>').appendTo('#rg_chat').hide().show("Fast");
    // //$('#rg_chat').append(s);
    // // console.log($('#id_'+count).length);
    // $('.body').animate({scrollTop:$('figure').last().offset().top}, 'slow');
    // // $('.sending-message textarea').val(null);
}

// $(".sending-message button").click(function() {
//     sendMess();
// });