var user = $.cookie("user");

function activate(){
    // 验证身份证号
    var reg_idcard = /^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$/;

    var id_card = $("#id_card").val();
    var password = $("#psd-1").val();
    if(id_card.match(reg_idcard)) {
            $.ajax({
                url: "/api/home/activate",
                type: "POST",
                data: {"user_id": user, "password": password, "id_card":id_card},
                success: function (data) {
                    if (data.code == "0000") {
                        alert("激活成功！");
                        window.location.href = "/bxjy/main2"
                    } else {
                        alert(data.message);
                    }
                }
            })
        }
        else {
            alert("请输入正确的身份证号！")
        }
}