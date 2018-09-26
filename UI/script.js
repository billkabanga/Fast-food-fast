//grab the form from the dom
let form = document.getElementById("loginForm");
//get the value of the check box from the form using its name
let clientInputs = form.querySelectorAll("input[name='clientType']");

//listen for when the user changes the client type and update the form action accordingly
clientInputs.forEach(function(input) {
    input.addEventListener("change", function(event) {
        //get the client value
        let client = event.currentTarget.value;
        let action=client === "admin" ? "admin.html":"user.html";
        form.setAttribute("action",action);
    });
});