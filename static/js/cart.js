

const updateCartButtons =document.getElementsByClassName('updateCart')


for (let i=0;i<updateCartButtons.length;i++){
    updateCartButtons[i].addEventListener('click',function(){
        
        const productId=this.getAttribute('data-product');
        const action =this.dataset.action
        console.log(`id ${productId} and action ${action}`)
        

        if (user === 'AnonymousUser') {
            console.log('User is not logged in')
            addCookieItem(productId, action)
            
        }else{
            console.log('User is authenticated, sending data...')
            updateUserCart(productId, action)
        }
    })
}


// Function to update the user's cart

function addCookieItem(productId, action) {
    console.log('User is not authenticated, adding item to cookie...');

    if (action === 'add') {
        if (cart[productId] === undefined) {
            cart[productId] = {'quantity': 1}
        } else {
            cart[productId]['quantity'] += 1
        }
    }

    if (action === 'remove') {
        cart[productId]['quantity'] -= 1
        if (cart[productId]['quantity'] <= 0) {
            console.log('Item removed from cart')
            delete cart[productId]
        }
    }

    console.log('Cart:', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
}



const updateUserCart = (productId, action) => {
    console.log('User is authenticated, sending data...');

    const url = '/update-cart/';
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken // Ensure you have a function to get the CSRF token
        },
        body:JSON.stringify({
            productId: productId,
            action: action
        })
    })
    .then(
        response=> response.json()
    )
    .then (data => {
        console.log('Data:', data);
        location.reload() // Reload the page to reflect changes in the cart
    })
    .catch(Error=> console.log('Error:', Error));
}




// const updateCartButtons = document.querySelectorAll('.update-cart');
// updateCartButtons.forEach(button => {
//     button.addEventListener('click', function(event) {
//         event.preventDefault();
//         const productId = this.getAttribute('data-product');
//         const action = this.getAttribute('data-action');

//         fetch('/update-cart/', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-CSRFToken': getCookie('csrftoken')
//             },
//             body: JSON.stringify({
//                 productId: productId,
//                 action: action
//             })
//         })
//         .then(response => response.json())
//         .then(data => {
//             console.log('Cart updated:', data);
//             // Optionally, update the cart UI here
//         })
//         .catch(error => {
//             console.error('Error updating cart:', error);
//         });
//     });
// });