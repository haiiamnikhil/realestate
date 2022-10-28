function genToast(message, theme) {
    let toast = $(document).find('.toast');
    toast.find('.toast-body').html(message)
    toast.toast({delay:5000})
    toast.addClass(theme)
    toast.toast('show');
    toast.on('hide.bs.toast',function(){
        toast.removeClass(theme)
    });
};


$(window).ready(function () {
    $(function () {
        var current = location.pathname;
        $('.nav-menu li').each(function () {
            var $this = $(this);
            $this.removeClass('active')
            if ($this.find('a').attr('href') == current) {
                $this.addClass('active');
            }
        })
        $('#sideNavroute li').each(function () {
            var $this = $(this);
            $this.removeClass('active')

            if ($this.find('a').attr('href') == current) {
                $this.addClass('active');
            }
        })
    })


    $(document).on('change', '#sysettings input[type="checkbox"]', function () {
        if ($(this).prop('checked')) {
            $(this).closest('.settings').parent().find('.collapse').collapse('show')
        } else {
            $(this).closest('.settings').parent().find('.collapse').collapse('hide')
            let $form = $(this).closest('form')
            let uid = $form.find('input[name="uid"]').val()
            if (uid) {
                let url = $form.attr('action')
                let type = $form.attr('method')
                let formData = new FormData();
                formData.append('is_enabled', $(this).prop('checked'))
                $.ajax({
                    url: url,
                    type: type,
                    data: formData,
                    processData: false,
                    contentType: false,
                    success: function (response) {
                        if (response.success) {
                            genToast(response.message,'success')
                        };
                    }
                })
            }
        }
    });

    $('#lstPrpFrm input, #lstPrpFrm select').each(function(){
        if ($(this).val()){
            $(this).attr('name',$(this).attr('data-val'))
        }
    })

    $('#lstPrpFrm').find("select,input").on('change',function(){
        $(this).attr('name',$(this).attr('data-val'))
    });

});