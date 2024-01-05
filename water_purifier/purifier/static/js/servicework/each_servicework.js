$(document).ready(function () {

    var selectedCustomer = $('#formServiceWorkCustomer').val();

    console.log(selectedCustomer);

    var productSelect = document.getElementById('formServiceWorkProduct');
    var productSelectLabel = document.getElementById('serviceWorkProductLabel');
    // productSelect.innerHTML = '';

    var serviceSelect = document.getElementById('formServiceWorkService');
    var serviceSelectLabel = document.getElementById('serviceWorkServiceLabel');
    // serviceSelect.innerHTML = '';

    $(serviceSelectLabel).show();
    $(serviceSelect).show();

    $(productSelectLabel).show();
    $(productSelect).show();


    function productChange() {

        console.log('in product');

        productSelect.innerHTML = '';

        var selectedCustomer = $('#formServiceWorkCustomer').val();

        console.log(selectedCustomer);

        if (selectedCustomer !== '') {
            
            $(productSelectLabel).show();
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
                        option.selected = true;
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
            $(productSelectLabel).hide();
            $(productSelect).hide();

            $(serviceSelectLabel).hide();
            $(serviceSelect).hide();
        }

    }


    function serviceChange() {

        console.log('in service');
        serviceSelect.innerHTML = '';

        var selectedProduct = $('#formServiceWorkProduct').val();

        console.log(selectedProduct);

    if (selectedProduct !== '') {
        
        $(serviceSelectLabel).show();
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
                    option.selected = true;
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
        $(serviceSelectLabel).hide();
        $(serviceSelect).hide();
    }
    }


    $("#formServiceWorkCustomer").change(function () {

        productChange();

    });



    

    $("#formServiceWorkProduct").change(function () {

        serviceChange();

    });


});