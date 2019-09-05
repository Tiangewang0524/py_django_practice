function login() {
        // 验证user_id是否为手机号
        var reg=/^[1][3,4,5,6,7,8][0-9]{9}$/;
        var user_id = $("#id_user_id").val();
        var password = $("#id_password").val();
        if(user_id.match(reg)) {
            $.ajax({
                url: "/api/home/login",
                type: "POST",
                data: {"user_id": user_id, "password": password},
                success: function (data) {
                    if (data.code == "0002") {
                        alert("用户不存在，即将跳转到注册页面！");
                        $.cookie("user", data.data, {"path": "/"});
                        console.log($.cookie("user"));
                        window.location.href = "/bxjy/register-OK"
                    } else {
                        alert(data.message);
                        if (data.message == '登陆成功') {
                            $.cookie("user", data.data, {"path": "/"});
                            console.log($.cookie("user"));
                            if (data.isSupperUser == '1'){
                                window.location.href = "/bxjy/audit/index"
                            }
                            else {
                                if (data.state == '0') {
                                    window.location.href = "/bxjy/main"
                                } else {
                                    window.location.href = "/bxjy/main2"
                                }
                            }
                        }
                    }
                }
            })
        }
        else {
            alert("请输入正确的手机号！")
        }
    }