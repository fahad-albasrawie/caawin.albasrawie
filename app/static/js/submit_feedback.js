

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function () {
  // Get the button by its ID
  var button = document.getElementById('search-helper-btn');

  // Listen for a click event on the button
  button.addEventListener('click', function () {
    // Add the 'clicked-effect' class to the button
    this.classList.add('clicked-effect');

    // Set a timeout to remove the class after 1 second (1000 milliseconds)
    setTimeout(() => {
      this.classList.remove('clicked-effect');
    }, 1000);
  });
});

// show or hide btn
function showHideBtn(hidden_btn, show_btn) {
  document.getElementById(hidden_btn).style.display = 'none';
  document.getElementById(show_btn).style.display = 'block';

} // End of showHideBtn


// Rating values ====================
let star = document.querySelectorAll('.start-rating');
let showValue = document.querySelector('#rating-value');

for (let i = 0; i < star.length; i++) {
  star[i].addEventListener('click', function () {
    i = this.value;

    showValue.innerHTML = i + " tiiba 5";
  });
}

// feedback, trainee_id, helper_id, request_id, stars
function get_data() {

  var feedback = document.getElementById('help_feedback')
  var trainee_id = document.getElementById('trainee_id')
  var helper_id = document.getElementById('helper_id')
  var request_id = document.getElementById('request_id')
  var stars = document.getElementById('rating-value')
  var topic_name = document.getElementById('help-title');


  // Messages
  var submit_feedback_err = document.getElementById('submit_feedback_err')
  var submit_feedback_success = document.getElementById('submit_feedback_success')

  submit_feedback_err.innerHTML = ''
  submit_feedback_success.innerHTML = ''

  // check if the user has entered all the required data or not and display the error message
  if (trainee_id.value == "" || helper_id.value == "") {

    console.log('Please fill all the fields')
    submit_feedback_err.innerHTML = 'Fadlan gali aqoonsigaaga iyo aqoonsiga qofka ku caawiyey.'
    submit_feedback_success.style.display = 'none'
    return;
  } else if (request_id.value == "") {

    console.log('Fadlan dooro cinwaanka laguugu caawiyey.')
    submit_feedback_err.innerHTML = 'Fadlan dooro cinwaanka laguugu caawiyey.'
    submit_feedback_success.style.display = 'none'
    return;
  }
  // now check if whole data data are entered
  else if (stars.innerHTML == 0) {

    console.log('Fadlan qiimee sida laguu caawiyey adigoo siinaya xiddigo.')
    submit_feedback_err.innerHTML = 'Fadlan qiimee sida laguu caawiyey adigoo siinaya xiddigo.'
    submit_feedback_success.style.display = 'none'
    return;
  }

  var data = {
    feedback: feedback.value,
    trainee_id: trainee_id.value,
    helper_id: helper_id.value,
    request_id: request_id.value,
    stars: stars.innerHTML,
    topic_name: topic_name.innerHTML
  }

  // display data
  console.log(data)

}


// Function to insert topics into dropdown items=======================================================================================================
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('request_id').value = '';  // Clears the input field
  // Clears the dropdown menu
    document.getElementById('topic-menu').innerHTML = '';
});
function insertTopics(topics) {
  const menu = document.getElementById('topic-menu');
  menu.innerHTML = ''; // Clear existing items if any

  topics.forEach(topic => {
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.className = 'dropdown-item';
      link.href = '#';
      link.textContent = topic.topic; // Ensure property name matches
      link.onclick = () => selectDropdownItem(topic.topic, topic.id);
      item.appendChild(link);
      menu.appendChild(item);
  });
}
// Function to update button text and input field on selection
function selectDropdownItem(topicName, topicId) {
  const button = document.getElementById('help-title');
  const input = document.getElementById('request_id');
  button.textContent = topicName;  // Set button text to the topic name
  input.value = topicId;  // Set input value to the topic id
}

// Example usage
// Assume you have received data from Python as follows:
const topicsData = [{'id': 1, 'topicname': "a"}, {'id': 2, 'topicname': 'b'}];
insertTopics(topicsData);  // Call this function when you want to populate the dropdown ==========================================================================


