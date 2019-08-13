function login() {
    var username = $("#username").val();
    var password = $("#id_password").val();
    $.ajax({
        url:"/api/home/login",
        type:"POST",
        data:{"username":username,"password":password},
        success:function (data) {
            if(data.code == "0000"){
                window.location.href = "/backend/main/se01"
            }else {
                alert(data.message);
            }
        }
    })
}