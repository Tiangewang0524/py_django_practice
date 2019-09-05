// var user = $.cookie("user");
// console.log(user)
$(function(){
    $.ajax({
        url:"/api/home/admin",
        type:"POST",
        data:{},
        success:function (result) {
            if(result.code == "0000"){
                $("#tbody").html();
                var neirong = "";
                for(var i=0; i<result.data.length; i++) {
                    id = result.data[i].id
                    neirong += "        <tr class=\"table-td\">\n" +
                        "            <td><input type=\"checkbox\" name='checkbox_buy' value='" + id + "'><span>" + result.data[i].username + "/" + result.data[i].user_id +"</span></td>\n" +
                        "            <td>" + result.data[i].add_time + "</td>\n" +
                        "            <td>" + "¥" + result.data[i].count + "</td>\n" +
                        "        </tr>"
                }
                $("#tbody").html(neirong);
            }else {
                alert("信息数据读取错误！");
            }
        }
    })
});

$(function(){
    $.ajax({
        url:"/api/home/admin",
        type:"GET",
        data:{},
        success:function (result) {
            if(result.code == "0000"){
                $("#tbody_2").html();
                var neirong = "";
                for(var i=0; i<result.data.length; i++) {
                    neirong += "        <tr class=\"table-td\">\n" +
                        "            <td><input type=\"checkbox\" name='checkbox_sale' value='" + result.data[i].id + "'><span>" + result.data[i].username + "/" + result.data[i].user_id +"</span></td>\n" +
                        "            <td>" + result.data[i].add_time + "</td>\n" +
                        "            <td>" + "¥" + result.data[i].count + "</td>\n" +
                        "        </tr>"
                }
                $("#tbody_2").html(neirong);
            }else {
                alert("信息数据读取错误！");
            }
        }
    })
});

function addMatch() {
    var buy_id = document.getElementsByName("checkbox_buy");
    var all_buy = "";
    for(i in buy_id){
        if(buy_id[i].checked){
            all_buy += (buy_id[i].value + "|")
        }
    }
    var sale_id = document.getElementsByName("checkbox_sale");
    var all_sale = "";
    for(j in sale_id){
        if(sale_id[j].checked){
            all_sale += (sale_id[j].value + "|")
        }
    }
    var params = {"all_buy": all_buy, "all_sale": all_sale};

    $.ajax({
        url:"/api/home/match",
        type:"POST",
        data:params,
        // traditional:true,
        success:function (result) {
            if(result.code == "0000"){
                alert("信息匹配成功！");
                window.location.reload();
            }else {
                alert(result.message);
            }
        }
    })
}