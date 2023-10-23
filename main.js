function login(){
    let username = document.getElementById("username");
    let password = document.getElementById("password");
    if (username==="" || password==="") {
        alert("Username or Password not acceptable");
    } else {
        ///request http on 127.0.0.1::8080/login/$usr={username}&psswd={password}
    }
}