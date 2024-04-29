// show or hide btn
function showHideBtn(hidden_btn, show_btn) {
    document.getElementById(hidden_btn).style.display = 'none';
    document.getElementById(show_btn).style.display = 'block';

} // End of showHideBtn

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('checking_link_input').value = '';  // Clears the input field
    document.getElementById('google_drive_input').value = '';
    // Clears the dropdown menu
});
function openGoogleDriveLink() {

    var link = document.getElementById('google_drive_input').value;
    var checking_link_input = document.getElementById('checking_link_input');
    var submit_feedback_err = document.getElementById('googledrivelinkErr');
    var checking_link_btn = document.getElementById('checking_link_btn');

    submit_feedback_err.style.display = 'none';
    if (link) {
        // Opens the link in a new tab
        checking_link_input.value = 1;
        checking_link_btn.style.display = 'block';
        window.open(link, '_self');
    } else {
        submit_feedback_err.style.display = 'block';
    }
}


// window.onload = function() {
//     // Check if the div was previously displayed
//     if (localStorage.getItem('checkingLinkVisible') === 'true') {
//         document.getElementById('checking_link_btn').style.display = 'block';
//     }
// };

// function LinkChecked() {
//     var checking_link_btn = document.getElementById('checking_link_btn');
//     var link_checked = document.getElementById('link_checked');
//     var checking_link_input = document.getElementById('checking_link_input');
//     var work_submitted_err = document.getElementById('submit_feedback_err1')

//     // Hides the button and shows the message
//     work_submitted_err.innerHTML = ''
//     checking_link_btn.style.display = 'none';
//     link_checked.style.display = 'block';
//     checking_link_input.value = 2;

//     // Save the state to local storage
//     localStorage.setItem('checkingLinkVisible', 'true');
// }
window.onload = function() {
    var wasVisible = localStorage.getItem('checkingLinkVisible');
    console.log('Loaded state:', wasVisible);  // Debug: Check the loaded state

    if (wasVisible === 'true') {
        document.getElementById('checking_link_btn').style.display = 'block';
    } else {
        document.getElementById('checking_link_btn').style.display = 'none';
    }
};

function LinkChecked() {
    var checking_link_btn = document.getElementById('checking_link_btn');
    var link_checked = document.getElementById('link_checked');
    var checking_link_input = document.getElementById('checking_link_input');
    var work_submitted_err = document.getElementById('submit_feedback_err1');

    work_submitted_err.innerHTML = '';  // Clear error message

    if (checking_link_btn.style.display === 'block' || checking_link_btn.style.display === '') {
        checking_link_btn.style.display = 'none';
        link_checked.style.display = 'block';
        checking_link_input.value = 2;
        localStorage.setItem('checkingLinkVisible', 'false');
        console.log('Div hidden, state set to false');  // Debug: Log action
    } else {
        checking_link_btn.style.display = 'block';
        link_checked.style.display = 'none';
        checking_link_input.value = '';  // Reset value as needed
        localStorage.setItem('checkingLinkVisible', 'true');
        console.log('Div shown, state set to true');  // Debug: Log action
    }
}

// ============================================Gooooooooooooooood Looooooooooooooogic start

document.addEventListener('DOMContentLoaded', function () {
    const inputField = document.getElementById('wok_sender_id');
    const checkBoxTeam = document.getElementById('team_work');
    const checkBoxIndividual = document.getElementById('individual');
    const working_type_notice = document.getElementById('working_type_notice');

    inputField.addEventListener('input', function (event) {
        let value = inputField.value;

        // Prevent starting with a comma, having two consecutive commas, and ensure only numbers and commas
        if (value.startsWith(',') || /,,/.test(value) || /[^0-9,]/.test(value)) {
            inputField.value = value.slice(0, -1);
            return;
        }

        // Determine checkbox states based on input
        const numbers = value.split(',').filter(n => n.trim() !== '');
        if (numbers.length > 1) {
            checkBoxTeam.checked = true;
            checkBoxTeam.value = 'team';
            working_type_notice.innerHTML = 'Koox-koox ayaad u shaqayseen, fiican!'
            working_type_notice.style.color = '#FF5F1F'
            // working_type_notice.style.fontWeight = 'bold'
            checkBoxIndividual.checked = false;
        } else if (numbers.length === 1) {
            checkBoxIndividual.checked = true;
            checkBoxTeam.value = 'individual';
            working_type_notice.innerHTML = 'Adiga kaligaaga baad shaqaysay, baraawo!.'
            working_type_notice.style.color = '#FF974D'
            // working_type_notice.style.fontWeight = 'bold'
            checkBoxTeam.checked = false;
        } else {
            checkBoxIndividual.checked = false;
            checkBoxIndividual.value = '';
            checkBoxTeam.value = '';
            working_type_notice.innerHTML = ''
            checkBoxTeam.checked = false;
        }
    });

    inputField.addEventListener('keydown', function (event) {
        // Allow backspace, arrow keys, and numbers
        if (!event.key.match(/Backspace|ArrowLeft|ArrowRight|,/g) && (event.key < '0' || event.key > '9')) {
            event.preventDefault();
        }
    });

    inputField.addEventListener('paste', function (event) {
        // Prevent pasting into the input
        event.preventDefault();
    });
});


// ============================================Gooooooooooooooood Looooooooooooooogic end


