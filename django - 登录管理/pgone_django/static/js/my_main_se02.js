var user = $.cookie("user");

$(function(){
    $.ajax({
        url:"/api/home/get_problems",
        type:"GET",
        data:{'user_id': user},
        success:function (result) {
            if(result.code == "0000"){
                $("#tbody").html();
                var type = ["java", "UI", "web"];
                var neirong = "";
                for(var i=0; i<result.data.length; i++){
                    if(result.data[i].raise_user_id == user){
                        neirong += "        <tr>\n" +
                            "            <td>" + type[result.data[i].type] + "</td>\n" +
                            "            <td>" + result.data[i].context + "</td>\n" +
                            "            <td>" + result.data[i].raise_user + "</td>\n" +
                            "            <td>" + formatDate(result.data[i].raise_time * 1000) + "</td>\n" +
                            "            <td>" + (result.data[i].state ? "已解决" : "未解决") + "</td>\n" +
                            "            <td>" + (result.data[i].solve_user ? result.data[i].solve_user : '----') + "</td>\n" +
                            "            <td>" + (result.data[i].solve_time ? formatDate(result.data[i].solve_time * 1000) : '----') + "</td>\n" +
                            "        </tr>"
                    }
                }
                $("#tbody").html(neirong);
            }else {
                alert(data.message);
            }
        }
    })
});
function formatDate(now) {
     now = new Date(now);
     var year=now.getFullYear();
     var month=now.getMonth()+1;
     var date=now.getDate();
     var hour=now.getHours();
     var minute=now.getMinutes();
     var second=now.getSeconds();
     return year+"-"+month+"-"+date+" "+hour+":"+minute+":"+second;
}