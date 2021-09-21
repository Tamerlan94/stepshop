$(document).ready(function () {
    const inp = $('.basket_list');

    function change_inp (t_href, current) {
         console.log(t_href);
        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data){
                if (t_href.value > 0) {
                    $('.basket_summary').replaceWith(data.result);
                    current.parent().next().text('$' + data.product_total_price);
                } else {
                    current.parent().parent().detach();
                }
            },
        });
    }

    inp.on('click', 'input[type=number]', function (event) {
        change_inp(event.target, $(this));
    });

    $('.table').on('click', '.row_delete', function(e){

        var tr = $(this).closest('tr');
        var idx = $(this).data('index');
        console.log(idx);
        $.ajax({
            url: "/basket/remove/" + idx + "/",
            success: function(data){
                tr.remove();
                $('.basket_summary').replaceWith(data.result);
                    current.parent().next().text('$' + data.product_total_price);
            }
        });
    });
});