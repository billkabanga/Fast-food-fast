function divShow() {
    document.getElementById('itemForm').style.display = "block"; 
}

document.getElementById('foodForm').addEventListener('submit', postOrder);
document.getElementById('user-menu').addEventListener('load', getUserMenu());
document.getElementById('orderItem').addEventListener('load', getOrderHistory());
const orderUrl = 'https://bill-fast-food.herokuapp.com/api/v1/users/orders';
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
function getImgSrc(item){
    let srcObj = {
        rolex: '../UI/img/rolex.jpg',
        chips: '../UI/img/chip.jpg',
        pilau: '../UI/img/pilau.jpg',
        pizza: '../UI/img/pizza.jpg',
        sausage: '../UI/img/sausage.png'
    };
    for (let key of Object.keys(srcObj)){
        if (item === key){
            src = srcObj[key];
        }
    }
}

function getUserMenu(){
    let menuUrl = 'https://bill-fast-food.herokuapp.com/api/v1/menu';
    fetch(menuUrl)
    .then(res => res.json())
    .then(response => {
        let output = ''
        for(let k in response){
            console.log(response[k].item);
            getImgSrc(response[k].item)
            output += `
            <div class="food-item">
                <h2>${response[k].item}</h2>
                <img src="${src}">
                <p> Price: ......................... ${response[k].price}/=<br/>
                    <button type="submit" class="button-search">Add to cart</button>
                </p>
            </div>`;
            console.log(output);}
        document.getElementById('user-menu').innerHTML = output;
    })
}

function getOrderHistory() {
    let histUrl = 'https://bill-fast-food.herokuapp.com/api/v1/users/orders';
    token = localStorage.getItem('token')
    fetch(histUrl, {
        headers: {
            'Authorization': `Bearer ${token}`
        } 
    })
    .then(res => res.json())
    .then(response => {
        let output = `
        <tr class="col">
            <th>Order</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>Status</th>
            <th>Date</th>
        </tr>`
        for(let k in response){
            console.log(response[k].item);
            output += `
            <tr class="order">
                <td>${response[k].item}</td>
                <td>${response[k].quantity}</td>
                <td>${response[k].price}</td>
                <td>${response[k].order_status}</td>
                <td>${response[k].order_date}</td>
            </tr>`;
            console.log(output);}
        document.getElementById('orderItem').innerHTML = output;
    })
}