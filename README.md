# oracle

# baas上的oracle tutorial http rest api：

共有五个服务，调用方法和普通rest api使用方式一样，可以参考auditee/test.sh

## http://host:port/generate

POST类型请求

参数：json字符串，包含"target"属性

返回值：filename，生成的证据文件在服务器上的名字

## http://host:port/download/<filename>

Get类型，POST类型都支持

参数：url路径中的filename

返回值：下载证据文件

## http://host:port/ipfs/<filename>

Get类型，POST类型都支持

参数：url路径中的filename

返回值：保存在ipfs上的文件的hash值，可以用来访问ipfs上的文件

## http://host:port/upload

POST请求

参数：request.data = 待上传文件内容

返回值：filename，文件上传到服务器上后，服务器会给生成新的名字，并返回新的名字

## http://host:port/review/<filename>

POST请求

参数：filename，已经保存在服务器上的证据文件的名字

返回值：字符串，证据文件的验证报告。


