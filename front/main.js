async function login(){
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    if (username.value != "" && password.value != "") {
        const resp = await fetch("/login/$usr="+username+"&psswd="+password)
        const txt = await resp.text()
        if (txt == 0){
            alert("Login Failed")
        }else{
            alert("Login sucessful")
        }
    } else {
        alert("Username or Password not acceptable");
    }
}