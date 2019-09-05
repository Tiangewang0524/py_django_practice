var user = $.cookie("user");
console.log(user)
function sell(){
    var pay_pwd = $("#pay_pwd").val();
    var sell_val = $("#sell_static").val();
    $.ajax({
        url:"/api/home/sell",
        type:"POST",
        data:{'user_id': user, 'pay_pwd':pay_pwd, 'sell_val':sell_val},
        success:function (result) {
            if(result.code == "0000"){
                alert("卖出信息发布成功！")
                window.location.href = "/bxjy/main2"
            }
            else {
                alert(result.message)
            }
        }
    })
}