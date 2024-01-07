$(document).ready(function() {

    var productDetails = document.querySelectorAll('.product-details');

    productDetails.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            // customer_id = link.getAttribute('data-bs-customer');
            var product_id = link.getAttribute('data-bs-product');
            // console.log(customer_id);
            // console.log(product_id);

        });
    });

    

    $(".custom-card").click(function(e) {
        e.preventDefault();

        console.log("knsfy");
        // var product_id = $(this).data('bs-product');

        console.log(product_id);

        // Make an AJAX request to the update_category view
        
        $.ajax({
            url: `/fetch_customer_products/`,
            type: 'GET',
            dataType: 'json',
            data: {'product_id': product_id},
            success: function(data) {

                $('#productDetailsModalTitle').text(data.product.name);

            },
            error: function(error) {
                console.error('Error fetching product_details view:', error);
            }
        });
    });
});