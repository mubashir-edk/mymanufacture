$(document).ready(function () {

    var productSelect = document.getElementById('formServiceWorkProduct');
    var productSelectLabel = document.getElementById('serviceWorkProductLabel');
    productSelect.innerHTML = '';

    $(productSelectLabel).hide();
    $(productSelect).hide();

    $("#formServiceWorkCustomer").change(function () {

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
        $(productSelectLabel).hide();
        $(productSelect).hide();
    }

    });


    var serviceSelect = document.getElementById('formServiceWorkService');
    var serviceSelectLabel = document.getElementById('serviceWorkServiceLabel');
    serviceSelect.innerHTML = '';

    $(serviceSelectLabel).hide();
    $(serviceSelect).hide();

    $("#formServiceWorkProduct").change(function () {

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

                data.services.forEach(function (service) {
                    var checkbox = $('<input type="checkbox">').attr({
                        id: 'service_' + service.id,
                        value: service.id,
                        name: 'service_' + service.id, // Adjust the name as needed for form submission
                        class: 'form-checkbox',
                    });
                    var label = $('<label>').attr('for', 'service_' + service.id).addClass('form-label').text(service.name);
                    $(serviceSelect).append(checkbox).append(label).append('<br>');
                });


            },
            error: function (error) {
                console.error(error);
            }
        });

    } else {
        $(serviceSelectLabel).hide();
        $(serviceSelect).hide();
    }

    });

});