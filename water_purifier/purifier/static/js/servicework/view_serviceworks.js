$(document).ready(function () {


    var productSelect = document.getElementById('formServiceWorkProduct');
    productSelect.innerHTML = '';

    $(productSelect).hide();

    $("#formServiceWorkCustomer").change(function () {

        productSelect.innerHTML = '';

        var selectedCustomer = $('#formServiceWorkCustomer').val();

        console.log(selectedCustomer);

    if (selectedCustomer !== '') {
        
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
                    option.text = '---------';
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

    } else {
        // If selectedCustomer is empty, hide the productSelect
        $(productSelect).hide();
    }

    });



    var serviceSelect = document.getElementById('formServiceWorkService');
    serviceSelect.innerHTML = '';

    $(serviceSelect).hide();

    $("#formServiceWorkProduct").change(function () {

        serviceSelect.innerHTML = '';

        var selectedProduct = $('#formServiceWorkProduct').val();

        console.log(selectedProduct);

    if (selectedProduct !== '') {
        
        $(serviceSelect).show();

        $.ajax({
            url: `/view_serviceworks/`,
            type: "GET",
            dataType: "json",
            data: {
                'selectedProduct': selectedProduct,
            },
            success: function (data) {

                
                // const products = data.products;

                console.log(data.products);

                var option = document.createElement('option');
                    option.value = '';
                    option.text = '---------';
                    option.selected;
                    serviceSelect.add(option);

                data.services.forEach(function (service) {
                    var option = document.createElement('option');
                    option.value = service.id;
                    option.text = service.name;
                    serviceSelect.add(option);
                });


            },
            error: function (error) {
                console.error(error);
            }
        });

    } else {
        // If selectedCustomer is empty, hide the productSelect
        $(serviceSelect).hide();
    }

    });


});