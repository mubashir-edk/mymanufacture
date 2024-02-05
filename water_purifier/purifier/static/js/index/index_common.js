$(document).ready(function() {
    // modal close reload
    $('.modal-close').click(function() {
        // Reload the page when the close button is clicked
        location.reload();
    });

    $('#sideNavBoolean').change(function() {

        // sidenav = $('#sideNav');
        // maincontent = $('#mainContent');
        pageBody = $('#pageBodyView');

        if ($(this).prop('checked')) {
            console.log('Checkbox is checked');

            // Add a class to hide the sideNav
            // sidenav.addClass('hidesidenav');
            // maincontent.addClass('editmaincontent');
            pageBody.addClass('view-modify');

        } else {
            console.log('Checkbox is unchecked');

            // Remove the class to show the sideNav
            // sidenav.removeClass('hidesidenav');
            // maincontent.removeClass('editmaincontent');
            pageBody.removeClass('view-modify');
        }

    });

});