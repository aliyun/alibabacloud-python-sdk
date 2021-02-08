[← 首页](../../README-CN.md) | 快速使用[(English)](0-Usage-EN.md) | [客户端与凭证 →](1-Client-CN.md)

![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)

# Python SDK 使用说明

## 要求

- Python >= 3.6

## 安装

你可以使用 `pip` 来安装你的依赖。

```sh
$ pip install alibabacloud-ecs20140526
```

## 快速使用

在您开始之前，您需要注册阿里云帐户并获取您的[凭证](https://usercenter.console.aliyun.com/#/manage/ak)。
SDK 使用 [credentials](https://github.com/aliyun/credentials-python/blob/master/README-CN.md) 来管理凭证。

## 使用示例
1.同步使用
```python
from alibabacloud_ecs20140526.models import DescribeImagesRequest
from alibabacloud_ecs20140526.client import Client
from alibabacloud_tea_openapi.models import Config

'''云服务器示例'''
# 初始化Config
config = Config(
    access_key_id='<ACCESS-KEY-ID>',
    access_key_secret='<ACCESS-KEY-SECRET>',
    region_id='cn-hangzhou'
)
client = Client(config)
# 初始化Request
request = DescribeImagesRequest(image_id='<image-id>')
# 调用api
response = client.describe_images(request)

for image in response.images.image:
    print(image.image_id)
    print(image.image_name)
```

2.异步使用
```python
import asyncio

from alibabacloud_ecs20140526.models import DescribeImagesRequest
from alibabacloud_ecs20140526.client import Client
from alibabacloud_tea_openapi.models import Config

'''云服务器示例'''

async def main():
    config = Config(
        access_key_id='<ACCESS-KEY-ID>',
        access_key_secret='<ACCESS-KEY-SECRET>',
        region_id='cn-hangzhou'
    )
    client = Client(config)
    request = DescribeImagesRequest(image_id='<image-id>')
    
    response = await client.describe_images_async(request)
    print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

3.数据流
```python
from alibabacloud_imagesearch20200212.client import Client
from alibabacloud_imagesearch20200212.models import SearchImageByPicAdvanceRequest
from alibabacloud_oss_util.models import RuntimeOptions
from alibabacloud_tea_openapi.models import Config

'''图像搜索示例'''

with open('pic.jpg', 'rb') as f:
    # 初始化Request
    request = SearchImageByPicAdvanceRequest(
        instance_name='name',
        pic_content_object=f  # 文件流或BytesIO
    )
    
    # 初始化Config
    config = Config(
        access_key_id='<your_accsee_key_id>',
        access_key_secret='<your_access_key_secret>',
        endpoint='<your_endpoint>',
        region_id='cn-shanghai',
        type='access_key'
    )
    
    # 初始化RuntimeObject
    runtime_option = RuntimeOptions()
    
    # 初始化Client
    client = Client(config)
    
    # 调用api
    response = client.search_image_by_pic_advance(request, runtime_option)

print(response)
print('request id:', response.request_id)
print('code:', response.code)
print('message:', response.msg)

# head
print('docs return:', response.head.docs_return)
print('docs found:', response.head.docs_found)
print('search time:', response.head.search_time)

# pic info
print('category id:', response.pic_info.category_id)
print('region:', response.pic_info.region)
print('all categories:', response.pic_info.all_categories)

# Auctions
for aut in response.auctions:
    print('category id:', aut.category_id)
    print('product id:', aut.product_id)
```

## 参数说明

```python
'''Config'''
class Config(TeaModel):
    def __init__(self):
        self.access_key_id = access_key_id          # access key id
        self.access_key_secret = access_key_secret  # access key secret
        self.security_token = security_token        # Security Token
        self.protocol = protocol                    # 请求协议 http|https
        self.region_id = region_id                  # 区域id
        self.read_timeout = read_timeout            # 读超时
        self.connect_timeout = connect_timeout      # 连接超时
        self.http_proxy = http_proxy                # http代理
        self.https_proxy = https_proxy              # https代理
        self.endpoint = endpoint                    # endpoint
        self.no_proxy = no_proxy                    # 代理白名单
        self.max_idle_conns = max_idle_conns        # 最大连接数
        self.user_agent = user_agent                # User-Agent
        self.socks_5proxy = socks_5proxy            # socks5代理
        self.socks_5net_work = socks_5net_work      # socks5代理协议
        self.endpoint_type = endpoint_type          # 域名类型：internal，accelerate 或不填
        self.open_platform_endpoint = open_platform_endpoint  # 文件上传时授权使用的域名(目前暂不需要填写)
        self.type = type                            # 凭证类型，如有疑问请参考https://github.com/aliyun/credentials-python/blob/master/README-CN.md


'''RuntimeOptions'''
class RuntimeOptions(TeaModel):
    def __init__(self):
        self.autoretry = autoretry                    # 是否开启重试
        self.ignore_ssl = ignore_ssl                  # 是否忽略 SSL 校验
        self.max_attempts = max_attempts              # 最大重试次数， 默认为 3
        self.backoff_policy = backoff_policy          # 重试休眠策略，默认为 no
        self.backoff_period = backoff_period          # 重试休眠时间， 默认为 1
        self.read_timeout = read_timeout              # 读超时
        self.connect_timeout = connect_timeout        # 连接超时
        self.local_addr = local_addr                  # 本地网卡 ip
        self.http_proxy = http_proxy                  # http 的代理
        self.https_proxy = https_proxy                # https 的代理
        self.no_proxy = no_proxy                      # 代理白名单
        self.max_idle_conns = max_idle_conns          # 最大连接数
        self.socks_5proxy = socks_5proxy              # socks5 代理
        self.socks_5net_work = socks_5net_work        # socks5 代理协议
```
