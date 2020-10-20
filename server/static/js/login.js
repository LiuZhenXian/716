$(document).ready(function(){
      $("#formLogin").click(function(){
        var formdata = new FormData();
        formdata.append("user",$("#user").val())
        formdata.append("pwd",$("#pwd").val())
      $.ajax({
            url: "/login/",
            type: "post",
            data: formdata,
            contentType: false,
            processData: false,
            success: function (data) {
                if(data==0){//0：登录失败
                     alert("用户名或密码错误！")
                }else {
                    var dt = JSON.parse(data);
                    $.each(dt,function(index,value){
                        //写入cookie中保存
                        $.cookie('Username', value.Password, { expires: 1, path: '/' });
                        //获取cookie
                        //var ss=$.cookie('Username')
                        //删除cookie
                        //$.removeCookie('userid', { path: '/' });
                     });
                    //跳转到index页面
                    window.location = "/index";
                }
            },
            error: function (data) {
                alert("连接失败！")
                console.log(data)
            }
        })

      });
    });