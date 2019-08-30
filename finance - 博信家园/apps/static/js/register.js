function register(){
    // 验证user_id是否为手机号
    var reg_phone =/^[1][3,4,5,6,7,8][0-9]{9}$/;
    // 验证银行卡号
    var reg_bankcard = /^([1-9]{1})(\d{14}|\d{15}|\d{18})$/;

    var user_id = $("#id_user_id").val();
    var username = $("#id_username").val();
    var password = $("#psd-1").val();
    var alipay_id = $("#alipay_id").val();
    var pay_pwd = $("#pay_pwd").val();
    var superior_phone = $("#superior_phone").val();
    var bank_card = $("#bank_card").val();
    if(bank_card.match(reg_bankcard)) {
        if (user_id.match(reg_phone)) {
            if (check_pwd() && check_paypwd(pay_pwd)){
                // 密码一致
                $.ajax({
                    url: "/api/home/register",
                    type: "POST",
                    data: {"user_id": user_id, "username": username, "password": password,
                        "alipay_id":alipay_id, "pay_pwd":pay_pwd, "superior_phone":superior_phone,
                        "bank_card":bank_card},
                    success: function (data) {
                        if (data.code === "0000") {
                            window.location.href = "/bxjy"
                            alert("用户注册成功！前往登录页面");
                        } else {
                            alert(data.message);
                        }
                    }
                })
            }
            else {
                alert("注册失败，请检查信息是否输入正确！")
            }
        } else {
            alert("注册名必须为手机号！")
        }
    }else {
        alert("请输入正确的银行卡号！")
    }
}

function check_pwd() {
    var reg_pwd = /^.{6,12}$/;
    var password = $("#psd-1").val();
    var p2 = $("#psd-2").val();
    if(password == "" || p2 == ""){
        alert("请输入密码！");
        return false;
    }
    else if(password.match(reg_pwd)) {
        if (password != p2) {
            alert("两次密码不一致！");
            return false;
        } else {
            return true;
        }
    }
    else {
        alert("密码长度不正确！");
        return false;
    }
}

function check_paypwd(pay_pwd) {
    var reg_pwd = /^.{6}$/;
    if(pay_pwd.match(reg_pwd)) {
        return true;
    }
    else {
        return false;
    }
}