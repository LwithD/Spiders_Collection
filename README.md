# Spiders_Collection
## Save all spiders I've wrote  
<br>
<br>  

## 笔记  
asyncio不支持request库，可使用aiohttp.<br>  
baiduTranslateSignJson.js 这个文件是生成sign的json函数文件.<br><br>
chromedriver在浏览器版本88.0之后设置enable-automation反检测的手段失效，首页中有新解决方案.

<br>
<br>

## 模拟登录  

### 1.验证码识别  
### 2.模拟cookie登录  
<br>
-手动处理：通过抓包工具获取cookie值并封装到request请求的headers中  
<br>
-自动处理：创建session对象：requests.Session()  

-使用session对象进行模拟登录post请求的发送(cookie会存储在session中)  

-session对象对个人主页对应的get请求进行发送（携带cookie)  

