// tinymce.init({
//     selector: '#help_decs',
//     setup: function(editor) {
//         editor.on('init', function() {
//             // Set initial character count
//             updateCharCount(editor.getContent().length);
            
//             // Update character count on every change
//             editor.on('input', function() {
//                 updateCharCount(editor.getContent().length);
//             });

//             // Disable typing when character limit is reached
//             editor.on('keydown', function(e) {
//                 const maxLength = 10;
//                 const currentLength = editor.getContent({ format: 'text' }).length;
//                 if (currentLength >= maxLength && e.key.length === 1 && !e.ctrlKey && !e.metaKey) {
//                     e.preventDefault();
//                 }
//             });
//         });
//     }
// });

// function updateCharCount(length) {
//     const maxLength = 10;
//     const charsSpan = document.getElementById('chars');
//     charsSpan.textContent = length;
//     // If the length exceeds the maximum, set the color to red
//     if (length > maxLength) {
//         charsSpan.style.color = 'red';
//     } else {
//         charsSpan.style.color = ''; // Reset to default color
//     }
// }

tinymce.init({
    selector: '#help_decs',
    setup: function (editor) {
        function updateCount() {
            var textLength = editor.getContent({format: 'text'}).length; // Get text content length
            var charCounter = document.getElementById('chars');
            charCounter.textContent = textLength; // Update the counter display
            // help_decs_chars.value = textLength; // Update the hidden input field
        }

        editor.on('init', updateCount); // Update count on init
        editor.on('keyup', updateCount); // Update count on keyup

        // Allowing specific keys to function even after reaching the limit
        editor.on('keydown', function (e) {
            var textLength = editor.getContent({format: 'text'}).length;
            // Allow backspace (8), delete (46), and arrow keys (37-40), and Ctrl combinations (e.g., cut/copy/paste)

             // Messages
             var ask_help_error_message_container = document.getElementById('ask_help_error_message_container') 
             var ask_help_error_message = document.getElementById('ask_help_error_message') 
             ask_help_error_message_container.style.display = 'none'

            if (textLength >= 601 && !(
                e.keyCode === 8 || 
                e.keyCode === 46 || 
                (e.keyCode >= 37 && e.keyCode <= 40) ||
                e.ctrlKey
            )) {
                e.preventDefault(); // Stop the default action of the event
                e.stopPropagation(); // Stop the propagation of the event

               

                ask_help_error_message_container.style.display = 'block'
                ask_help_error_message.innerHTML = 'Fadlan warbixinta codsigaaga ku soo koob ugu badnaan 600 xarfo.'
                // alert('Maximum character limit of 10 reached.'); // Alert the user
                return false; // Return false to directly cancel the event
            }
        });
    }
});


// alert("Hello from ask_help.js!")
// show or hide btn
function showHideBtn(hidden_btn, show_btn) {
    document.getElementById(hidden_btn).style.display = 'none';
    document.getElementById(show_btn).style.display = 'inline-block';

} // End of showHideBtn

function get_data(){
    var full_name = document.getElementById('full_name')
    var phone_number = document.getElementById('phone_number')
    var trainee_id = document.getElementById('trainee_id')
    var help_type = document.getElementById('help_type')
    var help_topic = document.getElementById('help_topic')
    var help_decs = tinymce.get('help_decs');


    // Messages
    var ask_help_error_message_container = document.getElementById('ask_help_error_message_container') 
    var ask_help_error_message = document.getElementById('ask_help_error_message') 
    var ask_help_success_message = document.getElementById('ask_help_success_message') 
    var ask_help_success_message_container = document.getElementById('ask_help_success_message_container')

        // check if the user has entered all the required data or not and display the error message
        if (full_name.value == "" || phone_number.value == "" || trainee_id.value == "" || help_type.value == "" || help_topic.value == "" || help_decs.getContent() == "") {
        
            console.log('Please fill all the fields')
            ask_help_error_message_container.style.display = 'block'
            ask_help_success_message_container.style.display = 'none'
            ask_help_error_message.innerHTML = 'Waanu ka xunnahay tababbarte, fadlan buuxi dhammaan xogta.'
    
            return;
        }


    var data = {
        full_name: full_name.value,
        phone_number: phone_number.value,
        trainee_id: trainee_id.value,
        help_type: help_type.value,
        help_topic: help_topic.value,
        help_decs: help_decs.getContent()
    }

    // display data
    console.log(data)

    ask_help_error_message_container.style.display = 'none'
    ask_help_success_message_container.style.display = 'block'
    ask_help_success_message.innerHTML = 'Waanu ka xunnahay tababbarte, fadlan buuxi dhammaan xogta.'
}


function ask_help(hidden_btn, show_btn) {

    var full_name = document.getElementById('full_name')
    var phone_number = document.getElementById('phone_number')
    var trainee_id = document.getElementById('trainee_id')
    var help_type = document.getElementById('help_type')
    var help_topic = document.getElementById('help_topic')
    var help_decs = tinymce.get('help_decs');

    var help_decs_chars = document.getElementById('chars');
    


    // Messages
    var ask_help_error_message_container = document.getElementById('ask_help_error_message_container') 
    var ask_help_error_message = document.getElementById('ask_help_error_message') 
    var ask_help_success_message = document.getElementById('ask_help_success_message') 
    var ask_help_success_message_container = document.getElementById('ask_help_success_message_container')

    ask_help_error_message_container.style.display = 'none'
    ask_help_success_message_container.style.display = 'none'

    // check if the user has entered all the required data or not and display the error message
    if (full_name.value == "" || phone_number.value == "" || trainee_id.value == "" || help_type.value == "" || help_topic.value == "" || help_decs.getContent() == "") {
    
        console.log('Please fill all the fields')
        ask_help_error_message_container.style.display = 'block'
        ask_help_success_message_container.style.display = 'none'
        ask_help_error_message.innerHTML = 'Waanu ka xunnahay tababbarte, fadlan buuxi dhammaan xogta.'

        return;
    }

    // Convert data into obj
    var data = {
        full_name: full_name.value,
        phone_number: phone_number.value,
        trainee_id: trainee_id.value,
        help_type: help_type.value,
        help_topic: help_topic.value,
        help_decs: help_decs.getContent(),
        help_decs_chars: help_decs_chars.innerText
    }

    console.log(data)

    showHideBtn(hidden_btn, show_btn)

    // Sending data
    fetch('/ask_help',
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
                return;
            }
            response.json().then(function (data) {
                // This is the message from Python
                console.log('Here is the Python Meaasge: ')
                console.log(data)

                if(data['status'] == 'success'){
                    ask_help_error_message_container.style.display = 'none'
                    ask_help_success_message_container.style.display = 'block'
                    ask_help_success_message.innerHTML = data['text']

                    // Clear the form
                    full_name.value = ''
                    phone_number.value = ''
                    trainee_id.value = ''
                    help_type.value = ''
                    help_topic.value = ''
                    help_decs.setContent('')
                    help_decs_chars.innerText = '0'
                    

                    showHideBtn(show_btn, hidden_btn)
                }else{
                    ask_help_error_message_container.style.display = 'block'
                    ask_help_success_message_container.style.display = 'none'
                    ask_help_error_message.innerHTML = data['text']
                    showHideBtn(show_btn, hidden_btn)
                }
              

            })
        })// End of then
   
}