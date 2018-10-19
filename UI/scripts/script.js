//grab the form from the dom
document.getElementById('loginForm').addEventListener('submit', loginUser);
const url = 'http://127.0.0.1:5000/api/v1/auth/login';

function loginUser(e){
    e.preventDefault();
    let username = document.getElementById('username').value;
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
        if (response.message === 'Logged in successfully'){
            token = response.access_token;
            localStorage.setItem('token', token)
            switch (role) {
                case 'admin':
                    window.location.replace('admin.html');
                    break;
                case 'client':
                    window.location.replace('user.html');
                    break;
                default:
                    break;
            }
            alert(`Welcome back ${username}`);
        } else {
            alert(response.message);
        }
    })
    .catch(err => console.log(err));
}
