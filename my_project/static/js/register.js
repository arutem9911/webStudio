let registerData = {}
$('#SubmitBtn').on('click', function(event) {
    event.preventDefault();
    email = $('#id_email').val();
    phone = $('#id_phone').val();
    birth_date = $('#id_birth_date_year').val() + '-' + $('#id_birth_date_month').val() + '-' + $('#id_birth_date_day').val()
    username = $('#id_username').val();
    password = $('#id_password1').val();
    first_name = $('#id_first_name').val();
    last_name = $('#id_last_name').val();
    sendData = {
        "email": email,
        "phone": phone,
        "birth_date": birth_date,
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name
    };

    async $.ajax({
        url: `http://127.0.0.1:8000/api/user/`,
        method: 'POST',
        data: sendData.serialize(),
        headers: {},
        success: async function(data, status) {
            registerData = data

        },
        error: function(status) {
            console.log(status);
        }
    })
    window.location.href = `api/user/`;

    })
})
console.log(registerData);