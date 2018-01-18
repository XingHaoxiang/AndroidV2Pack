## Android V2签名再打包工具。


#### 原理:
- 使用Android BuildTools内的apksigner.jar 进行签名再打包。
	

#### 使用方式:
- 安装Python2
- 配置av2pConfig.json
- 使用命令 Python av2p.py

#### av2pConfig配置说明:

- **apksignerPath** 里面配置apksigner所在的位置,一般在androidSDK\build-tools\lib下。

- **keyStorePath** 配置你的KeyStore或者jenkins的地址

- **keystoreAlias** 填入Keystore的别名

- **KeyStorePwd** keystore的密码

- **aliasPwd** alias密码

- **outPath** 输出路径

- **inputPath** apk所在路径

> 注意所有的路径用双斜线，否则json会出问题。

#### 参考



----------
V2签名可以参考谷歌对于V2的解释

[https://developer.android.com/about/versions/nougat/android-7.0.html#apk_signature_v2](https://developer.android.com/about/versions/nougat/android-7.0.html#apk_signature_v2 "APK signature scheme v2")