$(function () {
    $('.header .navbar-nav a').smoothScroll();

    function activate(navbarItem) {
      navbarItem.addClass('active').siblings('li').removeClass('active');
    }   

    $('.section').mouseenter(function() {
      var sectionName = $(this).attr('id');
      console.log(sectionName)
      var navbarItem = $('.navbar-nav a[href="#' + sectionName + '"]').parent();
      console.log(navbarItem)
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
