// alert("Hello from submit_feedback.js!")

function selectDropdownItem(text_length){
    var help_title = document.getElementById("help-title");


    // cut chars if the data chars are more than 15 chars and if it is less than 15 chars then add dots that makes 15 chars
    var data = text_length.length > 15 ? text_length.substring(0, 15) : text_length + ".".repeat(15 - text_length.length);

   
    help_title.innerHTML =  data;
}


  // Wait for the DOM to load
  document.addEventListener('DOMContentLoaded', function() {
    // Get the button by its ID
    var button = document.getElementById('search-helper-btn');
    
    // Listen for a click event on the button
    button.addEventListener('click', function() {
      // Add the 'clicked-effect' class to the button
      this.classList.add('clicked-effect');
      
      // Set a timeout to remove the class after 1 second (1000 milliseconds)
      setTimeout(() => {
        this.classList.remove('clicked-effect');
      }, 1000);
    });
  });



// Rating values ====================
let star = document.querySelectorAll('.start-rating');
let showValue = document.querySelector('#rating-value');

for (let i = 0; i < star.length; i++) {
	star[i].addEventListener('click', function() {
		i = this.value;

		showValue.innerHTML = i + " tiiba 5";
	});
}