function search_helping_topics(hidden_btn, show_btn) {

            var trainee_id = document.getElementById('trainee_id');
            var helper_id = document.getElementById('helper_id');
            // var request_id = document.getElementById('request_id');
            // var topic_name = document.getElementById('help-title');


            // Messages
            var submit_feedback_err = document.getElementById('submit_feedback_err')
            var submit_feedback_success = document.getElementById('submit_feedback_success')

            submit_feedback_err.innerHTML = ''
            submit_feedback_success.innerHTML = ''

            // check if the user has entered all the required data or not and display the error message
            if (trainee_id.value == "" || helper_id.value == "") {
              console.log('Fadlan gali aqoonsigaaga iyo aqoonsiga qofka ku caawiyey.')
              submit_feedback_err.innerHTML = 'Fadlan gali aqoonsigaaga iyo aqoonsiga qofka ku caawiyey.'
              submit_feedback_success.style.display = 'none'
              return;
            }

            // Convert data into obj
            var data = {
              trainee_id: trainee_id.value,
              helper_id: helper_id.value,
            }

            console.log(data)

            showHideBtn(hidden_btn, show_btn)

            document.getElementById('request_id').value = '';  // Clears the input field
            // Clears the dropdown menu
            document.getElementById('topic-menu').innerHTML = '';

          // Sending data
          fetch('/search_helping_topics',
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
                // console.log(data)

                if (data['status'] == 'success') {
                  submit_feedback_err.innerHTML = ''
                  submit_feedback_success.innerHTML = 'Haa, waa la soo helay cinwaano laguugu caawinayey. Fadlan door ee ku soco.'
                  submit_feedback_success.style.display = 'block'
                  showHideBtn(show_btn, hidden_btn)
                  console.log(data['topics'])
                  insertTopics(data['topics'] ); // Call this function when you want to populate the dropdown ==========================================================================
                } else {
                  submit_feedback_err.innerHTML = data['text']
                  submit_feedback_success.innerHTML = ''
                  showHideBtn(show_btn, hidden_btn)
                }


              })
            })// End of then

}

function submit_help(hidden_btn, show_btn) {

              var feedback = document.getElementById('help_feedback')
              var trainee_id = document.getElementById('trainee_id')
              var helper_id = document.getElementById('helper_id')
              var request_id = document.getElementById('request_id')
              var stars = document.getElementById('rating-value')
              var topic_name = document.getElementById('help-title');


              // Messages
              var submit_feedback_err = document.getElementById('submit_feedback_err')
              var submit_feedback_success = document.getElementById('submit_feedback_success')

              submit_feedback_err.innerHTML = ''
              submit_feedback_success.innerHTML = ''

              // check if the user has entered all the required data or not and display the error message
              if (trainee_id.value == "" || helper_id.value == "") {

                console.log('Please fill all the fields')
                submit_feedback_err.innerHTML = 'Fadlan gali aqoonsigaaga iyo aqoonsiga qofka ku caawiyey.'
                submit_feedback_success.style.display = 'none'
                return;
              } else if (request_id.value == "") {

                console.log('Fadlan dooro cinwaanka laguugu caawiyey.')
                submit_feedback_err.innerHTML = 'Fadlan dooro cinwaanka laguugu caawiyey.'
                submit_feedback_success.style.display = 'none'
                return;
              }
              // now check if whole data data are entered
              else if (stars.innerHTML == 0) {

                console.log('Fadlan qiimee sida laguu caawiyey adigoo siinaya xiddigo.')
                submit_feedback_err.innerHTML = 'Fadlan qiimee sida laguu caawiyey adigoo siinaya xiddigo.'
                submit_feedback_success.style.display = 'none'
                return;
              }

              var data = {
                feedback: feedback.value,
                trainee_id: trainee_id.value,
                helper_id: helper_id.value,
                request_id: request_id.value,
                stars: stars.innerHTML,
                topic_name: topic_name.innerHTML
                
              }

              // display data
              // console.log(data)

  showHideBtn(hidden_btn, show_btn)

  // Sending data
  fetch('/submit_help_feedback',
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
        submit_feedback_err.innerHTML = 'Waanu ka xunnahay dhib baa dhacay, fadlan la xirriiri maamulka +252617306831'
        showHideBtn(show_btn, hidden_btn)
        return;
      }
      response.json().then(function (data) {
                // This is the message from Python
                console.log('Here is the Python Meaasge: ')
                // console.log(data)

                if (data['status'] == 'success') {
                  submit_feedback_err.innerHTML = ''
                  submit_feedback_success.innerHTML = data['text']
                  submit_feedback_success.style.display = 'block'

                  // Clear the form
                  feedback.value = ''
                  trainee_id.value = ''
                  helper_id.value = ''
                  request_id.value = ''
                  stars.innerHTML = '0'
                  topic_name.innerHTML = 'Cinwaankaan Ayaa'
                  document.getElementById('topic-menu').innerHTML = '';

                  showHideBtn(show_btn, hidden_btn)
                } else {
                  submit_feedback_err.innerHTML = data['text']
                  submit_feedback_success.innerHTML = ''
                  showHideBtn(show_btn, hidden_btn)
                }

      })
    })// End of then

}