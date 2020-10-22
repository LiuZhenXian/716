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
                mainkg(dt);
                erkg2(dt);
                erkg3(dt);
                orderT(dt);
                // $("hfwx").html("sadasd");
            }
        },
        error: function (data) {
            alert("连接失败！")
            console.log(data)
        }
    })
}

//态势图谱
function mainkg(dt){
    var container = document.getElementById("VIS_draw1");
    var data = {
        nodes: dt["ent_a"][0],
        edges: dt["ent_a"][1]
    };
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
    network.on("doubleClick", (e) => {
        // 执行双击事件具体操作
        var nodes=data["nodes"]
        for (var i in nodes) {
            if(nodes[i]["id"]==e.nodes){
                alert("实体名称："+nodes[i]["label"]);
            }

        }

      });

}
//威胁最大的实体
function erkg2(dt){
    var container = document.getElementById("VIS_draw2");
    var data = {
        nodes: dt["ent_b"][0],
        edges: dt["ent_b"][1]
    };
    var options = {
      nodes: {
          shape: 'dot',
          size: 40,
          font: {
              size: 25
          }
      },
      edges: {
          font: {
              size: 25,
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
function erkg3(dt){
    var container = document.getElementById("VIS_draw3");
    var data = {
        nodes: dt["ent_d"][0],
        edges: dt["ent_d"][1]
    };
    var options = {
      nodes: {
          shape: 'dot',
          size: 30,
          font: {
              size: 25
          }
      },
      edges: {
          font: {
              size: 25,
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
//赋值指令推理过程
function orderT(data){
    console.log(data["ent_a"][0][0]["label"])


     //H方威胁度最大实体
     var ent_a=data["ent_a"][0][0]["label"];
     document.getElementById("hfwx").innerHTML=ent_a;
     //H方相关协同实体
     var ent_b=data["ent_b"][0][0]["label"];
     document.getElementById("hfxx").innerHTML=ent_b;
     //L方出动实体
     var ent_d=data["ent_d"][0][0]["label"];
     document.getElementById("lfcd").innerHTML=ent_d;
     //F-16事件链
     document.getElementById("esjl").innerHTML=ent_d+"事件链";
     document.getElementById("sjl").innerHTML="起飞-到达区域-返航";
}


