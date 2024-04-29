function copyTextToClipboard(helping_message_id, tick_icon_id, copy_icon_id) {
  // Get the text from the div
  var textToCopy = document.getElementById(helping_message_id).innerText;

  // Use the Clipboard API to copy the text
  navigator.clipboard.writeText(textToCopy).then(function () {
    // Success: Display and then hide the copied message
    var copy_icon = document.getElementById(copy_icon_id);
    var tick_icon = document.getElementById(tick_icon_id);
    // Optionally, you can show a message indicating the copy was successful.
    // var messageDiv = document.getElementById("std_hemis_no");
    // messageDiv.innerHTML = "Waa la guuriyey!";
    copy_icon.style.display = 'none';
    tick_icon.style.display = 'inline';
    setTimeout(function () {
      // Optionally, reset the message after some time.
      // messageDiv.innerHTML = "Guuri farriinta";
      copy_icon.style.display = 'inline';
      tick_icon.style.display = 'none';
    }, 2000);
  }).catch(function (err) {
    // Error handling
    console.error('Could not copy text: ', err);
  });
}


// function copyTextDelayTime(info_btn, info_text){
//   document.getElementById(info_btn).addEventListener('click', function() {
//     var infoText = document.getElementById(info_text);
//     infoText.style.display = 'block'; // Show the info text

//     // Set a timeout to hide the info text after 3 seconds
//     setTimeout(function() {
//         infoText.style.display = 'none'; // Hide the info text
//     }, 4000);
//   });

// }



document.addEventListener('DOMContentLoaded', (event) => {
  // Get all tabs in a NodeList
  const tabs = document.querySelectorAll('.message-taps');

  // Function to remove classes
  function removeClasses() {
    tabs.forEach(tab => {
      tab.classList.remove('border-bottom', 'border-2', 'border-primary', 'text-primary');
      tab.querySelector('button').classList.remove('text-primary');
    });
  }

  // Function to add classes to the active tab
  function addClasses(activeTab) {
    activeTab.classList.add('border-bottom', 'border-2', 'border-primary');
    activeTab.querySelector('button').classList.add('text-primary');
  }

  // Add click event listener to each tab
  tabs.forEach(tab => {
    tab.addEventListener('click', function () {
      removeClasses(); // First, remove the classes from all tabs
      addClasses(this); // Then, add them to the clicked tab
    });
  });
});
// Show tap content =========================================================
function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tabbuttons;

  // Get all elements with class="tab-content" and hide them
  tabcontent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tab-button" and remove the class "active"
  tabbuttons = document.getElementsByClassName("tab-button");
  for (i = 0; i < tabbuttons.length; i++) {
    tabbuttons[i].className = tabbuttons[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

// Initialize the default tab
document.addEventListener('DOMContentLoaded', function () {
  openTab(event, 'Guud');
});
// Show tap content end =========================================================












// Sending data =========================================================================

function get_data(trainee_id, helper_id, request_id, message_card_id) {

  var trainee_id = document.getElementById(trainee_id)
  var helper_id = document.getElementById(helper_id)
  var request_id = document.getElementById(request_id)
  var message_card = document.getElementById(message_card_id)

  message_card.style.display = 'block'

  var data = {
    trainee_id: trainee_id.innerHTML,
    helper_id: helper_id.value,
    request_id: request_id.innerHTML
  }

  // display data
  console.log(data)

}



function show_dive_hide_eye(div_id, eye_id, hidden_eye) {
  var div = document.getElementById(div_id)
  var eye = document.getElementById(eye_id)
  var hidden_eye = document.getElementById(hidden_eye)
  hidden_eye.style.display = 'inline-block'
  eye.style.display = 'none'
  div.style.display = 'block'
}

function show_eye_hide_dive(div_id, eye_id) {
  var div = document.getElementById(div_id)
  var eye = document.getElementById(eye_id)
  eye.style.display = 'inline-block'
  div.style.display = 'none'
}




// show or hide btn
function showHideBtn(hidden_btn, show_btn) {
  document.getElementById(hidden_btn).style.display = 'none';
  document.getElementById(show_btn).style.display = 'block';

} // End of showHideBtn

function accept_help(hidden_btn, show_btn, accept_help_btn,
   trainee_id, helper_id, request_id, 
   message_card_id,
   accept_help_error_message_container,
   accept_help_error_message,
   accept_help_success_message,
   accept_help_success_message_container,
   helper_placeholder_id1,
   helper_placeholder_id2
  ) {

  var trainee_id = document.getElementById(trainee_id)
  var helper_id = document.getElementById(helper_id)
  var request_id = document.getElementById(request_id)
  var message_card = document.getElementById(message_card_id)

  var accept_help_error_message_container = document.getElementById(accept_help_error_message_container)
  var accept_help_error_message = document.getElementById(accept_help_error_message)
  var accept_help_success_message = document.getElementById(accept_help_success_message)
  var accept_help_success_message_container = document.getElementById(accept_help_success_message_container)

  var accept_help_btn = document.getElementById(accept_help_btn)

  var helper_placeholder1 = document.getElementById(helper_placeholder_id1)
  var helper_placeholder2 = document.getElementById(helper_placeholder_id2)
  
  accept_help_error_message_container.style.display = 'none'
  accept_help_success_message_container.style.display = 'none'



  // check if the user has entered all the required data or not and display the error message
  console.log(helper_id.value)
  if (helper_id.value === "") {

    console.log('Please fill all the fields')
    accept_help_error_message_container.style.display = 'block'
    accept_help_success_message_container.style.display = 'none'
    accept_help_error_message.innerHTML = 'Waanu ka xunnahay caawiye, fadlan soo gali aqoonsigaaga.'

    return;
  }

  // Convert data into obj
  var data = {
    trainee_id: trainee_id.innerHTML,
    helper_id: helper_id.value,
    request_id: request_id.innerHTML
  }

  console.log(data)

  // show or hide btn
  message_card.style.display = 'none'
  accept_help_btn.style.display = 'none'
  showHideBtn(hidden_btn, show_btn)

  // Sending data
  fetch('/accept_helping',
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

        if (data['status'] == 'success') {

          accept_help_error_message_container.style.display = 'none'
          accept_help_success_message_container.style.display = 'block'
          accept_help_success_message.innerHTML = data['text']

          // hide the message card
          showHideBtn(show_btn, hidden_btn)

          helper_placeholder1.innerText = data['helper_full_name']
          helper_placeholder2.innerText = data['helper_full_name']
          
          message_card.style.display = 'block'



        } else {
          accept_help_error_message_container.style.display = 'block'
          accept_help_success_message_container.style.display = 'none'
          accept_help_error_message.innerHTML = data['text']

          accept_help_btn.style.display = 'block'
          // hidden_btn.style.display = 'none'
          document.getElementById(hidden_btn).style.display = 'none';
          document.getElementById(show_btn).style.display = 'none';
        }


      })
    })// End of then

} // End of ask_help