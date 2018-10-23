//function for pop-up window for the menu add
function divShow() {
    document.getElementById('itemForm').style.display = "block"; 
}

document.getElementById('foodForm').addEventListener('submit', addItem);
document.getElementById('menu').addEventListener('load', getMenu());
document.getElementById('orderTable').addEventListener('load', getOrders());

const menuUrl = 'http://127.0.0.1:5000/api/v1/menu';
token = localStorage.getItem('token')
function addItem(e){
    e.preventDefault();

    let item = document.getElementById('item').value;
    let price = document.getElementById('price').value;
    let file = document.getElementById('file').files[0];

    let formData =  new FormData();
    formData.append('item', item);
    formData.append('price', price);
    formData.append('file', file);

    fetch(menuUrl, {
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
        if (response.message === 'Food option added successfuly'){
            alert('New food item added');
            window.location.replace('admin.html');
        } else {
            alert(response.message);
        }
    })
    .catch(err => console.log(err));
}

function getMenu() {
    console.log('Method called');
    let Url = 'http://127.0.0.1:5000/api/v1/menu';
    fetch(Url)
    .then(res => {
        console.log(res);
        return res.json()
    })
    .then(response => {
        let output = ''
        for(let k in response){
            console.log(response[k].item);
            output += `
            <div class="food-item" id="admin-item">
                <h2>${response[k].item}</h2>
                <img src="${response[k].image}">
                <p> Price: ......................... ${response[k].price}/=<br/>
                    <button type="submit" class="button-search">Edit</button>
                    <button type="submit" class="button-search">Delete</button>
                </p>
            </div>`;
            console.log(output);}
        document.getElementById('menu').innerHTML = output;
    })
}

function getOrders() {
    let ordersUrl = 'http://127.0.0.1:5000/api/v1/orders';
    token = localStorage.getItem('token')
    fetch(ordersUrl, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(response => {
        let output = `
        <tr class="col">
            <th>Order No.</th>
            <th>Order</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>Client-name</th>
            <th>Contact</th>
            <th>Status</th>
        </tr>`
        for(let k in response){
            console.log(response[k].item);
            output += `
            <tr class="order">
                <td>${response[k].orderid}</td>
                <td>${response[k].item}</td>
                <td>${response[k].quantity}</td>
                <td>${response[k].price}</td>
                <td>${response[k].client}</td>
                <td>${response[k].contact}</td>
                <td>${response[k].order_status}</td>
            </tr>`;}
        document.getElementById('orderTable').innerHTML = output;
    })
}

document.getElementById('getSpecific').onclick = function getSpecificOrder() {
    console.log('get spec')
    let order_id = document.getElementById('orderSearch').value;
    console.log(order_id)
    let specOrdersUrl = `http://127.0.0.1:5000/api/v1/orders/${order_id}`;
    token = localStorage.getItem('token')
    fetch(specOrdersUrl, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(response => {
        if (response.message === 'Order not found'){
            alert(response.message);
        } else {
            let output = ''
            for(let k in response){
                console.log(response[k].item);
                output += `
                <div id="itemAdd">
                    <form id="foodForm" method="POST">
                        <h2>Order ${order_id}</h2>
                        <p>Order item:  ${response[k].item}</p>
                        <p>Price:  ${response[k].price}/=</p>
                        <p>Client:  ${response[k].client}</p>
                        <p>Contact:  ${response[k].contact}</p>
                        <button type="submit" class="button-acc">Accept</button>
                        <button type="submit" class="button-acc">Decline</button>
                    </form>
                </div>`;
                console.log(output);}
            document.getElementById('orderForm').innerHTML = output;
            document.getElementById('orderForm').style.display = "block";
            }
    })
}
