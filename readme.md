# Copymanga-Proxy

为拷贝漫画第三方客户端[fumiama/copymanga](https://github.com/fumiama/copymanga)开发的图床加速代理。  
修改该项目文件`app/src/main/res/values/strings.xml`中的`<string name="imgProxyApiUrl">https://copymanga.azurewebsites.net/api/img?code=%1$s&amp;url=%2$s</string>`  
配置为`<string name="imgProxyApiUrl">https://<本项目的域名>/proxy?code=%1$s&amp;url=%2$s</string>`并打包安装。将`APIKEY`填入应用配置中。  

## 快速启动
```bash
docker run -d \
--name copymanga-proxy \
-p 5000:5000 \
tcol123/copymanga-proxy
```