

const updateCartButtons =document.getElementsByClassName('updateCart')


for (let i=0;i<updateCartButtons.length;i++){
    updateCartButtons[i].addEventListener('click',function(){
        
        const productId=this.getAttribute('data-product');
        const action =this.dataset.action
        console.log(`id ${productId} and action ${action}`)
        

        if (user === 'AnonymousUser') {
            console.log('User is not logged in')
            alert('Please log in to add items to your cart.')
        }else{
            console.log('User is authenticated, sending data...')
            updateUserCart(productId, action)
        }
    })
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