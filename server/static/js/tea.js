//config的设置是全局的
layui.config({
  base: '/static/assets/lay/modules/' //假设这是你存放拓展模块的根目录
}).extend({ //设定模块别名
  home: 'mymod' //如果 mymod.js 是在根目录，也可以不用设定别名
  ,mod1: 'admin/mod1' //相对于上述 base 目录的子目录
});
 

//使用拓展模块
layui.use(['mymod', 'mod1'], function(){
  var mymod = layui.mymod
  ,mod1 = layui.mod1
  ,mod2 = layui.mod2;
  
  mymod.hello('World!'); //弹出 Hello World!
});
     