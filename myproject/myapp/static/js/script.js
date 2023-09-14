$(document).ready(function() {

// side-nav toggle

const checkbox = document.getElementById("check");
const sideNav = document.getElementById("sideNav");
const navBrand = document.getElementById("navbrandImg");
const sideNavContent = document.querySelectorAll("#sideNavContent");
const chevIcon = document.querySelectorAll("#chevron-icon");
const collapseElements = document.querySelectorAll(".collapse");
const sideNavsubhead = document.querySelectorAll(".sidenav-subhead");
const sideNavFooter = document.getElementById("sideNavFooter");
const sideNavAlign = document.querySelectorAll("#dropdownMenuLink");


sideNavAlign.forEach(alignnav => alignnav.style.justifyContent = "space-between");


function applyIfCondition() {
    sideNav.style.width = "72px";
    sideNav.style.overflowY = "hidden";
    sideNav.style.overflowX = "hidden";
    sideNavAlign.forEach(alignnav => alignnav.style.justifyContent = "center");
    navBrand.style.display = "none";
    sideNavContent.forEach(content => content.style.display = "none");
    chevIcon.forEach(icon => icon.style.display = "none");
    collapseElements.forEach(collapse => collapse.classList.remove("show"));
    sideNavsubhead.forEach(subhead => subhead.style.visibility = "hidden");
    sideNavFooter.style.visibility = "hidden";
}

function applyElseCondition() {
    sideNav.style.width = "293px";
    sideNav.style.overflowY = "visible";
    navBrand.style.display = "inline";
    sideNavContent.forEach(content => content.style.display = "inline");
    sideNavAlign.forEach(alignnav => alignnav.style.justifyContent = "space-between");
    chevIcon.forEach(icon => icon.style.display = "inline");
    collapseElements.forEach(collapse => collapse.classList.remove("show"));
    sideNavsubhead.forEach(subhead => subhead.style.visibility = "visible");
    sideNavFooter.style.visibility = "visible";
}

function enableHoverEffects() {
    sideNav.addEventListener("mouseenter", function() {
        if (checkbox.checked) {
            applyElseCondition();

            checkButton.addEventListener("click", function() {
                // checkbox.checked = false; // Set checkbox back to false
                applyElseCondition();
            });
        }
    });

    sideNav.addEventListener("mouseleave", function() {
        if (checkbox.checked) {
            applyIfCondition();
        }
    });
}

document.getElementById("checkButton").addEventListener("click", function() {
    checkbox.checked = !checkbox.checked; // Set checkbox to true

    if (checkbox.checked) {
        applyIfCondition();
        enableHoverEffects();
    } else {
        applyElseCondition();
    }
});
    

// sidenav dropdown arrow rotate
const chevronIcon = document.getElementById('chevron-icon');
const dropdownDashboard = document.getElementById('dropdownDashboard');

dropdownDashboard.addEventListener('show.bs.collapse', function () {
    chevronIcon.classList.remove('bi-chevron-down');
    chevronIcon.classList.add('bi-chevron-up');
});

dropdownDashboard.addEventListener('hide.bs.collapse', function () {
    chevronIcon.classList.remove('bi-chevron-up');
    chevronIcon.classList.add('bi-chevron-down');
});


// sidenav dropdown one collapse at a time
$(".navbar-toggle").click(function() {
  var target = $(this).data("target"); // Get the data-bs-target value
  
  $(".collapse").not(target).collapse("hide"); // Close all other open dropdowns
});


// popovers
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="hover"]'));
var options = {
    trigger: 'hover', // Show popover on hover
    placement: 'top', // Position the popover above the element
    content: '200+ in-house components and 3rd-party plugins', // Content of the popover
};
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl)
    {
        return new bootstrap.Popover(popoverTriggerEl, options);
    });


});
// scroll Top

var amountScrolled = 250;
var scrollbtn = document.getElementById("scroll-top")

$(window).scroll(function() {

    if ( $(window).scrollTop() > amountScrolled ) {
        $('button.scroll-top').addClass('show');
    } else {
        $('button.scroll-top').removeClass('show');
    }

});

$('button.scroll-top').click(function() {
    $('html, body').animate({
        scrollTop: 0
    }, 10);
    return false;
});




