function divShow() {
    document.getElementById('itemForm').style.display = "block"; 
}

document.getElementById('foodForm').addEventListener('submit', postOrder);
document.getElementById('user-menu').addEventListener('load', getUserMenu());
const orderUrl = 'http://127.0.0.1:5000/api/v1/users/orders';
token = localStorage.getItem('token')

function postOrder(e){
    e.preventDefault();

    let item = document.getElementById('item').value;
    let quantity = document.getElementById('quantity').value;
    
    let formData =  new FormData();
    formData.append('item', item);
    formData.append('quantity', quantity);

    fetch(orderUrl, {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Authorization': `Bearer ${token}`
        },
        body: formData
    })
    .then(res => res.json())
    .then(response => {
        console.log(response);
        if (response.message === 'Order placed successfully'){
            alert('Your order has been placed');
            window.location.replace('user.html');
        } else {
            alert(response.message);
        }
    })
    .catch(err => console.log(err));
}

function getUserMenu(){
    let menuUrl = 'http://127.0.0.1:5000/api/v1/menu';
    fetch(menuUrl)
    .then(res => res.json())
    .then(response => {
        let output = ''
        for(let k in response){
            console.log(response[k].item);
            output += `
            <div class="food-item">
                <h2>${response[k].item}</h2>
                <img src="${response[k].image}">
                <p> Price: ......................... ${response[k].price}/=<br/>
                    <button type="submit" class="button-search">Add to cart</button>
                </p>
            </div>`;
            console.log(output);}
        document.getElementById('user-menu').innerHTML = output;
    })
}