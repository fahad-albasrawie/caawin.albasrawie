


function changePage(hrefValue) {
    // Check if the hrefValue is a valid URL
    console.log(hrefValue);
    if (!/^https?:\/\//i.test(hrefValue)) {
        console.error("Invalid URL format. Please provide a valid URL starting with 'http://' or 'https://'.");
        return;
    }
    
    // Change the current page's URL
    window.location.href = hrefValue;
}


function hide_sidebar(sidebar, hide_sidebar_btn, show_sidebar_btn) {
    // Hide the sidebar by class name
    // Hide the sidebar by adding d-none class
    document.querySelector('.' + sidebar).classList.add("d-none");
    // hide hide-sidebar-btn using Style

    document.querySelector('.' + hide_sidebar_btn).classList.add("d-none")
    document.querySelector('.' + show_sidebar_btn).classList.remove("d-none");


    console.log("Sidebar hidden");
}

function show_sidebar(sidebar, hide_sidebar_btn, show_sidebar_btn) {
    // Show the sidebar by class name
    // Show the sidebar by removing d-none class
    document.querySelector('.' + sidebar).classList.remove("d-none");
    // Ensure that on larger screens, the sidebar is visible
    // Ensure that on larger screens, the sidebar is visible
    if (window.matchMedia('(min-width: 992px)').matches) {
        document.querySelector('.' + sidebar).classList.remove("d-md-block");
    }

    document.querySelector('.' + hide_sidebar_btn).classList.remove("d-none");
    document.querySelector('.' + show_sidebar_btn).classList.add("d-none")
    console.log("Sidebar shown");
}


document.querySelectorAll('.admin_avater').forEach(item => {
    item.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        // Add your custom click event handling logic here
    });
});


function clickMe() {
    console.log('Button clicked');
}