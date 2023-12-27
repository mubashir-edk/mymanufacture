$(document).ready(function () {


    var productSelect = document.getElementById('formServiceWorkProduct');
    productSelect.innerHTML = '';

    $(productSelect).hide();

    $("#formServiceWorkCustomer").change(function () {

        var selectedCustomer = $('#formServiceWorkCustomer').val();

        console.log(selectedCustomer);

        $(productSelect).show();

        $.ajax({
            url: `/view_serviceworks/`,
            type: "GET",
            dataType: "json",
            data: {
                'selectedCustomer': selectedCustomer,
            },
            success: function (data) {

                
                // const products = data.products;

                console.log(data.products);

                var option = document.createElement('option');
                    option.value = '';
                    option.text = '';
                    option.selected;
                    productSelect.add(option);

                data.products.forEach(function (product) {
                    var option = document.createElement('option');
                    option.value = product.id;
                    option.text = product.name;
                    productSelect.add(option);
                });


            },
            error: function (error) {
                console.error(error);
            }
        });

    });
});