// feedback, trainee_id, helper_id, request_id, stars
function get_data(hidden_btn, show_btn) {

    var work_type = document.getElementById('work_type')
    var checking_link = document.getElementById('checking_link_input')
    var google_drive = document.getElementById('google_drive_input')
    var wok_sender_id = document.getElementById('wok_sender_id')
    var work_desc = document.getElementById('work_desc')
    var submit_feedback_warning = document.getElementById('submit_feedback_warning')
    var link_checked = document.getElementById('link_checked');
    

    // const checkBoxTeam = document.getElementById('team_work');
    

    // Messages
    var work_submitted_err = document.getElementById('submit_feedback_err1')
    var work_submitted_success = document.getElementById('submit_feedback_success')
    var working_type_err_notice = document.getElementById('working_type_err_notice')

    work_submitted_err.innerHTML = ''
    work_submitted_success.innerHTML = ''
    submit_feedback_warning.innerHTML = ''
    work_submitted_success.style.display = 'none'
    submit_feedback_warning.style.display = 'none'
    link_checked.style.display = 'none';
    

    // check if the work type text is not "Dooro hawlmaalmeedka"
    if (work_type.value == 'Dooro hawlmaalmeedka' || work_type.value == '') {
        work_submitted_err.innerHTML = 'Fadlan dooro nooca hawlmaalmeedka.'

        return
    }

    // check if the work type text is not "Dooro hawlmaalmeedka"
    if (google_drive.value == '') {
        work_submitted_err.innerHTML = 'Fadlan buuxi godka lifaaqa (link-ga) GoogleDrive.'

        return
    }
    // check if the work type text is not "Dooro hawlmaalmeedka"
    if (wok_sender_id.value == '') {
        work_submitted_err.innerHTML = 'Fadlan buuxi godka aqoonsiga.'

        return
    }

    var team_work = false;
    // Check if the wok_sender_id length is greater than 1
    // note, check all are numbers separated by comma, and delete the first and last comma
    // Get the value from the input and trim whitespace
    var ids = wok_sender_id.value.trim();

    // Remove leading and trailing commas if present
    ids = ids.replace(/^,+|,+$/g, '');
    // Split the cleaned ids by commas to form an array
    var idArray = ids.split(',');

    console.log('Ids:', idArray, 'Number of IDs:', idArray.length);
    if (idArray.length > 1) {
        team_work = true;
    }
    

 



    // if the user checked the link or not
    if (checking_link.value == '1') {
        work_submitted_err.innerHTML = 'Fadlan taabo batoonka "Haa" haddii aad hubisay in lifaaqu (link-ga) shaqaynayo.'
        return
    } else if (checking_link.value == '') {
        work_submitted_err.innerHTML = 'Fadlan taabo batoonka lifaaqa (link-ga) si aah u hubiso in lifaaqa uu furmayo iyo in kale.'
        return
    }



    var data = {
        'work_type': work_type.value,
        'checking_link': checking_link.value,
        'google_drive': google_drive.value,
        'wok_sender_id': wok_sender_id.value,
        'work_desc': work_desc.value,
        'team_work': team_work
    }

    // display data
    console.log(data)

    showHideBtn(hidden_btn, show_btn)
    // Sending data
    fetch('/submit_work',
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
                work_submitted_err.innerHTML = 'Waanu ka xunnahay dhib baa dhacay, fadlan isku day mar kale ama la xirriiri maamulka +252617306831'
                showHideBtn(show_btn, hidden_btn)
                return;
            }
            response.json().then(function (data) {
                // This is the message from Python
                console.log('Here is the Python Meaasge: ')
                console.log(data)

                if (data['status'] == 'success') {
                    work_submitted_err.innerHTML = '';

                    team_work = data['team_work'];

                    // check if the team work is true or false
                    if (team_work) {
                        work_submitted_success.innerHTML = data['team_message'];
                        // check if there are unavailbel id
                        if (data['unavailable_ids']) {
                            console.log('Unavailable ids: ' + data['unavailable_ids'])
                            submit_feedback_warning.innerHTML = "Fiirmo gaar: Aqoonsiyadaan [" + data['unavailable_ids'] + "] lama helin, xogtoodana lama gudbin, fadlan hubi mar, kalana soo dira. Mahadsanidiin.";
                            submit_feedback_warning.style.display = 'block';
                        }
                    } else {
                        work_submitted_success.innerHTML = data['individual_message'];
                    }

                    

                    work_submitted_success.style.display = 'block'
                    showHideBtn(show_btn, hidden_btn);

                    // Clear the input fields
                    document.getElementById('work_type').value = 'Dooro hawlmaalmeedka';
                    document.getElementById('google_drive_input').value = '';
                    document.getElementById('wok_sender_id').value = '';
                    document.getElementById('work_desc').value = '';
                    document.getElementById('checking_link_input').value = '';
                    document.getElementById('team_work').checked = false;
                    document.getElementById('individual').checked = false;
                    document.getElementById('working_type_notice').innerHTML = '';
                    link_checked.style.display = 'none';
                    return;
                } else {
                    
                    work_submitted_err.innerHTML = data['text'];
                    work_submitted_success.innerHTML = '';
                    work_submitted_success.style.display = 'none'
                    showHideBtn(show_btn, hidden_btn);
                    return;
                }


            })
        })// End of then

}