//function for pop-up window for the menu add
function divShow() {
    document.getElementById('itemForm').style.display = "block"; 
}

document.getElementById('foodForm').addEventListener('submit', addItem);
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