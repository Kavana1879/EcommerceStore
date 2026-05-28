document.addEventListener('DOMContentLoaded', function() {
    var updateBtns = document.getElementsByClassName('update-cart');

    for (var i = 0; i < updateBtns.length; i++) {
        updateBtns[i].addEventListener('click', function(e){
            e.preventDefault();
            var productId = this.dataset.product;
            var action = this.dataset.action;
            updateUserOrder(productId, action);
        });
    }

    function updateUserOrder(productId, action){
        var url = '/update_item/';

        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            }, 
            body: JSON.stringify({'productId': productId, 'action': action})
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            if (action === 'add') {
                showToast("Item added to your cart!");
                // Update cart count badge
                var cartTotal = document.getElementById('cart-total');
                if(cartTotal) {
                    cartTotal.innerText = parseInt(cartTotal.innerText) + 1;
                }
            } else {
                location.reload(); // Reload for removes to update totals accurately
            }
        });
    }

    function showToast(message) {
        var toastEl = document.getElementById('cartToast');
        if (toastEl) {
            var toastBody = toastEl.querySelector('.toast-body');
            toastBody.innerText = message;
            var toast = new bootstrap.Toast(toastEl);
            toast.show();
        } else {
            alert(message);
        }
    }
});
