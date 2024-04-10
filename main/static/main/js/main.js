;(function($, undefined) {

    $('#id_username').on('click', function() {

        $(".helptext").fadeToggle();
        $(".helptext").delay(7000).hide(100);
    })

    $('#id_password1').on('click', function() {

        $(".form-info ul").fadeToggle();
        $(".form-info ul").delay(7000).hide(100);
    });

    $('#id_url_large').on('click', function() {

        $("#id_url_large_helptext").fadeToggle();
        $("#id_url_large_helptext").delay(7000).hide(100);
    });

    $('#id_url_small').on('click', function() {

        $("#id_url_small_helptext").fadeToggle();
        $("#id_url_small_helptext").delay(7000).hide(100);
    });

})(jQuery);