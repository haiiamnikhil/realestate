$(window).ready(function () {
    $(document).on('change', '#sysettings input', function () {
        if ($(this).prop('checked')) {
            $(this).closest('.settings').parent().find('.collapse').collapse('show')
        } else {
            $(this).closest('.settings').parent().find('.collapse').collapse('hide')
        }
    });
});