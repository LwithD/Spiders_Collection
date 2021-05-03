## 中间件  

-下载中间件<br>
&emsp;-位置：引擎和下载器之间<br>
&emsp;-作用：批量拦截到整个工程中的请求和响应  
&emsp;-拦截请求：  
&emsp;&emsp;-UA伪装:process_request  
&emsp;&emsp;-代理IP:process_exception:return request  
&emsp;-拦截响应:  
&emsp;&emsp;-更改响应数据，响应对象
