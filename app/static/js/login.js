// get hemis number fuction
function enter_student_page(password) {

    var password = document.getElementById(password).value;


    // Convert data into obj
    data = {
        'std_hu_id': password
    }   


    console.log('Here is the admin login data: ', data)

    // showHideBtn(hidden_btn, show_btn)

    // Show progress bar
    showProgressBar()
    // Sending data
    //https://hemis-hu-back-end.onrender.com/get_hemis_no
    // http://127.0.0.1:2026
    
    fetch('http://127.0.0.1:2026/get_hemis_no',
        {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(data),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            })

        }) 
        // Then do something other withe respond...
        .then(function (response) {
            if (response.status != 200) {
                console.log('There was aproblem while sending data')
                console.log(`Response status were not 200: ${response.status}`);
                err_message_3.style.display = 'block';
                hideProgressBar()
                return;
            }
            response.json().then(function (data) {
                // This is the message from Python
                console.log('Fiiri xogta la soo celiyey:')
                console.log(data)

                if (data['status'] == 'success') {
                    std_full_name.innerHTML = data['data']['full_name'];
                    std_hemis_no.innerHTML = data['data']['hemis_no'];
                    std_faculty.innerHTML = data['data']['faculty'];
                    std_dept.innerHTML = data['data']['dept'];
                    std_prog.innerHTML = data['data']['program'];
                    // std_status.innerHTML = data['data']['student_status'];

                    if (data['data']['student_status'] != 'learning'){
                        graduation_status.style.display = 'inline-block';
                        learning_status.style.display = 'none';

                    }else{
                        graduation_status.style.display = 'none';
                        learning_status.style.display = 'inline-block';
                    }

                    showResultSection()
                    // showProgressBar()
                } else if (data['status'] == 'error1'){
                    err_message_1.innerHTML = data['message'];
                    err_message_1.style.display = 'block';
                    hideProgressBar()
                    // showSearchSection()
                   
                }else if (data['status'] == 'error2'){
                    err_message_2.innerHTML = data['message'];
                    err_message_2.style.display = 'block';
                    hideProgressBar()
                    // showSearchSection()
                }else if (data['status'] == 'error3'){
                    err_message_3.innerHTML = data['message'];
                    err_message_3.style.display = 'block';
                    hideProgressBar()
                    // showSearchSection()
                }

            })
        })// End of then

}