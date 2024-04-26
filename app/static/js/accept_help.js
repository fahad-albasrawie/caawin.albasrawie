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
      tab.addEventListener('click', function() {
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
document.addEventListener('DOMContentLoaded', function() {
    openTab(event, 'Guud');
});
  // Show tap content end =========================================================