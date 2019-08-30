var user = $.cookie("user");
console.log(user)
$(function(){
    $.ajax({
        url:"/api/home/main",
        type:"GET",
        data:{'user_id': user},
        success:function (result) {
            if(result.code == "0000"){
                $("#account").html(result.user.user_id);
                if(result.user.state == 0) {
                    $("#state").html("未激活");
                }
                else {
                    $("#state").html("已激活");
                }
                $("#welcome").html("尊敬的 " + result.user.username + " 用户, 欢迎您！");
                $("#static_balance").html(result.user.static_balance);
                $("#static_blocked_balance").html(result.user.static_blocked_balance);
                $("#dynamic_balance").html(result.user.dynamic_balance);
                $("#jiayuan_coin").html(result.user.jiayuan_coin);
            }else {
                alert("用户数据读取错误！");
            }
        }
    })
});