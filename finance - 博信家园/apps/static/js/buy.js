var user = $.cookie("user");
console.log(user)
function buy(){
    var pay_pwd = $("#pay_pwd").val();
    var buy_val = $("#buy_val").text();
    $.ajax({
        url:"/api/home/buy",
        type:"POST",
        data:{'user_id': user, 'pay_pwd':pay_pwd, 'buy_val':buy_val},
        success:function (result) {
            if(result.code == "0000"){
                alert("买入信息发布成功！")
                window.location.href = "/bxjy/main2"
            }
            else {
                alert(result.message)
            }
        }
    })
}