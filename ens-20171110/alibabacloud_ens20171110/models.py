# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class BucketInfo(TeaModel):
    def __init__(
        self,
        bucket_acl: str = None,
        bucket_name: str = None,
        comment: str = None,
        create_time: str = None,
        data_redundancy_type: str = None,
        dispatcher_type: str = None,
        endpoint: str = None,
        ens_region_id: str = None,
        modify_time: str = None,
        resource_type: str = None,
        storage_class: str = None,
    ):
        # Bucket读写权限类型： public-read-write：公共读写 public-read：公共读 private：私有（默认值）
        self.bucket_acl = bucket_acl
        # Bucket名称。 3~50 个字符，只允许小写字母、数字、短横线（-），且不能以短横线开头或结尾。
        self.bucket_name = bucket_name
        # 备注。 1-128个字符或汉字，UTF-8编码。
        self.comment = comment
        # Bucket创建时间。 （格式：yyyy-mm-ddThh:mm:ss.timezone, 例如 2011-12-01T12:27:13.000Z）
        self.create_time = create_time
        # 指定Bucket的数据容灾类型。 取值范围： LRS（默认值）。本地冗余LRS ZRS 同城冗余ZRS采用多可用区（AZ）机制。
        self.data_redundancy_type = data_redundancy_type
        # Bucket的调度类型： node：节点(同城) area：区域(多城市) global：全局(全国)
        self.dispatcher_type = dispatcher_type
        # 访问域名，边缘存储取值： eos.aliyuncs.com
        self.endpoint = endpoint
        # 节点区域id，如果为空表示全局
        self.ens_region_id = ens_region_id
        # Bucket修改时间。 （格式：yyyy-mm-ddThh:mm:ss.timezone, 例如 2011-12-01T12:27:13.000Z）
        self.modify_time = modify_time
        # 指定Bucket的资源类型。 取值范围： general：通用 national-network：国网
        self.resource_type = resource_type
        # Bucket存储类型，支持Standard
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class DataDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
    ):
        # 数据盘
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class HealthCheck(TeaModel):
    def __init__(
        self,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # 是否开启健康检查。  取值：on | off。
        self.health_check = health_check
        # 健康检查的后端服务器的端口。  取值： 1~65535。    说明 在HealthCheck值为on时才会有效。
        self.health_check_connect_port = health_check_connect_port
        # 每次健康检查响应的最大超时时间。  取值：1~300（秒）。  默认值：5。
        self.health_check_connect_timeout = health_check_connect_timeout
        # 用于健康检查的域名，取值：  $_ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。是否要支持？ domain：域名长度为1-80字符，只能包含字母、数字、点号（.）和连字符（-）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_domain = health_check_domain
        # 健康检查正常的HTTP状态码，多个状态码用逗号分隔。  默认值为http_2xx。  取值：http_2xx | http_3xx | http_4xx | http_5xx。   说明 在HealthCheck值为on时才会有效。
        self.health_check_http_code = health_check_http_code
        # 健康检查的时间间隔。  取值： 1~50（秒）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_interval = health_check_interval
        # 健康检查的method
        self.health_check_method = health_check_method
        # 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。在HealthCheck值为on时才会有效。  取值：1~300（秒）。   说明 如果HealthCHeckTimeout的值小于HealthCheckInterval的值，则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。
        self.health_check_timeout = health_check_timeout
        # 健康检查类型。  取值：tcp（默认值） | http。
        self.health_check_type = health_check_type
        # 用于健康检查的URI。  长度限制为1~80，只能使用字母、数字和”-/.%?#&amp;“这些字符。 URL不能只为”/“，但必须以”/“开头。    说明 在HealthCheck值为on时才会有效。
        self.health_check_uri = health_check_uri
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值：2~10。    说明 在HealthCheck值为on时才会有效。
        self.healthy_threshold = healthy_threshold
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2~10。   说明 在HealthCheck值为on时才会有效。
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class HttpConfig(TeaModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        idle_timeout: int = None,
        request_timeout: int = None,
        scheduler: str = None,
        server_certificate_id: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        xforwarded_for: str = None,
    ):
        # 服务器上配置的Cookie。 长度为1-200，只能包含ASCII英文字母和数字字符，不能包含逗号、分号或空格，也不能以$开头。 说明 当StickySession为on且StickySessionType为server时，该参数必选。
        self.cookie = cookie
        # Cookie超时时间。  取值：1~86400（秒）。   说明 当StickySession为on且StickySessionType为insert时，该参数必选。
        self.cookie_timeout = cookie_timeout
        # 指定连接空闲超时时间，取值范围为1~60秒，默认值为15秒。  在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。
        self.idle_timeout = idle_timeout
        # 指定请求超时时间，取值范围为1~180秒，默认值为60秒。  在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504 错误码。
        self.request_timeout = request_timeout
        # 调度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。
        self.scheduler = scheduler
        # 服务器证书的ID。
        self.server_certificate_id = server_certificate_id
        # 是否开启会话保持。  取值：on | off。
        self.sticky_session = sticky_session
        # cookie的处理方式。取值：  insert：植入Cookie。  客户端第一次访问时，负载均衡会在返回请求中植入Cookie（即在HTTP/HTTPS响应报文中插入SERVERID），下次客户端携带此Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。  server：重写Cookie。  负载均衡发现用户自定义了Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。   说明 当StickySession的值为on时，必须指定该参数。
        self.sticky_session_type = sticky_session_type
        # 是否开启通过X-Forwarded-For头字段获取来访者真实 IP。  取值为on。
        self.xforwarded_for = xforwarded_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')
        return self


class SecurityGroupRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        dest_cidr_ip: str = None,
        direction: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
        priority: int = None,
    ):
        # 描述
        self.description = description
        # 目标网段
        self.dest_cidr_ip = dest_cidr_ip
        # 方向
        self.direction = direction
        # 协议
        self.ip_protocol = ip_protocol
        # 授权策略
        self.policy = policy
        # 目的端口
        self.port_range = port_range
        # 源网段
        self.source_cidr_ip = source_cidr_ip
        # 源端口
        self.source_port_range = source_port_range
        # 优先级
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        if self.priority is not None:
            result['priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        return self


class TcpConfig(TeaModel):
    def __init__(
        self,
        established_timeout: int = None,
        persistence_timeout: int = None,
        scheduler: str = None,
    ):
        # 连接超时时间。取值：10~900（秒）。
        self.established_timeout = established_timeout
        # 会话保持的超时时间。取值：0~3600（秒）。默认值：0，表示关闭会话保持。
        self.persistence_timeout = persistence_timeout
        # 调度算法。取值：wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。rr：按照访问顺序依次将外部请求依序分发到后端服务器。sch：基于源IP地址的一致性hash，相同的源地址会调度到相同的后端服务器。
        self.scheduler = scheduler

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        return self


class UdpCheck(TeaModel):
    def __init__(
        self,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_interval: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # 健康检查使用的端口。取值：1-65535  不设置此参数时，表示使用后端服务端口（BackendServerPort）。
        self.health_check_connect_port = health_check_connect_port
        # 接收来自运行状况检查的响应需要等待的时间。  如果后端ENS在指定的时间内没有正确响应，则判定为健康检查失败。  取值：1-300（秒）。默认为5秒
        self.health_check_connect_timeout = health_check_connect_timeout
        # 健康检查的时间间隔。  取值：1-50（秒）。
        self.health_check_interval = health_check_interval
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值：2-10。
        self.healthy_threshold = healthy_threshold
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2-10。
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class UdpConfig(TeaModel):
    def __init__(
        self,
        hash_key: str = None,
        scheduler: str = None,
    ):
        # hash key
        self.hash_key = hash_key
        # 调度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 sch：基于源IP地址的一致性hash，相同的源地址会调度到相同的后端服务器。
        self.scheduler = scheduler

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hash_key is not None:
            result['HashKey'] = self.hash_key
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        return self


class AddBackendServersRequestBackendServers(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.ip = ip
        # 端口
        self.port = port
        self.server_id = server_id
        # 后端服务器类型。  ens：ENS实例（默认）
        self.type = type
        # 后端服务器的权重。  取值：0~100  默认值为100，如果值为0，则不会将请求转发给该后端服务器。
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class AddBackendServersRequest(TeaModel):
    def __init__(
        self,
        backend_servers: List[AddBackendServersRequestBackendServers] = None,
        load_balancer_id: str = None,
    ):
        self.backend_servers = backend_servers
        self.load_balancer_id = load_balancer_id

    def validate(self):
        if self.backend_servers:
            for k in self.backend_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackendServers'] = []
        if self.backend_servers is not None:
            for k in self.backend_servers:
                result['BackendServers'].append(k.to_map() if k else None)
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_servers = []
        if m.get('BackendServers') is not None:
            for k in m.get('BackendServers'):
                temp_model = AddBackendServersRequestBackendServers()
                self.backend_servers.append(temp_model.from_map(k))
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class AddBackendServersShrinkRequest(TeaModel):
    def __init__(
        self,
        backend_servers_shrink: str = None,
        load_balancer_id: str = None,
    ):
        self.backend_servers_shrink = backend_servers_shrink
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_servers_shrink is not None:
            result['BackendServers'] = self.backend_servers_shrink
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            self.backend_servers_shrink = m.get('BackendServers')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class AddBackendServersResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.ip = ip
        self.port = port
        self.server_id = server_id
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class AddBackendServersResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[AddBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = AddBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class AddBackendServersResponseBody(TeaModel):
    def __init__(
        self,
        backend_servers: AddBackendServersResponseBodyBackendServers = None,
        request_id: str = None,
    ):
        self.backend_servers = backend_servers
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            temp_model = AddBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddBackendServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddBackendServersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddBackendServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDeviceInternetPortRequest(TeaModel):
    def __init__(
        self,
        isp: str = None,
        instance_id: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        nat_type: str = None,
        region_id: str = None,
    ):
        self.isp = isp
        # 实例ID
        self.instance_id = instance_id
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.nat_type = nat_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.nat_type is not None:
            result['NatType'] = self.nat_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddDeviceInternetPortResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_ids: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # RuleIds
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        return self


class AddDeviceInternetPortResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDeviceInternetPortResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddDeviceInternetPortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddNetworkInterfaceToInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_start: bool = None,
        instance_id: str = None,
        networks: str = None,
    ):
        self.auto_start = auto_start
        self.instance_id = instance_id
        self.networks = networks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.networks is not None:
            result['Networks'] = self.networks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Networks') is not None:
            self.networks = m.get('Networks')
        return self


class AddNetworkInterfaceToInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddNetworkInterfaceToInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddNetworkInterfaceToInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddNetworkInterfaceToInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateEnsEipAddressRequest(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.allocation_id = allocation_id
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class AssociateEnsEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateEnsEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateEnsEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociateEnsEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDiskRequest(TeaModel):
    def __init__(
        self,
        delete_with_instance: str = None,
        disk_id: str = None,
        instance_id: str = None,
    ):
        self.delete_with_instance = delete_with_instance
        self.disk_id = disk_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AttachDiskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachEnsInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        scripts: str = None,
        version: str = None,
    ):
        self.instance_id = instance_id
        self.scripts = scripts
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.scripts is not None:
            result['Scripts'] = self.scripts
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Scripts') is not None:
            self.scripts = m.get('Scripts')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class AttachEnsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachEnsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachEnsInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachEnsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        security_group_id: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
        version: str = None,
    ):
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.security_group_id = security_group_id
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class AuthorizeSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuthorizeSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AuthorizeSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AuthorizeSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeSecurityGroupEgressRequest(TeaModel):
    def __init__(
        self,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        security_group_id: str = None,
        source_port_range: str = None,
        version: str = None,
    ):
        self.dest_cidr_ip = dest_cidr_ip
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.security_group_id = security_group_id
        self.source_port_range = source_port_range
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class AuthorizeSecurityGroupEgressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuthorizeSecurityGroupEgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AuthorizeSecurityGroupEgressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AuthorizeSecurityGroupEgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        template: str = None,
        timeout: int = None,
    ):
        self.template = template
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template is not None:
            result['Template'] = self.template
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiskRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        ens_region_id: str = None,
        instance_charge_type: str = None,
        size: str = None,
    ):
        # 磁盘种类 高效云盘:cloud_efficiency 全闪云盘:cloud_ssd
        self.category = category
        # 节点ID
        self.ens_region_id = ens_region_id
        # 实例付费方式，取值 PrePaid:预付费，包年包月 PostPaid:按量付费。目前只支持：PostPaid
        self.instance_charge_type = instance_charge_type
        # 磁盘大小,单位GB
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateDiskResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # 实列ID集合
        self.instance_ids = instance_ids
        # 订单id,多个以逗号分割，可以直接跳转到收银行台 只有预付费返回订单号，后付费不返回
        self.order_id = order_id
        # 请求唯一ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEipInstanceRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        ens_region_id: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        isp: str = None,
        name: str = None,
    ):
        # EIP的带宽峰值
        self.bandwidth = bandwidth
        # ENS节点ID
        self.ens_region_id = ens_region_id
        # EIP的计费方式，取值：  PrePaid：包年包月。 PostPaid（默认值）：按量计费。 当InstanceChargeType取值为PostPaid时，InternetChargeType不能为PayByBandwidth
        self.instance_charge_type = instance_charge_type
        # EIP的计量方式，取值：  PayByBandwidth（默认值）：按带宽计费。 取值：95BandwidthByMonth：月95。
        self.internet_charge_type = internet_charge_type
        # 运营商信息
        self.isp = isp
        # EIP实例名称。
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateEipInstanceResponseBody(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        request_id: str = None,
    ):
        # EIP的ID。
        self.allocation_id = allocation_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEipInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEipInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEipInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnsRouteEntryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_block: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        route_entry_name: str = None,
        route_table_id: str = None,
    ):
        # 自定义路由条目的描述信息。
        self.description = description
        # 自定义路由条目的目标网段。
        self.destination_cidr_block = destination_cidr_block
        # 自定义路由条目的下一跳实例的ID。
        self.next_hop_id = next_hop_id
        # 自定义路由条目的下一跳的类型
        self.next_hop_type = next_hop_type
        # 要创建的自定义路由条目的名称。
        self.route_entry_name = route_entry_name
        # 要创建自定义路由条目的路由表ID。
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class CreateEnsRouteEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        route_entry_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 路由条目id。
        self.route_entry_id = route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')
        return self


class CreateEnsRouteEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEnsRouteEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnsRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnsServiceRequest(TeaModel):
    def __init__(
        self,
        ens_service_id: str = None,
        order_type: str = None,
        version: str = None,
    ):
        self.ens_service_id = ens_service_id
        self.order_type = order_type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_service_id is not None:
            result['EnsServiceId'] = self.ens_service_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsServiceId') is not None:
            self.ens_service_id = m.get('EnsServiceId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateEnsServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEnsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEnsServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_name: str = None,
        epninstance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        networking_model: str = None,
    ):
        self.epninstance_name = epninstance_name
        self.epninstance_type = epninstance_type
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.networking_model = networking_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        if self.epninstance_type is not None:
            result['EPNInstanceType'] = self.epninstance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        if m.get('EPNInstanceType') is not None:
            self.epninstance_type = m.get('EPNInstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        return self


class CreateEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        request_id: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateForwardEntryRequest(TeaModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_name: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        nat_gateway_id: str = None,
    ):
        self.external_ip = external_ip
        self.external_port = external_port
        self.forward_entry_name = forward_entry_name
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.forward_entry_name is not None:
            result['ForwardEntryName'] = self.forward_entry_name
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('ForwardEntryName') is not None:
            self.forward_entry_name = m.get('ForwardEntryName')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        return self


class CreateForwardEntryResponseBody(TeaModel):
    def __init__(
        self,
        forward_entry_id: str = None,
        request_id: str = None,
    ):
        self.forward_entry_id = forward_entry_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateForwardEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateForwardEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateForwardEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageRequest(TeaModel):
    def __init__(
        self,
        delete_after_image_upload: str = None,
        image_name: str = None,
        instance_id: str = None,
        product: str = None,
    ):
        self.delete_after_image_upload = delete_after_image_upload
        self.image_name = image_name
        self.instance_id = instance_id
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_after_image_upload is not None:
            result['DeleteAfterImageUpload'] = self.delete_after_image_upload
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAfterImageUpload') is not None:
            self.delete_after_image_upload = m.get('DeleteAfterImageUpload')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class CreateImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        image_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        # 镜像ID
        self.image_id = image_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestDataDisk(TeaModel):
    def __init__(
        self,
        size: str = None,
    ):
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateInstanceRequestSystemDisk(TeaModel):
    def __init__(
        self,
        size: str = None,
    ):
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        data_disk: List[CreateInstanceRequestDataDisk] = None,
        system_disk: CreateInstanceRequestSystemDisk = None,
        auto_renew: str = None,
        auto_renew_period: str = None,
        ens_region_id: str = None,
        host_name: str = None,
        image_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        ip_type: str = None,
        key_pair_name: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        payment_type: str = None,
        period: str = None,
        private_ip_address: str = None,
        public_ip_identification: bool = None,
        quantity: str = None,
        unique_suffix: bool = None,
        user_data: str = None,
        v_switch_id: str = None,
    ):
        self.data_disk = data_disk
        self.system_disk = system_disk
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.ens_region_id = ens_region_id
        self.host_name = host_name
        self.image_id = image_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.internet_charge_type = internet_charge_type
        self.ip_type = ip_type
        self.key_pair_name = key_pair_name
        self.owner_id = owner_id
        self.password = password
        # 是否使用镜像预设的密码。使用该参数时，Password参数必须为空，同时您需要确保使用的镜像已经设置了密码。
        self.password_inherit = password_inherit
        self.payment_type = payment_type
        self.period = period
        self.private_ip_address = private_ip_address
        self.public_ip_identification = public_ip_identification
        self.quantity = quantity
        self.unique_suffix = unique_suffix
        self.user_data = user_data
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.period is not None:
            result['Period'] = self.period
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.public_ip_identification is not None:
            result['PublicIpIdentification'] = self.public_ip_identification
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.unique_suffix is not None:
            result['UniqueSuffix'] = self.unique_suffix
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = CreateInstanceRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('SystemDisk') is not None:
            temp_model = CreateInstanceRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('PublicIpIdentification') is not None:
            self.public_ip_identification = m.get('PublicIpIdentification')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('UniqueSuffix') is not None:
            self.unique_suffix = m.get('UniqueSuffix')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateInstanceResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        instance_ids: CreateInstanceResponseBodyInstanceIds = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_ids = instance_ids
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceIds') is not None:
            temp_model = CreateInstanceResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyPairRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        version: str = None,
    ):
        self.key_pair_name = key_pair_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        key_pair_finger_print: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
        private_key_body: str = None,
        request_id: str = None,
    ):
        self.key_pair_finger_print = key_pair_finger_print
        self.key_pair_id = key_pair_id
        self.key_pair_name = key_pair_name
        self.private_key_body = private_key_body
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.private_key_body is not None:
            result['PrivateKeyBody'] = self.private_key_body
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PrivateKeyBody') is not None:
            self.private_key_body = m.get('PrivateKeyBody')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        network_id: str = None,
        pay_type: str = None,
        v_switch_id: str = None,
    ):
        # ENS节点ID。
        self.ens_region_id = ens_region_id
        # 负载均衡实例的名称。
        self.load_balancer_name = load_balancer_name
        # 负载均衡实例的名称。
        self.load_balancer_spec = load_balancer_spec
        # 要创建的ELB实例的网络ID
        self.network_id = network_id
        # 付费类型。PostPaid（目前只支持此种）：按量付费
        self.pay_type = pay_type
        # 专有网络实例的所属的交换机ID。
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        network_id: str = None,
        request_id: str = None,
        v_switch_id: str = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.network_id = network_id
        self.request_id = request_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerHTTPListenerRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        forward_port: int = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        listener_forward: str = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        request_timeout: int = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
        xforwarded_for: str = None,
    ):
        # 设置监听的描述信息。  长度限制为1-80个字符，允许包含字母、数字、“-”、“/”、“.”和“_”等字符。支持中文描述。
        self.description = description
        # HTTP至HTTPS的监听转发端口。
        self.forward_port = forward_port
        # 是否开启健康检查。  取值：on | off。
        self.health_check = health_check
        # 健康检查的后端服务器的端口。  取值： 1~65535。    说明 在HealthCheck值为on时才会有效。
        self.health_check_connect_port = health_check_connect_port
        # 用于健康检查的域名，取值：  $_ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。是否要支持？ domain：域名长度为1-80字符，只能包含字母、数字、点号（.）和连字符（-）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_domain = health_check_domain
        # 健康检查正常的HTTP状态码，多个状态码用逗号分隔。  默认值为http_2xx。  取值：http_2xx | http_3xx | http_4xx | http_5xx。   说明 在HealthCheck值为on时才会有效。
        self.health_check_http_code = health_check_http_code
        # 健康检查的时间间隔。  取值： 1~50（秒）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_interval = health_check_interval
        self.health_check_method = health_check_method
        # 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。在HealthCheck值为on时才会有效。  取值：1~300（秒）。   说明 如果HealthCHeckTimeout的值小于HealthCheckInterval的值，则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。
        self.health_check_timeout = health_check_timeout
        # 用于健康检查的URI。  长度限制为1~80，只能使用字母、数字和”-/.%?#&amp;“这些字符。 URL不能只为”/“，但必须以”/“开头。    说明 在HealthCheck值为on时才会有效。
        self.health_check_uri = health_check_uri
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值：2~10。    说明 在HealthCheck值为on时才会有效。
        self.healthy_threshold = healthy_threshold
        # 指定连接空闲超时时间，取值范围为1~60秒，默认值为15秒。  在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。
        self.idle_timeout = idle_timeout
        # 是否开启HTTP至HTTPS的转发。取值：on | off。
        self.listener_forward = listener_forward
        # 负载均衡实例前端使用的端口。  取值：1-65535。
        self.listener_port = listener_port
        # 负载均衡实例的ID。
        self.load_balancer_id = load_balancer_id
        # 指定请求超时时间，取值范围为1~180秒，默认值为60秒。  在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504 错误码。
        self.request_timeout = request_timeout
        # 调度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。
        self.scheduler = scheduler
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2~10。   说明 在HealthCheck值为on时才会有效。
        self.unhealthy_threshold = unhealthy_threshold
        # 是否开启通过X-Forwarded-For头字段获取来访者真实 IP。  取值为on。
        self.xforwarded_for = xforwarded_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')
        return self


class CreateLoadBalancerHTTPListenerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLoadBalancerHTTPListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerHTTPListenerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLoadBalancerHTTPListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerHTTPSListenerRequest(TeaModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        description: str = None,
        forward_port: int = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        listener_forward: str = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        request_timeout: int = None,
        scheduler: str = None,
        server_certificate_id: str = None,
        sticky_session_type: str = None,
        unhealthy_threshold: int = None,
    ):
        # 服务器上配置的Cookie。 长度为1-200，只能包含ASCII英文字母和数字字符，不能包含逗号、分号或空格，也不能以$开头。 说明 当StickySession为on且StickySessionType为server时，该参数必选。
        self.cookie = cookie
        # Cookie超时时间。  取值：1~86400（秒）。   说明 当StickySession为on且StickySessionType为insert时，该参数必选。
        self.cookie_timeout = cookie_timeout
        # 设置监听的描述信息。  长度限制为1-80个字符，允许包含字母、数字、“-”、“/”、“.”和“_”等字符。支持中文描述。
        self.description = description
        # HTTP至HTTPS的监听转发端口。
        self.forward_port = forward_port
        # 是否开启健康检查。  取值：on | off。
        self.health_check = health_check
        # 健康检查的后端服务器的端口。  取值： 1~65535。    说明 在HealthCheck值为on时才会有效。
        self.health_check_connect_port = health_check_connect_port
        # 用于健康检查的域名，取值：  $_ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。是否要支持？ domain：域名长度为1-80字符，只能包含字母、数字、点号（.）和连字符（-）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_domain = health_check_domain
        # 健康检查正常的HTTP状态码，多个状态码用逗号分隔。  默认值为http_2xx。  取值：http_2xx | http_3xx | http_4xx | http_5xx。   说明 在HealthCheck值为on时才会有效。
        self.health_check_http_code = health_check_http_code
        # 健康检查的时间间隔。  取值： 1~50（秒）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_interval = health_check_interval
        self.health_check_method = health_check_method
        # 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。在HealthCheck值为on时才会有效。  取值：1~300（秒）。   说明 如果HealthCHeckTimeout的值小于HealthCheckInterval的值，则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。
        self.health_check_timeout = health_check_timeout
        # 用于健康检查的URI。  长度限制为1~80，只能使用字母、数字和”-/.%?#&amp;“这些字符。 URL不能只为”/“，但必须以”/“开头。    说明 在HealthCheck值为on时才会有效。
        self.health_check_uri = health_check_uri
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值：2~10。    说明 在HealthCheck值为on时才会有效。
        self.healthy_threshold = healthy_threshold
        # 指定连接空闲超时时间，取值范围为1~60秒，默认值为15秒。  在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。
        self.idle_timeout = idle_timeout
        # 是否开启HTTP至HTTPS的转发。取值：on | off。
        self.listener_forward = listener_forward
        # 负载均衡实例前端使用的端口。  取值：1-65535。
        self.listener_port = listener_port
        # 负载均衡实例的ID。
        self.load_balancer_id = load_balancer_id
        # 指定请求超时时间，取值范围为1~180秒，默认值为60秒。  在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504 错误码。
        self.request_timeout = request_timeout
        # 调度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。
        self.scheduler = scheduler
        # 服务器证书的ID。
        self.server_certificate_id = server_certificate_id
        # cookie的处理方式。取值：  insert：植入Cookie。  客户端第一次访问时，负载均衡会在返回请求中植入Cookie（即在HTTP/HTTPS响应报文中插入SERVERID），下次客户端携带此Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。  server：重写Cookie。  负载均衡发现用户自定义了Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器。   说明 当StickySession的值为on时，必须指定该参数。
        self.sticky_session_type = sticky_session_type
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2~10。   说明 在HealthCheck值为on时才会有效。
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.description is not None:
            result['Description'] = self.description
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class CreateLoadBalancerHTTPSListenerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLoadBalancerHTTPSListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerHTTPSListenerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLoadBalancerHTTPSListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerTCPListenerRequest(TeaModel):
    def __init__(
        self,
        backend_server_port: int = None,
        description: str = None,
        eip_transmit: str = None,
        established_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        persistence_timeout: int = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
    ):
        # 负载均衡实例后端使用的端口，取值：1~65535
        self.backend_server_port = backend_server_port
        # 设置监听的描述信息。  长度限制为1-80个字符，允许包含字母、数字、“-”、“/”、“.”和“_”等字符。支持中文描述。
        self.description = description
        self.eip_transmit = eip_transmit
        # 连接超时时间。  取值：10~900（秒）。
        self.established_timeout = established_timeout
        # 健康检查使用的端口。  取值：1~65535。  不设置此参数时，表示使用后端服务端口（BackendServerPort）。
        self.health_check_connect_port = health_check_connect_port
        # 每次健康检查响应的最大超时时间。  取值：1~300（秒）。  默认值：5。
        self.health_check_connect_timeout = health_check_connect_timeout
        # 用于健康检查的域名
        self.health_check_domain = health_check_domain
        # 健康检查正常的HTTP状态码，多个状态码用逗号（,）分割。  取值：http_2xx（默认值） | http_3xx | http_4xx | http_5xx。
        self.health_check_http_code = health_check_http_code
        # 健康检查的时间间隔。  取值：1~50（秒）。
        self.health_check_interval = health_check_interval
        # 健康检查类型。  取值：tcp（默认值） | http。
        self.health_check_type = health_check_type
        # 用于健康检查的URI。长度限制为1~80，只能使用字母、数字、短横线（-）、正斜杠（/）、点号（.）、百分号（%）、#和&amp;这些字符。 URL不能只为/，但必须以/开头。  当TCP监听需要使用HTTP健康检查时可配置此参数，如不配置则按TCP健康检查。
        self.health_check_uri = health_check_uri
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值： 2~10。
        self.healthy_threshold = healthy_threshold
        # 负载均衡实例前端使用的端口。  取值：1-65535。
        self.listener_port = listener_port
        # 负载均衡实例的ID。
        self.load_balancer_id = load_balancer_id
        # 会话保持的超时时间。  取值：0~3600（秒）。  默认值：0，表示关闭会话保持。
        self.persistence_timeout = persistence_timeout
        # 度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 sch：基于源IP地址的一致性hash，相同的源地址会调度到相同的后端服务器。
        self.scheduler = scheduler
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2~10。
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.description is not None:
            result['Description'] = self.description
        if self.eip_transmit is not None:
            result['EipTransmit'] = self.eip_transmit
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EipTransmit') is not None:
            self.eip_transmit = m.get('EipTransmit')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class CreateLoadBalancerTCPListenerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLoadBalancerTCPListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerTCPListenerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLoadBalancerTCPListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerUDPListenerRequest(TeaModel):
    def __init__(
        self,
        backend_server_port: int = None,
        description: str = None,
        eip_transmit: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_exp: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
    ):
        # 负载均衡实例后端使用的端口，取值：1~65535
        self.backend_server_port = backend_server_port
        # 设置监听的描述信息。  长度限制为1-80个字符，允许包含字母、数字、“-”、“/”、“.”和“_”等字符。支持中文描述。
        self.description = description
        self.eip_transmit = eip_transmit
        # 健康检查使用的端口。取值：1-65535  不设置此参数时，表示使用后端服务端口（BackendServerPort）
        self.health_check_connect_port = health_check_connect_port
        # 接收来自运行状况检查的响应需要等待的时间。  如果后端ENS在指定的时间内没有正确响应，则判定为健康检查失败。  取值：1-300（秒）。默认为5秒
        self.health_check_connect_timeout = health_check_connect_timeout
        # UDP监听健康检查的响应串，只允许包含字母、数字，最大长度限制为64个字符。
        self.health_check_exp = health_check_exp
        # 健康检查的时间间隔。  取值：1-50（秒）。
        self.health_check_interval = health_check_interval
        # UDP监听健康检查的请求串，只允许包含字母、数字，最大长度限制为64个字符。
        self.health_check_req = health_check_req
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值：2-10。
        self.healthy_threshold = healthy_threshold
        # 负载均衡实例前端使用的端口。  取值：1-65535。
        self.listener_port = listener_port
        # 负载均衡实例的ID。
        self.load_balancer_id = load_balancer_id
        # 调度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 sch：基于源IP地址的一致性hash，相同的源地址会调度到相同的后端服务器。
        self.scheduler = scheduler
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2-10。
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.description is not None:
            result['Description'] = self.description
        if self.eip_transmit is not None:
            result['EipTransmit'] = self.eip_transmit
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_exp is not None:
            result['HealthCheckExp'] = self.health_check_exp
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EipTransmit') is not None:
            self.eip_transmit = m.get('EipTransmit')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckExp') is not None:
            self.health_check_exp = m.get('HealthCheckExp')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class CreateLoadBalancerUDPListenerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLoadBalancerUDPListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerUDPListenerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLoadBalancerUDPListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNatGatewayRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        name: str = None,
        network_id: str = None,
        v_switch_id: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.name = name
        self.network_id = network_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateNatGatewayResponseBody(TeaModel):
    def __init__(
        self,
        nat_gateway_id: str = None,
        request_id: str = None,
    ):
        self.nat_gateway_id = nat_gateway_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNatGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNatGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNatGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkRequest(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        ens_region_id: str = None,
        network_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.description = description
        self.ens_region_id = ens_region_id
        self.network_name = network_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.description is not None:
            result['Description'] = self.description
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.network_name is not None:
            result['NetworkName'] = self.network_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')
        return self


class CreateNetworkResponseBody(TeaModel):
    def __init__(
        self,
        network_id: str = None,
        request_id: str = None,
    ):
        self.network_id = network_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNetworkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNetworkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        security_group_name: str = None,
        version: str = None,
    ):
        self.description = description
        self.security_group_name = security_group_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_group_id: str = None,
    ):
        self.request_id = request_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class CreateSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnatEntryRequest(TeaModel):
    def __init__(
        self,
        nat_gateway_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        source_cidr: str = None,
        source_vswitch_id: str = None,
    ):
        self.nat_gateway_id = nat_gateway_id
        self.snat_entry_name = snat_entry_name
        self.snat_ip = snat_ip
        self.source_cidr = source_cidr
        self.source_vswitch_id = source_vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name
        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip
        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr
        if self.source_vswitch_id is not None:
            result['SourceVSwitchId'] = self.source_vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')
        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')
        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')
        if m.get('SourceVSwitchId') is not None:
            self.source_vswitch_id = m.get('SourceVSwitchId')
        return self


class CreateSnatEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        snat_entry_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.snat_entry_id = snat_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')
        return self


class CreateSnatEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSnatEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSnatEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVSwitchRequest(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        ens_region_id: str = None,
        network_id: str = None,
        v_switch_name: str = None,
        version: str = None,
    ):
        self.cidr_block = cidr_block
        self.description = description
        self.ens_region_id = ens_region_id
        self.network_id = network_id
        self.v_switch_name = v_switch_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.description is not None:
            result['Description'] = self.description
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateVSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        v_switch_id: str = None,
    ):
        self.request_id = request_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateVSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        timeout: int = None,
    ):
        self.app_id = app_id
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceInternetPortRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        nat_type: str = None,
        rule_id: str = None,
    ):
        # InstanceId
        self.instance_id = instance_id
        # NatType
        self.nat_type = nat_type
        # RuleId
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nat_type is not None:
            result['NatType'] = self.nat_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteDeviceInternetPortResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rule_ids: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # RuleIds
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        return self


class DeleteDeviceInternetPortResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceInternetPortResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDeviceInternetPortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnsRouteEntryRequest(TeaModel):
    def __init__(
        self,
        route_entry_id: str = None,
    ):
        # 要删除的路由条目ID。
        self.route_entry_id = route_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')
        return self


class DeleteEnsRouteEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEnsRouteEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEnsRouteEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEnsRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
    ):
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        return self


class DeleteEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteForwardEntryRequest(TeaModel):
    def __init__(
        self,
        forward_entry_id: str = None,
    ):
        self.forward_entry_id = forward_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')
        return self


class DeleteForwardEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteForwardEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteForwardEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteForwardEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeyPairsRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        version: str = None,
    ):
        self.key_pair_name = key_pair_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DeleteKeyPairsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteKeyPairsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoadBalancerListenerRequest(TeaModel):
    def __init__(
        self,
        listener_port: int = None,
        load_balancer_id: str = None,
    ):
        self.listener_port = listener_port
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DeleteLoadBalancerListenerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLoadBalancerListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLoadBalancerListenerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteLoadBalancerListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNatGatewayRequest(TeaModel):
    def __init__(
        self,
        nat_gateway_id: str = None,
    ):
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        return self


class DeleteNatGatewayResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNatGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNatGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNatGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkRequest(TeaModel):
    def __init__(
        self,
        network_id: str = None,
    ):
        self.network_id = network_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        return self


class DeleteNetworkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNetworkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNetworkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        version: str = None,
    ):
        self.security_group_id = security_group_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DeleteSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnatEntryRequest(TeaModel):
    def __init__(
        self,
        snat_entry_id: str = None,
    ):
        self.snat_entry_id = snat_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')
        return self


class DeleteSnatEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSnatEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSnatEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSnatEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVSwitchRequest(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        version: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DeleteVSwitchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_versions: str = None,
        level: str = None,
        out_detail_stat_params: str = None,
    ):
        self.app_id = app_id
        self.app_versions = app_versions
        self.level = level
        self.out_detail_stat_params = out_detail_stat_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_versions is not None:
            result['AppVersions'] = self.app_versions
        if self.level is not None:
            result['Level'] = self.level
        if self.out_detail_stat_params is not None:
            result['OutDetailStatParams'] = self.out_detail_stat_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersions') is not None:
            self.app_versions = m.get('AppVersions')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('OutDetailStatParams') is not None:
            self.out_detail_stat_params = m.get('OutDetailStatParams')
        return self


class DescribeApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application: str = None,
        request_id: str = None,
    ):
        self.application = application
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationResourceSummaryRequest(TeaModel):
    def __init__(
        self,
        level: str = None,
        resource_type: str = None,
    ):
        self.level = level
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeApplicationResourceSummaryResponseBody(TeaModel):
    def __init__(
        self,
        application_resource: str = None,
        request_id: str = None,
    ):
        self.application_resource = application_resource
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_resource is not None:
            result['ApplicationResource'] = self.application_resource
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationResource') is not None:
            self.application_resource = m.get('ApplicationResource')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApplicationResourceSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationResourceSummaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApplicationResourceSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAvailableResourceResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
    ):
        self.image_id = image_id
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        return self


class DescribeAvailableResourceResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeAvailableResourceResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeAvailableResourceResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodySupportResourcesSupportResource(TeaModel):
    def __init__(
        self,
        data_disk_size: str = None,
        ens_region_id: str = None,
        instance_spec: str = None,
        support_resources_count: str = None,
        system_disk_size: str = None,
    ):
        self.data_disk_size = data_disk_size
        self.ens_region_id = ens_region_id
        self.instance_spec = instance_spec
        self.support_resources_count = support_resources_count
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.support_resources_count is not None:
            result['SupportResourcesCount'] = self.support_resources_count
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('SupportResourcesCount') is not None:
            self.support_resources_count = m.get('SupportResourcesCount')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeAvailableResourceResponseBodySupportResources(TeaModel):
    def __init__(
        self,
        support_resource: List[DescribeAvailableResourceResponseBodySupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k in m.get('SupportResource'):
                temp_model = DescribeAvailableResourceResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        images: DescribeAvailableResourceResponseBodyImages = None,
        request_id: str = None,
        support_resources: DescribeAvailableResourceResponseBodySupportResources = None,
    ):
        self.code = code
        self.images = images
        self.request_id = request_id
        self.support_resources = support_resources

    def validate(self):
        if self.images:
            self.images.validate()
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Images') is not None:
            temp_model = DescribeAvailableResourceResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m['SupportResources'])
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAvailableResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceInfoRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAvailableResourceInfoResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        image_size: int = None,
    ):
        self.image_id = image_id
        self.image_name = image_name
        self.image_size = image_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        return self


class DescribeAvailableResourceInfoResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeAvailableResourceInfoResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeAvailableResourceInfoResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceBandwidthTypes(TeaModel):
    def __init__(
        self,
        bandwidth_type: List[str] = None,
    ):
        self.bandwidth_type = bandwidth_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        return self


class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIds(TeaModel):
    def __init__(
        self,
        ens_region_id: List[str] = None,
    ):
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        return self


class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtendsEnsRegionId(TeaModel):
    def __init__(
        self,
        area: str = None,
        en_name: str = None,
        ens_region_id: str = None,
        name: str = None,
        province: str = None,
    ):
        self.area = area
        self.en_name = en_name
        self.ens_region_id = ens_region_id
        self.name = name
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtends(TeaModel):
    def __init__(
        self,
        ens_region_id: List[DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtendsEnsRegionId] = None,
    ):
        self.ens_region_id = ens_region_id

    def validate(self):
        if self.ens_region_id:
            for k in self.ens_region_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnsRegionId'] = []
        if self.ens_region_id is not None:
            for k in self.ens_region_id:
                result['EnsRegionId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_region_id = []
        if m.get('EnsRegionId') is not None:
            for k in m.get('EnsRegionId'):
                temp_model = DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtendsEnsRegionId()
                self.ens_region_id.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceInstanceSpeces(TeaModel):
    def __init__(
        self,
        instance_spec: List[str] = None,
    ):
        self.instance_spec = instance_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        return self


class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResource(TeaModel):
    def __init__(
        self,
        bandwidth_types: DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceBandwidthTypes = None,
        data_disk_max_size: int = None,
        data_disk_min_size: int = None,
        ens_region_ids: DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIds = None,
        ens_region_ids_extends: DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtends = None,
        instance_speces: DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceInstanceSpeces = None,
        system_disk_max_size: int = None,
        system_disk_min_size: int = None,
    ):
        self.bandwidth_types = bandwidth_types
        self.data_disk_max_size = data_disk_max_size
        self.data_disk_min_size = data_disk_min_size
        self.ens_region_ids = ens_region_ids
        self.ens_region_ids_extends = ens_region_ids_extends
        self.instance_speces = instance_speces
        self.system_disk_max_size = system_disk_max_size
        self.system_disk_min_size = system_disk_min_size

    def validate(self):
        if self.bandwidth_types:
            self.bandwidth_types.validate()
        if self.ens_region_ids:
            self.ens_region_ids.validate()
        if self.ens_region_ids_extends:
            self.ens_region_ids_extends.validate()
        if self.instance_speces:
            self.instance_speces.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_types is not None:
            result['BandwidthTypes'] = self.bandwidth_types.to_map()
        if self.data_disk_max_size is not None:
            result['DataDiskMaxSize'] = self.data_disk_max_size
        if self.data_disk_min_size is not None:
            result['DataDiskMinSize'] = self.data_disk_min_size
        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids.to_map()
        if self.ens_region_ids_extends is not None:
            result['EnsRegionIdsExtends'] = self.ens_region_ids_extends.to_map()
        if self.instance_speces is not None:
            result['InstanceSpeces'] = self.instance_speces.to_map()
        if self.system_disk_max_size is not None:
            result['SystemDiskMaxSize'] = self.system_disk_max_size
        if self.system_disk_min_size is not None:
            result['SystemDiskMinSize'] = self.system_disk_min_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthTypes') is not None:
            temp_model = DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceBandwidthTypes()
            self.bandwidth_types = temp_model.from_map(m['BandwidthTypes'])
        if m.get('DataDiskMaxSize') is not None:
            self.data_disk_max_size = m.get('DataDiskMaxSize')
        if m.get('DataDiskMinSize') is not None:
            self.data_disk_min_size = m.get('DataDiskMinSize')
        if m.get('EnsRegionIds') is not None:
            temp_model = DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIds()
            self.ens_region_ids = temp_model.from_map(m['EnsRegionIds'])
        if m.get('EnsRegionIdsExtends') is not None:
            temp_model = DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtends()
            self.ens_region_ids_extends = temp_model.from_map(m['EnsRegionIdsExtends'])
        if m.get('InstanceSpeces') is not None:
            temp_model = DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceInstanceSpeces()
            self.instance_speces = temp_model.from_map(m['InstanceSpeces'])
        if m.get('SystemDiskMaxSize') is not None:
            self.system_disk_max_size = m.get('SystemDiskMaxSize')
        if m.get('SystemDiskMinSize') is not None:
            self.system_disk_min_size = m.get('SystemDiskMinSize')
        return self


class DescribeAvailableResourceInfoResponseBodySupportResources(TeaModel):
    def __init__(
        self,
        support_resource: List[DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k in m.get('SupportResource'):
                temp_model = DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceInfoResponseBody(TeaModel):
    def __init__(
        self,
        images: DescribeAvailableResourceInfoResponseBodyImages = None,
        request_id: str = None,
        support_resources: DescribeAvailableResourceInfoResponseBodySupportResources = None,
    ):
        self.images = images
        self.request_id = request_id
        self.support_resources = support_resources

    def validate(self):
        if self.images:
            self.images.validate()
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            temp_model = DescribeAvailableResourceInfoResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportResources') is not None:
            temp_model = DescribeAvailableResourceInfoResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m['SupportResources'])
        return self


class DescribeAvailableResourceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAvailableResourceInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAvailableResourceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBandWithdChargeTypeRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeBandWithdChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        band_with_type_info: str = None,
        charge_contract_type: str = None,
        charge_cycle_info: str = None,
        code: int = None,
        request_id: str = None,
    ):
        self.band_with_type_info = band_with_type_info
        self.charge_contract_type = charge_contract_type
        self.charge_cycle_info = charge_cycle_info
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_with_type_info is not None:
            result['BandWithTypeInfo'] = self.band_with_type_info
        if self.charge_contract_type is not None:
            result['ChargeContractType'] = self.charge_contract_type
        if self.charge_cycle_info is not None:
            result['ChargeCycleInfo'] = self.charge_cycle_info
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWithTypeInfo') is not None:
            self.band_with_type_info = m.get('BandWithTypeInfo')
        if m.get('ChargeContractType') is not None:
            self.charge_contract_type = m.get('ChargeContractType')
        if m.get('ChargeCycleInfo') is not None:
            self.charge_cycle_info = m.get('ChargeCycleInfo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBandWithdChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBandWithdChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBandWithdChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBandwitdhByInternetChargeTypeRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        ens_region_id: str = None,
        isp: str = None,
        start_time: str = None,
        version: str = None,
    ):
        self.end_time = end_time
        self.ens_region_id = ens_region_id
        self.isp = isp
        self.start_time = start_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeBandwitdhByInternetChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_value: int = None,
        internet_charge_type: str = None,
        request_id: str = None,
        time_stamp: str = None,
    ):
        self.bandwidth_value = bandwidth_value
        self.internet_charge_type = internet_charge_type
        self.request_id = request_id
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_value is not None:
            result['BandwidthValue'] = self.bandwidth_value
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthValue') is not None:
            self.bandwidth_value = m.get('BandwidthValue')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeBandwitdhByInternetChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBandwitdhByInternetChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBandwitdhByInternetChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudDiskAvailableResourceInfoResponseBodySupportResourcesSupportResource(TeaModel):
    def __init__(
        self,
        can_buy_count: int = None,
        category: str = None,
        default_disk_size: int = None,
        disk_max_size: int = None,
        disk_min_size: int = None,
        ens_region_id: str = None,
        ens_region_name: str = None,
    ):
        self.can_buy_count = can_buy_count
        self.category = category
        self.default_disk_size = default_disk_size
        self.disk_max_size = disk_max_size
        self.disk_min_size = disk_min_size
        self.ens_region_id = ens_region_id
        self.ens_region_name = ens_region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_buy_count is not None:
            result['CanBuyCount'] = self.can_buy_count
        if self.category is not None:
            result['Category'] = self.category
        if self.default_disk_size is not None:
            result['DefaultDiskSize'] = self.default_disk_size
        if self.disk_max_size is not None:
            result['DiskMaxSize'] = self.disk_max_size
        if self.disk_min_size is not None:
            result['DiskMinSize'] = self.disk_min_size
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.ens_region_name is not None:
            result['EnsRegionName'] = self.ens_region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBuyCount') is not None:
            self.can_buy_count = m.get('CanBuyCount')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DefaultDiskSize') is not None:
            self.default_disk_size = m.get('DefaultDiskSize')
        if m.get('DiskMaxSize') is not None:
            self.disk_max_size = m.get('DiskMaxSize')
        if m.get('DiskMinSize') is not None:
            self.disk_min_size = m.get('DiskMinSize')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('EnsRegionName') is not None:
            self.ens_region_name = m.get('EnsRegionName')
        return self


class DescribeCloudDiskAvailableResourceInfoResponseBodySupportResources(TeaModel):
    def __init__(
        self,
        support_resource: List[DescribeCloudDiskAvailableResourceInfoResponseBodySupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k in m.get('SupportResource'):
                temp_model = DescribeCloudDiskAvailableResourceInfoResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        return self


class DescribeCloudDiskAvailableResourceInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        support_resources: DescribeCloudDiskAvailableResourceInfoResponseBodySupportResources = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.support_resources = support_resources

    def validate(self):
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportResources') is not None:
            temp_model = DescribeCloudDiskAvailableResourceInfoResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m['SupportResources'])
        return self


class DescribeCloudDiskAvailableResourceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCloudDiskAvailableResourceInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCloudDiskAvailableResourceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudDiskTypesRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
    ):
        # A short description of struct
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        return self


class DescribeCloudDiskTypesResponseBodySupportResourcesSupportResource(TeaModel):
    def __init__(
        self,
        category: str = None,
        ens_region_id: str = None,
    ):
        self.category = category
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        return self


class DescribeCloudDiskTypesResponseBodySupportResources(TeaModel):
    def __init__(
        self,
        support_resource: List[DescribeCloudDiskTypesResponseBodySupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k in m.get('SupportResource'):
                temp_model = DescribeCloudDiskTypesResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        return self


class DescribeCloudDiskTypesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        support_resources: DescribeCloudDiskTypesResponseBodySupportResources = None,
    ):
        self.request_id = request_id
        self.support_resources = support_resources

    def validate(self):
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportResources') is not None:
            temp_model = DescribeCloudDiskTypesResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m['SupportResources'])
        return self


class DescribeCloudDiskTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCloudDiskTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCloudDiskTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCreatePrePaidInstanceResultRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        version: str = None,
    ):
        self.instance_id = instance_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeCreatePrePaidInstanceResultResponseBodyInstanceCreateResult(TeaModel):
    def __init__(
        self,
        instance_create_status: str = None,
        instance_id: str = None,
    ):
        self.instance_create_status = instance_create_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_create_status is not None:
            result['InstanceCreateStatus'] = self.instance_create_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCreateStatus') is not None:
            self.instance_create_status = m.get('InstanceCreateStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeCreatePrePaidInstanceResultResponseBody(TeaModel):
    def __init__(
        self,
        instance_create_result: DescribeCreatePrePaidInstanceResultResponseBodyInstanceCreateResult = None,
        request_id: str = None,
    ):
        self.instance_create_result = instance_create_result
        self.request_id = request_id

    def validate(self):
        if self.instance_create_result:
            self.instance_create_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_create_result is not None:
            result['InstanceCreateResult'] = self.instance_create_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCreateResult') is not None:
            temp_model = DescribeCreatePrePaidInstanceResultResponseBodyInstanceCreateResult()
            self.instance_create_result = temp_model.from_map(m['InstanceCreateResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCreatePrePaidInstanceResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCreatePrePaidInstanceResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCreatePrePaidInstanceResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataDistResultRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        data_names: str = None,
        data_versions: str = None,
        instance_ids: str = None,
        max_date: str = None,
        min_date: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.data_names = data_names
        self.data_versions = data_versions
        self.instance_ids = instance_ids
        self.max_date = max_date
        self.min_date = min_date
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.data_names is not None:
            result['DataNames'] = self.data_names
        if self.data_versions is not None:
            result['DataVersions'] = self.data_versions
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.max_date is not None:
            result['MaxDate'] = self.max_date
        if self.min_date is not None:
            result['MinDate'] = self.min_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DataNames') is not None:
            self.data_names = m.get('DataNames')
        if m.get('DataVersions') is not None:
            self.data_versions = m.get('DataVersions')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')
        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstancesInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_time: str = None,
        status_descrip: str = None,
        update_time: str = None,
    ):
        self.instance_id = instance_id
        self.start_time = start_time
        self.status_descrip = status_descrip
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_descrip is not None:
            result['StatusDescrip'] = self.status_descrip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusDescrip') is not None:
            self.status_descrip = m.get('StatusDescrip')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstances(TeaModel):
    def __init__(
        self,
        instance: List[DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStat(TeaModel):
    def __init__(
        self,
        instance_count: str = None,
        instances: DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstances = None,
        status: str = None,
    ):
        self.instance_count = instance_count
        self.instances = instances
        self.status = status

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Instances') is not None:
            temp_model = DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStatInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResultStatusStats(TeaModel):
    def __init__(
        self,
        status_stat: List[DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStat] = None,
    ):
        self.status_stat = status_stat

    def validate(self):
        if self.status_stat:
            for k in self.status_stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StatusStat'] = []
        if self.status_stat is not None:
            for k in self.status_stat:
                result['StatusStat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.status_stat = []
        if m.get('StatusStat') is not None:
            for k in m.get('StatusStat'):
                temp_model = DescribeDataDistResultResponseBodyDistResultsDistResultStatusStatsStatusStat()
                self.status_stat.append(temp_model.from_map(k))
        return self


class DescribeDataDistResultResponseBodyDistResultsDistResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        status_stats: DescribeDataDistResultResponseBodyDistResultsDistResultStatusStats = None,
        version: str = None,
    ):
        self.name = name
        self.status_stats = status_stats
        self.version = version

    def validate(self):
        if self.status_stats:
            self.status_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.status_stats is not None:
            result['StatusStats'] = self.status_stats.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StatusStats') is not None:
            temp_model = DescribeDataDistResultResponseBodyDistResultsDistResultStatusStats()
            self.status_stats = temp_model.from_map(m['StatusStats'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeDataDistResultResponseBodyDistResults(TeaModel):
    def __init__(
        self,
        dist_result: List[DescribeDataDistResultResponseBodyDistResultsDistResult] = None,
    ):
        self.dist_result = dist_result

    def validate(self):
        if self.dist_result:
            for k in self.dist_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistResult'] = []
        if self.dist_result is not None:
            for k in self.dist_result:
                result['DistResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dist_result = []
        if m.get('DistResult') is not None:
            for k in m.get('DistResult'):
                temp_model = DescribeDataDistResultResponseBodyDistResultsDistResult()
                self.dist_result.append(temp_model.from_map(k))
        return self


class DescribeDataDistResultResponseBody(TeaModel):
    def __init__(
        self,
        dist_results: DescribeDataDistResultResponseBodyDistResults = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dist_results = dist_results
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.dist_results:
            self.dist_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dist_results is not None:
            result['DistResults'] = self.dist_results.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistResults') is not None:
            temp_model = DescribeDataDistResultResponseBodyDistResults()
            self.dist_results = temp_model.from_map(m['DistResults'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataDistResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataDistResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDataDistResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataDownloadURLRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        data_name: str = None,
        data_version: str = None,
        expire_timeout: int = None,
        server_filter_strategy: str = None,
    ):
        self.app_id = app_id
        self.data_name = data_name
        self.data_version = data_version
        self.expire_timeout = expire_timeout
        self.server_filter_strategy = server_filter_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.data_name is not None:
            result['DataName'] = self.data_name
        if self.data_version is not None:
            result['DataVersion'] = self.data_version
        if self.expire_timeout is not None:
            result['ExpireTimeout'] = self.expire_timeout
        if self.server_filter_strategy is not None:
            result['ServerFilterStrategy'] = self.server_filter_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')
        if m.get('DataVersion') is not None:
            self.data_version = m.get('DataVersion')
        if m.get('ExpireTimeout') is not None:
            self.expire_timeout = m.get('ExpireTimeout')
        if m.get('ServerFilterStrategy') is not None:
            self.server_filter_strategy = m.get('ServerFilterStrategy')
        return self


class DescribeDataDownloadURLResponseBodyDataServerList(TeaModel):
    def __init__(
        self,
        host: str = None,
        region_id: str = None,
    ):
        self.host = host
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDataDownloadURLResponseBodyData(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        server_list: List[DescribeDataDownloadURLResponseBodyDataServerList] = None,
        url: str = None,
    ):
        self.expire_time = expire_time
        self.server_list = server_list
        self.url = url

    def validate(self):
        if self.server_list:
            for k in self.server_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        result['ServerList'] = []
        if self.server_list is not None:
            for k in self.server_list:
                result['ServerList'].append(k.to_map() if k else None)
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        self.server_list = []
        if m.get('ServerList') is not None:
            for k in m.get('ServerList'):
                temp_model = DescribeDataDownloadURLResponseBodyDataServerList()
                self.server_list.append(temp_model.from_map(k))
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDataDownloadURLResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeDataDownloadURLResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeDataDownloadURLResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataDownloadURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataDownloadURLResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDataDownloadURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataPushResultRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        data_names: str = None,
        data_versions: str = None,
        max_date: str = None,
        min_date: str = None,
        page_number: int = None,
        page_size: int = None,
        region_ids: str = None,
    ):
        self.app_id = app_id
        self.data_names = data_names
        self.data_versions = data_versions
        self.max_date = max_date
        self.min_date = min_date
        self.page_number = page_number
        self.page_size = page_size
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.data_names is not None:
            result['DataNames'] = self.data_names
        if self.data_versions is not None:
            result['DataVersions'] = self.data_versions
        if self.max_date is not None:
            result['MaxDate'] = self.max_date
        if self.min_date is not None:
            result['MinDate'] = self.min_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DataNames') is not None:
            self.data_names = m.get('DataNames')
        if m.get('DataVersions') is not None:
            self.data_versions = m.get('DataVersions')
        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')
        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIdsRegionId(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        start_time: str = None,
        status_descrip: str = None,
        update_time: str = None,
    ):
        self.region_id = region_id
        self.start_time = start_time
        self.status_descrip = status_descrip
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_descrip is not None:
            result['StatusDescrip'] = self.status_descrip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusDescrip') is not None:
            self.status_descrip = m.get('StatusDescrip')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIds(TeaModel):
    def __init__(
        self,
        region_id: List[DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIdsRegionId] = None,
    ):
        self.region_id = region_id

    def validate(self):
        if self.region_id:
            for k in self.region_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionId'] = []
        if self.region_id is not None:
            for k in self.region_id:
                result['RegionId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_id = []
        if m.get('RegionId') is not None:
            for k in m.get('RegionId'):
                temp_model = DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIdsRegionId()
                self.region_id.append(temp_model.from_map(k))
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStat(TeaModel):
    def __init__(
        self,
        region_id_count: int = None,
        region_ids: DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIds = None,
        status: str = None,
    ):
        self.region_id_count = region_id_count
        self.region_ids = region_ids
        self.status = status

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id_count is not None:
            result['RegionIdCount'] = self.region_id_count
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIdCount') is not None:
            self.region_id_count = m.get('RegionIdCount')
        if m.get('RegionIds') is not None:
            temp_model = DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStatRegionIds()
            self.region_ids = temp_model.from_map(m['RegionIds'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatS(TeaModel):
    def __init__(
        self,
        status_stat: List[DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStat] = None,
    ):
        self.status_stat = status_stat

    def validate(self):
        if self.status_stat:
            for k in self.status_stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StatusStat'] = []
        if self.status_stat is not None:
            for k in self.status_stat:
                result['StatusStat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.status_stat = []
        if m.get('StatusStat') is not None:
            for k in m.get('StatusStat'):
                temp_model = DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatSStatusStat()
                self.status_stat.append(temp_model.from_map(k))
        return self


class DescribeDataPushResultResponseBodyPushResultsPushResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        status_stat_s: DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatS = None,
        version: str = None,
    ):
        self.name = name
        self.status_stat_s = status_stat_s
        self.version = version

    def validate(self):
        if self.status_stat_s:
            self.status_stat_s.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.status_stat_s is not None:
            result['StatusStatS'] = self.status_stat_s.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StatusStatS') is not None:
            temp_model = DescribeDataPushResultResponseBodyPushResultsPushResultStatusStatS()
            self.status_stat_s = temp_model.from_map(m['StatusStatS'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeDataPushResultResponseBodyPushResults(TeaModel):
    def __init__(
        self,
        push_result: List[DescribeDataPushResultResponseBodyPushResultsPushResult] = None,
    ):
        self.push_result = push_result

    def validate(self):
        if self.push_result:
            for k in self.push_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PushResult'] = []
        if self.push_result is not None:
            for k in self.push_result:
                result['PushResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_result = []
        if m.get('PushResult') is not None:
            for k in m.get('PushResult'):
                temp_model = DescribeDataPushResultResponseBodyPushResultsPushResult()
                self.push_result.append(temp_model.from_map(k))
        return self


class DescribeDataPushResultResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        push_results: DescribeDataPushResultResponseBodyPushResults = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.push_results = push_results
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.push_results:
            self.push_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.push_results is not None:
            result['PushResults'] = self.push_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PushResults') is not None:
            temp_model = DescribeDataPushResultResponseBodyPushResults()
            self.push_results = temp_model.from_map(m['PushResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDataPushResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataPushResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDataPushResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceServiceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        order_id: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        self.app_id = app_id
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.order_id = order_id
        self.region_id = region_id
        # Service ID
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DescribeDeviceServiceResponseBodyAppMetaData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_stable_version: str = None,
        app_type: str = None,
        cluster_name: str = None,
        create_time: str = None,
        description: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_stable_version = app_stable_version
        self.app_type = app_type
        self.cluster_name = cluster_name
        self.create_time = create_time
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_stable_version is not None:
            result['AppStableVersion'] = self.app_stable_version
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStableVersion') is not None:
            self.app_stable_version = m.get('AppStableVersion')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class DescribeDeviceServiceResponseBodyAppStatus(TeaModel):
    def __init__(
        self,
        phase: str = None,
        status_descrip: str = None,
        update_time: str = None,
    ):
        self.phase = phase
        self.status_descrip = status_descrip
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.status_descrip is not None:
            result['StatusDescrip'] = self.status_descrip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('StatusDescrip') is not None:
            self.status_descrip = m.get('StatusDescrip')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDeviceServiceResponseBodyResourceDetailInfos(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        id: str = None,
        ip: str = None,
        isp: str = None,
        image_id: str = None,
        mac: str = None,
        region_id: str = None,
        server: str = None,
        status: str = None,
        type: str = None,
    ):
        self.device_name = device_name
        self.id = id
        self.ip = ip
        self.isp = isp
        self.image_id = image_id
        self.mac = mac
        self.region_id = region_id
        self.server = server
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.id is not None:
            result['ID'] = self.id
        if self.ip is not None:
            result['IP'] = self.ip
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.image_id is not None:
            result['ImageID'] = self.image_id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        if self.server is not None:
            result['Server'] = self.server
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('ImageID') is not None:
            self.image_id = m.get('ImageID')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDeviceServiceResponseBodyResourceInfosDeviceInfosNetwork(TeaModel):
    def __init__(
        self,
        container_ports: str = None,
        external_ip: str = None,
        host_ports: str = None,
        protocol: str = None,
    ):
        self.container_ports = container_ports
        self.external_ip = external_ip
        self.host_ports = host_ports
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_ports is not None:
            result['ContainerPorts'] = self.container_ports
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.host_ports is not None:
            result['HostPorts'] = self.host_ports
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerPorts') is not None:
            self.container_ports = m.get('ContainerPorts')
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('HostPorts') is not None:
            self.host_ports = m.get('HostPorts')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeDeviceServiceResponseBodyResourceInfosDeviceInfos(TeaModel):
    def __init__(
        self,
        name: str = None,
        network: List[DescribeDeviceServiceResponseBodyResourceInfosDeviceInfosNetwork] = None,
        status: str = None,
    ):
        self.name = name
        self.network = network
        self.status = status

    def validate(self):
        if self.network:
            for k in self.network:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Network'] = []
        if self.network is not None:
            for k in self.network:
                result['Network'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.network = []
        if m.get('Network') is not None:
            for k in m.get('Network'):
                temp_model = DescribeDeviceServiceResponseBodyResourceInfosDeviceInfosNetwork()
                self.network.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDeviceServiceResponseBodyResourceInfosInternalIps(TeaModel):
    def __init__(
        self,
        ip: str = None,
    ):
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDeviceServiceResponseBodyResourceInfosPublicIps(TeaModel):
    def __init__(
        self,
        ip: str = None,
    ):
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDeviceServiceResponseBodyResourceInfos(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        area_code: str = None,
        area_name: str = None,
        create_time: str = None,
        device_infos: List[DescribeDeviceServiceResponseBodyResourceInfosDeviceInfos] = None,
        instance_id: str = None,
        instance_status: str = None,
        internal_ips: List[DescribeDeviceServiceResponseBodyResourceInfosInternalIps] = None,
        public_ips: List[DescribeDeviceServiceResponseBodyResourceInfosPublicIps] = None,
        region_code: str = None,
        region_id: str = None,
        region_name: str = None,
    ):
        self.app_version = app_version
        self.area_code = area_code
        self.area_name = area_name
        self.create_time = create_time
        self.device_infos = device_infos
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.internal_ips = internal_ips
        self.public_ips = public_ips
        self.region_code = region_code
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        if self.device_infos:
            for k in self.device_infos:
                if k:
                    k.validate()
        if self.internal_ips:
            for k in self.internal_ips:
                if k:
                    k.validate()
        if self.public_ips:
            for k in self.public_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.area_code is not None:
            result['AreaCode'] = self.area_code
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k in self.device_infos:
                result['DeviceInfos'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        result['InternalIps'] = []
        if self.internal_ips is not None:
            for k in self.internal_ips:
                result['InternalIps'].append(k.to_map() if k else None)
        result['PublicIps'] = []
        if self.public_ips is not None:
            for k in self.public_ips:
                result['PublicIps'].append(k.to_map() if k else None)
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k in m.get('DeviceInfos'):
                temp_model = DescribeDeviceServiceResponseBodyResourceInfosDeviceInfos()
                self.device_infos.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        self.internal_ips = []
        if m.get('InternalIps') is not None:
            for k in m.get('InternalIps'):
                temp_model = DescribeDeviceServiceResponseBodyResourceInfosInternalIps()
                self.internal_ips.append(temp_model.from_map(k))
        self.public_ips = []
        if m.get('PublicIps') is not None:
            for k in m.get('PublicIps'):
                temp_model = DescribeDeviceServiceResponseBodyResourceInfosPublicIps()
                self.public_ips.append(temp_model.from_map(k))
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeDeviceServiceResponseBody(TeaModel):
    def __init__(
        self,
        app_meta_data: DescribeDeviceServiceResponseBodyAppMetaData = None,
        app_status: DescribeDeviceServiceResponseBodyAppStatus = None,
        request_id: str = None,
        resource_detail_infos: List[DescribeDeviceServiceResponseBodyResourceDetailInfos] = None,
        resource_infos: List[DescribeDeviceServiceResponseBodyResourceInfos] = None,
    ):
        self.app_meta_data = app_meta_data
        self.app_status = app_status
        # Id of the request
        self.request_id = request_id
        self.resource_detail_infos = resource_detail_infos
        self.resource_infos = resource_infos

    def validate(self):
        if self.app_meta_data:
            self.app_meta_data.validate()
        if self.app_status:
            self.app_status.validate()
        if self.resource_detail_infos:
            for k in self.resource_detail_infos:
                if k:
                    k.validate()
        if self.resource_infos:
            for k in self.resource_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_meta_data is not None:
            result['AppMetaData'] = self.app_meta_data.to_map()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceDetailInfos'] = []
        if self.resource_detail_infos is not None:
            for k in self.resource_detail_infos:
                result['ResourceDetailInfos'].append(k.to_map() if k else None)
        result['ResourceInfos'] = []
        if self.resource_infos is not None:
            for k in self.resource_infos:
                result['ResourceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppMetaData') is not None:
            temp_model = DescribeDeviceServiceResponseBodyAppMetaData()
            self.app_meta_data = temp_model.from_map(m['AppMetaData'])
        if m.get('AppStatus') is not None:
            temp_model = DescribeDeviceServiceResponseBodyAppStatus()
            self.app_status = temp_model.from_map(m['AppStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_detail_infos = []
        if m.get('ResourceDetailInfos') is not None:
            for k in m.get('ResourceDetailInfos'):
                temp_model = DescribeDeviceServiceResponseBodyResourceDetailInfos()
                self.resource_detail_infos.append(temp_model.from_map(k))
        self.resource_infos = []
        if m.get('ResourceInfos') is not None:
            for k in m.get('ResourceInfos'):
                temp_model = DescribeDeviceServiceResponseBodyResourceInfos()
                self.resource_infos.append(temp_model.from_map(k))
        return self


class DescribeDeviceServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDeviceServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisksRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_ids: str = None,
        disk_name: str = None,
        disk_type: str = None,
        ens_region_id: str = None,
        ens_region_ids: str = None,
        order_by_params: str = None,
        page_number: str = None,
        page_size: str = None,
        status: str = None,
        type: str = None,
    ):
        self.category = category
        self.disk_charge_type = disk_charge_type
        self.disk_id = disk_id
        self.disk_ids = disk_ids
        self.disk_name = disk_name
        self.disk_type = disk_type
        self.ens_region_id = ens_region_id
        self.ens_region_ids = ens_region_ids
        self.order_by_params = order_by_params
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids
        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')
        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDisksResponseBodyDisksDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        creation_time: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_name: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        portable: bool = None,
        size: int = None,
        status: str = None,
        type: str = None,
    ):
        self.category = category
        self.creation_time = creation_time
        self.disk_charge_type = disk_charge_type
        self.disk_id = disk_id
        self.disk_name = disk_name
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.portable = portable
        self.size = size
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.portable is not None:
            result['Portable'] = self.portable
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Portable') is not None:
            self.portable = m.get('Portable')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDisksResponseBodyDisks(TeaModel):
    def __init__(
        self,
        disks: List[DescribeDisksResponseBodyDisksDisks] = None,
    ):
        self.disks = disks

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDisksResponseBodyDisksDisks()
                self.disks.append(temp_model.from_map(k))
        return self


class DescribeDisksResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        disks: DescribeDisksResponseBodyDisks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.disks = disks
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.disks:
            self.disks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.disks is not None:
            result['Disks'] = self.disks.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Disks') is not None:
            temp_model = DescribeDisksResponseBodyDisks()
            self.disks = temp_model.from_map(m['Disks'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDisksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDisksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEipAddressesRequest(TeaModel):
    def __init__(
        self,
        eips: str = None,
        ens_region_id: str = None,
        version: str = None,
    ):
        self.eips = eips
        self.ens_region_id = ens_region_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eips is not None:
            result['Eips'] = self.eips
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eips') is not None:
            self.eips = m.get('Eips')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEipAddressesResponseBodyEipAddressesEipAddress(TeaModel):
    def __init__(
        self,
        eip: str = None,
        instance_id_internet_ip: str = None,
    ):
        self.eip = eip
        self.instance_id_internet_ip = instance_id_internet_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.instance_id_internet_ip is not None:
            result['InstanceIdInternetIp'] = self.instance_id_internet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('InstanceIdInternetIp') is not None:
            self.instance_id_internet_ip = m.get('InstanceIdInternetIp')
        return self


class DescribeEipAddressesResponseBodyEipAddresses(TeaModel):
    def __init__(
        self,
        eip_address: List[DescribeEipAddressesResponseBodyEipAddressesEipAddress] = None,
    ):
        self.eip_address = eip_address

    def validate(self):
        if self.eip_address:
            for k in self.eip_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k in self.eip_address:
                result['EipAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_address = []
        if m.get('EipAddress') is not None:
            for k in m.get('EipAddress'):
                temp_model = DescribeEipAddressesResponseBodyEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k))
        return self


class DescribeEipAddressesResponseBody(TeaModel):
    def __init__(
        self,
        eip_addresses: DescribeEipAddressesResponseBodyEipAddresses = None,
        request_id: str = None,
    ):
        self.eip_addresses = eip_addresses
        self.request_id = request_id

    def validate(self):
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAddresses') is not None:
            temp_model = DescribeEipAddressesResponseBodyEipAddresses()
            self.eip_addresses = temp_model.from_map(m['EipAddresses'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEipAddressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEipAddressesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEipAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElbAvailableResourceInfoResponseBodyElbAvailableResourceInfo(TeaModel):
    def __init__(
        self,
        area: str = None,
        can_buy_count: str = None,
        en_name: str = None,
        ens_region_id: str = None,
        load_balancer_spec: List[str] = None,
        name: str = None,
        province: str = None,
    ):
        self.area = area
        self.can_buy_count = can_buy_count
        self.en_name = en_name
        self.ens_region_id = ens_region_id
        self.load_balancer_spec = load_balancer_spec
        self.name = name
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.can_buy_count is not None:
            result['CanBuyCount'] = self.can_buy_count
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec
        if self.name is not None:
            result['Name'] = self.name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('CanBuyCount') is not None:
            self.can_buy_count = m.get('CanBuyCount')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribeElbAvailableResourceInfoResponseBody(TeaModel):
    def __init__(
        self,
        elb_available_resource_info: List[DescribeElbAvailableResourceInfoResponseBodyElbAvailableResourceInfo] = None,
        request_id: str = None,
    ):
        self.elb_available_resource_info = elb_available_resource_info
        self.request_id = request_id

    def validate(self):
        if self.elb_available_resource_info:
            for k in self.elb_available_resource_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ElbAvailableResourceInfo'] = []
        if self.elb_available_resource_info is not None:
            for k in self.elb_available_resource_info:
                result['ElbAvailableResourceInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elb_available_resource_info = []
        if m.get('ElbAvailableResourceInfo') is not None:
            for k in m.get('ElbAvailableResourceInfo'):
                temp_model = DescribeElbAvailableResourceInfoResponseBodyElbAvailableResourceInfo()
                self.elb_available_resource_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeElbAvailableResourceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeElbAvailableResourceInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeElbAvailableResourceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsEipAddressesRequest(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        associated_instance_id: str = None,
        associated_instance_type: str = None,
        eip_address: str = None,
        ens_region_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 要查询的EIP实例的ID。  最多支持输入50个EIP实例ID，实例ID之间用逗号（,）分隔。
        self.allocation_id = allocation_id
        self.associated_instance_id = associated_instance_id
        self.associated_instance_type = associated_instance_type
        # 要查询的EIP的IP地址。  最多支持输入50个EIP的IP地址，IP地址之间用逗号（,）分隔。
        self.eip_address = eip_address
        # ENS节点ID
        self.ens_region_id = ens_region_id
        # 列表的页码，默认值为1。
        self.page_number = page_number
        # 分页查询时每页的行数，最大值为100，默认值为10。
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.associated_instance_id is not None:
            result['AssociatedInstanceId'] = self.associated_instance_id
        if self.associated_instance_type is not None:
            result['AssociatedInstanceType'] = self.associated_instance_type
        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('AssociatedInstanceId') is not None:
            self.associated_instance_id = m.get('AssociatedInstanceId')
        if m.get('AssociatedInstanceType') is not None:
            self.associated_instance_type = m.get('AssociatedInstanceType')
        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeEnsEipAddressesResponseBodyEipAddressesEipAddress(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        allocation_time: str = None,
        bandwidth: int = None,
        charge_type: str = None,
        description: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        isp: str = None,
        name: str = None,
        status: str = None,
    ):
        self.allocation_id = allocation_id
        self.allocation_time = allocation_time
        self.bandwidth = bandwidth
        self.charge_type = charge_type
        self.description = description
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.internet_charge_type = internet_charge_type
        self.ip_address = ip_address
        self.isp = isp
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.allocation_time is not None:
            result['AllocationTime'] = self.allocation_time
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.description is not None:
            result['Description'] = self.description
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('AllocationTime') is not None:
            self.allocation_time = m.get('AllocationTime')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEnsEipAddressesResponseBodyEipAddresses(TeaModel):
    def __init__(
        self,
        eip_address: List[DescribeEnsEipAddressesResponseBodyEipAddressesEipAddress] = None,
    ):
        self.eip_address = eip_address

    def validate(self):
        if self.eip_address:
            for k in self.eip_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k in self.eip_address:
                result['EipAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_address = []
        if m.get('EipAddress') is not None:
            for k in m.get('EipAddress'):
                temp_model = DescribeEnsEipAddressesResponseBodyEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k))
        return self


class DescribeEnsEipAddressesResponseBody(TeaModel):
    def __init__(
        self,
        eip_addresses: DescribeEnsEipAddressesResponseBodyEipAddresses = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.eip_addresses = eip_addresses
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAddresses') is not None:
            temp_model = DescribeEnsEipAddressesResponseBodyEipAddresses()
            self.eip_addresses = temp_model.from_map(m['EipAddresses'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEnsEipAddressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsEipAddressesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsEipAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsNetDistrictRequest(TeaModel):
    def __init__(
        self,
        net_district_code: str = None,
        net_level_code: str = None,
        version: str = None,
    ):
        self.net_district_code = net_district_code
        self.net_level_code = net_level_code
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        if self.net_level_code is not None:
            result['NetLevelCode'] = self.net_level_code
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        if m.get('NetLevelCode') is not None:
            self.net_level_code = m.get('NetLevelCode')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEnsNetDistrictResponseBodyEnsNetDistrictsEnsNetDistrict(TeaModel):
    def __init__(
        self,
        ens_region_id_count: str = None,
        net_district_code: str = None,
        net_district_en_name: str = None,
        net_district_father_code: str = None,
        net_district_level: str = None,
        net_district_name: str = None,
    ):
        self.ens_region_id_count = ens_region_id_count
        self.net_district_code = net_district_code
        self.net_district_en_name = net_district_en_name
        self.net_district_father_code = net_district_father_code
        self.net_district_level = net_district_level
        self.net_district_name = net_district_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id_count is not None:
            result['EnsRegionIdCount'] = self.ens_region_id_count
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        if self.net_district_en_name is not None:
            result['NetDistrictEnName'] = self.net_district_en_name
        if self.net_district_father_code is not None:
            result['NetDistrictFatherCode'] = self.net_district_father_code
        if self.net_district_level is not None:
            result['NetDistrictLevel'] = self.net_district_level
        if self.net_district_name is not None:
            result['NetDistrictName'] = self.net_district_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionIdCount') is not None:
            self.ens_region_id_count = m.get('EnsRegionIdCount')
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        if m.get('NetDistrictEnName') is not None:
            self.net_district_en_name = m.get('NetDistrictEnName')
        if m.get('NetDistrictFatherCode') is not None:
            self.net_district_father_code = m.get('NetDistrictFatherCode')
        if m.get('NetDistrictLevel') is not None:
            self.net_district_level = m.get('NetDistrictLevel')
        if m.get('NetDistrictName') is not None:
            self.net_district_name = m.get('NetDistrictName')
        return self


class DescribeEnsNetDistrictResponseBodyEnsNetDistricts(TeaModel):
    def __init__(
        self,
        ens_net_district: List[DescribeEnsNetDistrictResponseBodyEnsNetDistrictsEnsNetDistrict] = None,
    ):
        self.ens_net_district = ens_net_district

    def validate(self):
        if self.ens_net_district:
            for k in self.ens_net_district:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnsNetDistrict'] = []
        if self.ens_net_district is not None:
            for k in self.ens_net_district:
                result['EnsNetDistrict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_net_district = []
        if m.get('EnsNetDistrict') is not None:
            for k in m.get('EnsNetDistrict'):
                temp_model = DescribeEnsNetDistrictResponseBodyEnsNetDistrictsEnsNetDistrict()
                self.ens_net_district.append(temp_model.from_map(k))
        return self


class DescribeEnsNetDistrictResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ens_net_districts: DescribeEnsNetDistrictResponseBodyEnsNetDistricts = None,
        request_id: str = None,
    ):
        self.code = code
        self.ens_net_districts = ens_net_districts
        self.request_id = request_id

    def validate(self):
        if self.ens_net_districts:
            self.ens_net_districts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_net_districts is not None:
            result['EnsNetDistricts'] = self.ens_net_districts.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsNetDistricts') is not None:
            temp_model = DescribeEnsNetDistrictResponseBodyEnsNetDistricts()
            self.ens_net_districts = temp_model.from_map(m['EnsNetDistricts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnsNetDistrictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsNetDistrictResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsNetDistrictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsNetLevelRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEnsNetLevelResponseBodyEnsNetLevelsEnsNetLevel(TeaModel):
    def __init__(
        self,
        ens_net_level_code: str = None,
    ):
        self.ens_net_level_code = ens_net_level_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_net_level_code is not None:
            result['EnsNetLevelCode'] = self.ens_net_level_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsNetLevelCode') is not None:
            self.ens_net_level_code = m.get('EnsNetLevelCode')
        return self


class DescribeEnsNetLevelResponseBodyEnsNetLevels(TeaModel):
    def __init__(
        self,
        ens_net_level: List[DescribeEnsNetLevelResponseBodyEnsNetLevelsEnsNetLevel] = None,
    ):
        self.ens_net_level = ens_net_level

    def validate(self):
        if self.ens_net_level:
            for k in self.ens_net_level:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnsNetLevel'] = []
        if self.ens_net_level is not None:
            for k in self.ens_net_level:
                result['EnsNetLevel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_net_level = []
        if m.get('EnsNetLevel') is not None:
            for k in m.get('EnsNetLevel'):
                temp_model = DescribeEnsNetLevelResponseBodyEnsNetLevelsEnsNetLevel()
                self.ens_net_level.append(temp_model.from_map(k))
        return self


class DescribeEnsNetLevelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ens_net_levels: DescribeEnsNetLevelResponseBodyEnsNetLevels = None,
        request_id: str = None,
    ):
        self.code = code
        self.ens_net_levels = ens_net_levels
        self.request_id = request_id

    def validate(self):
        if self.ens_net_levels:
            self.ens_net_levels.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_net_levels is not None:
            result['EnsNetLevels'] = self.ens_net_levels.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsNetLevels') is not None:
            temp_model = DescribeEnsNetLevelResponseBodyEnsNetLevels()
            self.ens_net_levels = temp_model.from_map(m['EnsNetLevels'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnsNetLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsNetLevelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsNetLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsNetSaleDistrictRequest(TeaModel):
    def __init__(
        self,
        net_district_code: str = None,
        net_level_code: str = None,
        version: str = None,
    ):
        self.net_district_code = net_district_code
        self.net_level_code = net_level_code
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        if self.net_level_code is not None:
            result['NetLevelCode'] = self.net_level_code
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        if m.get('NetLevelCode') is not None:
            self.net_level_code = m.get('NetLevelCode')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEnsNetSaleDistrictResponseBodyEnsNetDistrictsEnsNetDistrict(TeaModel):
    def __init__(
        self,
        ens_region_id_count: str = None,
        instance_count: str = None,
        net_district_code: str = None,
        net_district_en_name: str = None,
        net_district_father_code: str = None,
        net_district_level: str = None,
        net_district_name: str = None,
    ):
        self.ens_region_id_count = ens_region_id_count
        self.instance_count = instance_count
        self.net_district_code = net_district_code
        self.net_district_en_name = net_district_en_name
        self.net_district_father_code = net_district_father_code
        self.net_district_level = net_district_level
        self.net_district_name = net_district_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id_count is not None:
            result['EnsRegionIdCount'] = self.ens_region_id_count
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        if self.net_district_en_name is not None:
            result['NetDistrictEnName'] = self.net_district_en_name
        if self.net_district_father_code is not None:
            result['NetDistrictFatherCode'] = self.net_district_father_code
        if self.net_district_level is not None:
            result['NetDistrictLevel'] = self.net_district_level
        if self.net_district_name is not None:
            result['NetDistrictName'] = self.net_district_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionIdCount') is not None:
            self.ens_region_id_count = m.get('EnsRegionIdCount')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        if m.get('NetDistrictEnName') is not None:
            self.net_district_en_name = m.get('NetDistrictEnName')
        if m.get('NetDistrictFatherCode') is not None:
            self.net_district_father_code = m.get('NetDistrictFatherCode')
        if m.get('NetDistrictLevel') is not None:
            self.net_district_level = m.get('NetDistrictLevel')
        if m.get('NetDistrictName') is not None:
            self.net_district_name = m.get('NetDistrictName')
        return self


class DescribeEnsNetSaleDistrictResponseBodyEnsNetDistricts(TeaModel):
    def __init__(
        self,
        ens_net_district: List[DescribeEnsNetSaleDistrictResponseBodyEnsNetDistrictsEnsNetDistrict] = None,
    ):
        self.ens_net_district = ens_net_district

    def validate(self):
        if self.ens_net_district:
            for k in self.ens_net_district:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnsNetDistrict'] = []
        if self.ens_net_district is not None:
            for k in self.ens_net_district:
                result['EnsNetDistrict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_net_district = []
        if m.get('EnsNetDistrict') is not None:
            for k in m.get('EnsNetDistrict'):
                temp_model = DescribeEnsNetSaleDistrictResponseBodyEnsNetDistrictsEnsNetDistrict()
                self.ens_net_district.append(temp_model.from_map(k))
        return self


class DescribeEnsNetSaleDistrictResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ens_net_districts: DescribeEnsNetSaleDistrictResponseBodyEnsNetDistricts = None,
        request_id: str = None,
    ):
        self.code = code
        self.ens_net_districts = ens_net_districts
        self.request_id = request_id

    def validate(self):
        if self.ens_net_districts:
            self.ens_net_districts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_net_districts is not None:
            result['EnsNetDistricts'] = self.ens_net_districts.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsNetDistricts') is not None:
            temp_model = DescribeEnsNetSaleDistrictResponseBodyEnsNetDistricts()
            self.ens_net_districts = temp_model.from_map(m['EnsNetDistricts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnsNetSaleDistrictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsNetSaleDistrictResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsNetSaleDistrictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsRegionIdIpv6InfoRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        version: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEnsRegionIdIpv6InfoResponseBodySupportIpv6Info(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        support_ipv_6: bool = None,
    ):
        self.ens_region_id = ens_region_id
        self.support_ipv_6 = support_ipv_6

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.support_ipv_6 is not None:
            result['SupportIpv6'] = self.support_ipv_6
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('SupportIpv6') is not None:
            self.support_ipv_6 = m.get('SupportIpv6')
        return self


class DescribeEnsRegionIdIpv6InfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        support_ipv_6info: DescribeEnsRegionIdIpv6InfoResponseBodySupportIpv6Info = None,
    ):
        self.request_id = request_id
        self.support_ipv_6info = support_ipv_6info

    def validate(self):
        if self.support_ipv_6info:
            self.support_ipv_6info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_ipv_6info is not None:
            result['SupportIpv6Info'] = self.support_ipv_6info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportIpv6Info') is not None:
            temp_model = DescribeEnsRegionIdIpv6InfoResponseBodySupportIpv6Info()
            self.support_ipv_6info = temp_model.from_map(m['SupportIpv6Info'])
        return self


class DescribeEnsRegionIdIpv6InfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsRegionIdIpv6InfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsRegionIdIpv6InfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsRegionIdResourceRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        isp: str = None,
        order_by_params: str = None,
        page_number: int = None,
        page_size: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.isp = isp
        self.order_by_params = order_by_params
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResourcesEnsRegionIdResource(TeaModel):
    def __init__(
        self,
        area: str = None,
        area_code: str = None,
        biz_date: str = None,
        ens_region_id: str = None,
        ens_region_id_name: str = None,
        instance_count: int = None,
        internet_bandwidth: int = None,
        isp: str = None,
        vcpu: int = None,
    ):
        self.area = area
        self.area_code = area_code
        self.biz_date = biz_date
        self.ens_region_id = ens_region_id
        self.ens_region_id_name = ens_region_id_name
        self.instance_count = instance_count
        self.internet_bandwidth = internet_bandwidth
        self.isp = isp
        self.vcpu = vcpu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.area_code is not None:
            result['AreaCode'] = self.area_code
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.ens_region_id_name is not None:
            result['EnsRegionIdName'] = self.ens_region_id_name
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.internet_bandwidth is not None:
            result['InternetBandwidth'] = self.internet_bandwidth
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.vcpu is not None:
            result['VCpu'] = self.vcpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('EnsRegionIdName') is not None:
            self.ens_region_id_name = m.get('EnsRegionIdName')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InternetBandwidth') is not None:
            self.internet_bandwidth = m.get('InternetBandwidth')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('VCpu') is not None:
            self.vcpu = m.get('VCpu')
        return self


class DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResources(TeaModel):
    def __init__(
        self,
        ens_region_id_resource: List[DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResourcesEnsRegionIdResource] = None,
    ):
        self.ens_region_id_resource = ens_region_id_resource

    def validate(self):
        if self.ens_region_id_resource:
            for k in self.ens_region_id_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnsRegionIdResource'] = []
        if self.ens_region_id_resource is not None:
            for k in self.ens_region_id_resource:
                result['EnsRegionIdResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_region_id_resource = []
        if m.get('EnsRegionIdResource') is not None:
            for k in m.get('EnsRegionIdResource'):
                temp_model = DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResourcesEnsRegionIdResource()
                self.ens_region_id_resource.append(temp_model.from_map(k))
        return self


class DescribeEnsRegionIdResourceResponseBody(TeaModel):
    def __init__(
        self,
        ens_region_id_resources: DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResources = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.ens_region_id_resources = ens_region_id_resources
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ens_region_id_resources:
            self.ens_region_id_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id_resources is not None:
            result['EnsRegionIdResources'] = self.ens_region_id_resources.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionIdResources') is not None:
            temp_model = DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResources()
            self.ens_region_id_resources = temp_model.from_map(m['EnsRegionIdResources'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEnsRegionIdResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsRegionIdResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsRegionIdResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsRegionsRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        version: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEnsRegionsResponseBodyEnsRegionsEnsRegions(TeaModel):
    def __init__(
        self,
        area: str = None,
        en_name: str = None,
        ens_region_id: str = None,
        name: str = None,
        province: str = None,
    ):
        self.area = area
        self.en_name = en_name
        self.ens_region_id = ens_region_id
        self.name = name
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class DescribeEnsRegionsResponseBodyEnsRegions(TeaModel):
    def __init__(
        self,
        ens_regions: List[DescribeEnsRegionsResponseBodyEnsRegionsEnsRegions] = None,
    ):
        self.ens_regions = ens_regions

    def validate(self):
        if self.ens_regions:
            for k in self.ens_regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnsRegions'] = []
        if self.ens_regions is not None:
            for k in self.ens_regions:
                result['EnsRegions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_regions = []
        if m.get('EnsRegions') is not None:
            for k in m.get('EnsRegions'):
                temp_model = DescribeEnsRegionsResponseBodyEnsRegionsEnsRegions()
                self.ens_regions.append(temp_model.from_map(k))
        return self


class DescribeEnsRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ens_regions: DescribeEnsRegionsResponseBodyEnsRegions = None,
        request_id: str = None,
    ):
        self.code = code
        self.ens_regions = ens_regions
        self.request_id = request_id

    def validate(self):
        if self.ens_regions:
            self.ens_regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_regions is not None:
            result['EnsRegions'] = self.ens_regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsRegions') is not None:
            temp_model = DescribeEnsRegionsResponseBodyEnsRegions()
            self.ens_regions = temp_model.from_map(m['EnsRegions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnsRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsResourceUsageRequest(TeaModel):
    def __init__(
        self,
        expired_end_time: str = None,
        expired_start_time: str = None,
    ):
        # vm实例使用结束时间查询结束范围，，格式： yyyy-MM-dd或yyyy-MM-dd HH:mm:ss
        self.expired_end_time = expired_end_time
        # vm实例使用结束时间查询开始范围，格式： yyyy-MM-dd或yyyy-MM-dd HH:mm:ss
        self.expired_start_time = expired_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_end_time is not None:
            result['ExpiredEndTime'] = self.expired_end_time
        if self.expired_start_time is not None:
            result['ExpiredStartTime'] = self.expired_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredEndTime') is not None:
            self.expired_end_time = m.get('ExpiredEndTime')
        if m.get('ExpiredStartTime') is not None:
            self.expired_start_time = m.get('ExpiredStartTime')
        return self


class DescribeEnsResourceUsageResponseBodyEnsResourceUsage(TeaModel):
    def __init__(
        self,
        compute_resource_count: int = None,
        cpu_sum: int = None,
        disk_count: int = None,
        down_count: int = None,
        expired_count: int = None,
        expiring_count: int = None,
        gpu_sum: int = None,
        instance_count: int = None,
        running_count: int = None,
        service_type: str = None,
        storage_sum: int = None,
    ):
        self.compute_resource_count = compute_resource_count
        self.cpu_sum = cpu_sum
        self.disk_count = disk_count
        self.down_count = down_count
        self.expired_count = expired_count
        self.expiring_count = expiring_count
        self.gpu_sum = gpu_sum
        self.instance_count = instance_count
        self.running_count = running_count
        self.service_type = service_type
        self.storage_sum = storage_sum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource_count is not None:
            result['ComputeResourceCount'] = self.compute_resource_count
        if self.cpu_sum is not None:
            result['CpuSum'] = self.cpu_sum
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.down_count is not None:
            result['DownCount'] = self.down_count
        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count
        if self.expiring_count is not None:
            result['ExpiringCount'] = self.expiring_count
        if self.gpu_sum is not None:
            result['GpuSum'] = self.gpu_sum
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.running_count is not None:
            result['RunningCount'] = self.running_count
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.storage_sum is not None:
            result['StorageSum'] = self.storage_sum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResourceCount') is not None:
            self.compute_resource_count = m.get('ComputeResourceCount')
        if m.get('CpuSum') is not None:
            self.cpu_sum = m.get('CpuSum')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DownCount') is not None:
            self.down_count = m.get('DownCount')
        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')
        if m.get('ExpiringCount') is not None:
            self.expiring_count = m.get('ExpiringCount')
        if m.get('GpuSum') is not None:
            self.gpu_sum = m.get('GpuSum')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('RunningCount') is not None:
            self.running_count = m.get('RunningCount')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('StorageSum') is not None:
            self.storage_sum = m.get('StorageSum')
        return self


class DescribeEnsResourceUsageResponseBody(TeaModel):
    def __init__(
        self,
        ens_resource_usage: List[DescribeEnsResourceUsageResponseBodyEnsResourceUsage] = None,
        request_id: str = None,
    ):
        self.ens_resource_usage = ens_resource_usage
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.ens_resource_usage:
            for k in self.ens_resource_usage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnsResourceUsage'] = []
        if self.ens_resource_usage is not None:
            for k in self.ens_resource_usage:
                result['EnsResourceUsage'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_resource_usage = []
        if m.get('EnsResourceUsage') is not None:
            for k in m.get('EnsResourceUsage'):
                temp_model = DescribeEnsResourceUsageResponseBodyEnsResourceUsage()
                self.ens_resource_usage.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEnsResourceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsResourceUsageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsResourceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnsRouteEntryListRequest(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        page_number: int = None,
        page_size: int = None,
        route_entry_id: str = None,
        route_entry_name: str = None,
        route_entry_type: str = None,
        route_table_id: str = None,
    ):
        # 路由条目的目标网段
        self.destination_cidr_block = destination_cidr_block
        # 下一跳实例ID。
        self.next_hop_id = next_hop_id
        # 下一跳类型
        self.next_hop_type = next_hop_type
        # 列表的页码，默认值为1。
        self.page_number = page_number
        # 分页查询时每页的行数，最大值为100，默认值为10。
        self.page_size = page_size
        # 要查询的路由条目的ID。
        self.route_entry_id = route_entry_id
        # 路由条目的名称。
        self.route_entry_name = route_entry_name
        # 路由条目的类型
        self.route_entry_type = route_entry_type
        # 要查询的路由表的ID。
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id
        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name
        if self.route_entry_type is not None:
            result['RouteEntryType'] = self.route_entry_type
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')
        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')
        if m.get('RouteEntryType') is not None:
            self.route_entry_type = m.get('RouteEntryType')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeEnsRouteEntryListResponseBodyRouteEntrysNextHops(TeaModel):
    def __init__(
        self,
        next_hop_id: str = None,
        next_hop_type: str = None,
    ):
        # 下一跳实例ID。
        self.next_hop_id = next_hop_id
        # 下一跳类型
        self.next_hop_type = next_hop_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        return self


class DescribeEnsRouteEntryListResponseBodyRouteEntrys(TeaModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_block: str = None,
        next_hops: List[DescribeEnsRouteEntryListResponseBodyRouteEntrysNextHops] = None,
        route_entry_id: str = None,
        route_entry_name: str = None,
        route_table_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # 路由条目的描述信息。
        self.description = description
        # 路由条目的目标网段。
        self.destination_cidr_block = destination_cidr_block
        # 下一跳
        self.next_hops = next_hops
        # 路由条目的ID。
        self.route_entry_id = route_entry_id
        # 路由条目的名称。
        self.route_entry_name = route_entry_name
        # 路由表ID。
        self.route_table_id = route_table_id
        # 路由条目的状态
        self.status = status
        # 路由条目的类型
        self.type = type

    def validate(self):
        if self.next_hops:
            for k in self.next_hops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        result['NextHops'] = []
        if self.next_hops is not None:
            for k in self.next_hops:
                result['NextHops'].append(k.to_map() if k else None)
        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id
        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        self.next_hops = []
        if m.get('NextHops') is not None:
            for k in m.get('NextHops'):
                temp_model = DescribeEnsRouteEntryListResponseBodyRouteEntrysNextHops()
                self.next_hops.append(temp_model.from_map(k))
        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')
        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeEnsRouteEntryListResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        route_entrys: List[DescribeEnsRouteEntryListResponseBodyRouteEntrys] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # 路由条目信息。
        self.route_entrys = route_entrys
        self.total_count = total_count

    def validate(self):
        if self.route_entrys:
            for k in self.route_entrys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RouteEntrys'] = []
        if self.route_entrys is not None:
            for k in self.route_entrys:
                result['RouteEntrys'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.route_entrys = []
        if m.get('RouteEntrys') is not None:
            for k in m.get('RouteEntrys'):
                temp_model = DescribeEnsRouteEntryListResponseBodyRouteEntrys()
                self.route_entrys.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEnsRouteEntryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnsRouteEntryListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEnsRouteEntryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnBandWidthDataRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        end_time: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        isp: str = None,
        networking_model: str = None,
        period: str = None,
        start_time: str = None,
        version: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.end_time = end_time
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.isp = isp
        self.networking_model = networking_model
        self.period = period
        self.start_time = start_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.period is not None:
            result['Period'] = self.period
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEpnBandWidthDataResponseBodyMonitorDataBandWidthMonitorData(TeaModel):
    def __init__(
        self,
        down_band_width: int = None,
        internet_rx: int = None,
        internet_tx: int = None,
        time_stamp: str = None,
        up_band_width: int = None,
    ):
        self.down_band_width = down_band_width
        self.internet_rx = internet_rx
        self.internet_tx = internet_tx
        self.time_stamp = time_stamp
        self.up_band_width = up_band_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_band_width is not None:
            result['DownBandWidth'] = self.down_band_width
        if self.internet_rx is not None:
            result['InternetRX'] = self.internet_rx
        if self.internet_tx is not None:
            result['InternetTX'] = self.internet_tx
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.up_band_width is not None:
            result['UpBandWidth'] = self.up_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownBandWidth') is not None:
            self.down_band_width = m.get('DownBandWidth')
        if m.get('InternetRX') is not None:
            self.internet_rx = m.get('InternetRX')
        if m.get('InternetTX') is not None:
            self.internet_tx = m.get('InternetTX')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UpBandWidth') is not None:
            self.up_band_width = m.get('UpBandWidth')
        return self


class DescribeEpnBandWidthDataResponseBodyMonitorData(TeaModel):
    def __init__(
        self,
        band_width_monitor_data: List[DescribeEpnBandWidthDataResponseBodyMonitorDataBandWidthMonitorData] = None,
        max_down_band_width: int = None,
        max_up_band_width: int = None,
    ):
        self.band_width_monitor_data = band_width_monitor_data
        self.max_down_band_width = max_down_band_width
        self.max_up_band_width = max_up_band_width

    def validate(self):
        if self.band_width_monitor_data:
            for k in self.band_width_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BandWidthMonitorData'] = []
        if self.band_width_monitor_data is not None:
            for k in self.band_width_monitor_data:
                result['BandWidthMonitorData'].append(k.to_map() if k else None)
        if self.max_down_band_width is not None:
            result['MaxDownBandWidth'] = self.max_down_band_width
        if self.max_up_band_width is not None:
            result['MaxUpBandWidth'] = self.max_up_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_monitor_data = []
        if m.get('BandWidthMonitorData') is not None:
            for k in m.get('BandWidthMonitorData'):
                temp_model = DescribeEpnBandWidthDataResponseBodyMonitorDataBandWidthMonitorData()
                self.band_width_monitor_data.append(temp_model.from_map(k))
        if m.get('MaxDownBandWidth') is not None:
            self.max_down_band_width = m.get('MaxDownBandWidth')
        if m.get('MaxUpBandWidth') is not None:
            self.max_up_band_width = m.get('MaxUpBandWidth')
        return self


class DescribeEpnBandWidthDataResponseBody(TeaModel):
    def __init__(
        self,
        monitor_data: DescribeEpnBandWidthDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        self.monitor_data = monitor_data
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorData') is not None:
            temp_model = DescribeEpnBandWidthDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m['MonitorData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEpnBandWidthDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnBandWidthDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnBandWidthDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnBandwitdhByInternetChargeTypeRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        ens_region_id: str = None,
        isp: str = None,
        networking_model: str = None,
        start_time: str = None,
        version: str = None,
    ):
        self.end_time = end_time
        self.ens_region_id = ens_region_id
        self.isp = isp
        self.networking_model = networking_model
        self.start_time = start_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEpnBandwitdhByInternetChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_value: int = None,
        internet_charge_type: str = None,
        request_id: str = None,
        time_stamp: str = None,
    ):
        self.bandwidth_value = bandwidth_value
        self.internet_charge_type = internet_charge_type
        self.request_id = request_id
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_value is not None:
            result['BandwidthValue'] = self.bandwidth_value
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthValue') is not None:
            self.bandwidth_value = m.get('BandwidthValue')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeEpnBandwitdhByInternetChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnBandwitdhByInternetChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnBandwitdhByInternetChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
    ):
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        return self


class DescribeEpnInstanceAttributeResponseBodyConfVersions(TeaModel):
    def __init__(
        self,
        conf_version: str = None,
        ens_region_id: str = None,
    ):
        self.conf_version = conf_version
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conf_version is not None:
            result['ConfVersion'] = self.conf_version
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfVersion') is not None:
            self.conf_version = m.get('ConfVersion')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        return self


class DescribeEpnInstanceAttributeResponseBodyInstances(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        isp: str = None,
        private_ip_address: str = None,
        public_ip_address: str = None,
        status: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.isp = isp
        self.private_ip_address = private_ip_address
        self.public_ip_address = public_ip_address
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEpnInstanceAttributeResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        ens_region_id: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.ens_region_id = ens_region_id
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeEpnInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        conf_versions: List[DescribeEpnInstanceAttributeResponseBodyConfVersions] = None,
        epninstance_id: str = None,
        epninstance_name: str = None,
        instances: List[DescribeEpnInstanceAttributeResponseBodyInstances] = None,
        networking_model: str = None,
        request_id: str = None,
        v_switches: List[DescribeEpnInstanceAttributeResponseBodyVSwitches] = None,
    ):
        self.conf_versions = conf_versions
        self.epninstance_id = epninstance_id
        self.epninstance_name = epninstance_name
        self.instances = instances
        self.networking_model = networking_model
        self.request_id = request_id
        self.v_switches = v_switches

    def validate(self):
        if self.conf_versions:
            for k in self.conf_versions:
                if k:
                    k.validate()
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfVersions'] = []
        if self.conf_versions is not None:
            for k in self.conf_versions:
                result['ConfVersions'].append(k.to_map() if k else None)
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conf_versions = []
        if m.get('ConfVersions') is not None:
            for k in m.get('ConfVersions'):
                temp_model = DescribeEpnInstanceAttributeResponseBodyConfVersions()
                self.conf_versions.append(temp_model.from_map(k))
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeEpnInstanceAttributeResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = DescribeEpnInstanceAttributeResponseBodyVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        return self


class DescribeEpnInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnInstancesRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        epninstance_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.epninstance_id = epninstance_id
        self.epninstance_name = epninstance_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeEpnInstancesResponseBodyEPNInstancesEPNInstance(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        epninstance_id: str = None,
        epninstance_name: str = None,
        epninstance_type: str = None,
        end_time: str = None,
        internet_max_bandwidth_out: int = None,
        modify_time: str = None,
        networking_model: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.creation_time = creation_time
        self.epninstance_id = epninstance_id
        self.epninstance_name = epninstance_name
        self.epninstance_type = epninstance_type
        self.end_time = end_time
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.modify_time = modify_time
        self.networking_model = networking_model
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        if self.epninstance_type is not None:
            result['EPNInstanceType'] = self.epninstance_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        if m.get('EPNInstanceType') is not None:
            self.epninstance_type = m.get('EPNInstanceType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEpnInstancesResponseBodyEPNInstances(TeaModel):
    def __init__(
        self,
        epninstance: List[DescribeEpnInstancesResponseBodyEPNInstancesEPNInstance] = None,
    ):
        self.epninstance = epninstance

    def validate(self):
        if self.epninstance:
            for k in self.epninstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EPNInstance'] = []
        if self.epninstance is not None:
            for k in self.epninstance:
                result['EPNInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.epninstance = []
        if m.get('EPNInstance') is not None:
            for k in m.get('EPNInstance'):
                temp_model = DescribeEpnInstancesResponseBodyEPNInstancesEPNInstance()
                self.epninstance.append(temp_model.from_map(k))
        return self


class DescribeEpnInstancesResponseBody(TeaModel):
    def __init__(
        self,
        epninstances: DescribeEpnInstancesResponseBodyEPNInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.epninstances = epninstances
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.epninstances:
            self.epninstances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstances is not None:
            result['EPNInstances'] = self.epninstances.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstances') is not None:
            temp_model = DescribeEpnInstancesResponseBodyEPNInstances()
            self.epninstances = temp_model.from_map(m['EPNInstances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEpnInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEpnMeasurementDataRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        start_date: str = None,
        version: str = None,
    ):
        self.end_date = end_date
        self.start_date = start_date
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData(TeaModel):
    def __init__(
        self,
        cost_code: str = None,
        cost_name: str = None,
        cost_type: str = None,
        cost_val: int = None,
        isp_line: str = None,
    ):
        self.cost_code = cost_code
        self.cost_name = cost_name
        self.cost_type = cost_type
        self.cost_val = cost_val
        self.isp_line = isp_line

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_code is not None:
            result['CostCode'] = self.cost_code
        if self.cost_name is not None:
            result['CostName'] = self.cost_name
        if self.cost_type is not None:
            result['CostType'] = self.cost_type
        if self.cost_val is not None:
            result['CostVal'] = self.cost_val
        if self.isp_line is not None:
            result['IspLine'] = self.isp_line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCode') is not None:
            self.cost_code = m.get('CostCode')
        if m.get('CostName') is not None:
            self.cost_name = m.get('CostName')
        if m.get('CostType') is not None:
            self.cost_type = m.get('CostType')
        if m.get('CostVal') is not None:
            self.cost_val = m.get('CostVal')
        if m.get('IspLine') is not None:
            self.isp_line = m.get('IspLine')
        return self


class DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas(TeaModel):
    def __init__(
        self,
        band_width_fee_data: List[DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData] = None,
    ):
        self.band_width_fee_data = band_width_fee_data

    def validate(self):
        if self.band_width_fee_data:
            for k in self.band_width_fee_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BandWidthFeeData'] = []
        if self.band_width_fee_data is not None:
            for k in self.band_width_fee_data:
                result['BandWidthFeeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_fee_data = []
        if m.get('BandWidthFeeData') is not None:
            for k in m.get('BandWidthFeeData'):
                temp_model = DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData()
                self.band_width_fee_data.append(temp_model.from_map(k))
        return self


class DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementData(TeaModel):
    def __init__(
        self,
        band_width_fee_datas: DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas = None,
        charge_model: str = None,
        cost_cycle: str = None,
        cost_end_time: str = None,
        cost_start_time: str = None,
    ):
        self.band_width_fee_datas = band_width_fee_datas
        self.charge_model = charge_model
        self.cost_cycle = cost_cycle
        self.cost_end_time = cost_end_time
        self.cost_start_time = cost_start_time

    def validate(self):
        if self.band_width_fee_datas:
            self.band_width_fee_datas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width_fee_datas is not None:
            result['BandWidthFeeDatas'] = self.band_width_fee_datas.to_map()
        if self.charge_model is not None:
            result['ChargeModel'] = self.charge_model
        if self.cost_cycle is not None:
            result['CostCycle'] = self.cost_cycle
        if self.cost_end_time is not None:
            result['CostEndTime'] = self.cost_end_time
        if self.cost_start_time is not None:
            result['CostStartTime'] = self.cost_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidthFeeDatas') is not None:
            temp_model = DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas()
            self.band_width_fee_datas = temp_model.from_map(m['BandWidthFeeDatas'])
        if m.get('ChargeModel') is not None:
            self.charge_model = m.get('ChargeModel')
        if m.get('CostCycle') is not None:
            self.cost_cycle = m.get('CostCycle')
        if m.get('CostEndTime') is not None:
            self.cost_end_time = m.get('CostEndTime')
        if m.get('CostStartTime') is not None:
            self.cost_start_time = m.get('CostStartTime')
        return self


class DescribeEpnMeasurementDataResponseBodyMeasurementDatas(TeaModel):
    def __init__(
        self,
        measurement_data: List[DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementData] = None,
    ):
        self.measurement_data = measurement_data

    def validate(self):
        if self.measurement_data:
            for k in self.measurement_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MeasurementData'] = []
        if self.measurement_data is not None:
            for k in self.measurement_data:
                result['MeasurementData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.measurement_data = []
        if m.get('MeasurementData') is not None:
            for k in m.get('MeasurementData'):
                temp_model = DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementData()
                self.measurement_data.append(temp_model.from_map(k))
        return self


class DescribeEpnMeasurementDataResponseBody(TeaModel):
    def __init__(
        self,
        measurement_datas: DescribeEpnMeasurementDataResponseBodyMeasurementDatas = None,
        request_id: str = None,
    ):
        self.measurement_datas = measurement_datas
        self.request_id = request_id

    def validate(self):
        if self.measurement_datas:
            self.measurement_datas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.measurement_datas is not None:
            result['MeasurementDatas'] = self.measurement_datas.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeasurementDatas') is not None:
            temp_model = DescribeEpnMeasurementDataResponseBodyMeasurementDatas()
            self.measurement_datas = temp_model.from_map(m['MeasurementDatas'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEpnMeasurementDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEpnMeasurementDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEpnMeasurementDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExportImageInfoRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.image_id = image_id
        self.image_name = image_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeExportImageInfoResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        creation_time: str = None,
        exported_image_url: str = None,
        image_export_status: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        platform: str = None,
    ):
        self.architecture = architecture
        self.creation_time = creation_time
        self.exported_image_url = exported_image_url
        self.image_export_status = image_export_status
        self.image_id = image_id
        self.image_name = image_name
        self.image_owner_alias = image_owner_alias
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.exported_image_url is not None:
            result['ExportedImageURL'] = self.exported_image_url
        if self.image_export_status is not None:
            result['ImageExportStatus'] = self.image_export_status
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ExportedImageURL') is not None:
            self.exported_image_url = m.get('ExportedImageURL')
        if m.get('ImageExportStatus') is not None:
            self.image_export_status = m.get('ImageExportStatus')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class DescribeExportImageInfoResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeExportImageInfoResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeExportImageInfoResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeExportImageInfoResponseBody(TeaModel):
    def __init__(
        self,
        images: DescribeExportImageInfoResponseBodyImages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.images = images
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            temp_model = DescribeExportImageInfoResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExportImageInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExportImageInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExportImageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExportImageStatusRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        version: str = None,
    ):
        self.image_id = image_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeExportImageStatusResponseBody(TeaModel):
    def __init__(
        self,
        image_export_status: str = None,
        request_id: str = None,
    ):
        self.image_export_status = image_export_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_export_status is not None:
            result['ImageExportStatus'] = self.image_export_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageExportStatus') is not None:
            self.image_export_status = m.get('ImageExportStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeExportImageStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExportImageStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeExportImageStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeForwardTableEntriesRequest(TeaModel):
    def __init__(
        self,
        external_ip: str = None,
        forward_entry_id: str = None,
        forward_entry_name: str = None,
        internal_ip: str = None,
        ip_protocol: str = None,
        nat_gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.external_ip = external_ip
        self.forward_entry_id = forward_entry_id
        self.forward_entry_name = forward_entry_name
        self.internal_ip = internal_ip
        self.ip_protocol = ip_protocol
        self.nat_gateway_id = nat_gateway_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id
        if self.forward_entry_name is not None:
            result['ForwardEntryName'] = self.forward_entry_name
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')
        if m.get('ForwardEntryName') is not None:
            self.forward_entry_name = m.get('ForwardEntryName')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeForwardTableEntriesResponseBodyForwardTableEntries(TeaModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_id: str = None,
        forward_entry_name: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        nat_gateway_id: str = None,
        status: str = None,
    ):
        self.external_ip = external_ip
        self.external_port = external_port
        self.forward_entry_id = forward_entry_id
        self.forward_entry_name = forward_entry_name
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.nat_gateway_id = nat_gateway_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id
        if self.forward_entry_name is not None:
            result['ForwardEntryName'] = self.forward_entry_name
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')
        if m.get('ForwardEntryName') is not None:
            self.forward_entry_name = m.get('ForwardEntryName')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeForwardTableEntriesResponseBody(TeaModel):
    def __init__(
        self,
        forward_table_entries: List[DescribeForwardTableEntriesResponseBodyForwardTableEntries] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.forward_table_entries = forward_table_entries
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.forward_table_entries:
            for k in self.forward_table_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardTableEntries'] = []
        if self.forward_table_entries is not None:
            for k in self.forward_table_entries:
                result['ForwardTableEntries'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forward_table_entries = []
        if m.get('ForwardTableEntries') is not None:
            for k in m.get('ForwardTableEntries'):
                temp_model = DescribeForwardTableEntriesResponseBodyForwardTableEntries()
                self.forward_table_entries.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeForwardTableEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeForwardTableEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeForwardTableEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageInfosRequest(TeaModel):
    def __init__(
        self,
        os_type: str = None,
        version: str = None,
    ):
        self.os_type = os_type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeImageInfosResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        description: str = None,
        image_id: str = None,
        image_size: str = None,
        image_version: str = None,
        osname: str = None,
        ostype: str = None,
    ):
        self.description = description
        self.image_id = image_id
        self.image_size = image_size
        self.image_version = image_version
        self.osname = osname
        self.ostype = ostype

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.osname is not None:
            result['OSName'] = self.osname
        if self.ostype is not None:
            result['OSType'] = self.ostype
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('OSName') is not None:
            self.osname = m.get('OSName')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        return self


class DescribeImageInfosResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeImageInfosResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeImageInfosResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeImageInfosResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        images: DescribeImageInfosResponseBodyImages = None,
        request_id: str = None,
    ):
        self.code = code
        self.images = images
        self.request_id = request_id

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Images') is not None:
            temp_model = DescribeImageInfosResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImageInfosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImageInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageSharePermissionRequest(TeaModel):
    def __init__(
        self,
        aliyun_id: int = None,
        image_id: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        self.aliyun_id = aliyun_id
        self.image_id = image_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeImageSharePermissionResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        account: List[str] = None,
    ):
        self.account = account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        return self


class DescribeImageSharePermissionResponseBody(TeaModel):
    def __init__(
        self,
        accounts: DescribeImageSharePermissionResponseBodyAccounts = None,
        image_id: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.accounts = accounts
        self.image_id = image_id
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = DescribeImageSharePermissionResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageSharePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImageSharePermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImageSharePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        image_id: str = None,
        image_name: str = None,
        page_number: str = None,
        page_size: str = None,
        status: str = None,
        version: str = None,
        product: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.image_id = image_id
        self.image_name = image_name
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.version = version
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class DescribeImagesResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        creation_time: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        image_size: str = None,
        platform: str = None,
    ):
        self.architecture = architecture
        self.creation_time = creation_time
        self.image_id = image_id
        self.image_name = image_name
        self.image_owner_alias = image_owner_alias
        self.image_size = image_size
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class DescribeImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeImagesResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeImagesResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeImagesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        images: DescribeImagesResponseBodyImages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.images = images
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Images') is not None:
            temp_model = DescribeImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        owner_id: int = None,
        version: str = None,
    ):
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributesInstanceRenewAttribute(TeaModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        duration: str = None,
        instance_id: str = None,
    ):
        self.auto_renewal = auto_renewal
        self.duration = duration
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes(TeaModel):
    def __init__(
        self,
        instance_renew_attribute: List[DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributesInstanceRenewAttribute] = None,
    ):
        self.instance_renew_attribute = instance_renew_attribute

    def validate(self):
        if self.instance_renew_attribute:
            for k in self.instance_renew_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceRenewAttribute'] = []
        if self.instance_renew_attribute is not None:
            for k in self.instance_renew_attribute:
                result['InstanceRenewAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_renew_attribute = []
        if m.get('InstanceRenewAttribute') is not None:
            for k in m.get('InstanceRenewAttribute'):
                temp_model = DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributesInstanceRenewAttribute()
                self.instance_renew_attribute.append(temp_model.from_map(k))
        return self


class DescribeInstanceAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        instance_renew_attributes: DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_renew_attributes = instance_renew_attributes
        self.request_id = request_id

    def validate(self):
        if self.instance_renew_attributes:
            self.instance_renew_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_renew_attributes is not None:
            result['InstanceRenewAttributes'] = self.instance_renew_attributes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceRenewAttributes') is not None:
            temp_model = DescribeInstanceAutoRenewAttributeResponseBodyInstanceRenewAttributes()
            self.instance_renew_attributes = temp_model.from_map(m['InstanceRenewAttributes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceAutoRenewAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceMonitorDataRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        period: str = None,
        start_time: str = None,
        version: str = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.period = period
        self.start_time = start_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period is not None:
            result['Period'] = self.period
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        instance_id: str = None,
        memory: str = None,
    ):
        self.cpu = cpu
        self.instance_id = instance_id
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class DescribeInstanceMonitorDataResponseBodyMonitorData(TeaModel):
    def __init__(
        self,
        instance_monitor_data: List[DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData] = None,
    ):
        self.instance_monitor_data = instance_monitor_data

    def validate(self):
        if self.instance_monitor_data:
            for k in self.instance_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceMonitorData'] = []
        if self.instance_monitor_data is not None:
            for k in self.instance_monitor_data:
                result['InstanceMonitorData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_monitor_data = []
        if m.get('InstanceMonitorData') is not None:
            for k in m.get('InstanceMonitorData'):
                temp_model = DescribeInstanceMonitorDataResponseBodyMonitorDataInstanceMonitorData()
                self.instance_monitor_data.append(temp_model.from_map(k))
        return self


class DescribeInstanceMonitorDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        monitor_data: DescribeInstanceMonitorDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        self.code = code
        self.monitor_data = monitor_data
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MonitorData') is not None:
            temp_model = DescribeInstanceMonitorDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m['MonitorData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceMonitorDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceMonitorDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceSpecResponseBodyInstanceSpecsInstanceSpec(TeaModel):
    def __init__(
        self,
        core: str = None,
        display_name: str = None,
        instance_type: str = None,
        memory: str = None,
    ):
        self.core = core
        self.display_name = display_name
        self.instance_type = instance_type
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core is not None:
            result['Core'] = self.core
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class DescribeInstanceSpecResponseBodyInstanceSpecs(TeaModel):
    def __init__(
        self,
        instance_spec: List[DescribeInstanceSpecResponseBodyInstanceSpecsInstanceSpec] = None,
    ):
        self.instance_spec = instance_spec

    def validate(self):
        if self.instance_spec:
            for k in self.instance_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceSpec'] = []
        if self.instance_spec is not None:
            for k in self.instance_spec:
                result['InstanceSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_spec = []
        if m.get('InstanceSpec') is not None:
            for k in m.get('InstanceSpec'):
                temp_model = DescribeInstanceSpecResponseBodyInstanceSpecsInstanceSpec()
                self.instance_spec.append(temp_model.from_map(k))
        return self


class DescribeInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_limit: int = None,
        code: int = None,
        data_disk_max_size: int = None,
        data_disk_min_size: int = None,
        instance_specs: DescribeInstanceSpecResponseBodyInstanceSpecs = None,
        request_id: str = None,
        system_disk_max_size: int = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        self.code = code
        self.data_disk_max_size = data_disk_max_size
        self.data_disk_min_size = data_disk_min_size
        self.instance_specs = instance_specs
        self.request_id = request_id
        self.system_disk_max_size = system_disk_max_size

    def validate(self):
        if self.instance_specs:
            self.instance_specs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit
        if self.code is not None:
            result['Code'] = self.code
        if self.data_disk_max_size is not None:
            result['DataDiskMaxSize'] = self.data_disk_max_size
        if self.data_disk_min_size is not None:
            result['DataDiskMinSize'] = self.data_disk_min_size
        if self.instance_specs is not None:
            result['InstanceSpecs'] = self.instance_specs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_disk_max_size is not None:
            result['SystemDiskMaxSize'] = self.system_disk_max_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DataDiskMaxSize') is not None:
            self.data_disk_max_size = m.get('DataDiskMaxSize')
        if m.get('DataDiskMinSize') is not None:
            self.data_disk_min_size = m.get('DataDiskMinSize')
        if m.get('InstanceSpecs') is not None:
            temp_model = DescribeInstanceSpecResponseBodyInstanceSpecs()
            self.instance_specs = temp_model.from_map(m['InstanceSpecs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemDiskMaxSize') is not None:
            self.system_disk_max_size = m.get('SystemDiskMaxSize')
        return self


class DescribeInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTypesRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceTypesResponseBodyInstanceTypesInstanceType(TeaModel):
    def __init__(
        self,
        cpu_core_count: int = None,
        instance_type_id: str = None,
        instance_type_name: str = None,
        memory_size: int = None,
    ):
        self.cpu_core_count = cpu_core_count
        self.instance_type_id = instance_type_id
        self.instance_type_name = instance_type_name
        self.memory_size = memory_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        if self.instance_type_name is not None:
            result['InstanceTypeName'] = self.instance_type_name
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        if m.get('InstanceTypeName') is not None:
            self.instance_type_name = m.get('InstanceTypeName')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        return self


class DescribeInstanceTypesResponseBodyInstanceTypes(TeaModel):
    def __init__(
        self,
        instance_type: List[DescribeInstanceTypesResponseBodyInstanceTypesInstanceType] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type:
            for k in self.instance_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k in self.instance_type:
                result['InstanceType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k in m.get('InstanceType'):
                temp_model = DescribeInstanceTypesResponseBodyInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k))
        return self


class DescribeInstanceTypesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        instance_types: DescribeInstanceTypesResponseBodyInstanceTypes = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_types = instance_types
        self.request_id = request_id

    def validate(self):
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceTypes') is not None:
            temp_model = DescribeInstanceTypesResponseBodyInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceVncUrlRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # 实例ID。
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceVncUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vnc_url: str = None,
    ):
        # 请求ID。
        self.request_id = request_id
        # 管理终端Url。
        self.vnc_url = vnc_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vnc_url is not None:
            result['VncUrl'] = self.vnc_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VncUrl') is not None:
            self.vnc_url = m.get('VncUrl')
        return self


class DescribeInstanceVncUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceVncUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceVncUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        ens_region_ids: str = None,
        ens_service_id: str = None,
        image_id: str = None,
        instance_id: str = None,
        instance_ids: str = None,
        instance_name: str = None,
        instance_resource_type: str = None,
        network_id: str = None,
        order_by_params: str = None,
        page_number: int = None,
        page_size: str = None,
        search_key: str = None,
        security_group_id: str = None,
        status: str = None,
        v_switch_id: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.ens_region_ids = ens_region_ids
        self.ens_service_id = ens_service_id
        self.image_id = image_id
        self.instance_id = instance_id
        self.instance_ids = instance_ids
        self.instance_name = instance_name
        self.instance_resource_type = instance_resource_type
        self.network_id = network_id
        self.order_by_params = order_by_params
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.security_group_id = security_group_id
        self.status = status
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids
        if self.ens_service_id is not None:
            result['EnsServiceId'] = self.ens_service_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_resource_type is not None:
            result['InstanceResourceType'] = self.instance_resource_type
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')
        if m.get('EnsServiceId') is not None:
            self.ens_service_id = m.get('EnsServiceId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceResourceType') is not None:
            self.instance_resource_type = m.get('InstanceResourceType')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeInstancesResponseBodyInstancesInstanceDataDiskDataDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        disk_id: str = None,
        disk_name: str = None,
        size: int = None,
        device_type: str = None,
        disk_type: str = None,
        name: str = None,
        storage: int = None,
        uuid: str = None,
    ):
        self.category = category
        self.disk_id = disk_id
        self.disk_name = disk_name
        self.size = size
        self.device_type = device_type
        self.disk_type = disk_type
        self.name = name
        self.storage = storage
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.size is not None:
            result['Size'] = self.size
        if self.device_type is not None:
            result['device_type'] = self.device_type
        if self.disk_type is not None:
            result['disk_type'] = self.disk_type
        if self.name is not None:
            result['name'] = self.name
        if self.storage is not None:
            result['storage'] = self.storage
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('device_type') is not None:
            self.device_type = m.get('device_type')
        if m.get('disk_type') is not None:
            self.disk_type = m.get('disk_type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class DescribeInstancesResponseBodyInstancesInstanceDataDisk(TeaModel):
    def __init__(
        self,
        data_disk: List[DescribeInstancesResponseBodyInstancesInstanceDataDiskDataDisk] = None,
    ):
        self.data_disk = data_disk

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribeInstancesResponseBodyInstancesInstanceDataDiskDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesInstanceInnerIpAddress(TeaModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        return self


class DescribeInstancesResponseBodyInstancesInstanceNetworkAttributesPrivateIpAddress(TeaModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        return self


class DescribeInstancesResponseBodyInstancesInstanceNetworkAttributes(TeaModel):
    def __init__(
        self,
        network_id: str = None,
        private_ip_address: DescribeInstancesResponseBodyInstancesInstanceNetworkAttributesPrivateIpAddress = None,
        v_switch_id: str = None,
    ):
        self.network_id = network_id
        self.private_ip_address = private_ip_address
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.private_ip_address:
            self.private_ip_address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('PrivateIpAddress') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstanceNetworkAttributesPrivateIpAddress()
            self.private_ip_address = temp_model.from_map(m['PrivateIpAddress'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeInstancesResponseBodyInstancesInstancePrivateIpAddressesPrivateIpAddress(TeaModel):
    def __init__(
        self,
        gate_way: str = None,
        ip: str = None,
        isp: str = None,
    ):
        self.gate_way = gate_way
        self.ip = ip
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gate_way is not None:
            result['GateWay'] = self.gate_way
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GateWay') is not None:
            self.gate_way = m.get('GateWay')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeInstancesResponseBodyInstancesInstancePrivateIpAddresses(TeaModel):
    def __init__(
        self,
        private_ip_address: List[DescribeInstancesResponseBodyInstancesInstancePrivateIpAddressesPrivateIpAddress] = None,
    ):
        self.private_ip_address = private_ip_address

    def validate(self):
        if self.private_ip_address:
            for k in self.private_ip_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrivateIpAddress'] = []
        if self.private_ip_address is not None:
            for k in self.private_ip_address:
                result['PrivateIpAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_ip_address = []
        if m.get('PrivateIpAddress') is not None:
            for k in m.get('PrivateIpAddress'):
                temp_model = DescribeInstancesResponseBodyInstancesInstancePrivateIpAddressesPrivateIpAddress()
                self.private_ip_address.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesInstancePublicIpAddress(TeaModel):
    def __init__(
        self,
        ip_address: List[str] = None,
    ):
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        return self


class DescribeInstancesResponseBodyInstancesInstancePublicIpAddressesPublicIpAddress(TeaModel):
    def __init__(
        self,
        gate_way: str = None,
        ip: str = None,
        isp: str = None,
    ):
        self.gate_way = gate_way
        self.ip = ip
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gate_way is not None:
            result['GateWay'] = self.gate_way
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GateWay') is not None:
            self.gate_way = m.get('GateWay')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeInstancesResponseBodyInstancesInstancePublicIpAddresses(TeaModel):
    def __init__(
        self,
        public_ip_address: List[DescribeInstancesResponseBodyInstancesInstancePublicIpAddressesPublicIpAddress] = None,
    ):
        self.public_ip_address = public_ip_address

    def validate(self):
        if self.public_ip_address:
            for k in self.public_ip_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PublicIpAddress'] = []
        if self.public_ip_address is not None:
            for k in self.public_ip_address:
                result['PublicIpAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.public_ip_address = []
        if m.get('PublicIpAddress') is not None:
            for k in m.get('PublicIpAddress'):
                temp_model = DescribeInstancesResponseBodyInstancesInstancePublicIpAddressesPublicIpAddress()
                self.public_ip_address.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesInstanceSecurityGroupIds(TeaModel):
    def __init__(
        self,
        security_group_id: List[str] = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeInstancesResponseBodyInstancesInstanceSystemDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        disk_id: str = None,
        disk_name: str = None,
        size: int = None,
        device_type: str = None,
        disk_type: str = None,
        name: str = None,
        storage: int = None,
        uuid: str = None,
    ):
        self.category = category
        self.disk_id = disk_id
        self.disk_name = disk_name
        self.size = size
        self.device_type = device_type
        self.disk_type = disk_type
        self.name = name
        self.storage = storage
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.size is not None:
            result['Size'] = self.size
        if self.device_type is not None:
            result['device_type'] = self.device_type
        if self.disk_type is not None:
            result['disk_type'] = self.disk_type
        if self.name is not None:
            result['name'] = self.name
        if self.storage is not None:
            result['storage'] = self.storage
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('device_type') is not None:
            self.device_type = m.get('device_type')
        if m.get('disk_type') is not None:
            self.disk_type = m.get('disk_type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class DescribeInstancesResponseBodyInstancesInstance(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        creation_time: str = None,
        data_disk: DescribeInstancesResponseBodyInstancesInstanceDataDisk = None,
        disk: int = None,
        ens_region_id: str = None,
        expired_time: str = None,
        host_name: str = None,
        image_id: str = None,
        inner_ip_address: DescribeInstancesResponseBodyInstancesInstanceInnerIpAddress = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_resource_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        memory: int = None,
        network_attributes: DescribeInstancesResponseBodyInstancesInstanceNetworkAttributes = None,
        osname: str = None,
        private_ip_addresses: DescribeInstancesResponseBodyInstancesInstancePrivateIpAddresses = None,
        public_ip_address: DescribeInstancesResponseBodyInstancesInstancePublicIpAddress = None,
        public_ip_addresses: DescribeInstancesResponseBodyInstancesInstancePublicIpAddresses = None,
        security_group_ids: DescribeInstancesResponseBodyInstancesInstanceSecurityGroupIds = None,
        spec_name: str = None,
        status: str = None,
        system_disk: DescribeInstancesResponseBodyInstancesInstanceSystemDisk = None,
    ):
        self.cpu = cpu
        self.creation_time = creation_time
        self.data_disk = data_disk
        self.disk = disk
        self.ens_region_id = ens_region_id
        self.expired_time = expired_time
        self.host_name = host_name
        self.image_id = image_id
        self.inner_ip_address = inner_ip_address
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_resource_type = instance_resource_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.memory = memory
        self.network_attributes = network_attributes
        self.osname = osname
        self.private_ip_addresses = private_ip_addresses
        self.public_ip_address = public_ip_address
        self.public_ip_addresses = public_ip_addresses
        self.security_group_ids = security_group_ids
        self.spec_name = spec_name
        self.status = status
        self.system_disk = system_disk

    def validate(self):
        if self.data_disk:
            self.data_disk.validate()
        if self.inner_ip_address:
            self.inner_ip_address.validate()
        if self.network_attributes:
            self.network_attributes.validate()
        if self.private_ip_addresses:
            self.private_ip_addresses.validate()
        if self.public_ip_address:
            self.public_ip_address.validate()
        if self.public_ip_addresses:
            self.public_ip_addresses.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_disk is not None:
            result['DataDisk'] = self.data_disk.to_map()
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.inner_ip_address is not None:
            result['InnerIpAddress'] = self.inner_ip_address.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_resource_type is not None:
            result['InstanceResourceType'] = self.instance_resource_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.network_attributes is not None:
            result['NetworkAttributes'] = self.network_attributes.to_map()
        if self.osname is not None:
            result['OSName'] = self.osname
        if self.private_ip_addresses is not None:
            result['PrivateIpAddresses'] = self.private_ip_addresses.to_map()
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address.to_map()
        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses.to_map()
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        if self.status is not None:
            result['Status'] = self.status
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataDisk') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstanceDataDisk()
            self.data_disk = temp_model.from_map(m['DataDisk'])
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InnerIpAddress') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstanceInnerIpAddress()
            self.inner_ip_address = temp_model.from_map(m['InnerIpAddress'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceResourceType') is not None:
            self.instance_resource_type = m.get('InstanceResourceType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetworkAttributes') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstanceNetworkAttributes()
            self.network_attributes = temp_model.from_map(m['NetworkAttributes'])
        if m.get('OSName') is not None:
            self.osname = m.get('OSName')
        if m.get('PrivateIpAddresses') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstancePrivateIpAddresses()
            self.private_ip_addresses = temp_model.from_map(m['PrivateIpAddresses'])
        if m.get('PublicIpAddress') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstancePublicIpAddress()
            self.public_ip_address = temp_model.from_map(m['PublicIpAddress'])
        if m.get('PublicIpAddresses') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstancePublicIpAddresses()
            self.public_ip_addresses = temp_model.from_map(m['PublicIpAddresses'])
        if m.get('SecurityGroupIds') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstanceSecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m['SecurityGroupIds'])
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemDisk') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstanceSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance: List[DescribeInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        instances: DescribeInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.instances = instances
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Instances') is not None:
            temp_model = DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyPairsRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        page_number: str = None,
        page_size: str = None,
        version: str = None,
    ):
        self.key_pair_name = key_pair_name
        self.page_number = page_number
        self.page_size = page_size
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeKeyPairsResponseBodyKeyPairsKeyPair(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        key_pair_finger_print: str = None,
        key_pair_name: str = None,
    ):
        self.creation_time = creation_time
        self.key_pair_finger_print = key_pair_finger_print
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class DescribeKeyPairsResponseBodyKeyPairs(TeaModel):
    def __init__(
        self,
        key_pair: List[DescribeKeyPairsResponseBodyKeyPairsKeyPair] = None,
    ):
        self.key_pair = key_pair

    def validate(self):
        if self.key_pair:
            for k in self.key_pair:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyPair'] = []
        if self.key_pair is not None:
            for k in self.key_pair:
                result['KeyPair'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_pair = []
        if m.get('KeyPair') is not None:
            for k in m.get('KeyPair'):
                temp_model = DescribeKeyPairsResponseBodyKeyPairsKeyPair()
                self.key_pair.append(temp_model.from_map(k))
        return self


class DescribeKeyPairsResponseBody(TeaModel):
    def __init__(
        self,
        key_pairs: DescribeKeyPairsResponseBodyKeyPairs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.key_pairs = key_pairs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.key_pairs:
            self.key_pairs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pairs is not None:
            result['KeyPairs'] = self.key_pairs.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairs') is not None:
            temp_model = DescribeKeyPairsResponseBodyKeyPairs()
            self.key_pairs = temp_model.from_map(m['KeyPairs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeKeyPairsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerAttributeRequest(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
    ):
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeLoadBalancerAttributeResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: str = None,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.ip = ip
        self.port = port
        self.server_id = server_id
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocols(TeaModel):
    def __init__(
        self,
        description: str = None,
        forward_port: int = None,
        listener_forward: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
    ):
        self.description = description
        self.forward_port = forward_port
        self.listener_forward = listener_forward
        self.listener_port = listener_port
        self.listener_protocol = listener_protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        return self


class DescribeLoadBalancerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_ipversion: str = None,
        backend_servers: List[DescribeLoadBalancerAttributeResponseBodyBackendServers] = None,
        bandwidth: int = None,
        create_time: str = None,
        end_time: str = None,
        ens_region_id: str = None,
        listener_ports: List[str] = None,
        listener_ports_and_protocols: List[DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocols] = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        load_balancer_status: str = None,
        network_id: str = None,
        pay_type: str = None,
        request_id: str = None,
        v_switch_id: str = None,
    ):
        self.address = address
        self.address_ipversion = address_ipversion
        self.backend_servers = backend_servers
        self.bandwidth = bandwidth
        self.create_time = create_time
        self.end_time = end_time
        self.ens_region_id = ens_region_id
        self.listener_ports = listener_ports
        self.listener_ports_and_protocols = listener_ports_and_protocols
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.load_balancer_spec = load_balancer_spec
        self.load_balancer_status = load_balancer_status
        self.network_id = network_id
        self.pay_type = pay_type
        # Id of the request
        self.request_id = request_id
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.backend_servers:
            for k in self.backend_servers:
                if k:
                    k.validate()
        if self.listener_ports_and_protocols:
            for k in self.listener_ports_and_protocols:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        result['BackendServers'] = []
        if self.backend_servers is not None:
            for k in self.backend_servers:
                result['BackendServers'].append(k.to_map() if k else None)
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.listener_ports is not None:
            result['ListenerPorts'] = self.listener_ports
        result['ListenerPortsAndProtocols'] = []
        if self.listener_ports_and_protocols is not None:
            for k in self.listener_ports_and_protocols:
                result['ListenerPortsAndProtocols'].append(k.to_map() if k else None)
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        self.backend_servers = []
        if m.get('BackendServers') is not None:
            for k in m.get('BackendServers'):
                temp_model = DescribeLoadBalancerAttributeResponseBodyBackendServers()
                self.backend_servers.append(temp_model.from_map(k))
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('ListenerPorts') is not None:
            self.listener_ports = m.get('ListenerPorts')
        self.listener_ports_and_protocols = []
        if m.get('ListenerPortsAndProtocols') is not None:
            for k in m.get('ListenerPortsAndProtocols'):
                temp_model = DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocols()
                self.listener_ports_and_protocols.append(temp_model.from_map(k))
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeLoadBalancerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLoadBalancerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerHTTPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        listener_port: int = None,
        load_balancer_id: str = None,
    ):
        self.listener_port = listener_port
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeLoadBalancerHTTPListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        description: str = None,
        forward_port: int = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        listener_forward: str = None,
        listener_port: int = None,
        request_id: str = None,
        request_timeout: int = None,
        scheduler: str = None,
        server_certificate_id: str = None,
        status: str = None,
        unhealthy_threshold: int = None,
    ):
        self.bandwidth = bandwidth
        self.description = description
        self.forward_port = forward_port
        self.health_check = health_check
        self.health_check_connect_port = health_check_connect_port
        self.health_check_domain = health_check_domain
        self.health_check_http_code = health_check_http_code
        self.health_check_interval = health_check_interval
        self.health_check_method = health_check_method
        self.health_check_timeout = health_check_timeout
        self.health_check_uri = health_check_uri
        self.healthy_threshold = healthy_threshold
        self.idle_timeout = idle_timeout
        self.listener_forward = listener_forward
        self.listener_port = listener_port
        # Id of the request
        self.request_id = request_id
        self.request_timeout = request_timeout
        self.scheduler = scheduler
        self.server_certificate_id = server_certificate_id
        self.status = status
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.status is not None:
            result['Status'] = self.status
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class DescribeLoadBalancerHTTPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerHTTPListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLoadBalancerHTTPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerHTTPSListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        listener_port: int = None,
        load_balancer_id: str = None,
    ):
        self.listener_port = listener_port
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeLoadBalancerHTTPSListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        description: str = None,
        forward_port: int = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        listener_forward: str = None,
        listener_port: int = None,
        request_id: str = None,
        request_timeout: int = None,
        scheduler: str = None,
        server_certificate_id: str = None,
        status: str = None,
        unhealthy_threshold: int = None,
    ):
        self.bandwidth = bandwidth
        self.description = description
        self.forward_port = forward_port
        self.health_check = health_check
        self.health_check_connect_port = health_check_connect_port
        self.health_check_domain = health_check_domain
        self.health_check_http_code = health_check_http_code
        self.health_check_interval = health_check_interval
        self.health_check_method = health_check_method
        self.health_check_timeout = health_check_timeout
        self.health_check_uri = health_check_uri
        self.healthy_threshold = healthy_threshold
        self.idle_timeout = idle_timeout
        self.listener_forward = listener_forward
        self.listener_port = listener_port
        # Id of the request
        self.request_id = request_id
        self.request_timeout = request_timeout
        self.scheduler = scheduler
        self.server_certificate_id = server_certificate_id
        self.status = status
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.status is not None:
            result['Status'] = self.status
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class DescribeLoadBalancerHTTPSListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerHTTPSListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLoadBalancerHTTPSListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerSpecRequest(TeaModel):
    def __init__(
        self,
        load_balancer_spec: str = None,
    ):
        self.load_balancer_spec = load_balancer_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')
        return self


class DescribeLoadBalancerSpecResponseBodyLoadBalancerSpecs(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        load_balancer_spec: str = None,
    ):
        self.display_name = display_name
        self.load_balancer_spec = load_balancer_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')
        return self


class DescribeLoadBalancerSpecResponseBody(TeaModel):
    def __init__(
        self,
        load_balancer_specs: List[DescribeLoadBalancerSpecResponseBodyLoadBalancerSpecs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.load_balancer_specs = load_balancer_specs
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.load_balancer_specs:
            for k in self.load_balancer_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancerSpecs'] = []
        if self.load_balancer_specs is not None:
            for k in self.load_balancer_specs:
                result['LoadBalancerSpecs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer_specs = []
        if m.get('LoadBalancerSpecs') is not None:
            for k in m.get('LoadBalancerSpecs'):
                temp_model = DescribeLoadBalancerSpecResponseBodyLoadBalancerSpecs()
                self.load_balancer_specs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLoadBalancerSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLoadBalancerSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerTCPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        listener_port: int = None,
        load_balancer_id: str = None,
    ):
        self.listener_port = listener_port
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeLoadBalancerTCPListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        backend_server_port: int = None,
        bandwidth: int = None,
        description: str = None,
        eip_transmit: str = None,
        established_timeout: int = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        persistence_timeout: int = None,
        request_id: str = None,
        scheduler: str = None,
        status: str = None,
        unhealthy_threshold: int = None,
    ):
        self.backend_server_port = backend_server_port
        self.bandwidth = bandwidth
        self.description = description
        self.eip_transmit = eip_transmit
        self.established_timeout = established_timeout
        self.health_check = health_check
        self.health_check_connect_port = health_check_connect_port
        self.health_check_connect_timeout = health_check_connect_timeout
        self.health_check_domain = health_check_domain
        self.health_check_http_code = health_check_http_code
        self.health_check_interval = health_check_interval
        self.health_check_type = health_check_type
        self.health_check_uri = health_check_uri
        self.healthy_threshold = healthy_threshold
        self.listener_port = listener_port
        self.persistence_timeout = persistence_timeout
        # Id of the request
        self.request_id = request_id
        self.scheduler = scheduler
        self.status = status
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.eip_transmit is not None:
            result['EipTransmit'] = self.eip_transmit
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.status is not None:
            result['Status'] = self.status
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EipTransmit') is not None:
            self.eip_transmit = m.get('EipTransmit')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class DescribeLoadBalancerTCPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerTCPListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLoadBalancerTCPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerUDPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        listener_port: int = None,
        load_balancer_id: str = None,
    ):
        self.listener_port = listener_port
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeLoadBalancerUDPListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        backend_server_port: int = None,
        bandwidth: int = None,
        description: str = None,
        eip_transmit: str = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_exp: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        request_id: str = None,
        scheduler: str = None,
        status: str = None,
        unhealthy_threshold: int = None,
    ):
        self.backend_server_port = backend_server_port
        self.bandwidth = bandwidth
        self.description = description
        self.eip_transmit = eip_transmit
        self.health_check = health_check
        self.health_check_connect_port = health_check_connect_port
        self.health_check_connect_timeout = health_check_connect_timeout
        self.health_check_exp = health_check_exp
        self.health_check_interval = health_check_interval
        self.health_check_req = health_check_req
        self.healthy_threshold = healthy_threshold
        self.listener_port = listener_port
        # Id of the request
        self.request_id = request_id
        self.scheduler = scheduler
        self.status = status
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.eip_transmit is not None:
            result['EipTransmit'] = self.eip_transmit
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_exp is not None:
            result['HealthCheckExp'] = self.health_check_exp
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.status is not None:
            result['Status'] = self.status
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EipTransmit') is not None:
            self.eip_transmit = m.get('EipTransmit')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckExp') is not None:
            self.health_check_exp = m.get('HealthCheckExp')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class DescribeLoadBalancerUDPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerUDPListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLoadBalancerUDPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancersRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        ens_region_id: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_status: str = None,
        network_id: str = None,
        page_number: int = None,
        page_size: int = None,
        server_id: str = None,
        v_switch_id: str = None,
    ):
        self.address = address
        self.ens_region_id = ens_region_id
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.load_balancer_status = load_balancer_status
        self.network_id = network_id
        self.page_number = page_number
        self.page_size = page_size
        self.server_id = server_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancer(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_ipversion: str = None,
        create_time: str = None,
        ens_region_id: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_status: str = None,
        network_id: str = None,
        pay_type: str = None,
        v_switch_id: str = None,
    ):
        self.address = address
        self.address_ipversion = address_ipversion
        self.create_time = create_time
        self.ens_region_id = ens_region_id
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.load_balancer_status = load_balancer_status
        self.network_id = network_id
        self.pay_type = pay_type
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeLoadBalancersResponseBodyLoadBalancers(TeaModel):
    def __init__(
        self,
        load_balancer: List[DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancer] = None,
    ):
        self.load_balancer = load_balancer

    def validate(self):
        if self.load_balancer:
            for k in self.load_balancer:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancer'] = []
        if self.load_balancer is not None:
            for k in self.load_balancer:
                result['LoadBalancer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer = []
        if m.get('LoadBalancer') is not None:
            for k in m.get('LoadBalancer'):
                temp_model = DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancer()
                self.load_balancer.append(temp_model.from_map(k))
        return self


class DescribeLoadBalancersResponseBody(TeaModel):
    def __init__(
        self,
        load_balancers: DescribeLoadBalancersResponseBodyLoadBalancers = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.load_balancers = load_balancers
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.load_balancers:
            self.load_balancers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancers is not None:
            result['LoadBalancers'] = self.load_balancers.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancers') is not None:
            temp_model = DescribeLoadBalancersResponseBodyLoadBalancers()
            self.load_balancers = temp_model.from_map(m['LoadBalancers'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLoadBalancersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLoadBalancersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMeasurementDataRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        start_date: str = None,
        version: str = None,
    ):
        self.end_date = end_date
        self.start_date = start_date
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData(TeaModel):
    def __init__(
        self,
        cost_code: str = None,
        cost_name: str = None,
        cost_val: int = None,
    ):
        self.cost_code = cost_code
        self.cost_name = cost_name
        self.cost_val = cost_val

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_code is not None:
            result['CostCode'] = self.cost_code
        if self.cost_name is not None:
            result['CostName'] = self.cost_name
        if self.cost_val is not None:
            result['CostVal'] = self.cost_val
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCode') is not None:
            self.cost_code = m.get('CostCode')
        if m.get('CostName') is not None:
            self.cost_name = m.get('CostName')
        if m.get('CostVal') is not None:
            self.cost_val = m.get('CostVal')
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas(TeaModel):
    def __init__(
        self,
        band_width_fee_data: List[DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData] = None,
    ):
        self.band_width_fee_data = band_width_fee_data

    def validate(self):
        if self.band_width_fee_data:
            for k in self.band_width_fee_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BandWidthFeeData'] = []
        if self.band_width_fee_data is not None:
            for k in self.band_width_fee_data:
                result['BandWidthFeeData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_fee_data = []
        if m.get('BandWidthFeeData') is not None:
            for k in m.get('BandWidthFeeData'):
                temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData()
                self.band_width_fee_data.append(temp_model.from_map(k))
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeData(TeaModel):
    def __init__(
        self,
        memory: int = None,
        storage: int = None,
        vcpu: int = None,
    ):
        self.memory = memory
        self.storage = storage
        self.vcpu = vcpu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.vcpu is not None:
            result['Vcpu'] = self.vcpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Vcpu') is not None:
            self.vcpu = m.get('Vcpu')
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail(TeaModel):
    def __init__(
        self,
        cost_code: str = None,
        cost_name: str = None,
        cost_val: int = None,
        resource_type: str = None,
    ):
        self.cost_code = cost_code
        self.cost_name = cost_name
        self.cost_val = cost_val
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_code is not None:
            result['CostCode'] = self.cost_code
        if self.cost_name is not None:
            result['CostName'] = self.cost_name
        if self.cost_val is not None:
            result['CostVal'] = self.cost_val
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCode') is not None:
            self.cost_code = m.get('CostCode')
        if m.get('CostName') is not None:
            self.cost_name = m.get('CostName')
        if m.get('CostVal') is not None:
            self.cost_val = m.get('CostVal')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetails(TeaModel):
    def __init__(
        self,
        resource_fee_data_detail: List[DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail] = None,
    ):
        self.resource_fee_data_detail = resource_fee_data_detail

    def validate(self):
        if self.resource_fee_data_detail:
            for k in self.resource_fee_data_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceFeeDataDetail'] = []
        if self.resource_fee_data_detail is not None:
            for k in self.resource_fee_data_detail:
                result['ResourceFeeDataDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_fee_data_detail = []
        if m.get('ResourceFeeDataDetail') is not None:
            for k in m.get('ResourceFeeDataDetail'):
                temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail()
                self.resource_fee_data_detail.append(temp_model.from_map(k))
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementData(TeaModel):
    def __init__(
        self,
        band_width_fee_datas: DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas = None,
        charge_model: str = None,
        cost_cycle: str = None,
        cost_end_time: str = None,
        cost_start_time: str = None,
        resource_fee_data: DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeData = None,
        resource_fee_data_details: DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetails = None,
    ):
        self.band_width_fee_datas = band_width_fee_datas
        self.charge_model = charge_model
        self.cost_cycle = cost_cycle
        self.cost_end_time = cost_end_time
        self.cost_start_time = cost_start_time
        self.resource_fee_data = resource_fee_data
        self.resource_fee_data_details = resource_fee_data_details

    def validate(self):
        if self.band_width_fee_datas:
            self.band_width_fee_datas.validate()
        if self.resource_fee_data:
            self.resource_fee_data.validate()
        if self.resource_fee_data_details:
            self.resource_fee_data_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width_fee_datas is not None:
            result['BandWidthFeeDatas'] = self.band_width_fee_datas.to_map()
        if self.charge_model is not None:
            result['ChargeModel'] = self.charge_model
        if self.cost_cycle is not None:
            result['CostCycle'] = self.cost_cycle
        if self.cost_end_time is not None:
            result['CostEndTime'] = self.cost_end_time
        if self.cost_start_time is not None:
            result['CostStartTime'] = self.cost_start_time
        if self.resource_fee_data is not None:
            result['ResourceFeeData'] = self.resource_fee_data.to_map()
        if self.resource_fee_data_details is not None:
            result['ResourceFeeDataDetails'] = self.resource_fee_data_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidthFeeDatas') is not None:
            temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas()
            self.band_width_fee_datas = temp_model.from_map(m['BandWidthFeeDatas'])
        if m.get('ChargeModel') is not None:
            self.charge_model = m.get('ChargeModel')
        if m.get('CostCycle') is not None:
            self.cost_cycle = m.get('CostCycle')
        if m.get('CostEndTime') is not None:
            self.cost_end_time = m.get('CostEndTime')
        if m.get('CostStartTime') is not None:
            self.cost_start_time = m.get('CostStartTime')
        if m.get('ResourceFeeData') is not None:
            temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeData()
            self.resource_fee_data = temp_model.from_map(m['ResourceFeeData'])
        if m.get('ResourceFeeDataDetails') is not None:
            temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetails()
            self.resource_fee_data_details = temp_model.from_map(m['ResourceFeeDataDetails'])
        return self


class DescribeMeasurementDataResponseBodyMeasurementDatas(TeaModel):
    def __init__(
        self,
        measurement_data: List[DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementData] = None,
    ):
        self.measurement_data = measurement_data

    def validate(self):
        if self.measurement_data:
            for k in self.measurement_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MeasurementData'] = []
        if self.measurement_data is not None:
            for k in self.measurement_data:
                result['MeasurementData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.measurement_data = []
        if m.get('MeasurementData') is not None:
            for k in m.get('MeasurementData'):
                temp_model = DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementData()
                self.measurement_data.append(temp_model.from_map(k))
        return self


class DescribeMeasurementDataResponseBody(TeaModel):
    def __init__(
        self,
        measurement_datas: DescribeMeasurementDataResponseBodyMeasurementDatas = None,
        request_id: str = None,
    ):
        self.measurement_datas = measurement_datas
        self.request_id = request_id

    def validate(self):
        if self.measurement_datas:
            self.measurement_datas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.measurement_datas is not None:
            result['MeasurementDatas'] = self.measurement_datas.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeasurementDatas') is not None:
            temp_model = DescribeMeasurementDataResponseBodyMeasurementDatas()
            self.measurement_datas = temp_model.from_map(m['MeasurementDatas'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMeasurementDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMeasurementDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMeasurementDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNatGatewaysRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        network_id: str = None,
        page_number: int = None,
        page_size: int = None,
        v_switch_id: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.network_id = network_id
        self.page_number = page_number
        self.page_size = page_size
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeNatGatewaysResponseBodyNatGateways(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        ens_region_id: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        network_id: str = None,
        v_switch_id: str = None,
    ):
        self.creation_time = creation_time
        self.ens_region_id = ens_region_id
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.network_id = network_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeNatGatewaysResponseBody(TeaModel):
    def __init__(
        self,
        nat_gateways: List[DescribeNatGatewaysResponseBodyNatGateways] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.nat_gateways = nat_gateways
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.nat_gateways:
            for k in self.nat_gateways:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NatGateways'] = []
        if self.nat_gateways is not None:
            for k in self.nat_gateways:
                result['NatGateways'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nat_gateways = []
        if m.get('NatGateways') is not None:
            for k in m.get('NatGateways'):
                temp_model = DescribeNatGatewaysResponseBodyNatGateways()
                self.nat_gateways.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNatGatewaysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNatGatewaysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNatGatewaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkAttributeRequest(TeaModel):
    def __init__(
        self,
        network_id: str = None,
    ):
        self.network_id = network_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        return self


class DescribeNetworkAttributeResponseBodyCloudResourcesCloudResourceSetType(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        resource_type: str = None,
    ):
        self.resource_count = resource_count
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeNetworkAttributeResponseBodyCloudResources(TeaModel):
    def __init__(
        self,
        cloud_resource_set_type: List[DescribeNetworkAttributeResponseBodyCloudResourcesCloudResourceSetType] = None,
    ):
        self.cloud_resource_set_type = cloud_resource_set_type

    def validate(self):
        if self.cloud_resource_set_type:
            for k in self.cloud_resource_set_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CloudResourceSetType'] = []
        if self.cloud_resource_set_type is not None:
            for k in self.cloud_resource_set_type:
                result['CloudResourceSetType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_resource_set_type = []
        if m.get('CloudResourceSetType') is not None:
            for k in m.get('CloudResourceSetType'):
                temp_model = DescribeNetworkAttributeResponseBodyCloudResourcesCloudResourceSetType()
                self.cloud_resource_set_type.append(temp_model.from_map(k))
        return self


class DescribeNetworkAttributeResponseBodyVSwitchIds(TeaModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeNetworkAttributeResponseBody(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        cloud_resources: DescribeNetworkAttributeResponseBodyCloudResources = None,
        created_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        network_id: str = None,
        network_name: str = None,
        request_id: str = None,
        router_table_id: str = None,
        status: str = None,
        v_switch_ids: DescribeNetworkAttributeResponseBodyVSwitchIds = None,
    ):
        self.cidr_block = cidr_block
        self.cloud_resources = cloud_resources
        self.created_time = created_time
        self.description = description
        self.ens_region_id = ens_region_id
        self.network_id = network_id
        self.network_name = network_name
        # Id of the request
        self.request_id = request_id
        self.router_table_id = router_table_id
        self.status = status
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.cloud_resources:
            self.cloud_resources.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.cloud_resources is not None:
            result['CloudResources'] = self.cloud_resources.to_map()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.network_name is not None:
            result['NetworkName'] = self.network_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.router_table_id is not None:
            result['RouterTableId'] = self.router_table_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CloudResources') is not None:
            temp_model = DescribeNetworkAttributeResponseBodyCloudResources()
            self.cloud_resources = temp_model.from_map(m['CloudResources'])
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RouterTableId') is not None:
            self.router_table_id = m.get('RouterTableId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchIds') is not None:
            temp_model = DescribeNetworkAttributeResponseBodyVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m['VSwitchIds'])
        return self


class DescribeNetworkAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNetworkAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNetworkAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkInterfacesRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        primary_ip_address: str = None,
        v_switch_id: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.primary_ip_address = primary_ip_address
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        mac_address: str = None,
        network_interface_id: str = None,
        primary_ip: str = None,
        primary_ip_type: str = None,
        status: str = None,
        v_switch_id: str = None,
    ):
        self.creation_time = creation_time
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.mac_address = mac_address
        self.network_interface_id = network_interface_id
        self.primary_ip = primary_ip
        self.primary_ip_type = primary_ip_type
        self.status = status
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.primary_ip is not None:
            result['PrimaryIp'] = self.primary_ip
        if self.primary_ip_type is not None:
            result['PrimaryIpType'] = self.primary_ip_type
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrimaryIp') is not None:
            self.primary_ip = m.get('PrimaryIp')
        if m.get('PrimaryIpType') is not None:
            self.primary_ip_type = m.get('PrimaryIpType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets(TeaModel):
    def __init__(
        self,
        network_interface_set: List[DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet] = None,
    ):
        self.network_interface_set = network_interface_set

    def validate(self):
        if self.network_interface_set:
            for k in self.network_interface_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkInterfaceSet'] = []
        if self.network_interface_set is not None:
            for k in self.network_interface_set:
                result['NetworkInterfaceSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interface_set = []
        if m.get('NetworkInterfaceSet') is not None:
            for k in m.get('NetworkInterfaceSet'):
                temp_model = DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet()
                self.network_interface_set.append(temp_model.from_map(k))
        return self


class DescribeNetworkInterfacesResponseBody(TeaModel):
    def __init__(
        self,
        network_interface_sets: DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.network_interface_sets = network_interface_sets
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.network_interface_sets:
            self.network_interface_sets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_interface_sets is not None:
            result['NetworkInterfaceSets'] = self.network_interface_sets.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceSets') is not None:
            temp_model = DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets()
            self.network_interface_sets = temp_model.from_map(m['NetworkInterfaceSets'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNetworkInterfacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNetworkInterfacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNetworkInterfacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworksRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        network_id: str = None,
        network_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.ens_region_id = ens_region_id
        self.network_id = network_id
        self.network_name = network_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.network_name is not None:
            result['NetworkName'] = self.network_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeNetworksResponseBodyNetworksNetworkVSwitchIds(TeaModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeNetworksResponseBodyNetworksNetwork(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        created_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        network_id: str = None,
        network_name: str = None,
        router_table_id: str = None,
        status: str = None,
        v_switch_ids: DescribeNetworksResponseBodyNetworksNetworkVSwitchIds = None,
    ):
        self.cidr_block = cidr_block
        self.created_time = created_time
        self.description = description
        self.ens_region_id = ens_region_id
        self.network_id = network_id
        self.network_name = network_name
        self.router_table_id = router_table_id
        self.status = status
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.network_name is not None:
            result['NetworkName'] = self.network_name
        if self.router_table_id is not None:
            result['RouterTableId'] = self.router_table_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')
        if m.get('RouterTableId') is not None:
            self.router_table_id = m.get('RouterTableId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchIds') is not None:
            temp_model = DescribeNetworksResponseBodyNetworksNetworkVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m['VSwitchIds'])
        return self


class DescribeNetworksResponseBodyNetworks(TeaModel):
    def __init__(
        self,
        network: List[DescribeNetworksResponseBodyNetworksNetwork] = None,
    ):
        self.network = network

    def validate(self):
        if self.network:
            for k in self.network:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Network'] = []
        if self.network is not None:
            for k in self.network:
                result['Network'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network = []
        if m.get('Network') is not None:
            for k in m.get('Network'):
                temp_model = DescribeNetworksResponseBodyNetworksNetwork()
                self.network.append(temp_model.from_map(k))
        return self


class DescribeNetworksResponseBody(TeaModel):
    def __init__(
        self,
        networks: DescribeNetworksResponseBodyNetworks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.networks = networks
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.networks:
            self.networks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.networks is not None:
            result['Networks'] = self.networks.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Networks') is not None:
            temp_model = DescribeNetworksResponseBodyNetworks()
            self.networks = temp_model.from_map(m['Networks'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNetworksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNetworksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNetworksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePrePaidInstanceStockRequest(TeaModel):
    def __init__(
        self,
        data_disk_size: int = None,
        ens_region_id: str = None,
        instance_spec: str = None,
        system_disk_size: int = None,
        version: str = None,
    ):
        self.data_disk_size = data_disk_size
        self.ens_region_id = ens_region_id
        self.instance_spec = instance_spec
        self.system_disk_size = system_disk_size
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribePrePaidInstanceStockResponseBody(TeaModel):
    def __init__(
        self,
        avaliable_count: int = None,
        cores: int = None,
        data_disk_size: int = None,
        ens_region_id: str = None,
        instance_spec: str = None,
        memory: int = None,
        request_id: str = None,
        system_disk_size: int = None,
    ):
        self.avaliable_count = avaliable_count
        self.cores = cores
        self.data_disk_size = data_disk_size
        self.ens_region_id = ens_region_id
        self.instance_spec = instance_spec
        self.memory = memory
        self.request_id = request_id
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avaliable_count is not None:
            result['AvaliableCount'] = self.avaliable_count
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvaliableCount') is not None:
            self.avaliable_count = m.get('AvaliableCount')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribePrePaidInstanceStockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePrePaidInstanceStockResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePrePaidInstanceStockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePriceRequestDataDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
    ):
        # 数据盘大小，单位GB。如果此字段不为空，则以此段为准。
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribePriceRequestSystemDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
    ):
        # 系统盘大小，单位：GB
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribePriceRequestDataDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        size: int = None,
    ):
        # 磁盘类型
        self.category = category
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribePriceRequest(TeaModel):
    def __init__(
        self,
        data_disk: List[DescribePriceRequestDataDisk] = None,
        system_disk: DescribePriceRequestSystemDisk = None,
        data_disks: List[DescribePriceRequestDataDisks] = None,
        ens_region_id: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        quantity: int = None,
    ):
        self.data_disk = data_disk
        self.system_disk = system_disk
        # 如果DataDisk.1.Size为空且此字段不为空时的则以此字段为准
        self.data_disks = data_disks
        # 节点ID。
        self.ens_region_id = ens_region_id
        # 实列规格。
        self.instance_type = instance_type
        # 带宽计费方式
        self.internet_charge_type = internet_charge_type
        # 购买资源的时长，如果不指定PeriodUnit，则默认按月购买。目前只支持按Days和Month。如果PeriodUnit=Day时，Period仅可以3。如果PeriodUnit=Monthc时，则Period可以为1-9,12。
        self.period = period
        # 查询云服务器ENS不同计费周期的价格。取值范围：
        # Month（默认）：按月计费的价格单位。
        # Day：按天计费的价格单位。
        self.period_unit = period_unit
        # 数量。
        self.quantity = quantity

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribePriceRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('SystemDisk') is not None:
            temp_model = DescribePriceRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DescribePriceRequestDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class DescribePriceShrinkRequestDataDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
    ):
        # 数据盘大小，单位GB。如果此字段不为空，则以此段为准。
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribePriceShrinkRequestSystemDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
    ):
        # 系统盘大小，单位：GB
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribePriceShrinkRequest(TeaModel):
    def __init__(
        self,
        data_disk: List[DescribePriceShrinkRequestDataDisk] = None,
        system_disk: DescribePriceShrinkRequestSystemDisk = None,
        data_disks_shrink: str = None,
        ens_region_id: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        quantity: int = None,
    ):
        self.data_disk = data_disk
        self.system_disk = system_disk
        # 如果DataDisk.1.Size为空且此字段不为空时的则以此字段为准
        self.data_disks_shrink = data_disks_shrink
        # 节点ID。
        self.ens_region_id = ens_region_id
        # 实列规格。
        self.instance_type = instance_type
        # 带宽计费方式
        self.internet_charge_type = internet_charge_type
        # 购买资源的时长，如果不指定PeriodUnit，则默认按月购买。目前只支持按Days和Month。如果PeriodUnit=Day时，Period仅可以3。如果PeriodUnit=Monthc时，则Period可以为1-9,12。
        self.period = period
        # 查询云服务器ENS不同计费周期的价格。取值范围：
        # Month（默认）：按月计费的价格单位。
        # Day：按天计费的价格单位。
        self.period_unit = period_unit
        # 数量。
        self.quantity = quantity

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.data_disks_shrink is not None:
            result['DataDisks'] = self.data_disks_shrink
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = DescribePriceShrinkRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('SystemDisk') is not None:
            temp_model = DescribePriceShrinkRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('DataDisks') is not None:
            self.data_disks_shrink = m.get('DataDisks')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class DescribePriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribePriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        price: DescribePriceResponseBodyPriceInfoPrice = None,
    ):
        self.price = price

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = DescribePriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(
        self,
        price_info: DescribePriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        self.price_info = price_info
        self.request_id = request_id

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = DescribePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionIspsRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
    ):
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        return self


class DescribeRegionIspsResponseBodyIsps(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeRegionIspsResponseBody(TeaModel):
    def __init__(
        self,
        isps: List[DescribeRegionIspsResponseBodyIsps] = None,
        request_id: str = None,
    ):
        self.isps = isps
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Isps'] = []
        if self.isps is not None:
            for k in self.isps:
                result['Isps'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isps = []
        if m.get('Isps') is not None:
            for k in m.get('Isps'):
                temp_model = DescribeRegionIspsResponseBodyIsps()
                self.isps.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionIspsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionIspsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionIspsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeReservedResourceRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeReservedResourceResponseBodyImagesImage(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
    ):
        self.image_id = image_id
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        return self


class DescribeReservedResourceResponseBodyImages(TeaModel):
    def __init__(
        self,
        image: List[DescribeReservedResourceResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k in m.get('Image'):
                temp_model = DescribeReservedResourceResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k))
        return self


class DescribeReservedResourceResponseBodySupportResourcesSupportResourceDataDiskSizes(TeaModel):
    def __init__(
        self,
        data_disk_size: List[str] = None,
    ):
        self.data_disk_size = data_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        return self


class DescribeReservedResourceResponseBodySupportResourcesSupportResourceSystemDiskSizes(TeaModel):
    def __init__(
        self,
        system_disk_size: List[str] = None,
    ):
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeReservedResourceResponseBodySupportResourcesSupportResource(TeaModel):
    def __init__(
        self,
        data_disk_sizes: DescribeReservedResourceResponseBodySupportResourcesSupportResourceDataDiskSizes = None,
        ens_region_id: str = None,
        instance_spec: str = None,
        support_resources_count: str = None,
        system_disk_sizes: DescribeReservedResourceResponseBodySupportResourcesSupportResourceSystemDiskSizes = None,
    ):
        self.data_disk_sizes = data_disk_sizes
        self.ens_region_id = ens_region_id
        self.instance_spec = instance_spec
        self.support_resources_count = support_resources_count
        self.system_disk_sizes = system_disk_sizes

    def validate(self):
        if self.data_disk_sizes:
            self.data_disk_sizes.validate()
        if self.system_disk_sizes:
            self.system_disk_sizes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_sizes is not None:
            result['DataDiskSizes'] = self.data_disk_sizes.to_map()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.support_resources_count is not None:
            result['SupportResourcesCount'] = self.support_resources_count
        if self.system_disk_sizes is not None:
            result['SystemDiskSizes'] = self.system_disk_sizes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSizes') is not None:
            temp_model = DescribeReservedResourceResponseBodySupportResourcesSupportResourceDataDiskSizes()
            self.data_disk_sizes = temp_model.from_map(m['DataDiskSizes'])
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('SupportResourcesCount') is not None:
            self.support_resources_count = m.get('SupportResourcesCount')
        if m.get('SystemDiskSizes') is not None:
            temp_model = DescribeReservedResourceResponseBodySupportResourcesSupportResourceSystemDiskSizes()
            self.system_disk_sizes = temp_model.from_map(m['SystemDiskSizes'])
        return self


class DescribeReservedResourceResponseBodySupportResources(TeaModel):
    def __init__(
        self,
        support_resource: List[DescribeReservedResourceResponseBodySupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k in m.get('SupportResource'):
                temp_model = DescribeReservedResourceResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        return self


class DescribeReservedResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        images: DescribeReservedResourceResponseBodyImages = None,
        request_id: str = None,
        support_resources: DescribeReservedResourceResponseBodySupportResources = None,
    ):
        self.code = code
        self.images = images
        self.request_id = request_id
        self.support_resources = support_resources

    def validate(self):
        if self.images:
            self.images.validate()
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Images') is not None:
            temp_model = DescribeReservedResourceResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportResources') is not None:
            temp_model = DescribeReservedResourceResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m['SupportResources'])
        return self


class DescribeReservedResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeReservedResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeReservedResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeSecurityGroupAttributeResponseBodyPermissionsPermission(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        dest_cidr_ip: str = None,
        direction: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.dest_cidr_ip = dest_cidr_ip
        self.direction = direction
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        return self


class DescribeSecurityGroupAttributeResponseBodyPermissions(TeaModel):
    def __init__(
        self,
        permission: List[DescribeSecurityGroupAttributeResponseBodyPermissionsPermission] = None,
    ):
        self.permission = permission

    def validate(self):
        if self.permission:
            for k in self.permission:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Permission'] = []
        if self.permission is not None:
            for k in self.permission:
                result['Permission'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permission = []
        if m.get('Permission') is not None:
            for k in m.get('Permission'):
                temp_model = DescribeSecurityGroupAttributeResponseBodyPermissionsPermission()
                self.permission.append(temp_model.from_map(k))
        return self


class DescribeSecurityGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        permissions: DescribeSecurityGroupAttributeResponseBodyPermissions = None,
        request_id: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        self.description = description
        self.permissions = permissions
        self.request_id = request_id
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name

    def validate(self):
        if self.permissions:
            self.permissions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.permissions is not None:
            result['Permissions'] = self.permissions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Permissions') is not None:
            temp_model = DescribeSecurityGroupAttributeResponseBodyPermissions()
            self.permissions = temp_model.from_map(m['Permissions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class DescribeSecurityGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_group_id: str = None,
        security_group_name: str = None,
        version: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        instance_count: int = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.instance_count = instance_count
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class DescribeSecurityGroupsResponseBodySecurityGroups(TeaModel):
    def __init__(
        self,
        security_group: List[DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup] = None,
    ):
        self.security_group = security_group

    def validate(self):
        if self.security_group:
            for k in self.security_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecurityGroup'] = []
        if self.security_group is not None:
            for k in self.security_group:
                result['SecurityGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_group = []
        if m.get('SecurityGroup') is not None:
            for k in m.get('SecurityGroup'):
                temp_model = DescribeSecurityGroupsResponseBodySecurityGroupsSecurityGroup()
                self.security_group.append(temp_model.from_map(k))
        return self


class DescribeSecurityGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        security_groups: DescribeSecurityGroupsResponseBodySecurityGroups = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.security_groups = security_groups
        self.total_count = total_count

    def validate(self):
        if self.security_groups:
            self.security_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroups') is not None:
            temp_model = DescribeSecurityGroupsResponseBodySecurityGroups()
            self.security_groups = temp_model.from_map(m['SecurityGroups'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServcieScheduleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        pod_config_name: str = None,
        uuid: str = None,
    ):
        self.app_id = app_id
        self.pod_config_name = pod_config_name
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pod_config_name is not None:
            result['PodConfigName'] = self.pod_config_name
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PodConfigName') is not None:
            self.pod_config_name = m.get('PodConfigName')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatusesContainerStatus(TeaModel):
    def __init__(
        self,
        container_id: str = None,
        name: str = None,
    ):
        self.container_id = container_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatuses(TeaModel):
    def __init__(
        self,
        container_status: List[DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatusesContainerStatus] = None,
    ):
        self.container_status = container_status

    def validate(self):
        if self.container_status:
            for k in self.container_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerStatus'] = []
        if self.container_status is not None:
            for k in self.container_status:
                result['ContainerStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_status = []
        if m.get('ContainerStatus') is not None:
            for k in m.get('ContainerStatus'):
                temp_model = DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatusesContainerStatus()
                self.container_status.append(temp_model.from_map(k))
        return self


class DescribeServcieScheduleResponseBodyPodAbstractInfo(TeaModel):
    def __init__(
        self,
        container_service: bool = None,
        container_statuses: DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatuses = None,
        name: bool = None,
        namespace: bool = None,
        resource_scope: bool = None,
        status: bool = None,
    ):
        self.container_service = container_service
        self.container_statuses = container_statuses
        self.name = name
        self.namespace = namespace
        self.resource_scope = resource_scope
        self.status = status

    def validate(self):
        if self.container_statuses:
            self.container_statuses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_service is not None:
            result['ContainerService'] = self.container_service
        if self.container_statuses is not None:
            result['ContainerStatuses'] = self.container_statuses.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.resource_scope is not None:
            result['ResourceScope'] = self.resource_scope
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerService') is not None:
            self.container_service = m.get('ContainerService')
        if m.get('ContainerStatuses') is not None:
            temp_model = DescribeServcieScheduleResponseBodyPodAbstractInfoContainerStatuses()
            self.container_statuses = temp_model.from_map(m['ContainerStatuses'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ResourceScope') is not None:
            self.resource_scope = m.get('ResourceScope')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeServcieScheduleResponseBody(TeaModel):
    def __init__(
        self,
        index: int = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_port: int = None,
        pod_abstract_info: DescribeServcieScheduleResponseBodyPodAbstractInfo = None,
        request_id: str = None,
        request_repeated: bool = None,
        tcp_ports: str = None,
    ):
        self.index = index
        self.instance_id = instance_id
        self.instance_ip = instance_ip
        self.instance_port = instance_port
        self.pod_abstract_info = pod_abstract_info
        self.request_id = request_id
        self.request_repeated = request_repeated
        self.tcp_ports = tcp_ports

    def validate(self):
        if self.pod_abstract_info:
            self.pod_abstract_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.pod_abstract_info is not None:
            result['PodAbstractInfo'] = self.pod_abstract_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_repeated is not None:
            result['RequestRepeated'] = self.request_repeated
        if self.tcp_ports is not None:
            result['TcpPorts'] = self.tcp_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('PodAbstractInfo') is not None:
            temp_model = DescribeServcieScheduleResponseBodyPodAbstractInfo()
            self.pod_abstract_info = temp_model.from_map(m['PodAbstractInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestRepeated') is not None:
            self.request_repeated = m.get('RequestRepeated')
        if m.get('TcpPorts') is not None:
            self.tcp_ports = m.get('TcpPorts')
        return self


class DescribeServcieScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServcieScheduleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServcieScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnatTableEntriesRequest(TeaModel):
    def __init__(
        self,
        nat_gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
        snat_entry_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        source_cidr: str = None,
    ):
        self.nat_gateway_id = nat_gateway_id
        self.page_number = page_number
        self.page_size = page_size
        self.snat_entry_id = snat_entry_id
        self.snat_entry_name = snat_entry_name
        self.snat_ip = snat_ip
        self.source_cidr = source_cidr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id
        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name
        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip
        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')
        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')
        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')
        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')
        return self


class DescribeSnatTableEntriesResponseBodySnatTableEntries(TeaModel):
    def __init__(
        self,
        nat_gateway_id: str = None,
        snat_entry_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        source_cidr: str = None,
        status: str = None,
    ):
        self.nat_gateway_id = nat_gateway_id
        self.snat_entry_id = snat_entry_id
        self.snat_entry_name = snat_entry_name
        self.snat_ip = snat_ip
        self.source_cidr = source_cidr
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id
        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name
        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip
        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')
        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')
        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')
        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSnatTableEntriesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snat_table_entries: List[DescribeSnatTableEntriesResponseBodySnatTableEntries] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.snat_table_entries = snat_table_entries
        self.total_count = total_count

    def validate(self):
        if self.snat_table_entries:
            for k in self.snat_table_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SnatTableEntries'] = []
        if self.snat_table_entries is not None:
            for k in self.snat_table_entries:
                result['SnatTableEntries'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snat_table_entries = []
        if m.get('SnatTableEntries') is not None:
            for k in m.get('SnatTableEntries'):
                temp_model = DescribeSnatTableEntriesResponseBodySnatTableEntries()
                self.snat_table_entries.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSnatTableEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSnatTableEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSnatTableEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBandWidthDataRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        isp: str = None,
        period: str = None,
        start_time: str = None,
        version: str = None,
    ):
        self.end_time = end_time
        self.ens_region_id = ens_region_id
        self.instance_id = instance_id
        self.isp = isp
        self.period = period
        self.start_time = start_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.period is not None:
            result['Period'] = self.period
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUserBandWidthDataResponseBodyMonitorDataBandWidthMonitorData(TeaModel):
    def __init__(
        self,
        down_band_width: int = None,
        internet_rx: int = None,
        internet_tx: int = None,
        time_stamp: str = None,
        up_band_width: int = None,
    ):
        self.down_band_width = down_band_width
        self.internet_rx = internet_rx
        self.internet_tx = internet_tx
        self.time_stamp = time_stamp
        self.up_band_width = up_band_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_band_width is not None:
            result['DownBandWidth'] = self.down_band_width
        if self.internet_rx is not None:
            result['InternetRX'] = self.internet_rx
        if self.internet_tx is not None:
            result['InternetTX'] = self.internet_tx
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.up_band_width is not None:
            result['UpBandWidth'] = self.up_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownBandWidth') is not None:
            self.down_band_width = m.get('DownBandWidth')
        if m.get('InternetRX') is not None:
            self.internet_rx = m.get('InternetRX')
        if m.get('InternetTX') is not None:
            self.internet_tx = m.get('InternetTX')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UpBandWidth') is not None:
            self.up_band_width = m.get('UpBandWidth')
        return self


class DescribeUserBandWidthDataResponseBodyMonitorData(TeaModel):
    def __init__(
        self,
        band_width_monitor_data: List[DescribeUserBandWidthDataResponseBodyMonitorDataBandWidthMonitorData] = None,
        max_down_band_width: str = None,
        max_up_band_width: str = None,
    ):
        self.band_width_monitor_data = band_width_monitor_data
        self.max_down_band_width = max_down_band_width
        self.max_up_band_width = max_up_band_width

    def validate(self):
        if self.band_width_monitor_data:
            for k in self.band_width_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BandWidthMonitorData'] = []
        if self.band_width_monitor_data is not None:
            for k in self.band_width_monitor_data:
                result['BandWidthMonitorData'].append(k.to_map() if k else None)
        if self.max_down_band_width is not None:
            result['MaxDownBandWidth'] = self.max_down_band_width
        if self.max_up_band_width is not None:
            result['MaxUpBandWidth'] = self.max_up_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_monitor_data = []
        if m.get('BandWidthMonitorData') is not None:
            for k in m.get('BandWidthMonitorData'):
                temp_model = DescribeUserBandWidthDataResponseBodyMonitorDataBandWidthMonitorData()
                self.band_width_monitor_data.append(temp_model.from_map(k))
        if m.get('MaxDownBandWidth') is not None:
            self.max_down_band_width = m.get('MaxDownBandWidth')
        if m.get('MaxUpBandWidth') is not None:
            self.max_up_band_width = m.get('MaxUpBandWidth')
        return self


class DescribeUserBandWidthDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        monitor_data: DescribeUserBandWidthDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        self.code = code
        self.monitor_data = monitor_data
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MonitorData') is not None:
            temp_model = DescribeUserBandWidthDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m['MonitorData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserBandWidthDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserBandWidthDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserBandWidthDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(
        self,
        ens_region_id: str = None,
        network_id: str = None,
        order_by_params: str = None,
        page_number: int = None,
        page_size: int = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        version: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.network_id = network_id
        self.order_by_params = order_by_params
        self.page_number = page_number
        self.page_size = page_size
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeVSwitchesResponseBodyVSwitchesVSwitch(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        created_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        free_ip_count: int = None,
        network_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.created_time = created_time
        self.description = description
        self.ens_region_id = ens_region_id
        self.free_ip_count = free_ip_count
        self.network_id = network_id
        self.status = status
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.free_ip_count is not None:
            result['FreeIpCount'] = self.free_ip_count
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('FreeIpCount') is not None:
            self.free_ip_count = m.get('FreeIpCount')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeVSwitchesResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        v_switch: List[DescribeVSwitchesResponseBodyVSwitchesVSwitch] = None,
    ):
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeVSwitchesResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeVSwitchesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        v_switches: DescribeVSwitchesResponseBodyVSwitches = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VSwitches') is not None:
            temp_model = DescribeVSwitchesResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVSwitchesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDiskRequest(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        instance_id: str = None,
    ):
        self.disk_id = disk_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DetachDiskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DistApplicationDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        data: str = None,
        dist_strategy: str = None,
    ):
        self.app_id = app_id
        self.data = data
        self.dist_strategy = dist_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.data is not None:
            result['Data'] = self.data
        if self.dist_strategy is not None:
            result['DistStrategy'] = self.dist_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DistStrategy') is not None:
            self.dist_strategy = m.get('DistStrategy')
        return self


class DistApplicationDataResponseBodyDistInstanceIds(TeaModel):
    def __init__(
        self,
        dist_instance_id: List[str] = None,
    ):
        self.dist_instance_id = dist_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dist_instance_id is not None:
            result['DistInstanceId'] = self.dist_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistInstanceId') is not None:
            self.dist_instance_id = m.get('DistInstanceId')
        return self


class DistApplicationDataResponseBodyDistResultsDistResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        result_code: int = None,
        result_descrip: str = None,
        version: str = None,
    ):
        self.name = name
        self.result_code = result_code
        self.result_descrip = result_descrip
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_descrip is not None:
            result['ResultDescrip'] = self.result_descrip
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultDescrip') is not None:
            self.result_descrip = m.get('ResultDescrip')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DistApplicationDataResponseBodyDistResults(TeaModel):
    def __init__(
        self,
        dist_result: List[DistApplicationDataResponseBodyDistResultsDistResult] = None,
    ):
        self.dist_result = dist_result

    def validate(self):
        if self.dist_result:
            for k in self.dist_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistResult'] = []
        if self.dist_result is not None:
            for k in self.dist_result:
                result['DistResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dist_result = []
        if m.get('DistResult') is not None:
            for k in m.get('DistResult'):
                temp_model = DistApplicationDataResponseBodyDistResultsDistResult()
                self.dist_result.append(temp_model.from_map(k))
        return self


class DistApplicationDataResponseBody(TeaModel):
    def __init__(
        self,
        dist_instance_ids: DistApplicationDataResponseBodyDistInstanceIds = None,
        dist_instance_total_count: int = None,
        dist_results: DistApplicationDataResponseBodyDistResults = None,
        request_id: str = None,
    ):
        self.dist_instance_ids = dist_instance_ids
        self.dist_instance_total_count = dist_instance_total_count
        self.dist_results = dist_results
        self.request_id = request_id

    def validate(self):
        if self.dist_instance_ids:
            self.dist_instance_ids.validate()
        if self.dist_results:
            self.dist_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dist_instance_ids is not None:
            result['DistInstanceIds'] = self.dist_instance_ids.to_map()
        if self.dist_instance_total_count is not None:
            result['DistInstanceTotalCount'] = self.dist_instance_total_count
        if self.dist_results is not None:
            result['DistResults'] = self.dist_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistInstanceIds') is not None:
            temp_model = DistApplicationDataResponseBodyDistInstanceIds()
            self.dist_instance_ids = temp_model.from_map(m['DistInstanceIds'])
        if m.get('DistInstanceTotalCount') is not None:
            self.dist_instance_total_count = m.get('DistInstanceTotalCount')
        if m.get('DistResults') is not None:
            temp_model = DistApplicationDataResponseBodyDistResults()
            self.dist_results = temp_model.from_map(m['DistResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DistApplicationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DistApplicationDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DistApplicationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportBillDetailDataRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        start_date: str = None,
    ):
        # 结束时间UTC格式
        self.end_date = end_date
        # 开始时间，UTC格式
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportBillDetailDataResponseBody(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        request_id: str = None,
    ):
        # 文件下载地址
        self.file_path = file_path
        # 请求ID，公共字段
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportBillDetailDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportBillDetailDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportBillDetailDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        ossbucket: str = None,
        ossprefix: str = None,
        ossregion_id: str = None,
        role_name: str = None,
    ):
        self.image_id = image_id
        self.ossbucket = ossbucket
        self.ossprefix = ossprefix
        self.ossregion_id = ossregion_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        if self.ossprefix is not None:
            result['OSSPrefix'] = self.ossprefix
        if self.ossregion_id is not None:
            result['OSSRegionId'] = self.ossregion_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        if m.get('OSSPrefix') is not None:
            self.ossprefix = m.get('OSSPrefix')
        if m.get('OSSRegionId') is not None:
            self.ossregion_id = m.get('OSSRegionId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ExportImageResponseBody(TeaModel):
    def __init__(
        self,
        exported_image_url: str = None,
        request_id: str = None,
    ):
        self.exported_image_url = exported_image_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exported_image_url is not None:
            result['ExportedImageURL'] = self.exported_image_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportedImageURL') is not None:
            self.exported_image_url = m.get('ExportedImageURL')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportMeasurementDataRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        start_date: str = None,
    ):
        # 结束时间，UTC格式
        self.end_date = end_date
        # 开始时间，UTC格式
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportMeasurementDataResponseBody(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        request_id: str = None,
    ):
        # 文件下载地址
        self.file_path = file_path
        # 请求ID，公共字段
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportMeasurementDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportMeasurementDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportMeasurementDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceInternetPortRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        nat_type: str = None,
        rule_id: str = None,
    ):
        # A short description of struct
        self.instance_id = instance_id
        self.nat_type = nat_type
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nat_type is not None:
            result['NatType'] = self.nat_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetDeviceInternetPortResponseBodyNetworkInfo(TeaModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        isp: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        status: str = None,
    ):
        self.external_ip = external_ip
        self.external_port = external_port
        self.isp = isp
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDeviceInternetPortResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        network_info: List[GetDeviceInternetPortResponseBodyNetworkInfo] = None,
        request_id: str = None,
    ):
        # InstanceId
        self.instance_id = instance_id
        self.network_info = network_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.network_info:
            for k in self.network_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['NetworkInfo'] = []
        if self.network_info is not None:
            for k in self.network_info:
                result['NetworkInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.network_info = []
        if m.get('NetworkInfo') is not None:
            for k in m.get('NetworkInfo'):
                temp_model = GetDeviceInternetPortResponseBodyNetworkInfo()
                self.network_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceInternetPortResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceInternetPortResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceInternetPortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeyPairRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        public_key_body: str = None,
        version: str = None,
    ):
        self.key_pair_name = key_pair_name
        self.public_key_body = public_key_body
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.public_key_body is not None:
            result['PublicKeyBody'] = self.public_key_body
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PublicKeyBody') is not None:
            self.public_key_body = m.get('PublicKeyBody')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ImportKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        key_pair_finger_print: str = None,
        key_pair_name: str = None,
        request_id: str = None,
    ):
        self.key_pair_finger_print = key_pair_finger_print
        self.key_pair_name = key_pair_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinPublicIpsToEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        instance_infos: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.instance_infos = instance_infos

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('InstanceInfos') is not None:
            self.instance_infos = m.get('InstanceInfos')
        return self


class JoinPublicIpsToEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinPublicIpsToEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinPublicIpsToEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = JoinPublicIpsToEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_group_id: str = None,
        version: str = None,
    ):
        self.instance_id = instance_id
        self.security_group_id = security_group_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class JoinSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = JoinSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinVSwitchesToEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        v_switches_info: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.v_switches_info = v_switches_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.v_switches_info is not None:
            result['VSwitchesInfo'] = self.v_switches_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('VSwitchesInfo') is not None:
            self.v_switches_info = m.get('VSwitchesInfo')
        return self


class JoinVSwitchesToEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinVSwitchesToEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinVSwitchesToEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = JoinVSwitchesToEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LeaveSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_group_id: str = None,
        version: str = None,
    ):
        self.instance_id = instance_id
        self.security_group_id = security_group_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class LeaveSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LeaveSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LeaveSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LeaveSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(
        self,
        app_versions: str = None,
        cluster_names: str = None,
        level: str = None,
        max_date: str = None,
        min_date: str = None,
        out_app_info_params: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_versions = app_versions
        self.cluster_names = cluster_names
        self.level = level
        self.max_date = max_date
        self.min_date = min_date
        self.out_app_info_params = out_app_info_params
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_versions is not None:
            result['AppVersions'] = self.app_versions
        if self.cluster_names is not None:
            result['ClusterNames'] = self.cluster_names
        if self.level is not None:
            result['Level'] = self.level
        if self.max_date is not None:
            result['MaxDate'] = self.max_date
        if self.min_date is not None:
            result['MinDate'] = self.min_date
        if self.out_app_info_params is not None:
            result['OutAppInfoParams'] = self.out_app_info_params
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersions') is not None:
            self.app_versions = m.get('AppVersions')
        if m.get('ClusterNames') is not None:
            self.cluster_names = m.get('ClusterNames')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')
        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')
        if m.get('OutAppInfoParams') is not None:
            self.out_app_info_params = m.get('OutAppInfoParams')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListApplicationsResponseBodyApplicationsApplicationAppListApp(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_info: str = None,
    ):
        self.app_id = app_id
        self.app_info = app_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_info is not None:
            result['AppInfo'] = self.app_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInfo') is not None:
            self.app_info = m.get('AppInfo')
        return self


class ListApplicationsResponseBodyApplicationsApplicationAppList(TeaModel):
    def __init__(
        self,
        app: List[ListApplicationsResponseBodyApplicationsApplicationAppListApp] = None,
    ):
        self.app = app

    def validate(self):
        if self.app:
            for k in self.app:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['App'] = []
        if self.app is not None:
            for k in self.app:
                result['App'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app = []
        if m.get('App') is not None:
            for k in m.get('App'):
                temp_model = ListApplicationsResponseBodyApplicationsApplicationAppListApp()
                self.app.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBodyApplicationsApplication(TeaModel):
    def __init__(
        self,
        app_list: ListApplicationsResponseBodyApplicationsApplicationAppList = None,
        cluster_name: str = None,
    ):
        self.app_list = app_list
        self.cluster_name = cluster_name

    def validate(self):
        if self.app_list:
            self.app_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_list is not None:
            result['AppList'] = self.app_list.to_map()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppList') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationAppList()
            self.app_list = temp_model.from_map(m['AppList'])
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class ListApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application: List[ListApplicationsResponseBodyApplicationsApplication] = None,
    ):
        self.application = application

    def validate(self):
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = ListApplicationsResponseBodyApplicationsApplication()
                self.application.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        applications: ListApplicationsResponseBodyApplications = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.applications = applications
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Applications') is not None:
            temp_model = ListApplicationsResponseBodyApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEnsEipAddressAttributeRequest(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        bandwidth: int = None,
        description: str = None,
        name: str = None,
    ):
        self.allocation_id = allocation_id
        self.bandwidth = bandwidth
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyEnsEipAddressAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyEnsEipAddressAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyEnsEipAddressAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyEnsEipAddressAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        epninstance_name: str = None,
        internet_max_bandwidth_out: int = None,
        networking_model: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.epninstance_name = epninstance_name
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.networking_model = networking_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')
        return self


class ModifyEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageAttributeRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        version: str = None,
        product: str = None,
    ):
        self.image_id = image_id
        self.image_name = image_name
        self.version = version
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.version is not None:
            result['Version'] = self.version
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class ModifyImageAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyImageAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyImageAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyImageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageSharePermissionRequest(TeaModel):
    def __init__(
        self,
        add_accounts: str = None,
        image_id: str = None,
        remove_accounts: str = None,
    ):
        self.add_accounts = add_accounts
        self.image_id = image_id
        self.remove_accounts = remove_accounts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_accounts is not None:
            result['AddAccounts'] = self.add_accounts
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.remove_accounts is not None:
            result['RemoveAccounts'] = self.remove_accounts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccounts') is not None:
            self.add_accounts = m.get('AddAccounts')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RemoveAccounts') is not None:
            self.remove_accounts = m.get('RemoveAccounts')
        return self


class ModifyImageSharePermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyImageSharePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyImageSharePermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyImageSharePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        password: str = None,
        version: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.password = password
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.password is not None:
            result['Password'] = self.password
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        auto_renew: str = None,
        duration: str = None,
        instance_ids: str = None,
        owner_id: str = None,
        renewal_status: str = None,
    ):
        self.auto_renew = auto_renew
        self.duration = duration
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        self.renewal_status = renewal_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class ModifyInstanceAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAutoRenewAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLoadBalancerAttributeRequest(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        return self


class ModifyLoadBalancerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyLoadBalancerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLoadBalancerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyLoadBalancerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        network_id: str = None,
        network_name: str = None,
    ):
        self.description = description
        self.network_id = network_id
        self.network_name = network_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.network_name is not None:
            result['NetworkName'] = self.network_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')
        return self


class ModifyNetworkAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNetworkAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyNetworkAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNetworkAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPrepayInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        # 变配实例id
        self.instance_id = instance_id
        # 更新的配置
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ModifyPrepayInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPrepayInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPrepayInstanceSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPrepayInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        self.description = description
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class ModifySecurityGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySecurityGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecurityGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySecurityGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVSwitchAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        self.description = description
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class ModifyVSwitchAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVSwitchAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVSwitchAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyVSwitchAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreCreateEnsServiceRequest(TeaModel):
    def __init__(
        self,
        bandwidth_type: str = None,
        buy_resources_detail: str = None,
        data_disk_size: str = None,
        ens_service_name: str = None,
        image_id: str = None,
        instance_bandwithd_limit: str = None,
        instance_spec: str = None,
        key_pair_name: str = None,
        net_level: str = None,
        password: str = None,
        scheduling_price_strategy: str = None,
        scheduling_strategy: str = None,
        system_disk_size: str = None,
        user_data: str = None,
        version: str = None,
    ):
        self.bandwidth_type = bandwidth_type
        self.buy_resources_detail = buy_resources_detail
        self.data_disk_size = data_disk_size
        self.ens_service_name = ens_service_name
        self.image_id = image_id
        self.instance_bandwithd_limit = instance_bandwithd_limit
        self.instance_spec = instance_spec
        self.key_pair_name = key_pair_name
        self.net_level = net_level
        self.password = password
        self.scheduling_price_strategy = scheduling_price_strategy
        self.scheduling_strategy = scheduling_strategy
        self.system_disk_size = system_disk_size
        self.user_data = user_data
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.buy_resources_detail is not None:
            result['BuyResourcesDetail'] = self.buy_resources_detail
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.ens_service_name is not None:
            result['EnsServiceName'] = self.ens_service_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_bandwithd_limit is not None:
            result['InstanceBandwithdLimit'] = self.instance_bandwithd_limit
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.net_level is not None:
            result['NetLevel'] = self.net_level
        if self.password is not None:
            result['Password'] = self.password
        if self.scheduling_price_strategy is not None:
            result['SchedulingPriceStrategy'] = self.scheduling_price_strategy
        if self.scheduling_strategy is not None:
            result['SchedulingStrategy'] = self.scheduling_strategy
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('BuyResourcesDetail') is not None:
            self.buy_resources_detail = m.get('BuyResourcesDetail')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('EnsServiceName') is not None:
            self.ens_service_name = m.get('EnsServiceName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceBandwithdLimit') is not None:
            self.instance_bandwithd_limit = m.get('InstanceBandwithdLimit')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('NetLevel') is not None:
            self.net_level = m.get('NetLevel')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SchedulingPriceStrategy') is not None:
            self.scheduling_price_strategy = m.get('SchedulingPriceStrategy')
        if m.get('SchedulingStrategy') is not None:
            self.scheduling_strategy = m.get('SchedulingStrategy')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PreCreateEnsServiceResponseBody(TeaModel):
    def __init__(
        self,
        buy_resources_detail: str = None,
        code: int = None,
        ens_service_id: str = None,
        net_level: str = None,
        request_id: str = None,
    ):
        self.buy_resources_detail = buy_resources_detail
        self.code = code
        self.ens_service_id = ens_service_id
        self.net_level = net_level
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_resources_detail is not None:
            result['BuyResourcesDetail'] = self.buy_resources_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.ens_service_id is not None:
            result['EnsServiceId'] = self.ens_service_id
        if self.net_level is not None:
            result['NetLevel'] = self.net_level
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyResourcesDetail') is not None:
            self.buy_resources_detail = m.get('BuyResourcesDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnsServiceId') is not None:
            self.ens_service_id = m.get('EnsServiceId')
        if m.get('NetLevel') is not None:
            self.net_level = m.get('NetLevel')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PreCreateEnsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PreCreateEnsServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PreCreateEnsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushApplicationDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        data: str = None,
        push_strategy: str = None,
        timeout: int = None,
    ):
        self.app_id = app_id
        self.data = data
        self.push_strategy = push_strategy
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.data is not None:
            result['Data'] = self.data
        if self.push_strategy is not None:
            result['PushStrategy'] = self.push_strategy
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PushStrategy') is not None:
            self.push_strategy = m.get('PushStrategy')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class PushApplicationDataResponseBodyPushResultsPushResult(TeaModel):
    def __init__(
        self,
        name: str = None,
        result_code: int = None,
        result_descrip: str = None,
        version: str = None,
    ):
        self.name = name
        self.result_code = result_code
        self.result_descrip = result_descrip
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_descrip is not None:
            result['ResultDescrip'] = self.result_descrip
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultDescrip') is not None:
            self.result_descrip = m.get('ResultDescrip')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PushApplicationDataResponseBodyPushResults(TeaModel):
    def __init__(
        self,
        push_result: List[PushApplicationDataResponseBodyPushResultsPushResult] = None,
    ):
        self.push_result = push_result

    def validate(self):
        if self.push_result:
            for k in self.push_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PushResult'] = []
        if self.push_result is not None:
            for k in self.push_result:
                result['PushResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_result = []
        if m.get('PushResult') is not None:
            for k in m.get('PushResult'):
                temp_model = PushApplicationDataResponseBodyPushResultsPushResult()
                self.push_result.append(temp_model.from_map(k))
        return self


class PushApplicationDataResponseBody(TeaModel):
    def __init__(
        self,
        push_results: PushApplicationDataResponseBodyPushResults = None,
        request_id: str = None,
    ):
        self.push_results = push_results
        self.request_id = request_id

    def validate(self):
        if self.push_results:
            self.push_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_results is not None:
            result['PushResults'] = self.push_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushResults') is not None:
            temp_model = PushApplicationDataResponseBodyPushResults()
            self.push_results = temp_model.from_map(m['PushResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushApplicationDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushApplicationDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PushApplicationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReInitDiskRequest(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        image_id: str = None,
        version: str = None,
    ):
        self.disk_id = disk_id
        self.image_id = image_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ReInitDiskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReInitDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReInitDiskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReInitDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootInstanceRequest(TeaModel):
    def __init__(
        self,
        force_stop: str = None,
        instance_id: str = None,
        version: str = None,
    ):
        self.force_stop = force_stop
        self.instance_id = instance_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class RebootInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RebootInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebootInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # 实例id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleaseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePostPaidInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        version: str = None,
    ):
        self.instance_id = instance_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ReleasePostPaidInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleasePostPaidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleasePostPaidInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleasePostPaidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePrePaidInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        version: str = None,
    ):
        self.instance_id = instance_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ReleasePrePaidInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleasePrePaidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleasePrePaidInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleasePrePaidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveBackendServersRequestBackendServers(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.ip = ip
        # 端口
        self.port = port
        self.server_id = server_id
        # 后端服务器类型。  ens：ENS实例（默认）
        self.type = type
        # 后端服务器的权重。  取值：0~100  默认值为100，如果值为0，则不会将请求转发给该后端服务器。
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class RemoveBackendServersRequest(TeaModel):
    def __init__(
        self,
        backend_servers: List[RemoveBackendServersRequestBackendServers] = None,
        load_balancer_id: str = None,
    ):
        self.backend_servers = backend_servers
        self.load_balancer_id = load_balancer_id

    def validate(self):
        if self.backend_servers:
            for k in self.backend_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackendServers'] = []
        if self.backend_servers is not None:
            for k in self.backend_servers:
                result['BackendServers'].append(k.to_map() if k else None)
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_servers = []
        if m.get('BackendServers') is not None:
            for k in m.get('BackendServers'):
                temp_model = RemoveBackendServersRequestBackendServers()
                self.backend_servers.append(temp_model.from_map(k))
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class RemoveBackendServersShrinkRequest(TeaModel):
    def __init__(
        self,
        backend_servers_shrink: str = None,
        load_balancer_id: str = None,
    ):
        self.backend_servers_shrink = backend_servers_shrink
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_servers_shrink is not None:
            result['BackendServers'] = self.backend_servers_shrink
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            self.backend_servers_shrink = m.get('BackendServers')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class RemoveBackendServersResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.ip = ip
        self.port = port
        self.server_id = server_id
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class RemoveBackendServersResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[RemoveBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = RemoveBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class RemoveBackendServersResponseBody(TeaModel):
    def __init__(
        self,
        backend_servers: RemoveBackendServersResponseBodyBackendServers = None,
        request_id: str = None,
    ):
        self.backend_servers = backend_servers
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            temp_model = RemoveBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveBackendServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveBackendServersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveBackendServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemovePublicIpsFromEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        instance_infos: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.instance_infos = instance_infos

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('InstanceInfos') is not None:
            self.instance_infos = m.get('InstanceInfos')
        return self


class RemovePublicIpsFromEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemovePublicIpsFromEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemovePublicIpsFromEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemovePublicIpsFromEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveVSwitchesFromEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
        v_switches_info: str = None,
    ):
        self.epninstance_id = epninstance_id
        self.v_switches_info = v_switches_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        if self.v_switches_info is not None:
            result['VSwitchesInfo'] = self.v_switches_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        if m.get('VSwitchesInfo') is not None:
            self.v_switches_info = m.get('VSwitchesInfo')
        return self


class RemoveVSwitchesFromEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveVSwitchesFromEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveVSwitchesFromEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveVSwitchesFromEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        period: int = None,
    ):
        # 需要续费的实例ID。
        self.instance_id = instance_id
        # 包年包月续费时长。
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period is not None:
            result['Period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RescaleApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        rescale_level: str = None,
        rescale_type: str = None,
        resource_selector: str = None,
        timeout: int = None,
        to_app_version: str = None,
    ):
        self.app_id = app_id
        self.rescale_level = rescale_level
        self.rescale_type = rescale_type
        self.resource_selector = resource_selector
        self.timeout = timeout
        self.to_app_version = to_app_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.rescale_level is not None:
            result['RescaleLevel'] = self.rescale_level
        if self.rescale_type is not None:
            result['RescaleType'] = self.rescale_type
        if self.resource_selector is not None:
            result['ResourceSelector'] = self.resource_selector
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.to_app_version is not None:
            result['ToAppVersion'] = self.to_app_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RescaleLevel') is not None:
            self.rescale_level = m.get('RescaleLevel')
        if m.get('RescaleType') is not None:
            self.rescale_type = m.get('RescaleType')
        if m.get('ResourceSelector') is not None:
            self.resource_selector = m.get('ResourceSelector')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('ToAppVersion') is not None:
            self.to_app_version = m.get('ToAppVersion')
        return self


class RescaleApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RescaleApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RescaleApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RescaleApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RescaleDeviceServiceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        image_id: str = None,
        ip_type: int = None,
        rescale_level: str = None,
        rescale_type: str = None,
        resource_info: str = None,
        resource_selector: str = None,
        resource_spec: str = None,
        service_id: str = None,
        timeout: int = None,
    ):
        self.app_id = app_id
        self.image_id = image_id
        self.ip_type = ip_type
        self.rescale_level = rescale_level
        self.rescale_type = rescale_type
        self.resource_info = resource_info
        self.resource_selector = resource_selector
        self.resource_spec = resource_spec
        self.service_id = service_id
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.rescale_level is not None:
            result['RescaleLevel'] = self.rescale_level
        if self.rescale_type is not None:
            result['RescaleType'] = self.rescale_type
        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info
        if self.resource_selector is not None:
            result['ResourceSelector'] = self.resource_selector
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('RescaleLevel') is not None:
            self.rescale_level = m.get('RescaleLevel')
        if m.get('RescaleType') is not None:
            self.rescale_type = m.get('RescaleType')
        if m.get('ResourceInfo') is not None:
            self.resource_info = m.get('ResourceInfo')
        if m.get('ResourceSelector') is not None:
            self.resource_selector = m.get('ResourceSelector')
        if m.get('ResourceSpec') is not None:
            self.resource_spec = m.get('ResourceSpec')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class RescaleDeviceServiceResponseBodyResourceDetailInfos(TeaModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        isp: str = None,
        mac: str = None,
        region_id: str = None,
        server: str = None,
        status: str = None,
        type: str = None,
    ):
        self.id = id
        self.ip = ip
        self.isp = isp
        self.mac = mac
        self.region_id = region_id
        self.server = server
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['ID'] = self.id
        if self.ip is not None:
            result['IP'] = self.ip
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        if self.server is not None:
            result['Server'] = self.server
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RescaleDeviceServiceResponseBody(TeaModel):
    def __init__(
        self,
        device_ids: List[str] = None,
        order_id: str = None,
        request_id: str = None,
        resource_detail_infos: List[RescaleDeviceServiceResponseBodyResourceDetailInfos] = None,
    ):
        self.device_ids = device_ids
        self.order_id = order_id
        # Id of the request
        self.request_id = request_id
        self.resource_detail_infos = resource_detail_infos

    def validate(self):
        if self.resource_detail_infos:
            for k in self.resource_detail_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceDetailInfos'] = []
        if self.resource_detail_infos is not None:
            for k in self.resource_detail_infos:
                result['ResourceDetailInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_detail_infos = []
        if m.get('ResourceDetailInfos') is not None:
            for k in m.get('ResourceDetailInfos'):
                temp_model = RescaleDeviceServiceResponseBodyResourceDetailInfos()
                self.resource_detail_infos.append(temp_model.from_map(k))
        return self


class RescaleDeviceServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RescaleDeviceServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RescaleDeviceServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDeviceInstanceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        image_id: str = None,
        instance_id: str = None,
    ):
        # A short description of struct
        self.app_id = app_id
        self.image_id = image_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ResetDeviceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetDeviceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetDeviceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetDeviceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDeviceInstanceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        instance_id: str = None,
    ):
        # App ID
        self.app_id = app_id
        # Instance ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RestartDeviceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartDeviceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartDeviceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartDeviceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        security_group_id: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
        version: str = None,
    ):
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.security_group_id = security_group_id
        self.source_cidr_ip = source_cidr_ip
        self.source_port_range = source_port_range
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class RevokeSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokeSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RevokeSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeSecurityGroupEgressRequest(TeaModel):
    def __init__(
        self,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        security_group_id: str = None,
        source_port_range: str = None,
        version: str = None,
    ):
        self.dest_cidr_ip = dest_cidr_ip
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.security_group_id = security_group_id
        self.source_port_range = source_port_range
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class RevokeSecurityGroupEgressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeSecurityGroupEgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokeSecurityGroupEgressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RevokeSecurityGroupEgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        from_app_version: str = None,
        timeout: int = None,
        to_app_version: str = None,
    ):
        self.app_id = app_id
        self.from_app_version = from_app_version
        self.timeout = timeout
        self.to_app_version = to_app_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.from_app_version is not None:
            result['FromAppVersion'] = self.from_app_version
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.to_app_version is not None:
            result['ToAppVersion'] = self.to_app_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('FromAppVersion') is not None:
            self.from_app_version = m.get('FromAppVersion')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('ToAppVersion') is not None:
            self.to_app_version = m.get('ToAppVersion')
        return self


class RollbackApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RollbackApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollbackApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RollbackApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunInstancesRequestDataDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        size: int = None,
    ):
        self.category = category
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class RunInstancesRequestSystemDisk(TeaModel):
    def __init__(
        self,
        size: int = None,
    ):
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class RunInstancesRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_renew: bool = None,
        carrier: str = None,
        data_disk: List[RunInstancesRequestDataDisk] = None,
        ens_region_id: str = None,
        host_name: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        key_pair_name: str = None,
        net_district_code: str = None,
        net_work_id: str = None,
        password: str = None,
        period: int = None,
        period_unit: str = None,
        private_ip_address: str = None,
        schedule_area_level: str = None,
        scheduling_price_strategy: str = None,
        scheduling_strategy: str = None,
        security_id: str = None,
        system_disk: RunInstancesRequestSystemDisk = None,
        unique_suffix: bool = None,
        user_data: str = None,
        v_switch_id: str = None,
    ):
        # 数量
        self.amount = amount
        # 是否自动续费，默认为false
        self.auto_renew = auto_renew
        # 运营商
        self.carrier = carrier
        # 数据盘规格
        self.data_disk = data_disk
        # 节点id
        self.ens_region_id = ens_region_id
        # 主机名称
        self.host_name = host_name
        # 镜像id
        self.image_id = image_id
        # 实例付费方式，PrePaid:预付费，包年包月 PostPaid:按量付费
        self.instance_charge_type = instance_charge_type
        # 实例名称。长度为2~128个字符，必须以大小字母或中文开头，不能以http://和https://开头。可以包含中文、英文、数字、半角冒号（:）、下划线（_）、点号（.）或者连字符（-）。默认值为实例的InstanceId
        self.instance_name = instance_name
        # 实例规格
        self.instance_type = instance_type
        # 带宽计费方式
        self.internet_charge_type = internet_charge_type
        # 公网最大带宽，如果参数InternetMaxBandwidthOut的值大于0，则自动为实例分配公网IP。
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # 密钥对名称
        self.key_pair_name = key_pair_name
        # 地区code
        self.net_district_code = net_district_code
        # 网络id
        self.net_work_id = net_work_id
        # 实例密码
        self.password = password
        # 购买资源的时长，单位为：月
        self.period = period
        # 查询云服务器ENS不同计费周期的价格。取值范围：
        # Month（默认）：按月计费的价格单位。
        # Day：按天计费的价格单位。
        self.period_unit = period_unit
        # 私网ip
        self.private_ip_address = private_ip_address
        # 调度层级
        self.schedule_area_level = schedule_area_level
        # 调度价格策略
        self.scheduling_price_strategy = scheduling_price_strategy
        # 调度策略
        self.scheduling_strategy = scheduling_strategy
        # 安全组id
        self.security_id = security_id
        # 系统盘规格
        self.system_disk = system_disk
        # 是否为HostName和InstanceName添加有序后缀，有序后缀从001开始递增，最大不能超过999
        self.unique_suffix = unique_suffix
        # 用户自定义数据，最大支持16KB 您可传入UserData信息。UserData以Base64的方式编码
        self.user_data = user_data
        # 交换机id
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        if self.net_work_id is not None:
            result['NetWorkId'] = self.net_work_id
        if self.password is not None:
            result['Password'] = self.password
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.schedule_area_level is not None:
            result['ScheduleAreaLevel'] = self.schedule_area_level
        if self.scheduling_price_strategy is not None:
            result['SchedulingPriceStrategy'] = self.scheduling_price_strategy
        if self.scheduling_strategy is not None:
            result['SchedulingStrategy'] = self.scheduling_strategy
        if self.security_id is not None:
            result['SecurityId'] = self.security_id
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.unique_suffix is not None:
            result['UniqueSuffix'] = self.unique_suffix
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k in m.get('DataDisk'):
                temp_model = RunInstancesRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        if m.get('NetWorkId') is not None:
            self.net_work_id = m.get('NetWorkId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('ScheduleAreaLevel') is not None:
            self.schedule_area_level = m.get('ScheduleAreaLevel')
        if m.get('SchedulingPriceStrategy') is not None:
            self.scheduling_price_strategy = m.get('SchedulingPriceStrategy')
        if m.get('SchedulingStrategy') is not None:
            self.scheduling_strategy = m.get('SchedulingStrategy')
        if m.get('SecurityId') is not None:
            self.security_id = m.get('SecurityId')
        if m.get('SystemDisk') is not None:
            temp_model = RunInstancesRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('UniqueSuffix') is not None:
            self.unique_suffix = m.get('UniqueSuffix')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class RunInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_renew: bool = None,
        carrier: str = None,
        data_disk_shrink: str = None,
        ens_region_id: str = None,
        host_name: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        key_pair_name: str = None,
        net_district_code: str = None,
        net_work_id: str = None,
        password: str = None,
        period: int = None,
        period_unit: str = None,
        private_ip_address: str = None,
        schedule_area_level: str = None,
        scheduling_price_strategy: str = None,
        scheduling_strategy: str = None,
        security_id: str = None,
        system_disk_shrink: str = None,
        unique_suffix: bool = None,
        user_data: str = None,
        v_switch_id: str = None,
    ):
        # 数量
        self.amount = amount
        # 是否自动续费，默认为false
        self.auto_renew = auto_renew
        # 运营商
        self.carrier = carrier
        # 数据盘规格
        self.data_disk_shrink = data_disk_shrink
        # 节点id
        self.ens_region_id = ens_region_id
        # 主机名称
        self.host_name = host_name
        # 镜像id
        self.image_id = image_id
        # 实例付费方式，PrePaid:预付费，包年包月 PostPaid:按量付费
        self.instance_charge_type = instance_charge_type
        # 实例名称。长度为2~128个字符，必须以大小字母或中文开头，不能以http://和https://开头。可以包含中文、英文、数字、半角冒号（:）、下划线（_）、点号（.）或者连字符（-）。默认值为实例的InstanceId
        self.instance_name = instance_name
        # 实例规格
        self.instance_type = instance_type
        # 带宽计费方式
        self.internet_charge_type = internet_charge_type
        # 公网最大带宽，如果参数InternetMaxBandwidthOut的值大于0，则自动为实例分配公网IP。
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # 密钥对名称
        self.key_pair_name = key_pair_name
        # 地区code
        self.net_district_code = net_district_code
        # 网络id
        self.net_work_id = net_work_id
        # 实例密码
        self.password = password
        # 购买资源的时长，单位为：月
        self.period = period
        # 查询云服务器ENS不同计费周期的价格。取值范围：
        # Month（默认）：按月计费的价格单位。
        # Day：按天计费的价格单位。
        self.period_unit = period_unit
        # 私网ip
        self.private_ip_address = private_ip_address
        # 调度层级
        self.schedule_area_level = schedule_area_level
        # 调度价格策略
        self.scheduling_price_strategy = scheduling_price_strategy
        # 调度策略
        self.scheduling_strategy = scheduling_strategy
        # 安全组id
        self.security_id = security_id
        # 系统盘规格
        self.system_disk_shrink = system_disk_shrink
        # 是否为HostName和InstanceName添加有序后缀，有序后缀从001开始递增，最大不能超过999
        self.unique_suffix = unique_suffix
        # 用户自定义数据，最大支持16KB 您可传入UserData信息。UserData以Base64的方式编码
        self.user_data = user_data
        # 交换机id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.data_disk_shrink is not None:
            result['DataDisk'] = self.data_disk_shrink
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code
        if self.net_work_id is not None:
            result['NetWorkId'] = self.net_work_id
        if self.password is not None:
            result['Password'] = self.password
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.schedule_area_level is not None:
            result['ScheduleAreaLevel'] = self.schedule_area_level
        if self.scheduling_price_strategy is not None:
            result['SchedulingPriceStrategy'] = self.scheduling_price_strategy
        if self.scheduling_strategy is not None:
            result['SchedulingStrategy'] = self.scheduling_strategy
        if self.security_id is not None:
            result['SecurityId'] = self.security_id
        if self.system_disk_shrink is not None:
            result['SystemDisk'] = self.system_disk_shrink
        if self.unique_suffix is not None:
            result['UniqueSuffix'] = self.unique_suffix
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('DataDisk') is not None:
            self.data_disk_shrink = m.get('DataDisk')
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')
        if m.get('NetWorkId') is not None:
            self.net_work_id = m.get('NetWorkId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('ScheduleAreaLevel') is not None:
            self.schedule_area_level = m.get('ScheduleAreaLevel')
        if m.get('SchedulingPriceStrategy') is not None:
            self.scheduling_price_strategy = m.get('SchedulingPriceStrategy')
        if m.get('SchedulingStrategy') is not None:
            self.scheduling_strategy = m.get('SchedulingStrategy')
        if m.get('SecurityId') is not None:
            self.security_id = m.get('SecurityId')
        if m.get('SystemDisk') is not None:
            self.system_disk_shrink = m.get('SystemDisk')
        if m.get('UniqueSuffix') is not None:
            self.unique_suffix = m.get('UniqueSuffix')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class RunInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunServiceScheduleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        client_ip: str = None,
        directorys: str = None,
        pod_config_name: str = None,
        pre_locked_timeout: int = None,
        schedule_strategy: str = None,
        service_action: str = None,
        service_commands: str = None,
        uuid: str = None,
    ):
        self.app_id = app_id
        self.client_ip = client_ip
        self.directorys = directorys
        self.pod_config_name = pod_config_name
        self.pre_locked_timeout = pre_locked_timeout
        self.schedule_strategy = schedule_strategy
        self.service_action = service_action
        self.service_commands = service_commands
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.directorys is not None:
            result['Directorys'] = self.directorys
        if self.pod_config_name is not None:
            result['PodConfigName'] = self.pod_config_name
        if self.pre_locked_timeout is not None:
            result['PreLockedTimeout'] = self.pre_locked_timeout
        if self.schedule_strategy is not None:
            result['ScheduleStrategy'] = self.schedule_strategy
        if self.service_action is not None:
            result['ServiceAction'] = self.service_action
        if self.service_commands is not None:
            result['ServiceCommands'] = self.service_commands
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Directorys') is not None:
            self.directorys = m.get('Directorys')
        if m.get('PodConfigName') is not None:
            self.pod_config_name = m.get('PodConfigName')
        if m.get('PreLockedTimeout') is not None:
            self.pre_locked_timeout = m.get('PreLockedTimeout')
        if m.get('ScheduleStrategy') is not None:
            self.schedule_strategy = m.get('ScheduleStrategy')
        if m.get('ServiceAction') is not None:
            self.service_action = m.get('ServiceAction')
        if m.get('ServiceCommands') is not None:
            self.service_commands = m.get('ServiceCommands')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class RunServiceScheduleResponseBodyCommandResultsCommandResult(TeaModel):
    def __init__(
        self,
        command: str = None,
        container_name: str = None,
        result_msg: str = None,
    ):
        self.command = command
        self.container_name = container_name
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        return self


class RunServiceScheduleResponseBodyCommandResults(TeaModel):
    def __init__(
        self,
        command_result: List[RunServiceScheduleResponseBodyCommandResultsCommandResult] = None,
    ):
        self.command_result = command_result

    def validate(self):
        if self.command_result:
            for k in self.command_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommandResult'] = []
        if self.command_result is not None:
            for k in self.command_result:
                result['CommandResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.command_result = []
        if m.get('CommandResult') is not None:
            for k in m.get('CommandResult'):
                temp_model = RunServiceScheduleResponseBodyCommandResultsCommandResult()
                self.command_result.append(temp_model.from_map(k))
        return self


class RunServiceScheduleResponseBody(TeaModel):
    def __init__(
        self,
        command_results: RunServiceScheduleResponseBodyCommandResults = None,
        index: int = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_port: int = None,
        request_id: str = None,
        request_repeated: str = None,
        tcp_ports: bool = None,
    ):
        self.command_results = command_results
        self.index = index
        self.instance_id = instance_id
        self.instance_ip = instance_ip
        self.instance_port = instance_port
        self.request_id = request_id
        self.request_repeated = request_repeated
        self.tcp_ports = tcp_ports

    def validate(self):
        if self.command_results:
            self.command_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_results is not None:
            result['CommandResults'] = self.command_results.to_map()
        if self.index is not None:
            result['Index'] = self.index
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_repeated is not None:
            result['RequestRepeated'] = self.request_repeated
        if self.tcp_ports is not None:
            result['TcpPorts'] = self.tcp_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandResults') is not None:
            temp_model = RunServiceScheduleResponseBodyCommandResults()
            self.command_results = temp_model.from_map(m['CommandResults'])
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestRepeated') is not None:
            self.request_repeated = m.get('RequestRepeated')
        if m.get('TcpPorts') is not None:
            self.tcp_ports = m.get('TcpPorts')
        return self


class RunServiceScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunServiceScheduleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunServiceScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetBackendServersRequestBackendServers(TeaModel):
    def __init__(
        self,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.server_id = server_id
        # 后端服务器类型。  ens：ENS实例（默认）
        self.type = type
        # 后端服务器的权重。  取值：0~100  默认值为100，如果值为0，则不会将请求转发给该后端服务器。
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SetBackendServersRequest(TeaModel):
    def __init__(
        self,
        backend_servers: List[SetBackendServersRequestBackendServers] = None,
        load_balancer_id: str = None,
    ):
        self.backend_servers = backend_servers
        self.load_balancer_id = load_balancer_id

    def validate(self):
        if self.backend_servers:
            for k in self.backend_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackendServers'] = []
        if self.backend_servers is not None:
            for k in self.backend_servers:
                result['BackendServers'].append(k.to_map() if k else None)
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_servers = []
        if m.get('BackendServers') is not None:
            for k in m.get('BackendServers'):
                temp_model = SetBackendServersRequestBackendServers()
                self.backend_servers.append(temp_model.from_map(k))
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class SetBackendServersShrinkRequest(TeaModel):
    def __init__(
        self,
        backend_servers_shrink: str = None,
        load_balancer_id: str = None,
    ):
        self.backend_servers_shrink = backend_servers_shrink
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_servers_shrink is not None:
            result['BackendServers'] = self.backend_servers_shrink
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            self.backend_servers_shrink = m.get('BackendServers')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class SetBackendServersResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.ip = ip
        self.port = port
        self.server_id = server_id
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SetBackendServersResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[SetBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = SetBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class SetBackendServersResponseBody(TeaModel):
    def __init__(
        self,
        backend_servers: SetBackendServersResponseBodyBackendServers = None,
        request_id: str = None,
    ):
        self.backend_servers = backend_servers
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            temp_model = SetBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetBackendServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetBackendServersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetBackendServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerHTTPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        request_timeout: int = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
    ):
        # 设置监听的描述信息。  长度限制为1-80个字符，允许包含字母、数字、“-”、“/”、“.”和“_”等字符。支持中文描述。
        self.description = description
        # 是否开启健康检查。  取值：on | off。
        self.health_check = health_check
        # 健康检查的后端服务器的端口。  取值： 1~65535。    说明 在HealthCheck值为on时才会有效。
        self.health_check_connect_port = health_check_connect_port
        # 用于健康检查的域名，取值：  $_ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。是否要支持？ domain：域名长度为1-80字符，只能包含字母、数字、点号（.）和连字符（-）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_domain = health_check_domain
        # 健康检查正常的HTTP状态码，多个状态码用逗号分隔。  默认值为http_2xx。  取值：http_2xx | http_3xx | http_4xx | http_5xx。   说明 在HealthCheck值为on时才会有效。
        self.health_check_http_code = health_check_http_code
        # 健康检查的时间间隔。  取值： 1~50（秒）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_interval = health_check_interval
        self.health_check_method = health_check_method
        # 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。在HealthCheck值为on时才会有效。  取值：1~300（秒）。   说明 如果HealthCHeckTimeout的值小于HealthCheckInterval的值，则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。
        self.health_check_timeout = health_check_timeout
        # 用于健康检查的URI。  长度限制为1~80，只能使用字母、数字和”-/.%?#&amp;“这些字符。 URL不能只为”/“，但必须以”/“开头。    说明 在HealthCheck值为on时才会有效。
        self.health_check_uri = health_check_uri
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值：2~10。    说明 在HealthCheck值为on时才会有效。
        self.healthy_threshold = healthy_threshold
        # 指定连接空闲超时时间，取值范围为1~60秒，默认值为15秒。  在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。
        self.idle_timeout = idle_timeout
        # 负载均衡实例前端使用的端口。  取值：1-65535。
        self.listener_port = listener_port
        # 负载均衡实例的ID。
        self.load_balancer_id = load_balancer_id
        # 指定请求超时时间，取值范围为1~180秒，默认值为60秒。  在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504 错误码。
        self.request_timeout = request_timeout
        # 调度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。
        self.scheduler = scheduler
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2~10。   说明 在HealthCheck值为on时才会有效。
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class SetLoadBalancerHTTPListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetLoadBalancerHTTPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerHTTPListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetLoadBalancerHTTPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerHTTPSListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        request_timeout: int = None,
        scheduler: str = None,
        server_certificate_id: str = None,
        unhealthy_threshold: int = None,
    ):
        # 设置监听的描述信息。  长度限制为1-80个字符，允许包含字母、数字、“-”、“/”、“.”和“_”等字符。支持中文描述。
        self.description = description
        # 是否开启健康检查。  取值：on | off。
        self.health_check = health_check
        # 健康检查的后端服务器的端口。  取值： 1~65535。    说明 在HealthCheck值为on时才会有效。
        self.health_check_connect_port = health_check_connect_port
        # 用于健康检查的域名，取值：  $_ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。是否要支持？ domain：域名长度为1-80字符，只能包含字母、数字、点号（.）和连字符（-）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_domain = health_check_domain
        # 健康检查正常的HTTP状态码，多个状态码用逗号分隔。  默认值为http_2xx。  取值：http_2xx | http_3xx | http_4xx | http_5xx。   说明 在HealthCheck值为on时才会有效。
        self.health_check_http_code = health_check_http_code
        # 健康检查的时间间隔。  取值： 1~50（秒）。   说明 在HealthCheck值为on时才会有效。
        self.health_check_interval = health_check_interval
        self.health_check_method = health_check_method
        # 接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。在HealthCheck值为on时才会有效。  取值：1~300（秒）。   说明 如果HealthCHeckTimeout的值小于HealthCheckInterval的值，则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。
        self.health_check_timeout = health_check_timeout
        # 用于健康检查的URI。  长度限制为1~80，只能使用字母、数字和”-/.%?#&amp;“这些字符。 URL不能只为”/“，但必须以”/“开头。    说明 在HealthCheck值为on时才会有效。
        self.health_check_uri = health_check_uri
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值：2~10。    说明 在HealthCheck值为on时才会有效。
        self.healthy_threshold = healthy_threshold
        # 指定连接空闲超时时间，取值范围为1~60秒，默认值为15秒。  在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。
        self.idle_timeout = idle_timeout
        # 负载均衡实例前端使用的端口。  取值：1-65535。
        self.listener_port = listener_port
        # 负载均衡实例的ID。
        self.load_balancer_id = load_balancer_id
        # 指定请求超时时间，取值范围为1~180秒，默认值为60秒。  在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，给客户端返回 HTTP 504 错误码。
        self.request_timeout = request_timeout
        # 调度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。
        self.scheduler = scheduler
        # 服务器证书的ID。
        self.server_certificate_id = server_certificate_id
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2~10。   说明 在HealthCheck值为on时才会有效。
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class SetLoadBalancerHTTPSListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetLoadBalancerHTTPSListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerHTTPSListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetLoadBalancerHTTPSListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerStatusRequest(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        load_balancer_status: str = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.load_balancer_status = load_balancer_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        return self


class SetLoadBalancerStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetLoadBalancerStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetLoadBalancerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerTCPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        eip_transmit: str = None,
        established_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        persistence_timeout: int = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
    ):
        # 设置监听的描述信息。  长度限制为1-80个字符，允许包含字母、数字、“-”、“/”、“.”和“_”等字符。支持中文描述。
        self.description = description
        self.eip_transmit = eip_transmit
        # 连接超时时间。  取值：10~900（秒）。
        self.established_timeout = established_timeout
        # 健康检查使用的端口。  取值：1~65535。  不设置此参数时，表示使用后端服务端口（BackendServerPort）。
        self.health_check_connect_port = health_check_connect_port
        # 每次健康检查响应的最大超时时间。  取值：1~300（秒）。  默认值：5。
        self.health_check_connect_timeout = health_check_connect_timeout
        # 用于健康检查的域名
        self.health_check_domain = health_check_domain
        # 健康检查正常的HTTP状态码，多个状态码用逗号（,）分割。  取值：http_2xx（默认值） | http_3xx | http_4xx | http_5xx。
        self.health_check_http_code = health_check_http_code
        # 健康检查的时间间隔。  取值：1~50（秒）。
        self.health_check_interval = health_check_interval
        # 健康检查类型。  取值：tcp（默认值） | http。
        self.health_check_type = health_check_type
        # 用于健康检查的URI。长度限制为1~80，只能使用字母、数字、短横线（-）、正斜杠（/）、点号（.）、百分号（%）、#和&amp;这些字符。 URL不能只为/，但必须以/开头。  当TCP监听需要使用HTTP健康检查时可配置此参数，如不配置则按TCP健康检查。
        self.health_check_uri = health_check_uri
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值： 2~10。
        self.healthy_threshold = healthy_threshold
        # 负载均衡实例前端使用的端口。  取值：1-65535。
        self.listener_port = listener_port
        # 负载均衡实例的ID。
        self.load_balancer_id = load_balancer_id
        # 会话保持的超时时间。  取值：0~3600（秒）。  默认值：0，表示关闭会话保持。
        self.persistence_timeout = persistence_timeout
        # 度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 sch：基于源IP地址的一致性hash，相同的源地址会调度到相同的后端服务器。
        self.scheduler = scheduler
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2~10。
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.eip_transmit is not None:
            result['EipTransmit'] = self.eip_transmit
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EipTransmit') is not None:
            self.eip_transmit = m.get('EipTransmit')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class SetLoadBalancerTCPListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetLoadBalancerTCPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerTCPListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetLoadBalancerTCPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerUDPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        eip_transmit: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_exp: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
    ):
        # 设置监听的描述信息。  长度限制为1-80个字符，允许包含字母、数字、“-”、“/”、“.”和“_”等字符。支持中文描述。
        self.description = description
        self.eip_transmit = eip_transmit
        # 健康检查使用的端口。取值：1-65535  不设置此参数时，表示使用后端服务端口（BackendServerPort）
        self.health_check_connect_port = health_check_connect_port
        # 接收来自运行状况检查的响应需要等待的时间。  如果后端ENS在指定的时间内没有正确响应，则判定为健康检查失败。  取值：1-300（秒）。默认为5秒
        self.health_check_connect_timeout = health_check_connect_timeout
        # UDP监听健康检查的响应串，只允许包含字母、数字，最大长度限制为64个字符。
        self.health_check_exp = health_check_exp
        # 健康检查的时间间隔。  取值：1-50（秒）。
        self.health_check_interval = health_check_interval
        # UDP监听健康检查的请求串，只允许包含字母、数字，最大长度限制为64个字符。
        self.health_check_req = health_check_req
        # 健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。  取值：2-10。
        self.healthy_threshold = healthy_threshold
        # 负载均衡实例前端使用的端口。  取值：1-65535。
        self.listener_port = listener_port
        # 负载均衡实例的ID。
        self.load_balancer_id = load_balancer_id
        # 调度算法。取值：  wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。 wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。 rr：按照访问顺序依次将外部请求依序分发到后端服务器。 sch：基于源IP地址的一致性hash，相同的源地址会调度到相同的后端服务器。
        self.scheduler = scheduler
        # 健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。  取值：2-10。
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.eip_transmit is not None:
            result['EipTransmit'] = self.eip_transmit
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_exp is not None:
            result['HealthCheckExp'] = self.health_check_exp
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EipTransmit') is not None:
            self.eip_transmit = m.get('EipTransmit')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckExp') is not None:
            self.health_check_exp = m.get('HealthCheckExp')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class SetLoadBalancerUDPListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetLoadBalancerUDPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerUDPListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetLoadBalancerUDPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
    ):
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        return self


class StartEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        version: str = None,
    ):
        self.instance_id = instance_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartLoadBalancerListenerRequest(TeaModel):
    def __init__(
        self,
        listener_port: int = None,
        load_balancer_id: str = None,
    ):
        self.listener_port = listener_port
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class StartLoadBalancerListenerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartLoadBalancerListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartLoadBalancerListenerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartLoadBalancerListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopEpnInstanceRequest(TeaModel):
    def __init__(
        self,
        epninstance_id: str = None,
    ):
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')
        return self


class StopEpnInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopEpnInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopEpnInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopEpnInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        force_stop: str = None,
        instance_id: str = None,
        version: str = None,
    ):
        self.force_stop = force_stop
        self.instance_id = instance_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLoadBalancerListenerRequest(TeaModel):
    def __init__(
        self,
        listener_port: int = None,
        load_balancer_id: str = None,
    ):
        self.listener_port = listener_port
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class StopLoadBalancerListenerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopLoadBalancerListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopLoadBalancerListenerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopLoadBalancerListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnAssociateEnsEipAddressRequest(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
    ):
        self.allocation_id = allocation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        return self


class UnAssociateEnsEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnAssociateEnsEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnAssociateEnsEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnAssociateEnsEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        template: str = None,
        timeout: int = None,
    ):
        self.app_id = app_id
        self.template = template
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template is not None:
            result['Template'] = self.template
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class UpgradeApplicationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


