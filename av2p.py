# coding: utf-8

import os
import json

with open('av2pConfig.json','r') as f:
	config = json.load(f)



apksignerPath = config['apksignerPath'] # apksigner路径
keyStorePath = config['keyStorePath'] #keystore 路径
keystoreAlias = config['keystoreAlias'] #签名文件的alias 
KeyStorePwd = config['KeyStorePwd'] #签名文件的密码
aliasPwd = config['aliasPwd'] #签名文件alias密码 
outPath = config['outPath'] #输出路径
inputPath = config['inputPath'] #apk安装包位置


def pack():
	cmd = 'java -jar {} sign --ks {} --ks-key-alias {} --ks-pass pass:{} --key-pass pass:{} --out {} {}'\
		.format(apksignerPath,keyStorePath,keystoreAlias,KeyStorePwd,aliasPwd,outPath,inputPath)
	print cmd
	os.system(cmd)


if __name__ == "__main__":
	pack()