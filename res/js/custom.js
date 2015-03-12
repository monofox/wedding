$(function () {
    $('.header .navbar-nav a').smoothScroll();

    function activate(navbarItem) {
      navbarItem.addClass('active').siblings('li').removeClass('active');
    }   

    $('.section').mouseenter(function() {
      var sectionName = $(this).attr('id');
      var navbarItem = $('.navbar-nav a[href="#' + sectionName + '"]').parent();
      activate(navbarItem);
    }); 

    $('.navbar-nav a').click(function() {
      var navbarItem = $(this).parent();
      activate(navbarItem);
    }); 


    $('#jump2top').css('bottom', '-100px');
    $(window).scroll(function () {
        var btn = $('#jump2top');
        if ($(this).scrollTop() > 100) {
            btn.stop().animate({ 'bottom': '0' }, 200);
        } else {
            btn.stop().animate({ 'bottom': '-100px' }, 200);
        }
    });

    $('#jump2top').smoothScroll();
    
    // Countdown
    $('.countdown').downCount({
        date: '09/12/2015 12:00:00',
        offset: +10
    });

    $('#wishorderform').ajaxForm(function(returnVal) {
      $('#wishorderform').html($(returnVal).html());
      if ($('#wishorderform input[name="form_status"]').val() != '0') {
        // Save wish id
        var wishId = $('#wishorderform input[name="form_status"]').val();
        $('article[data-wishid="'+wishId+'"]').remove();
        // form was sent with success! => reset status and close all things!
        $('#wishorderform input[name="form_status"]').val('0');
        $('.overlay').remove();
        $('#popup_content').css({'display':'none'});
      }
    });

    $('p.didYouOrdered button').click(function() {
        // only activate, when we don't have the overlay now.
        if ($('.overlay').size() <= 0) {
          var docHeight = $(document).height();
          $('body').append("<div class='overlay'></div>");
          $('.overlay').height(docHeight);
          // Warning: in case, they click somewhere else, we cancel!
          $('.overlay').click(function() {
            $(this).remove();
            $('#popup_content').css({'display':'none'});
            // He cancelled. So let us reset the form.
            var resetUrl = $('#wishorderform').data('reset');
            // Obtain the CSRF token
            var token = $('#wishorderform input[name="csrfmiddlewaretoken"]').val();
            $.post(resetUrl, { 'csrfmiddlewaretoken': token, }, function (returnVal) {
              $('#wishorderform').html($(returnVal).html());
            });
          });
          // Now show the form!
          $('#wishorderform input[name="wishid"]').val($(this).data('wishid'));
          $('#wishorderform input[name="form_status"]').val('0');
          $('#popup_content').css({'display':'block'});
        }
    });

    $('#contactform').ajaxForm(function(returnVal) {
      $('#contactform').html($(returnVal).html());
    });
});

function scrollTo(elem) {
    $('body,html').animate({
        scrollTop: elem.offset().top
    }, 500);
}

function valemail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}