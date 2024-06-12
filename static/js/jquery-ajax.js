$(document).ready(function () {
    var successMessage = $("#jq-notification");

    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();

        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);
        var goodsInCartCount_2 = $("#goods-in-cart-count-2");
        var cartCount_2 = parseInt(goodsInCartCount_2.text() || 0);

        var product_id = $(this).data("product-id");

        var add_to_cart_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 5000);

                cartCount++;
                cartCount_2++;
                goodsInCartCount.text(cartCount);
                goodsInCartCount_2.text(cartCount_2);

                var cartItemsContainer1 = $("#cart-items-container-1");
                var cartItemsContainer2 = $("#cart-items-container-2");
                var cartItemsContainer3 = $("#cart-items-container-3");
                var cartItemsContainer4 = $("#cart-items-container-4");

                cartItemsContainer1.html(data.cart_items_html_1);
                cartItemsContainer2.html(data.cart_items_html_2);
                cartItemsContainer3.html(data.cart_items_html_3);
                cartItemsContainer4.html(data.cart_items_html_4);

            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });




    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault();

        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);
        var goodsInCartCount_2 = $("#goods-in-cart-count-2");
        var cartCount_2 = parseInt(goodsInCartCount_2.text() || 0);

        var cart_id = $(this).data("cart-id");
        var remove_from_cart = $(this).attr("href");

        $.ajax({

            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {

                successMessage.html(data.message);
                successMessage.fadeIn(400);

                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 5000);

                cartCount -= data.quantity_deleted;
                goodsInCartCount.text(cartCount);
                cartCount_2 -= data.quantity_deleted;
                goodsInCartCount_2.text(cartCount_2);

                var cartItemsContainer1 = $("#cart-items-container-1");
                var cartItemsContainer2 = $("#cart-items-container-2");
                var cartItemsContainer3 = $("#cart-items-container-3");
                var cartItemsContainer4 = $("#cart-items-container-4");

                cartItemsContainer1.html(data.cart_items_html_1);
                cartItemsContainer2.html(data.cart_items_html_2);
                cartItemsContainer3.html(data.cart_items_html_3);
                cartItemsContainer4.html(data.cart_items_html_4);

            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });




    $(document).on("click", ".decrement", function () {
        var url = $(this).data("cart-change-url");
        var cartID = $(this).data("cart-id");
        var $input = $(this).closest('.inp-group').find('.number');
        var currentValue = parseInt($input.val());
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            updateCart(cartID, currentValue - 1, -1, url);
        }
    });

    $(document).on("click", ".increment", function () {
        var url = $(this).data("cart-change-url");
        var cartID = $(this).data("cart-id");
        var $input = $(this).closest('.inp-group').find('.number');
        var currentValue = parseInt($input.val());

        $input.val(currentValue + 1);

        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                     successMessage.fadeOut(400);
                }, 5000);

                var goodsInCartCount = $("#goods-in-cart-count");
                var cartCount = parseInt(goodsInCartCount.text() || 0);
                var goodsInCartCount_2 = $("#goods-in-cart-count-2");
                var cartCount_2 = parseInt(goodsInCartCount_2.text() || 0);
                cartCount += change;
                goodsInCartCount.text(cartCount);
                cartCount_2 += change;
                goodsInCartCount_2.text(cartCount_2);

                var cartItemsContainer1 = $("#cart-items-container-1");
                var cartItemsContainer2 = $("#cart-items-container-2");
                var cartItemsContainer3 = $("#cart-items-container-3");
                var cartItemsContainer4 = $("#cart-items-container-4");

                cartItemsContainer1.html(data.cart_items_html_1);
                cartItemsContainer2.html(data.cart_items_html_2);
                cartItemsContainer3.html(data.cart_items_html_3);
                cartItemsContainer4.html(data.cart_items_html_4);

            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    }

    var notification = $('#notification');
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 5000);
    }



    // Обработчик события радиокнопки выбора способа доставки
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});