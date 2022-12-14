// toast
function genToast(message, theme) {
    let toast = $(document).find('.toast');
    toast.find('.toast-body').html(message)
    toast.toast({ delay: 5000 })
    toast.addClass(theme)
    toast.toast('show');
    toast.on('hide.bs.toast', function () {
        toast.removeClass(theme)
    });
};
$(window).ready(function () {

    // Loader
    let loader = '<div class="div-loader" aria-busy="true" id="progress" aria-label="Loading, please wait." role="progressbar"></div>'

    // Create prop
    let uploadedFile = []
    $(document).on('change', '#propuplimg', function () {
        for (let i = 0; i < this.files.length; i++) {
            const file = this.files[i];
            uploadedFile.push(file)
            if (file) {
                let reader = new FileReader();
                reader.onload = function (event) {
                    $('#imgShdiv').find('span').hide()
                    $('#imgShdiv').find('i').hide()
                    $('#imgShdiv').addClass('d-flex')
                    let uploadImgDiv = '<div class="dropimg" id="dropimg"><img src=' + event.target.result + ' class="img-wd-150" alt=' + file.name + '></div>'
                    $('#imgShdiv').append(uploadImgDiv)
                }
                reader.readAsDataURL(file);
            }
        }
    });

    $(document).on('click', '#dropimg', function () {
        $(this).remove();
        let imgDiv = $("#imgShdiv").children('.dropimg').length
        if (imgDiv == 0) {
            $('#imgShdiv').find('span').show()
            $('#imgShdiv').find('i').show()
            $('#imgShdiv').removeClass('d-flex')
        }
    });

    $(document).on('click', '#subPrevProp', function (e) {
        e.preventDefault();
        let url = $('#crtProp').attr('action')
        let type = $('#crtProp').attr('method')
        let formValue = $('#crtProp').serializeArray()
        let data = $.merge(formValue, uploadedFile)

        let formData = new FormData()

        for (let i = 0; i < data.length; i++) {
            if (data[i] instanceof File) {
                formData.append('image', data[i])
            } else {
                formData.append(data[i].name, data[i].value)
            }
        };
        $.ajax({
            url: url,
            type: type,
            data: formData,
            contentType: false,
            processData: false,
            success: function (response) {
                if (response.success) {
                    window.location.href = response.redirect_url
                } else {
                    alert(response.message)
                }
            }
        })
    });

    // list cities search bar
    let cities = [
        "Alappuzha",
        "Kochi",
        "Idukki",
        "Kannur",
        "Kasaragod",
        "Kollam",
        "Kottayam",
        "Kozhikode",
        "Malappuram",
        "Palakkad",
        "Pathanamthitta",
        "Thiruvananthapuram",
        "Thrissur",
        "Wayanad"
    ]
    cities.sort()
    for (let i = 0; i < cities.length; i++) {
        $("select#cities").append('<option value=' + cities[i].toLowerCase() + '>' + $.camelCase(cities[i]) + '</option>')
    };

    // Update user details
    $(document).on('click', '#updUsrDlts', function (e) {
        e.preventDefault();
        let uid = $('#usrDltsFrm').attr('data-usr')
        let url = $('#usrDltsFrm').attr('action')
        let type = $('#usrDltsFrm').attr('method')
        let formValue = $('#usrDltsFrm').serializeArray()
        let formData = new FormData();
        for (let i = 0; i < formValue.length; i++) {
            formData.append(formValue[i].name, formValue[i].value)
        } formData.append('uid', uid)
        $.ajax({
            url: url,
            type: type,
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                if (response.success) {
                    window.location.href = response.redirect_url
                }
            }
        })
    });

    // Update user password
    $(document).on('click', '#updtUsrPass', function (e) {
        e.preventDefault();
        let uid = $('#updtpas').attr('data-usr')
        let url = $('#updtpas').attr('action')
        let type = $('#updtpas').attr('method')
        let formValue = $('#updtpas').serializeArray()
        let formData = new FormData();
        for (let i = 0; i < formValue.length; i++) {
            formData.append(formValue[i].name, formValue[i].value)
        } formData.append('uid', uid)
        $.ajax({
            url: url,
            type: type,
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                console.log(response)
                if (response.success) {
                    genToast(response.message, 'success')
                } else {
                    genToast(response.message, 'danger')
                }
            }
        })
    });

    // forgot password
    $('.re-set-password').hide()
    $(document).on('click', '#chngPaswd', function (e) {
        e.preventDefault();
        let form = $('#chngPaswdfrm')
        let url = form.attr('action')
        let type = form.attr('method')

        let formData = new FormData();

        let email = form.find('#user-email').val()
        let new_password = form.find('#new-password').val()
        let confirm_password = form.find('#confirm-password').val()

        formData.append('email', email)

        if (new_password && confirm_password) {
            if (new_password == confirm_password) {
                formData.append('new_password', new_password)
            } else {
                genToast('Password does not match', 'warning')
                return
            }
        }
        if (url != '/auth/forgot-password/update/') {
            $.ajax({
                url: url,
                type: type,
                data: formData,
                processData: false,
                contentType: false,
                success: function (response) {
                    if (response.success) {
                        form.find('#user-email').prop('disabled', true)
                        form.attr('action', response.redirect_url)
                        $('.re-set-password').show()
                    } else {
                        genToast(response.message)
                    }
                }
            })
        } else {
            $.ajax({
                url: url,
                type: type,
                data: formData,
                processData: false,
                contentType: false,
                success: function (response) {
                    if (response.success) {
                        window.location.href = response.redirect_url
                    }
                }
            })
        }
    });

    // Send property enquiry (message)
    $(document).on('click', '#sndmsg', function (e) {
        e.preventDefault();
        let form = $('#sndmsgFrm');
        let formValue = $('#sndmsgFrm').serializeArray();
        let url = form.attr('action');
        let type = form.attr('method');
        let property = form.attr('data-prop-id');
        let formData = new FormData();
        console.log(formValue)
        for (let i = 0; i < formValue.length; i++) {
            formData.append(formValue[i].name, formValue[i].value)
        };
        formData.append('prop_uid', property)
        $.ajax({
            url: url,
            type: type,
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                console.log(response)
                if (response.success) {
                    genToast(response.message, 'success')
                }
            }
        })
    });

    // delete property
    $(document).on('click', '#dltProp', function (e) {
        e.preventDefault();
        let url = $(this).attr('href');
        let uid = $(this).attr('data-prop-id')
        let formData = new FormData();
        formData.append('uid', uid)
        $.ajax({
            url: url,
            type: 'post',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                if (response.success && response.redirect_url == null) {
                    window.location.reload()
                } else if (response.redirect_url) {
                    window.location.href = redirect_url
                }
            }
        })
    })

    $(document).on('click', '#subEmail', function (e) {
        e.preventDefault();
        let $form = $('#emailNotif');
        let url = $form.attr('action');
        let type = $form.attr('method');
        let formValue = $form.serializeArray()
        let formData = new FormData();
        for (let i = 0; i < formValue.length; i++) {
            formData.append(formValue[i].name, formValue[i].value)
        }
        $.ajax({
            url: url,
            type: type,
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                if (response.success) {
                    genToast(response.message, 'success')
                } else {
                    genToast('Something went wrong', 'danger')
                }
            }
        });
    });
});

$(window).load(function () {
    $.ajax({
        url: '/properties/ajax/list/latest-prop/',
        type: 'GET',
        success: function (response) {
            if (response.success) {
                $('.latest_property_carousel').html('')
                $('.latest_property_carousel').html(response.template_render)
                $('.property-slide').slick({
                    dots: true,
                    lazyLoad: 'ondemand',
                    infinite: true,
                    speed: 300,
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    autoplay: true,
                    autoplaySpeed: 2000,
                    arrows : false,
                    responsive: [
                        {
                            breakpoint: 1024,
                            settings: {
                                slidesToShow: 3,
                                slidesToScroll: 2,
                                infinite: true,
                                dots: true
                            }
                        },
                        {
                            breakpoint: 800,
                            settings: {
                                slidesToShow: 2,
                                slidesToScroll: 2
                            }
                        },
                        {
                            breakpoint: 600,
                            settings: {
                                slidesToShow: 1,
                                slidesToScroll: 1
                            }
                        }
                    ]
                });
            } else {
                genToast(response.message,'danger')
            }
        }
    });
})