$(document).ready(function(){
    getApi()
});

function getApi(){
    setTimeout(getApi,10*1000);
    var date =new Date();
    var s=date.getSeconds();
    formdata={
        "times":s
    };
    $.ajax({
        url: "/orderkg/",
        type: "post",
        data: formdata,
        contentType: false,
        processData: false,
        success: function (data) {
            if(data==0){//0：登录失败
                 alert("用户名或密码错误！")
            }else {
                var dt = JSON.parse(data);
                mainkg(dt)
                erkg2(dt)
                erkg3(dt)
            }
        },
        error: function (data) {
            alert("连接失败！")
            console.log(data)
        }
    })
}

//态势图谱
function mainkg(data){
    var container = document.getElementById("VIS_draw1");
    var options = {
      nodes: {
          shape: 'dot',
          size: 30,
          font: {
              size: 18
          }
      },
      edges: {
          font: {
              size: 18,
              align: 'middle'
          },
          color: 'gray',
          arrows: {
              to: {enabled: true, scaleFactor: 0.6}
          },
          smooth: {enabled: false}
      },
      physics: {
          enabled: true
      }
    };

    var network = new vis.Network(container, data, options);

}
//威胁最大的实体
function erkg2(data){
    var container = document.getElementById("VIS_draw2");
    var options = {
      nodes: {
          shape: 'dot',
          size: 50,
          font: {
              size: 30
          }
      },
      edges: {
          font: {
              size: 40,
              align: 'middle'
          },
          color: 'gray',
          arrows: {
              to: {enabled: true, scaleFactor: 0.6}
          },
          smooth: {enabled: false}
      },
      physics: {
          enabled: true
      }
    };

    var network = new vis.Network(container, data, options);

}

//协调最大的实体
function erkg3(data){
    var container = document.getElementById("VIS_draw3");
    var options = {
      nodes: {
          shape: 'dot',
          size: 50,
          font: {
              size: 30
          }
      },
      edges: {
          font: {
              size: 40,
              align: 'middle'
          },
          color: 'gray',
          arrows: {
              to: {enabled: true, scaleFactor: 0.6}
          },
          smooth: {enabled: false}
      },
      physics: {
          enabled: true
      }
    };

    var network = new vis.Network(container, data, options);

}


