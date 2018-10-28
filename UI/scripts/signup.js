document.getElementById('signupForm').addEventListener('submit', registerUser);
const url = 'https://bill-fast-food.herokuapp.com/api/v1/auth/signup';

function registerUser(event){
    event.preventDefault();

    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let contact = document.getElementById('tel').value;
    let password = document.getElementById('password').value;
    let radioInput = document.getElementsByName('clientType');
    for (let i = 0; i < radioInput.length; i++){
        if (radioInput[i].checked){
            role = radioInput[i].value;
            break;
        }
    }
    let data = {
        username: username,
        email: email,
        contact: contact,
        password: password,
        role: role
    }

    fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        console.log(response);
        if (response.message === 'new user registered') {
            alert(`You have registered as ${data['username']}`);
            window.location.replace('usersignin.html');
        } else {
            alert(response.message);
        }
    })
    .catch(err => console.log(err));
}