# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AccelerationInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        # 镜像加速状态，取值 Preparing 或 Ready
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class AsyncConfigMeta(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        qualifier: str = None,
        service_name: str = None,
    ):
        # 异步配置所属函数名称。
        self.function_name = function_name
        # 异步配置所属服务版本/别名。
        self.qualifier = qualifier
        # 异步配置所属服务名称。
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class AvailableAZ(TeaModel):
    def __init__(
        self,
        available_azs: str = None,
    ):
        # az
        self.available_azs = available_azs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_azs is not None:
            result['availableAZs'] = self.available_azs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableAZs') is not None:
            self.available_azs = m.get('availableAZs')
        return self


class CDNEventsTriggerConfig(TeaModel):
    def __init__(
        self,
        event_name: str = None,
        event_version: str = None,
        filter: Dict[str, List[str]] = None,
        notes: str = None,
    ):
        # eventName
        self.event_name = event_name
        # eventVersion
        self.event_version = event_version
        # filter
        self.filter = filter
        # notes
        self.notes = notes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['eventName'] = self.event_name
        if self.event_version is not None:
            result['eventVersion'] = self.event_version
        if self.filter is not None:
            result['filter'] = self.filter
        if self.notes is not None:
            result['notes'] = self.notes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')
        if m.get('eventVersion') is not None:
            self.event_version = m.get('eventVersion')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('notes') is not None:
            self.notes = m.get('notes')
        return self


class CertConfig(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        certificate: str = None,
        private_key: str = None,
    ):
        # 证书名称
        self.cert_name = cert_name
        # 证书，如果是证书链则依次填写多个证书
        self.certificate = certificate
        # 私钥
        self.private_key = private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['certName'] = self.cert_name
        if self.certificate is not None:
            result['certificate'] = self.certificate
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certName') is not None:
            self.cert_name = m.get('certName')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        return self


class Code(TeaModel):
    def __init__(
        self,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        zip_file: str = None,
    ):
        # 函数代码包的OSS bucket name
        self.oss_bucket_name = oss_bucket_name
        # 函数代码包的OSS对象名
        self.oss_object_name = oss_object_name
        # 直接在request body中上传code zip包的base64编码
        self.zip_file = zip_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name
        if self.zip_file is not None:
            result['zipFile'] = self.zip_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')
        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')
        if m.get('zipFile') is not None:
            self.zip_file = m.get('zipFile')
        return self


class CustomContainerConfig(TeaModel):
    def __init__(
        self,
        acceleration_type: str = None,
        args: str = None,
        command: str = None,
        image: str = None,
        instance_id: str = None,
    ):
        # 镜像加速类型，取值Default为开启加速，None为关闭加速，默认开启
        self.acceleration_type = acceleration_type
        # 容器启动参数
        self.args = args
        # 容器启动命令，等同于 Docker ENTRYPOINT
        self.command = command
        # 容器镜像地址，实例值： registry-vpc.cn-hangzhou.aliyuncs.com/fc-demo/helloworld:v1beta1
        self.image = image
        # ACR企业版镜像仓库ID，使用ACR企业版镜像时须传入
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.image is not None:
            result['image'] = self.image
        if self.instance_id is not None:
            result['instanceID'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')
        return self


class CustomContainerConfigInfo(TeaModel):
    def __init__(
        self,
        acceleration_info: AccelerationInfo = None,
        acceleration_type: str = None,
        args: str = None,
        command: str = None,
        image: str = None,
        instance_id: str = None,
    ):
        self.acceleration_info = acceleration_info
        # 镜像加速类型，取值Default为开启加速，None为关闭加速，默认开启
        self.acceleration_type = acceleration_type
        # 容器启动参数
        self.args = args
        # 容器启动命令，等同于 Docker ENTRYPOINT
        self.command = command
        # 容器镜像地址，实例值： registry-vpc.cn-hangzhou.aliyuncs.com/fc-demo/helloworld:v1beta1
        self.image = image
        # ACR企业版镜像仓库ID，使用ACR企业版镜像时须传入
        self.instance_id = instance_id

    def validate(self):
        if self.acceleration_info:
            self.acceleration_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceleration_info is not None:
            result['accelerationInfo'] = self.acceleration_info.to_map()
        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.image is not None:
            result['image'] = self.image
        if self.instance_id is not None:
            result['instanceID'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerationInfo') is not None:
            temp_model = AccelerationInfo()
            self.acceleration_info = temp_model.from_map(m['accelerationInfo'])
        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')
        return self


class DNSOption(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # DNS option 名称
        self.name = name
        # DNS option 值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CustomDNS(TeaModel):
    def __init__(
        self,
        dns_options: List[DNSOption] = None,
        name_servers: List[str] = None,
        searches: List[str] = None,
    ):
        # DNS resolver 配置参数列表
        self.dns_options = dns_options
        # DNS 服务器的 IP 地址列表
        self.name_servers = name_servers
        # DNS 搜索域的列表
        self.searches = searches

    def validate(self):
        if self.dns_options:
            for k in self.dns_options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dnsOptions'] = []
        if self.dns_options is not None:
            for k in self.dns_options:
                result['dnsOptions'].append(k.to_map() if k else None)
        if self.name_servers is not None:
            result['nameServers'] = self.name_servers
        if self.searches is not None:
            result['searches'] = self.searches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dns_options = []
        if m.get('dnsOptions') is not None:
            for k in m.get('dnsOptions'):
                temp_model = DNSOption()
                self.dns_options.append(temp_model.from_map(k))
        if m.get('nameServers') is not None:
            self.name_servers = m.get('nameServers')
        if m.get('searches') is not None:
            self.searches = m.get('searches')
        return self


class CustomRuntimeConfig(TeaModel):
    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
    ):
        # 启动入口命令接收的参数
        self.args = args
        # 启动入口命令
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        return self


class Destination(TeaModel):
    def __init__(
        self,
        destination: str = None,
    ):
        # destination
        self.destination = destination

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['destination'] = self.destination
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destination') is not None:
            self.destination = m.get('destination')
        return self


class DestinationConfig(TeaModel):
    def __init__(
        self,
        on_failure: Destination = None,
        on_success: Destination = None,
    ):
        self.on_failure = on_failure
        self.on_success = on_success

    def validate(self):
        if self.on_failure:
            self.on_failure.validate()
        if self.on_success:
            self.on_success.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_failure is not None:
            result['onFailure'] = self.on_failure.to_map()
        if self.on_success is not None:
            result['onSuccess'] = self.on_success.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onFailure') is not None:
            temp_model = Destination()
            self.on_failure = temp_model.from_map(m['onFailure'])
        if m.get('onSuccess') is not None:
            temp_model = Destination()
            self.on_success = temp_model.from_map(m['onSuccess'])
        return self


class Error(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
    ):
        # 错误码
        self.error_code = error_code
        # 错误信息描述
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        return self


class ErrorInfo(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        stack_trace: str = None,
    ):
        # 错误信息
        self.error_message = error_message
        # 错误堆栈
        self.stack_trace = stack_trace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.stack_trace is not None:
            result['stackTrace'] = self.stack_trace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('stackTrace') is not None:
            self.stack_trace = m.get('stackTrace')
        return self


class SourceMNSParameters(TeaModel):
    def __init__(
        self,
        is_base_64decode: bool = None,
        queue_name: str = None,
        region_id: str = None,
    ):
        # IsBase64Decode
        self.is_base_64decode = is_base_64decode
        # QueueName
        self.queue_name = queue_name
        # RegionId
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SourceRabbitMQParameters(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        region_id: str = None,
        virtual_host_name: str = None,
    ):
        # InstanceId
        self.instance_id = instance_id
        # QueueName
        self.queue_name = queue_name
        # RegionId
        self.region_id = region_id
        # VirtualHostName
        self.virtual_host_name = virtual_host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class SourceRocketMQParameters(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        offset: str = None,
        region_id: str = None,
        tag: str = None,
        timestamp: int = None,
        topic: str = None,
    ):
        # GroupID
        self.group_id = group_id
        # InstanceId
        self.instance_id = instance_id
        # Offset
        self.offset = offset
        # RegionId
        self.region_id = region_id
        # Tag
        self.tag = tag
        # Timestamp
        self.timestamp = timestamp
        # Topic
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class EventSourceParameters(TeaModel):
    def __init__(
        self,
        source_mnsparameters: SourceMNSParameters = None,
        source_rabbit_mqparameters: SourceRabbitMQParameters = None,
        source_rocket_mqparameters: SourceRocketMQParameters = None,
    ):
        self.source_mnsparameters = source_mnsparameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters
        self.source_rocket_mqparameters = source_rocket_mqparameters

    def validate(self):
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_mnsparameters is not None:
            result['sourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['sourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['sourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceMNSParameters') is not None:
            temp_model = SourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['sourceMNSParameters'])
        if m.get('sourceRabbitMQParameters') is not None:
            temp_model = SourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['sourceRabbitMQParameters'])
        if m.get('sourceRocketMQParameters') is not None:
            temp_model = SourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['sourceRocketMQParameters'])
        return self


class EventSourceConfig(TeaModel):
    def __init__(
        self,
        event_source_parameters: EventSourceParameters = None,
        event_source_type: str = None,
    ):
        self.event_source_parameters = event_source_parameters
        # eventSourceType
        self.event_source_type = event_source_type

    def validate(self):
        if self.event_source_parameters:
            self.event_source_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_parameters is not None:
            result['eventSourceParameters'] = self.event_source_parameters.to_map()
        if self.event_source_type is not None:
            result['eventSourceType'] = self.event_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventSourceParameters') is not None:
            temp_model = EventSourceParameters()
            self.event_source_parameters = temp_model.from_map(m['eventSourceParameters'])
        if m.get('eventSourceType') is not None:
            self.event_source_type = m.get('eventSourceType')
        return self


class EventBridgeTriggerConfig(TeaModel):
    def __init__(
        self,
        async_invocation_type: bool = None,
        event_rule_filter_pattern: str = None,
        event_source_config: EventSourceConfig = None,
        trigger_enable: bool = None,
    ):
        # asyncInvocationType
        self.async_invocation_type = async_invocation_type
        # eventRuleFilterPattern
        self.event_rule_filter_pattern = event_rule_filter_pattern
        self.event_source_config = event_source_config
        # triggerEnable
        self.trigger_enable = trigger_enable

    def validate(self):
        if self.event_source_config:
            self.event_source_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_invocation_type is not None:
            result['asyncInvocationType'] = self.async_invocation_type
        if self.event_rule_filter_pattern is not None:
            result['eventRuleFilterPattern'] = self.event_rule_filter_pattern
        if self.event_source_config is not None:
            result['eventSourceConfig'] = self.event_source_config.to_map()
        if self.trigger_enable is not None:
            result['triggerEnable'] = self.trigger_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncInvocationType') is not None:
            self.async_invocation_type = m.get('asyncInvocationType')
        if m.get('eventRuleFilterPattern') is not None:
            self.event_rule_filter_pattern = m.get('eventRuleFilterPattern')
        if m.get('eventSourceConfig') is not None:
            temp_model = EventSourceConfig()
            self.event_source_config = temp_model.from_map(m['eventSourceConfig'])
        if m.get('triggerEnable') is not None:
            self.trigger_enable = m.get('triggerEnable')
        return self


class HTTPTriggerConfig(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        methods: List[str] = None,
    ):
        # 认证类型
        self.auth_type = auth_type
        # 允许的HTTP方法列表
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class LifecycleHook(TeaModel):
    def __init__(
        self,
        handler: str = None,
        timeout: int = None,
    ):
        # handler name
        self.handler = handler
        # timeout in second
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class InstanceLifecycleConfig(TeaModel):
    def __init__(
        self,
        pre_freeze: LifecycleHook = None,
        pre_stop: LifecycleHook = None,
    ):
        self.pre_freeze = pre_freeze
        self.pre_stop = pre_stop

    def validate(self):
        if self.pre_freeze:
            self.pre_freeze.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_freeze is not None:
            result['preFreeze'] = self.pre_freeze.to_map()
        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('preFreeze') is not None:
            temp_model = LifecycleHook()
            self.pre_freeze = temp_model.from_map(m['preFreeze'])
        if m.get('preStop') is not None:
            temp_model = LifecycleHook()
            self.pre_stop = temp_model.from_map(m['preStop'])
        return self


class JaegerConfig(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
    ):
        # endpoint
        self.endpoint = endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        return self


class JobConfig(TeaModel):
    def __init__(
        self,
        max_retry_time: int = None,
        trigger_interval: int = None,
    ):
        # maxRetryTime
        self.max_retry_time = max_retry_time
        # triggerInterval
        self.trigger_interval = trigger_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_retry_time is not None:
            result['maxRetryTime'] = self.max_retry_time
        if self.trigger_interval is not None:
            result['triggerInterval'] = self.trigger_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxRetryTime') is not None:
            self.max_retry_time = m.get('maxRetryTime')
        if m.get('triggerInterval') is not None:
            self.trigger_interval = m.get('triggerInterval')
        return self


class JobLogConfig(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
    ):
        # logstore
        self.logstore = logstore
        # project
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class LayerCode(TeaModel):
    def __init__(
        self,
        location: str = None,
        repository_type: str = None,
    ):
        # 层代码位置
        self.location = location
        # 层代码类型
        self.repository_type = repository_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['location'] = self.location
        if self.repository_type is not None:
            result['repositoryType'] = self.repository_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('repositoryType') is not None:
            self.repository_type = m.get('repositoryType')
        return self


class Layer(TeaModel):
    def __init__(
        self,
        acl: int = None,
        arn: str = None,
        code: LayerCode = None,
        code_checksum: str = None,
        code_size: int = None,
        compatible_runtime: List[str] = None,
        create_time: str = None,
        description: str = None,
        layer_name: str = None,
        version: int = None,
    ):
        # 层访问类型
        self.acl = acl
        # arn
        self.arn = arn
        # 层代码
        self.code = code
        # 层Checksum
        self.code_checksum = code_checksum
        # 层代码大小
        self.code_size = code_size
        # compatibleRuntime
        self.compatible_runtime = compatible_runtime
        # 层创建时间
        self.create_time = create_time
        # 层描述
        self.description = description
        # 层名称
        self.layer_name = layer_name
        # 层版本
        self.version = version

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.arn is not None:
            result['arn'] = self.arn
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.code_size is not None:
            result['codeSize'] = self.code_size
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.layer_name is not None:
            result['layerName'] = self.layer_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('code') is not None:
            temp_model = LayerCode()
            self.code = temp_model.from_map(m['code'])
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('layerName') is not None:
            self.layer_name = m.get('layerName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class LogConfig(TeaModel):
    def __init__(
        self,
        enable_instance_metrics: bool = None,
        enable_request_metrics: bool = None,
        log_begin_rule: str = None,
        logstore: str = None,
        project: str = None,
    ):
        # 开启实例级别指标
        self.enable_instance_metrics = enable_instance_metrics
        # 开启请求级别指标
        self.enable_request_metrics = enable_request_metrics
        # 日志切分规则
        self.log_begin_rule = log_begin_rule
        # 日志库
        self.logstore = logstore
        # 日志项目
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class SourceConfig(TeaModel):
    def __init__(
        self,
        logstore: str = None,
    ):
        # logstore
        self.logstore = logstore

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        return self


class LogTriggerConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        function_parameter: Dict[str, str] = None,
        job_config: JobConfig = None,
        log_config: JobLogConfig = None,
        source_config: SourceConfig = None,
    ):
        # enable
        self.enable = enable
        # functionParameter
        self.function_parameter = function_parameter
        self.job_config = job_config
        self.log_config = log_config
        self.source_config = source_config

    def validate(self):
        if self.job_config:
            self.job_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.source_config:
            self.source_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.function_parameter is not None:
            result['functionParameter'] = self.function_parameter
        if self.job_config is not None:
            result['jobConfig'] = self.job_config.to_map()
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.source_config is not None:
            result['sourceConfig'] = self.source_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('functionParameter') is not None:
            self.function_parameter = m.get('functionParameter')
        if m.get('jobConfig') is not None:
            temp_model = JobConfig()
            self.job_config = temp_model.from_map(m['jobConfig'])
        if m.get('logConfig') is not None:
            temp_model = JobLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('sourceConfig') is not None:
            temp_model = SourceConfig()
            self.source_config = temp_model.from_map(m['sourceConfig'])
        return self


class MeteringConfig(TeaModel):
    def __init__(
        self,
        log_config: LogConfig = None,
        payer_id: str = None,
        role: str = None,
    ):
        # 日志仓库
        self.log_config = log_config
        # 支付用户
        self.payer_id = payer_id
        # 权限
        self.role = role

    def validate(self):
        if self.log_config:
            self.log_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.payer_id is not None:
            result['payerId'] = self.payer_id
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('payerId') is not None:
            self.payer_id = m.get('payerId')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class MnsTopicTriggerConfig(TeaModel):
    def __init__(
        self,
        filter_tag: str = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
    ):
        # filterTag
        self.filter_tag = filter_tag
        # notifyContentFormat
        self.notify_content_format = notify_content_format
        # notifyStrategy
        self.notify_strategy = notify_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_tag is not None:
            result['filterTag'] = self.filter_tag
        if self.notify_content_format is not None:
            result['notifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['notifyStrategy'] = self.notify_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterTag') is not None:
            self.filter_tag = m.get('filterTag')
        if m.get('notifyContentFormat') is not None:
            self.notify_content_format = m.get('notifyContentFormat')
        if m.get('notifyStrategy') is not None:
            self.notify_strategy = m.get('notifyStrategy')
        return self


class NASConfigMountPoints(TeaModel):
    def __init__(
        self,
        mount_dir: str = None,
        server_addr: str = None,
    ):
        # 本地挂载目录
        self.mount_dir = mount_dir
        # NAS服务器地址
        self.server_addr = server_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')
        return self


class NASConfig(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[NASConfigMountPoints] = None,
        user_id: int = None,
    ):
        # groupID
        self.group_id = group_id
        # 挂载点
        self.mount_points = mount_points
        # userID
        self.user_id = user_id

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['mountPoints'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k in m.get('mountPoints'):
                temp_model = NASConfigMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class OSSTriggerKey(TeaModel):
    def __init__(
        self,
        prefix: str = None,
        suffix: str = None,
    ):
        # prefix
        self.prefix = prefix
        # suffix
        self.suffix = suffix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.suffix is not None:
            result['suffix'] = self.suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        return self


class OSSTriggerFilter(TeaModel):
    def __init__(
        self,
        key: OSSTriggerKey = None,
    ):
        self.key = key

    def validate(self):
        if self.key:
            self.key.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            temp_model = OSSTriggerKey()
            self.key = temp_model.from_map(m['key'])
        return self


class OSSTriggerConfig(TeaModel):
    def __init__(
        self,
        events: List[str] = None,
        filter: OSSTriggerFilter = None,
    ):
        # events
        self.events = events
        self.filter = filter

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['events'] = self.events
        if self.filter is not None:
            result['filter'] = self.filter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('events') is not None:
            self.events = m.get('events')
        if m.get('filter') is not None:
            temp_model = OSSTriggerFilter()
            self.filter = temp_model.from_map(m['filter'])
        return self


class OnDemandConfig(TeaModel):
    def __init__(
        self,
        maximum_instance_count: int = None,
        resource: str = None,
    ):
        # todo
        self.maximum_instance_count = maximum_instance_count
        # 函数详情
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class OpenReservedCapacity(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        cu: int = None,
        deadline: str = None,
        instance_id: str = None,
        is_refunded: str = None,
        last_modified_time: str = None,
    ):
        # createdTime
        self.created_time = created_time
        # cu
        self.cu = cu
        # deadline
        self.deadline = deadline
        # instanceId
        self.instance_id = instance_id
        # isRefunded
        self.is_refunded = is_refunded
        # lastModifiedTime
        self.last_modified_time = last_modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.cu is not None:
            result['cu'] = self.cu
        if self.deadline is not None:
            result['deadline'] = self.deadline
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_refunded is not None:
            result['isRefunded'] = self.is_refunded
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('deadline') is not None:
            self.deadline = m.get('deadline')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isRefunded') is not None:
            self.is_refunded = m.get('isRefunded')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        return self


class OutputCodeLocation(TeaModel):
    def __init__(
        self,
        location: str = None,
        repository_type: str = None,
    ):
        # location
        self.location = location
        # repositoryType
        self.repository_type = repository_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['location'] = self.location
        if self.repository_type is not None:
            result['repositoryType'] = self.repository_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('repositoryType') is not None:
            self.repository_type = m.get('repositoryType')
        return self


class PathConfig(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        methods: List[str] = None,
        path: str = None,
        qualifier: str = None,
        service_name: str = None,
    ):
        # 该路径/方法对应的函数名称
        self.function_name = function_name
        # 请求方法，不填表示当前路径的所有方法匹配同一函数
        self.methods = methods
        # 请求路径
        self.path = path
        # 该路径/方法对应服务的版本/别名
        self.qualifier = qualifier
        # 该路径/方法对应的服务名称
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.methods is not None:
            result['methods'] = self.methods
        if self.path is not None:
            result['path'] = self.path
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class PreFreeze(TeaModel):
    def __init__(
        self,
        handler: str = None,
        timeout: int = None,
    ):
        # preFreeze handler name
        self.handler = handler
        # handler timeout
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class PreStop(TeaModel):
    def __init__(
        self,
        handler: str = None,
        timeout: int = None,
    ):
        # PreStop handler
        self.handler = handler
        # PreStop hander timeout
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class RdsTriggerConfig(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        event_format: str = None,
        retry: int = None,
        subscription_objects: List[str] = None,
    ):
        # concurrency
        self.concurrency = concurrency
        # eventFormat
        self.event_format = event_format
        # retry
        self.retry = retry
        # subscriptionObjects
        self.subscription_objects = subscription_objects

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        if self.event_format is not None:
            result['eventFormat'] = self.event_format
        if self.retry is not None:
            result['retry'] = self.retry
        if self.subscription_objects is not None:
            result['subscriptionObjects'] = self.subscription_objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('eventFormat') is not None:
            self.event_format = m.get('eventFormat')
        if m.get('retry') is not None:
            self.retry = m.get('retry')
        if m.get('subscriptionObjects') is not None:
            self.subscription_objects = m.get('subscriptionObjects')
        return self


class Resource(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        # resourceArn
        self.resource_arn = resource_arn
        # tags
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class RouteConfig(TeaModel):
    def __init__(
        self,
        routes: List[PathConfig] = None,
    ):
        # routes
        self.routes = routes

    def validate(self):
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['routes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.routes = []
        if m.get('routes') is not None:
            for k in m.get('routes'):
                temp_model = PathConfig()
                self.routes.append(temp_model.from_map(k))
        return self


class ScheduledActions(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
    ):
        # endTime
        self.end_time = end_time
        # name
        self.name = name
        # scheduleExpression
        self.schedule_expression = schedule_expression
        # startTime
        self.start_time = start_time
        # target
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class StatefulAsyncInvocationEvent(TeaModel):
    def __init__(
        self,
        event_detail: str = None,
        event_id: int = None,
        status: str = None,
        timestamp: int = None,
    ):
        # 事件详细数据。
        self.event_detail = event_detail
        # 事件ID。
        self.event_id = event_id
        # 事件执行状态。
        self.status = status
        # 事件时间。
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_detail is not None:
            result['eventDetail'] = self.event_detail
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.status is not None:
            result['status'] = self.status
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventDetail') is not None:
            self.event_detail = m.get('eventDetail')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class StatefulAsyncInvocation(TeaModel):
    def __init__(
        self,
        already_retried_times: int = None,
        destination_status: str = None,
        end_time: int = None,
        events: List[StatefulAsyncInvocationEvent] = None,
        function_name: str = None,
        instance_id: str = None,
        invocation_error_message: str = None,
        invocation_id: str = None,
        invocation_payload: str = None,
        qualifier: str = None,
        request_id: str = None,
        service_name: str = None,
        started_time: int = None,
        status: str = None,
    ):
        # 异步任务调用失败后的已重试次数。
        self.already_retried_times = already_retried_times
        # 异步任务的目的状态。
        self.destination_status = destination_status
        # 异步任务的结束时间。
        self.end_time = end_time
        # 异步任务事件列表。
        self.events = events
        # 异步任务所属的函数的名称。
        self.function_name = function_name
        # 异步任务的执行实例ID。
        self.instance_id = instance_id
        # 异步任务的错误消息。
        self.invocation_error_message = invocation_error_message
        # 异步任务ID。
        self.invocation_id = invocation_id
        # 异步任务的任务触发事件。
        self.invocation_payload = invocation_payload
        # 异步任务所属的服务的别名或版本。
        self.qualifier = qualifier
        # 异步任务的请求ID。
        self.request_id = request_id
        # 异步任务所属的服务的名称。
        self.service_name = service_name
        # 异步任务的开始时间。
        self.started_time = started_time
        # 异步任务的执行状态。      Enqueued：异步消息已入队，等待处理。      Succeeded：调用执行成功。      Failed：调用执行失败。      Running：调用执行中。      Stopped：调用执行终止。      Stopping：执行停止中。      Invalid：您的执行因函数被删除等原因处于无效状态（任务未被执行）。      Expired：您为任务配置了最长排队等待的期限。该任务因为超期被丢弃（任务未被执行）。      Retrying：异步调用因执行错误重试中。
        self.status = status

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_retried_times is not None:
            result['alreadyRetriedTimes'] = self.already_retried_times
        if self.destination_status is not None:
            result['destinationStatus'] = self.destination_status
        if self.end_time is not None:
            result['endTime'] = self.end_time
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.invocation_error_message is not None:
            result['invocationErrorMessage'] = self.invocation_error_message
        if self.invocation_id is not None:
            result['invocationId'] = self.invocation_id
        if self.invocation_payload is not None:
            result['invocationPayload'] = self.invocation_payload
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.started_time is not None:
            result['startedTime'] = self.started_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alreadyRetriedTimes') is not None:
            self.already_retried_times = m.get('alreadyRetriedTimes')
        if m.get('destinationStatus') is not None:
            self.destination_status = m.get('destinationStatus')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = StatefulAsyncInvocationEvent()
                self.events.append(temp_model.from_map(k))
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('invocationErrorMessage') is not None:
            self.invocation_error_message = m.get('invocationErrorMessage')
        if m.get('invocationId') is not None:
            self.invocation_id = m.get('invocationId')
        if m.get('invocationPayload') is not None:
            self.invocation_payload = m.get('invocationPayload')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('startedTime') is not None:
            self.started_time = m.get('startedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class TLSConfig(TeaModel):
    def __init__(
        self,
        cipher_suites: List[str] = None,
        max_version: str = None,
        min_version: str = None,
    ):
        # TLS加密套件列表
        self.cipher_suites = cipher_suites
        # TLS最大版本号
        self.max_version = max_version
        # TLS最小版本号
        self.min_version = min_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cipher_suites is not None:
            result['cipherSuites'] = self.cipher_suites
        if self.max_version is not None:
            result['maxVersion'] = self.max_version
        if self.min_version is not None:
            result['minVersion'] = self.min_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cipherSuites') is not None:
            self.cipher_suites = m.get('cipherSuites')
        if m.get('maxVersion') is not None:
            self.max_version = m.get('maxVersion')
        if m.get('minVersion') is not None:
            self.min_version = m.get('minVersion')
        return self


class TargetTrackingPolicies(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_capacity: int = None,
        metric_target: float = None,
        metric_type: str = None,
        min_capacity: int = None,
        name: str = None,
        start_time: str = None,
    ):
        # endTime
        self.end_time = end_time
        # maxCapacity
        self.max_capacity = max_capacity
        # metricTarget
        self.metric_target = metric_target
        # metricType
        self.metric_type = metric_type
        # minCapacity
        self.min_capacity = min_capacity
        # name
        self.name = name
        # startTime
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.max_capacity is not None:
            result['maxCapacity'] = self.max_capacity
        if self.metric_target is not None:
            result['metricTarget'] = self.metric_target
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.min_capacity is not None:
            result['minCapacity'] = self.min_capacity
        if self.name is not None:
            result['name'] = self.name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('maxCapacity') is not None:
            self.max_capacity = m.get('maxCapacity')
        if m.get('metricTarget') is not None:
            self.metric_target = m.get('metricTarget')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('minCapacity') is not None:
            self.min_capacity = m.get('minCapacity')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class TimeTriggerConfig(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        enable: bool = None,
        payload: str = None,
    ):
        # cronExpression
        self.cron_expression = cron_expression
        # enable
        self.enable = enable
        # payload
        self.payload = payload

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.enable is not None:
            result['enable'] = self.enable
        if self.payload is not None:
            result['payload'] = self.payload
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('payload') is not None:
            self.payload = m.get('payload')
        return self


class TracingConfig(TeaModel):
    def __init__(
        self,
        params: Dict[str, str] = None,
        type: str = None,
    ):
        # 链路追踪参数。当协议类型为 Jaeger 时，参数为 map[string]string，其中 key 为 "endpoint"，value 为您的链路追踪内网接入点。例如 endpoint: http://tracing-analysis-dc-hz.aliyuncs.com/adapt_xxx/api/otlp/traces
        self.params = params
        # 链路追踪协议类型，目前只支持 Jaeger
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class VPCConfig(TeaModel):
    def __init__(
        self,
        role: str = None,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # Role
        self.role = role
        # 安全组ID
        self.security_group_id = security_group_id
        # VSwitch ID列表
        self.v_switch_ids = v_switch_ids
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['role'] = self.role
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class VendorConfig(TeaModel):
    def __init__(
        self,
        metering_config: MeteringConfig = None,
    ):
        self.metering_config = metering_config

    def validate(self):
        if self.metering_config:
            self.metering_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering_config is not None:
            result['meteringConfig'] = self.metering_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meteringConfig') is not None:
            temp_model = MeteringConfig()
            self.metering_config = temp_model.from_map(m['meteringConfig'])
        return self


class CreateAliasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateAliasRequest(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        description: str = None,
        version_id: str = None,
    ):
        # 额外版本权重
        self.additional_version_weight = additional_version_weight
        # 别名名称
        self.alias_name = alias_name
        # 别名描述
        self.description = description
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.description is not None:
            result['description'] = self.description
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class CreateAliasResponseBody(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        # 额外版本权重
        self.additional_version_weight = additional_version_weight
        # 别名名称
        self.alias_name = alias_name
        # 创建时间
        self.created_time = created_time
        # 别名描述
        self.description = description
        # 上次更新时间
        self.last_modified_time = last_modified_time
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class CreateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAliasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomDomainHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateCustomDomainRequest(TeaModel):
    def __init__(
        self,
        cert_config: CertConfig = None,
        domain_name: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
    ):
        self.cert_config = cert_config
        self.domain_name = domain_name
        self.protocol = protocol
        self.route_config = route_config
        self.tls_config = tls_config

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        return self


class CreateCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        cert_config: CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
    ):
        self.account_id = account_id
        self.api_version = api_version
        self.cert_config = cert_config
        self.created_time = created_time
        # Id of the request
        self.domain_name = domain_name
        self.last_modified_time = last_modified_time
        self.protocol = protocol
        self.route_config = route_config
        self.tls_config = tls_config

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        return self


class CreateCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_code_checksum = x_fc_code_checksum
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code: Code = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        function_name: str = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        layers: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # 自定义、自定义容器运行时 HTTP Server 的监听端口
        self.ca_port = ca_port
        self.code = code
        self.custom_container_config = custom_container_config
        # 函数自定义DNS配置
        self.custom_dns = custom_dns
        # Custom Runtime函数详细配置
        self.custom_runtime_config = custom_runtime_config
        # 函数描述
        self.description = description
        self.environment_variables = environment_variables
        # 函数名称
        self.function_name = function_name
        # function执行的入口，具体格式和语言相关
        self.handler = handler
        # 初始化function运行的超时时间，单位为秒，最小1秒，默认3秒。初始化function超过这个时间后会被终止执行
        self.initialization_timeout = initialization_timeout
        # 初始化 function 执行的入口，具体格式和语言相关
        self.initializer = initializer
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.instance_soft_concurrency = instance_soft_concurrency
        self.instance_type = instance_type
        # 层列表
        self.layers = layers
        # function的内存规格，单位为MB，为64MB的倍数
        self.memory_size = memory_size
        # function运行的语言环境，目前支持nodejs6, nodejs8, python2.7, python3, java8
        self.runtime = runtime
        # function运行的超时时间，单位为秒，最小1秒，默认3秒。function超过这个时间后会被终止执行
        self.timeout = timeout

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('code') is not None:
            temp_model = Code()
            self.code = temp_model.from_map(m['code'])
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code_checksum: str = None,
        code_size: int = None,
        created_time: str = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        function_id: str = None,
        function_name: str = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        last_modified_time: str = None,
        layers: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # 自定义、自定义容器运行时 HTTP Server 的监听端口
        self.ca_port = ca_port
        # function code包的CRC64值
        self.code_checksum = code_checksum
        # 系统返回的function的code包大小，单位为byte Example : 1024
        self.code_size = code_size
        # function创建时间
        self.created_time = created_time
        self.custom_container_config = custom_container_config
        # 函数自定义DNS配置
        self.custom_dns = custom_dns
        # Custom Runtime函数详细配置
        self.custom_runtime_config = custom_runtime_config
        # 函数描述
        self.description = description
        self.environment_variables = environment_variables
        # 系统为每个function生成的唯一ID
        self.function_id = function_id
        # 函数名称
        self.function_name = function_name
        # function的执行入口
        self.handler = handler
        # 初始化function运行的超时时间，单位为秒，最小1秒，默认3秒。初始化function超过这个时间后会被终止执行
        self.initialization_timeout = initialization_timeout
        # 初始化 function 执行的入口，具体格式和语言相关
        self.initializer = initializer
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.instance_soft_concurrency = instance_soft_concurrency
        self.instance_type = instance_type
        # function上次修改时间
        self.last_modified_time = last_modified_time
        self.layers = layers
        # function设置的内存大小，单位为MB
        self.memory_size = memory_size
        # function运行的语言环境，目前支持nodejs6, nodejs8, python2.7, python3, java8
        self.runtime = runtime
        # 运行的超时时间，单位为秒
        self.timeout = timeout

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.code_size is not None:
            result['codeSize'] = self.code_size
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateLayerVersionRequest(TeaModel):
    def __init__(
        self,
        code: Code = None,
        compatible_runtime: List[str] = None,
        description: str = None,
    ):
        self.code = code
        self.compatible_runtime = compatible_runtime
        self.description = description

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code.to_map()
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            temp_model = Code()
            self.code = temp_model.from_map(m['Code'])
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateLayerVersionResponseBody(TeaModel):
    def __init__(
        self,
        acl: int = None,
        arn: str = None,
        code: OutputCodeLocation = None,
        code_checksum: str = None,
        codesize: int = None,
        compatible_runtime: List[str] = None,
        create_time: str = None,
        description: str = None,
        layer_name: str = None,
        version: int = None,
    ):
        self.acl = acl
        self.arn = arn
        self.code = code
        self.code_checksum = code_checksum
        self.codesize = codesize
        self.compatible_runtime = compatible_runtime
        self.create_time = create_time
        self.description = description
        self.layer_name = layer_name
        self.version = version

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.arn is not None:
            result['arn'] = self.arn
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.codesize is not None:
            result['codesize'] = self.codesize
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.layer_name is not None:
            result['layerName'] = self.layer_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('code') is not None:
            temp_model = OutputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codesize') is not None:
            self.codesize = m.get('codesize')
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('layerName') is not None:
            self.layer_name = m.get('layerName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class CreateLayerVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLayerVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLayerVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        internet_access: bool = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        role: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        vpc_config: VPCConfig = None,
    ):
        # 服务描述
        self.description = description
        # 公网访问设置
        self.internet_access = internet_access
        self.log_config = log_config
        self.nas_config = nas_config
        # 服务角色
        self.role = role
        # 服务名称
        self.service_name = service_name
        self.tracing_config = tracing_config
        self.vpc_config = vpc_config

    def validate(self):
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        role: str = None,
        service_id: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        vendor_config: VendorConfig = None,
        vpc_config: VPCConfig = None,
    ):
        # 创建时间
        self.created_time = created_time
        # 服务描述
        self.description = description
        # 公网访问设置
        self.internet_access = internet_access
        # 上次更新时间
        self.last_modified_time = last_modified_time
        self.log_config = log_config
        self.nas_config = nas_config
        # 服务角色
        self.role = role
        # 服务ID
        self.service_id = service_id
        # 服务名称
        self.service_name = service_name
        self.tracing_config = tracing_config
        self.vendor_config = vendor_config
        self.vpc_config = vpc_config

    def validate(self):
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vendor_config:
            self.vendor_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vendorConfig') is not None:
            temp_model = VendorConfig()
            self.vendor_config = temp_model.from_map(m['vendorConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateTriggerRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        invocation_role: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
    ):
        self.description = description
        # event source，如OSS，使用该role去invoke function
        self.invocation_role = invocation_role
        # service版本
        self.qualifier = qualifier
        # event source的Aliyun Resource Name（ARN
        self.source_arn = source_arn
        # trigger配置，针对不同的trigger类型，trigger配置会有所不同
        self.trigger_config = trigger_config
        # trigger名称
        self.trigger_name = trigger_name
        # trigger类型，如 oss, log, tablestore, timer, http, cdn_events, mns_topic
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        return self


class CreateTriggerResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        domain_name: str = None,
        invocation_role: str = None,
        last_modified_time: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        # 创建时间
        self.created_time = created_time
        self.description = description
        # 域名名称，使用域名名称拼接上函数计算域名，可以采用HTTP协议调用到触发器对应版本的函数。例如{domainName}.cn-shanghai.fc.aliyuncs.com
        self.domain_name = domain_name
        # 调用函数使用的RAM角色的ARN
        self.invocation_role = invocation_role
        # 上次修改时间
        self.last_modified_time = last_modified_time
        # service版本
        self.qualifier = qualifier
        # event source的Aliyun Resource Name（ARN
        self.source_arn = source_arn
        # trigger配置对象
        self.trigger_config = trigger_config
        self.trigger_id = trigger_id
        # trigger名称
        self.trigger_name = trigger_name
        # trigger类型，如 oss, log, tablestore, timer, http, cdn_events, mns_topic
        self.trigger_type = trigger_type
        # 公网域名地址。在互联网可以通过HTTP协议或者HTTPS协议访问HTTP Trigger。
        self.url_internet = url_internet
        # 私网域名地址。在VPC可以通过HTTP协议或者HTTPS协议访问HTTP Trigger。
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class CreateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcBindingHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateVpcBindingRequest(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class CreateVpcBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAliasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteCustomDomainHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # 用于确保实际更改的资源和期望更改的资源是一致的，该值来自Create，Get和Update API的响应
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteFunctionAsyncInvokeConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteFunctionAsyncInvokeConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # 限定符
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class DeleteFunctionAsyncInvokeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteFunctionOnDemandConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteFunctionOnDemandConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # 服务别名或LATEST，不支持版本。
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class DeleteFunctionOnDemandConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteLayerVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteLayerVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteServiceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # 用于确保实际更改的资源和期望更改的资源是一致的，该值来自Create，Get和Update API的响应
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteServiceVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteTriggerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # 用于确保实际更改的资源和期望更改的资源是一致的，该值来自Create，Get和Update API的响应
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteVpcBindingHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteVpcBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeregisterEventSourceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeregisterEventSourceRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # 别名或版本
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class DeregisterEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetAccountSettingsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetAccountSettingsResponseBody(TeaModel):
    def __init__(
        self,
        available_azs: List[str] = None,
        default_role: str = None,
    ):
        # 可用区列表
        self.available_azs = available_azs
        # 默认服务角色
        self.default_role = default_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_azs is not None:
            result['availableAZs'] = self.available_azs
        if self.default_role is not None:
            result['defaultRole'] = self.default_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableAZs') is not None:
            self.available_azs = m.get('availableAZs')
        if m.get('defaultRole') is not None:
            self.default_role = m.get('defaultRole')
        return self


class GetAccountSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountSettingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccountSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAliasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetAliasResponseBody(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        # 额外版本权重
        self.additional_version_weight = additional_version_weight
        # 别名名称
        self.alias_name = alias_name
        # 创建时间
        self.created_time = created_time
        # 别名描述
        self.description = description
        # 上次更新时间
        self.last_modified_time = last_modified_time
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class GetAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAliasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomDomainHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        cert_config: CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
    ):
        self.account_id = account_id
        self.api_version = api_version
        self.cert_config = cert_config
        self.created_time = created_time
        # Id of the request
        self.domain_name = domain_name
        self.last_modified_time = last_modified_time
        self.protocol = protocol
        self.route_config = route_config
        self.tls_config = tls_config

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        return self


class GetCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCustomDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # service版本, 可以是versionId或者aliasName
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetFunctionResponseBody(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code_checksum: str = None,
        code_size: int = None,
        created_time: str = None,
        custom_container_config: CustomContainerConfigInfo = None,
        custom_dns: CustomDNS = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        function_id: str = None,
        function_name: str = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        last_modified_time: str = None,
        layers: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # 自定义、自定义容器运行时 HTTP Server 的监听端口
        self.ca_port = ca_port
        # function code包的CRC64值
        self.code_checksum = code_checksum
        # 系统返回的function的code包大小，单位为byte Example : 1024
        self.code_size = code_size
        # function创建时间
        self.created_time = created_time
        self.custom_container_config = custom_container_config
        # 函数自定义DNS配置
        self.custom_dns = custom_dns
        # Custom Runtime函数详细配置
        self.custom_runtime_config = custom_runtime_config
        # 函数描述
        self.description = description
        # 为函数设置的环境变量，可以在函数中获取环境变量的值
        self.environment_variables = environment_variables
        # 系统为每个function生成的唯一ID
        self.function_id = function_id
        # 函数名称
        self.function_name = function_name
        # function的执行入口
        self.handler = handler
        # 初始化function运行的超时时间，单位为秒，最小1秒，默认3秒。初始化function超过这个时间后会被终止执行
        self.initialization_timeout = initialization_timeout
        # 初始化 function 执行的入口，具体格式和语言相关
        self.initializer = initializer
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.instance_soft_concurrency = instance_soft_concurrency
        self.instance_type = instance_type
        # function上次修改时间
        self.last_modified_time = last_modified_time
        self.layers = layers
        # function设置的内存大小，单位为MB
        self.memory_size = memory_size
        # function运行的语言环境，目前支持nodejs6, nodejs8, python2.7, python3, java8
        self.runtime = runtime
        # 运行的超时时间，单位为秒
        self.timeout = timeout

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.code_size is not None:
            result['codeSize'] = self.code_size
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfigInfo()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class GetFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionAsyncInvokeConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionAsyncInvokeConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # 限定符
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetFunctionAsyncInvokeConfigResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        destination_config: DestinationConfig = None,
        function: str = None,
        last_modified_time: str = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
        qualifier: str = None,
        service: str = None,
        stateful_invocation: bool = None,
    ):
        # 创建时间
        self.created_time = created_time
        self.destination_config = destination_config
        # 函数名称
        self.function = function
        # 最后更改时间
        self.last_modified_time = last_modified_time
        # 消息最大存活时长
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # 异步调用失败后的最大重试次数
        self.max_async_retry_attempts = max_async_retry_attempts
        # 限定符
        self.qualifier = qualifier
        # 服务名称
        self.service = service
        self.stateful_invocation = stateful_invocation

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function is not None:
            result['function'] = self.function
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service is not None:
            result['service'] = self.service
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        return self


class GetFunctionAsyncInvokeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionAsyncInvokeConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionAsyncInvokeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionCodeHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionCodeRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # service版本, 可以是versionId或者aliasName
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetFunctionCodeResponseBody(TeaModel):
    def __init__(
        self,
        checksum: str = None,
        url: str = None,
    ):
        # function code包的CRC64值
        self.checksum = checksum
        # 获取function代码的URL
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['checksum'] = self.checksum
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetFunctionCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionOnDemandConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionOnDemandConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetFunctionOnDemandConfigResponseBody(TeaModel):
    def __init__(
        self,
        maximum_instance_count: int = None,
        resource: str = None,
    ):
        self.maximum_instance_count = maximum_instance_count
        # Id of the request
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class GetFunctionOnDemandConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionOnDemandConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionOnDemandConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetLayerVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Layer = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Layer()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProvisionConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetProvisionConfigRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # 别名名称
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetProvisionConfigResponseBody(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        current: int = None,
        current_error: str = None,
        resource: str = None,
        scheduled_actions: List[ScheduledActions] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicies] = None,
    ):
        # 是否始终分配CPU给函数实例。
        self.always_allocate_cpu = always_allocate_cpu
        # 实际资源个数
        self.current = current
        # 预留实例创建失败时的错误信息
        self.current_error = current_error
        # 资源描述
        self.resource = resource
        # 定时策略配置
        self.scheduled_actions = scheduled_actions
        # 目标资源个数
        self.target = target
        # 指标追踪伸缩策略配置
        self.target_tracking_policies = target_tracking_policies

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()
        if self.target_tracking_policies:
            for k in self.target_tracking_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        if self.current is not None:
            result['current'] = self.current
        if self.current_error is not None:
            result['currentError'] = self.current_error
        if self.resource is not None:
            result['resource'] = self.resource
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        result['targetTrackingPolicies'] = []
        if self.target_tracking_policies is not None:
            for k in self.target_tracking_policies:
                result['targetTrackingPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class GetProvisionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProvisionConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProvisionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTagsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetResourceTagsRequest(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
    ):
        # Resource ARN 全称或者简称
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        return self


class GetResourceTagsResponseBody(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        # Resource ARN 全称
        self.resource_arn = resource_arn
        # tag 列表
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class GetResourceTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetServiceRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # 限定符
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetServiceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        role: str = None,
        service_id: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        vpc_config: VPCConfig = None,
    ):
        # 创建时间
        self.created_time = created_time
        # 服务描述
        self.description = description
        # 公网访问设置
        self.internet_access = internet_access
        # 上次更新时间
        self.last_modified_time = last_modified_time
        self.log_config = log_config
        self.nas_config = nas_config
        # 服务角色
        self.role = role
        # 服务ID
        self.service_id = service_id
        # 服务名称
        self.service_name = service_name
        self.tracing_config = tracing_config
        self.vpc_config = vpc_config

    def validate(self):
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStatefulAsyncInvocationHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_code_checksum = x_fc_code_checksum
        self.x_fc_date = x_fc_date
        self.x_fc_invocation_type = x_fc_invocation_type
        self.x_fc_log_type = x_fc_log_type
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetStatefulAsyncInvocationRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetStatefulAsyncInvocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StatefulAsyncInvocation = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StatefulAsyncInvocation()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTriggerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetTriggerResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        domain_name: str = None,
        invocation_role: str = None,
        last_modified_time: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        # 创建时间
        self.created_time = created_time
        self.description = description
        # 域名名称，使用域名名称拼接上函数计算域名，可以采用HTTP协议调用到触发器对应版本的函数。例如{domainName}.cn-shanghai.fc.aliyuncs.com
        self.domain_name = domain_name
        # 调用函数使用的RAM角色的ARN
        self.invocation_role = invocation_role
        # 上次修改时间
        self.last_modified_time = last_modified_time
        # service版本
        self.qualifier = qualifier
        # event source的Aliyun Resource Name（ARN
        self.source_arn = source_arn
        # trigger配置对象
        self.trigger_config = trigger_config
        self.trigger_id = trigger_id
        # trigger名称
        self.trigger_name = trigger_name
        # trigger类型，如 oss, log, tablestore, timer, http, cdn_events, mns_topic
        self.trigger_type = trigger_type
        # 公网域名地址。在互联网可以通过HTTP协议或者HTTPS协议访问HTTP Trigger。
        self.url_internet = url_internet
        # 私网域名地址。在VPC可以通过HTTP协议或者HTTPS协议访问HTTP Trigger。
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class GetTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
        x_fc_stateful_async_invocation_id: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        # 调用方式:Sync或者Async，默认值：Sync
        self.x_fc_invocation_type = x_fc_invocation_type
        # 请求返回日志类型, Tail 为返回函数日志最后 4KB 数据，None 或空值则返回不带有日志，默认为 None
        self.x_fc_log_type = x_fc_log_type
        self.x_fc_stateful_async_invocation_id = x_fc_stateful_async_invocation_id
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_stateful_async_invocation_id is not None:
            result['X-Fc-Stateful-Async-Invocation-Id'] = self.x_fc_stateful_async_invocation_id
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Stateful-Async-Invocation-Id') is not None:
            self.x_fc_stateful_async_invocation_id = m.get('X-Fc-Stateful-Async-Invocation-Id')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class InvokeFunctionRequest(TeaModel):
    def __init__(
        self,
        body: bytes = None,
        qualifier: str = None,
    ):
        # 事件（event），binary type。函数计算服务将event传递给用户function来处理
        self.body = body
        # service版本, 可以是versionId或者aliasName
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class InvokeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: bytes = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ListAliasesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListAliasesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # 最多返回个数
        self.limit = limit
        # 下次查询token
        self.next_token = next_token
        # 前缀
        self.prefix = prefix
        # 起始key
        self.start_key = start_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListAliasesResponseBodyAliases(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        # 额外版本权重
        self.additional_version_weight = additional_version_weight
        # 别名名称
        self.alias_name = alias_name
        # 创建时间
        self.created_time = created_time
        # 别名描述
        self.description = description
        # 上次更新时间
        self.last_modified_time = last_modified_time
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListAliasesResponseBody(TeaModel):
    def __init__(
        self,
        aliases: List[ListAliasesResponseBodyAliases] = None,
        next_token: str = None,
    ):
        # 别名列表
        self.aliases = aliases
        # 下次查询token
        self.next_token = next_token

    def validate(self):
        if self.aliases:
            for k in self.aliases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['aliases'] = []
        if self.aliases is not None:
            for k in self.aliases:
                result['aliases'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aliases = []
        if m.get('aliases') is not None:
            for k in m.get('aliases'):
                temp_model = ListAliasesResponseBodyAliases()
                self.aliases.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAliasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAliasesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomDomainsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListCustomDomainsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        self.limit = limit
        self.next_token = next_token
        self.prefix = prefix
        self.start_key = start_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListCustomDomainsResponseBodyCustomDomains(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        cert_config: CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
    ):
        self.account_id = account_id
        self.api_version = api_version
        self.cert_config = cert_config
        self.created_time = created_time
        self.domain_name = domain_name
        self.last_modified_time = last_modified_time
        self.protocol = protocol
        self.route_config = route_config
        self.tls_config = tls_config

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        return self


class ListCustomDomainsResponseBody(TeaModel):
    def __init__(
        self,
        custom_domains: List[ListCustomDomainsResponseBodyCustomDomains] = None,
        next_token: str = None,
    ):
        self.custom_domains = custom_domains
        self.next_token = next_token

    def validate(self):
        if self.custom_domains:
            for k in self.custom_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['customDomains'] = []
        if self.custom_domains is not None:
            for k in self.custom_domains:
                result['customDomains'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k in m.get('customDomains'):
                temp_model = ListCustomDomainsResponseBodyCustomDomains()
                self.custom_domains.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListCustomDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventSourcesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListEventSourcesRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # 别名或版本
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class ListEventSourcesResponseBodyEventSources(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        source_arn: str = None,
    ):
        # 创建时间
        self.created_time = created_time
        # 事件源资源标识符
        self.source_arn = source_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        return self


class ListEventSourcesResponseBody(TeaModel):
    def __init__(
        self,
        event_sources: List[ListEventSourcesResponseBodyEventSources] = None,
    ):
        # 事件源列表
        self.event_sources = event_sources

    def validate(self):
        if self.event_sources:
            for k in self.event_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['eventSources'] = []
        if self.event_sources is not None:
            for k in self.event_sources:
                result['eventSources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_sources = []
        if m.get('eventSources') is not None:
            for k in m.get('eventSources'):
                temp_model = ListEventSourcesResponseBodyEventSources()
                self.event_sources.append(temp_model.from_map(k))
        return self


class ListEventSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionAsyncInvokeConfigsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_code_checksum = x_fc_code_checksum
        self.x_fc_date = x_fc_date
        self.x_fc_invocation_type = x_fc_invocation_type
        self.x_fc_log_type = x_fc_log_type
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListFunctionAsyncInvokeConfigsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
    ):
        # 最多返回个数
        self.limit = limit
        # 下次查询token
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionAsyncInvokeConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        destination_config: DestinationConfig = None,
        function: str = None,
        last_modified_time: str = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
        qualifier: str = None,
        service: str = None,
        stateful_invocation: bool = None,
    ):
        # 创建时间
        self.created_time = created_time
        self.destination_config = destination_config
        # 函数名称
        self.function = function
        # 最后更改时间
        self.last_modified_time = last_modified_time
        # 消息最大存活时长
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # 异步调用失败后的最大重试次数
        self.max_async_retry_attempts = max_async_retry_attempts
        # 限定符
        self.qualifier = qualifier
        # 服务名称
        self.service = service
        self.stateful_invocation = stateful_invocation

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function is not None:
            result['function'] = self.function
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service is not None:
            result['service'] = self.service
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        return self


class ListFunctionAsyncInvokeConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[ListFunctionAsyncInvokeConfigsResponseBodyConfigs] = None,
        next_token: str = None,
    ):
        # 异步配置列表
        self.configs = configs
        # 下次查询token
        self.next_token = next_token

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = ListFunctionAsyncInvokeConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionAsyncInvokeConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionAsyncInvokeConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionAsyncInvokeConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        qualifier: str = None,
        start_key: str = None,
    ):
        # 限定此次返回资源的数量。如果不设定，默认返回20，最大不能超过100。返回结果可能小于指定的数量，但不会多于指定的数量
        self.limit = limit
        # 用来返回更多结果。第一次查询不需要提供这个参数，后续查询的token从返回结果中获取
        self.next_token = next_token
        # 限定返回的资源名称必须以prefix作为前缀
        self.prefix = prefix
        # service版本, 可以是versionId或者aliasName
        self.qualifier = qualifier
        # 设定结果从startKey之后（包括startKey）按字母排序的第一个开始返回
        self.start_key = start_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListFunctionsResponseBodyFunctions(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code_checksum: str = None,
        code_size: int = None,
        created_time: str = None,
        custom_container_config: CustomContainerConfig = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        function_id: str = None,
        function_name: str = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_concurrency: int = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        last_modified_time: str = None,
        layers: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # 自定义、自定义容器运行时 HTTP Server 的监听端口
        self.ca_port = ca_port
        # function code包的CRC64值
        self.code_checksum = code_checksum
        # 系统返回的function的code包大小，单位为byte Example : 1024
        self.code_size = code_size
        # function创建时间
        self.created_time = created_time
        self.custom_container_config = custom_container_config
        # 函数描述
        self.description = description
        # 为函数设置的环境变量，可以在函数中获取环境变量的值
        self.environment_variables = environment_variables
        # 系统为每个function生成的唯一ID
        self.function_id = function_id
        # 函数名称
        self.function_name = function_name
        # function的执行入口
        self.handler = handler
        # 初始化function运行的超时时间，单位为秒，最小1秒，默认3秒。初始化function超过这个时间后会被终止执行
        self.initialization_timeout = initialization_timeout
        # 初始化 function 执行的入口，具体格式和语言相关
        self.initializer = initializer
        self.instance_concurrency = instance_concurrency
        self.instance_lifecycle_config = instance_lifecycle_config
        self.instance_soft_concurrency = instance_soft_concurrency
        self.instance_type = instance_type
        # function上次修改时间
        self.last_modified_time = last_modified_time
        self.layers = layers
        # function设置的内存大小，单位为MB
        self.memory_size = memory_size
        # function运行的语言环境，目前支持nodejs6, nodejs8, python2.7, python3, java8
        self.runtime = runtime
        # 运行的超时时间，单位为秒
        self.timeout = timeout

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.code_size is not None:
            result['codeSize'] = self.code_size
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class ListFunctionsResponseBody(TeaModel):
    def __init__(
        self,
        functions: List[ListFunctionsResponseBodyFunctions] = None,
        next_token: str = None,
    ):
        # 函数列表
        self.functions = functions
        # 用来返回更多的查询结果。如果这个值没有返回，则说明没有更多结果
        self.next_token = next_token

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['functions'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k in m.get('functions'):
                temp_model = ListFunctionsResponseBodyFunctions()
                self.functions.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        limit: int = None,
        qualifier: str = None,
    ):
        # 实例ID
        self.instance_ids = instance_ids
        # 限定此次返回资源的数量，取值范围[0,1000]。
        # 
        # 返回结果可以小于指定的数量，但不能多于指定的数量。
        self.limit = limit
        # 服务的版本或别名。默认是LATEST。
        # 
        # 此处的qualifier同InvokeFunction的qualifier含义一致，即调用ListInstances时指定qualifier=test查询出来的实例，就是调用InvokeFunction时qualifier=test链路上的实例。
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.limit is not None:
            result['limit'] = self.limit
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        version_id: str = None,
    ):
        # 实例ID。
        self.instance_id = instance_id
        # 实例所属的服务版本。如果是LATEST别名下的函数实例，则返回版本号为0。
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
    ):
        self.instances = instances

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayerVersionsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListLayerVersionsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        start_version: int = None,
    ):
        # 本次读取的最大数据记录数量
        self.limit = limit
        # 起始版本
        self.start_version = start_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.start_version is not None:
            result['startVersion'] = self.start_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('startVersion') is not None:
            self.start_version = m.get('startVersion')
        return self


class ListLayerVersionsResponseBody(TeaModel):
    def __init__(
        self,
        layers: List[Layer] = None,
        next_version: int = None,
    ):
        # 层版本列表
        self.layers = layers
        # 剩余列表起始版本号
        self.next_version = next_version

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['layers'].append(k.to_map() if k else None)
        if self.next_version is not None:
            result['nextVersion'] = self.next_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layers = []
        if m.get('layers') is not None:
            for k in m.get('layers'):
                temp_model = Layer()
                self.layers.append(temp_model.from_map(k))
        if m.get('nextVersion') is not None:
            self.next_version = m.get('nextVersion')
        return self


class ListLayerVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLayerVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLayerVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListLayersRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # 最大返回条目数
        self.limit = limit
        # 下一个层名称
        self.next_token = next_token
        # 层名称前缀
        self.prefix = prefix
        # 起始层名称
        self.start_key = start_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListLayersResponseBody(TeaModel):
    def __init__(
        self,
        layers: List[Layer] = None,
        next_token: str = None,
    ):
        # 层列表
        self.layers = layers
        # 剩余列表起始层名
        self.next_token = next_token

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['layers'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layers = []
        if m.get('layers') is not None:
            for k in m.get('layers'):
                temp_model = Layer()
                self.layers.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListLayersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLayersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLayersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOnDemandConfigsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListOnDemandConfigsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # 限定此次返回资源的数量。如果不设定，默认返回20，最大不能超过100。返回结果可以小于指定的数量，但不会多于指定的数量。
        self.limit = limit
        # 用来返回更多结果。第一次查询不需要提供这个参数，后续查询的Token从返回结果中获取。
        self.next_token = next_token
        # 限定返回的资源名称，名称必须以Prefix作为前缀，例如Prefix是a，则返回的资源名均是以a开始的。
        self.prefix = prefix
        # 设定结果从startKey之后（包括startKey）按字母排序的第一个开始返回。
        self.start_key = start_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListOnDemandConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: List[OnDemandConfig] = None,
        next_token: str = None,
    ):
        # 预留实例配置
        self.configs = configs
        # 用来返回更多的查询结果。如果这个值没有返回，则说明没有更多结果。
        self.next_token = next_token

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = OnDemandConfig()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListOnDemandConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOnDemandConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOnDemandConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProvisionConfigsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListProvisionConfigsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        qualifier: str = None,
        service_name: str = None,
    ):
        # 限定此次返回资源的数量。如果不设定，默认返回20，最大不能超过100。返回结果可能小于指定的数量，但不会多于指定的数量
        self.limit = limit
        # 用来返回更多结果。第一次查询不需要提供这个参数，后续查询的token从返回结果中获取
        self.next_token = next_token
        # 限定返回的资源名称必须属于该qualifier。qualifier只能是aliasName，且必须和serviceName共同使用
        self.qualifier = qualifier
        # 限定返回的资源名称必须属于该service
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListProvisionConfigsResponseBodyProvisionConfigs(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        current: int = None,
        current_error: str = None,
        resource: str = None,
        scheduled_actions: List[ScheduledActions] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicies] = None,
    ):
        # 是否始终分配CPU给函数实例。
        self.always_allocate_cpu = always_allocate_cpu
        # 实际资源个数
        self.current = current
        # 预留实例创建失败时的错误信息
        self.current_error = current_error
        # 资源描述
        self.resource = resource
        # 定时策略配置
        self.scheduled_actions = scheduled_actions
        # 目标资源个数
        self.target = target
        # 指标追踪伸缩策略配置
        self.target_tracking_policies = target_tracking_policies

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()
        if self.target_tracking_policies:
            for k in self.target_tracking_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        if self.current is not None:
            result['current'] = self.current
        if self.current_error is not None:
            result['currentError'] = self.current_error
        if self.resource is not None:
            result['resource'] = self.resource
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        result['targetTrackingPolicies'] = []
        if self.target_tracking_policies is not None:
            for k in self.target_tracking_policies:
                result['targetTrackingPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class ListProvisionConfigsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        provision_configs: List[ListProvisionConfigsResponseBodyProvisionConfigs] = None,
    ):
        # 下次查询的起始token
        self.next_token = next_token
        # 预留实例列表
        self.provision_configs = provision_configs

    def validate(self):
        if self.provision_configs:
            for k in self.provision_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['provisionConfigs'] = []
        if self.provision_configs is not None:
            for k in self.provision_configs:
                result['provisionConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.provision_configs = []
        if m.get('provisionConfigs') is not None:
            for k in m.get('provisionConfigs'):
                temp_model = ListProvisionConfigsResponseBodyProvisionConfigs()
                self.provision_configs.append(temp_model.from_map(k))
        return self


class ListProvisionConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProvisionConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProvisionConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReservedCapacitiesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListReservedCapacitiesRequest(TeaModel):
    def __init__(
        self,
        limit: str = None,
        next_token: str = None,
    ):
        # 一次返回的数量，取值范围[1, 100]
        self.limit = limit
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListReservedCapacitiesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        reserved_capacities: List[OpenReservedCapacity] = None,
    ):
        # nextToken
        self.next_token = next_token
        # reservedCapacities
        self.reserved_capacities = reserved_capacities

    def validate(self):
        if self.reserved_capacities:
            for k in self.reserved_capacities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['reservedCapacities'] = []
        if self.reserved_capacities is not None:
            for k in self.reserved_capacities:
                result['reservedCapacities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.reserved_capacities = []
        if m.get('reservedCapacities') is not None:
            for k in m.get('reservedCapacities'):
                temp_model = OpenReservedCapacity()
                self.reserved_capacities.append(temp_model.from_map(k))
        return self


class ListReservedCapacitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListReservedCapacitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListReservedCapacitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceVersionsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListServiceVersionsRequest(TeaModel):
    def __init__(
        self,
        direction: str = None,
        limit: int = None,
        next_token: str = None,
        start_key: str = None,
    ):
        # 排序方向
        self.direction = direction
        # 最多返回个数
        self.limit = limit
        # 下次查询token
        self.next_token = next_token
        # 起始key
        self.start_key = start_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListServiceVersionsResponseBodyVersions(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        # 创建时间
        self.created_time = created_time
        # 版本描述
        self.description = description
        # 上次更新时间
        self.last_modified_time = last_modified_time
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListServiceVersionsResponseBody(TeaModel):
    def __init__(
        self,
        direction: str = None,
        next_token: str = None,
        versions: List[ListServiceVersionsResponseBodyVersions] = None,
    ):
        # 排序方向
        self.direction = direction
        # 下次查询token
        self.next_token = next_token
        # 版本列表
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = ListServiceVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListServiceVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # 最多返回个数
        self.limit = limit
        # 下次查询token
        self.next_token = next_token
        # 前缀
        self.prefix = prefix
        # 起始key
        self.start_key = start_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        role: str = None,
        service_id: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        vpc_config: VPCConfig = None,
    ):
        # 创建时间
        self.created_time = created_time
        # 服务描述
        self.description = description
        # 公网访问设置
        self.internet_access = internet_access
        # 上次更新时间
        self.last_modified_time = last_modified_time
        self.log_config = log_config
        self.nas_config = nas_config
        # 服务角色
        self.role = role
        # 服务ID
        self.service_id = service_id
        # 服务信息
        self.service_name = service_name
        self.tracing_config = tracing_config
        self.vpc_config = vpc_config

    def validate(self):
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        services: List[ListServicesResponseBodyServices] = None,
    ):
        # 下次查询token
        self.next_token = next_token
        # 服务列表
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatefulAsyncInvocationFunctionsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # 您的阿里云账号（主账号）ID。
        self.x_fc_account_id = x_fc_account_id
        # 发起API调用的日期，用于对请求签名。格式为yyyy-mm-ddhh:mm:ss。
        self.x_fc_date = x_fc_date
        # 用于链路追踪的ID。
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListStatefulAsyncInvocationFunctionsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
    ):
        # 限定此次返回资源的数量。如果不设定，默认返回20，最大不能超过100。返回结果可以小于指定的数量，但不会多于指定的数量。
        self.limit = limit
        # 用来标记当前开始读取的位置，置空表示从头开始。第一次查询不需要提供这个参数，后续查询的Token从前一次查询的返回结果中获取。
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListStatefulAsyncInvocationFunctionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AsyncConfigMeta] = None,
        next_token: str = None,
    ):
        # 返回的实际数据列表。
        self.data = data
        # 用来表示当前调用返回读取到的位置，空代表数据已经读取完毕。
        self.next_token = next_token

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = AsyncConfigMeta()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListStatefulAsyncInvocationFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStatefulAsyncInvocationFunctionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStatefulAsyncInvocationFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatefulAsyncInvocationsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_code_checksum = x_fc_code_checksum
        self.x_fc_date = x_fc_date
        self.x_fc_invocation_type = x_fc_invocation_type
        self.x_fc_log_type = x_fc_log_type
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListStatefulAsyncInvocationsRequest(TeaModel):
    def __init__(
        self,
        include_payload: bool = None,
        invocation_id_prefix: str = None,
        limit: int = None,
        next_token: str = None,
        qualifier: str = None,
        sort_order_by_time: str = None,
        started_time_begin: int = None,
        started_time_end: int = None,
        status: str = None,
    ):
        self.include_payload = include_payload
        self.invocation_id_prefix = invocation_id_prefix
        self.limit = limit
        self.next_token = next_token
        self.qualifier = qualifier
        self.sort_order_by_time = sort_order_by_time
        self.started_time_begin = started_time_begin
        self.started_time_end = started_time_end
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_payload is not None:
            result['includePayload'] = self.include_payload
        if self.invocation_id_prefix is not None:
            result['invocationIdPrefix'] = self.invocation_id_prefix
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.sort_order_by_time is not None:
            result['sortOrderByTime'] = self.sort_order_by_time
        if self.started_time_begin is not None:
            result['startedTimeBegin'] = self.started_time_begin
        if self.started_time_end is not None:
            result['startedTimeEnd'] = self.started_time_end
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includePayload') is not None:
            self.include_payload = m.get('includePayload')
        if m.get('invocationIdPrefix') is not None:
            self.invocation_id_prefix = m.get('invocationIdPrefix')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sortOrderByTime') is not None:
            self.sort_order_by_time = m.get('sortOrderByTime')
        if m.get('startedTimeBegin') is not None:
            self.started_time_begin = m.get('startedTimeBegin')
        if m.get('startedTimeEnd') is not None:
            self.started_time_end = m.get('startedTimeEnd')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListStatefulAsyncInvocationsResponseBody(TeaModel):
    def __init__(
        self,
        invocations: List[StatefulAsyncInvocation] = None,
        next_token: str = None,
    ):
        self.invocations = invocations
        self.next_token = next_token

    def validate(self):
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['invocations'] = []
        if self.invocations is not None:
            for k in self.invocations:
                result['invocations'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocations = []
        if m.get('invocations') is not None:
            for k in m.get('invocations'):
                temp_model = StatefulAsyncInvocation()
                self.invocations.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListStatefulAsyncInvocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStatefulAsyncInvocationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStatefulAsyncInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaggedResourcesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListTaggedResourcesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
    ):
        self.limit = limit
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListTaggedResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resources: List[Resource] = None,
    ):
        self.next_token = next_token
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = Resource()
                self.resources.append(temp_model.from_map(k))
        return self


class ListTaggedResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTaggedResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTaggedResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTriggersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListTriggersRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        start_key: str = None,
    ):
        # 限定此次返回资源的数量。如果不设定，默认返回20，最大不能超过100。返回结果可能小于指定的数量，但不会多于指定的数量
        self.limit = limit
        # 用来返回更多结果。第一次查询不需要提供这个参数，后续查询的token从返回结果中获取
        self.next_token = next_token
        # 限定返回的资源名称必须以prefix作为前缀
        self.prefix = prefix
        # 设定结果从startKey之后（包括startKey）按字母排序的第一个开始返回
        self.start_key = start_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListTriggersResponseBodyTriggers(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        domain_name: str = None,
        invocation_role: str = None,
        last_modified_time: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        # 创建时间
        self.created_time = created_time
        self.description = description
        # 域名名称，使用域名名称拼接上函数计算域名，可以采用HTTP协议调用到触发器对应版本的函数。例如{domainName}.cn-shanghai.fc.aliyuncs.com
        self.domain_name = domain_name
        # 调用函数使用的RAM角色的ARN
        self.invocation_role = invocation_role
        # 上次修改时间
        self.last_modified_time = last_modified_time
        # service版本
        self.qualifier = qualifier
        # event source的Aliyun Resource Name（ARN
        self.source_arn = source_arn
        # trigger配置对象
        self.trigger_config = trigger_config
        self.trigger_id = trigger_id
        # trigger名称
        self.trigger_name = trigger_name
        # trigger类型，如 oss, log, tablestore, timer, http, cdn_events, mns_topic
        self.trigger_type = trigger_type
        # 公网域名地址。在互联网可以通过HTTP协议或者HTTPS协议访问HTTP Trigger。
        self.url_internet = url_internet
        # 私网域名地址。在VPC可以通过HTTP协议或者HTTPS协议访问HTTP Trigger。
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class ListTriggersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        triggers: List[ListTriggersResponseBodyTriggers] = None,
    ):
        # 用来返回更多的查询结果。如果这个值没有返回，则说明没有更多结果
        self.next_token = next_token
        # Trigger列表
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.triggers = []
        if m.get('triggers') is not None:
            for k in m.get('triggers'):
                temp_model = ListTriggersResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListTriggersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTriggersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTriggersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcBindingsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListVpcBindingsResponseBody(TeaModel):
    def __init__(
        self,
        vpc_ids: List[str] = None,
    ):
        self.vpc_ids = vpc_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_ids is not None:
            result['vpcIds'] = self.vpc_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpcIds') is not None:
            self.vpc_ids = m.get('vpcIds')
        return self


class ListVpcBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVpcBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVpcBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishServiceVersionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # 服务的ETag，可通过GetService接口获得。若发布版本时服务的ETag与传入的不一致，则发布版本会失败。
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PublishServiceVersionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        # 版本描述
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class PublishServiceVersionResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        # 创建时间
        self.created_time = created_time
        # 版本描述
        self.description = description
        # 上次更新时间
        self.last_modified_time = last_modified_time
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class PublishServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishServiceVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutFunctionAsyncInvokeConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutFunctionAsyncInvokeConfigRequest(TeaModel):
    def __init__(
        self,
        destination_config: DestinationConfig = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
        stateful_invocation: bool = None,
        qualifier: str = None,
    ):
        self.destination_config = destination_config
        # 消息最大存活时长
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # 异步调用失败后的最大重试次数
        self.max_async_retry_attempts = max_async_retry_attempts
        self.stateful_invocation = stateful_invocation
        # 别名或版本
        self.qualifier = qualifier

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutFunctionAsyncInvokeConfigResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        destination_config: DestinationConfig = None,
        function: str = None,
        last_modified_time: str = None,
        max_async_event_age_in_seconds: int = None,
        max_async_retry_attempts: int = None,
        qualifier: str = None,
        service: str = None,
        stateful_invocation: bool = None,
    ):
        # 创建时间
        self.created_time = created_time
        self.destination_config = destination_config
        # 函数名称
        self.function = function
        # 最后更改时间
        self.last_modified_time = last_modified_time
        # 消息最大存活时长
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds
        # 异步调用失败后的最大重试次数
        self.max_async_retry_attempts = max_async_retry_attempts
        # 限定符
        self.qualifier = qualifier
        # 服务名称
        self.service = service
        self.stateful_invocation = stateful_invocation

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function is not None:
            result['function'] = self.function
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service is not None:
            result['service'] = self.service
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        return self


class PutFunctionAsyncInvokeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutFunctionAsyncInvokeConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutFunctionAsyncInvokeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutFunctionOnDemandConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutFunctionOnDemandConfigRequest(TeaModel):
    def __init__(
        self,
        maximum_instance_count: int = None,
        qualifier: str = None,
    ):
        self.maximum_instance_count = maximum_instance_count
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutFunctionOnDemandConfigResponseBody(TeaModel):
    def __init__(
        self,
        maximum_instance_count: int = None,
        resource: str = None,
    ):
        self.maximum_instance_count = maximum_instance_count
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class PutFunctionOnDemandConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutFunctionOnDemandConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutFunctionOnDemandConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutProvisionConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutProvisionConfigRequest(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        scheduled_actions: List[ScheduledActions] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicies] = None,
        qualifier: str = None,
    ):
        # 当实例进入空闲状态时，是否继续分配CPU。
        self.always_allocate_cpu = always_allocate_cpu
        # 定时策略配置
        self.scheduled_actions = scheduled_actions
        # 预留的目标资源个数
        self.target = target
        # 指标追踪伸缩策略配置
        self.target_tracking_policies = target_tracking_policies
        # 别名名称
        self.qualifier = qualifier

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()
        if self.target_tracking_policies:
            for k in self.target_tracking_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        result['targetTrackingPolicies'] = []
        if self.target_tracking_policies is not None:
            for k in self.target_tracking_policies:
                result['targetTrackingPolicies'].append(k.to_map() if k else None)
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutProvisionConfigResponseBody(TeaModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        current: int = None,
        resource: str = None,
        scheduled_actions: List[ScheduledActions] = None,
        target: int = None,
        target_tracking_policies: List[TargetTrackingPolicies] = None,
    ):
        # 是否始终分配CPU给函数实例。
        self.always_allocate_cpu = always_allocate_cpu
        # 实际资源个数
        self.current = current
        # 资源描述
        self.resource = resource
        # 定时策略配置
        self.scheduled_actions = scheduled_actions
        # 目标资源个数
        self.target = target
        # 指标追踪伸缩策略配置
        self.target_tracking_policies = target_tracking_policies

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()
        if self.target_tracking_policies:
            for k in self.target_tracking_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        if self.current is not None:
            result['current'] = self.current
        if self.resource is not None:
            result['resource'] = self.resource
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        result['targetTrackingPolicies'] = []
        if self.target_tracking_policies is not None:
            for k in self.target_tracking_policies:
                result['targetTrackingPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class PutProvisionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutProvisionConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutProvisionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterEventSourceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class RegisterEventSourceRequest(TeaModel):
    def __init__(
        self,
        source_arn: str = None,
        qualifier: str = None,
    ):
        # 事件源资源标识符
        self.source_arn = source_arn
        # 别名或版本
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class RegisterEventSourceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        source_arn: str = None,
    ):
        # 创建时间
        self.created_time = created_time
        # 事件源资源标识符
        self.source_arn = source_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        return self


class RegisterEventSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterEventSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RegisterEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopStatefulAsyncInvocationHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class StopStatefulAsyncInvocationRequest(TeaModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class StopStatefulAsyncInvocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class TagResourceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class TagResourceRequest(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        self.resource_arn = resource_arn
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class TagResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UntagResourceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UntagResourceRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_arn: str = None,
        tag_keys: List[str] = None,
    ):
        # 删除所有 tag，默认值为 false
        self.all = all
        # 目前只能给 top level 资源 service 进行标签的相关操作, ARN 可以是类似 services/foo 或者 acs:fc:cn-shanghai:123456789:services/foo
        self.resource_arn = resource_arn
        # tag key 值列表， 最大为 20，当 all=false， length 至少为 1. 当 length 大于 1 时， 可以忽略 all 值
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tag_keys is not None:
            result['tagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tagKeys') is not None:
            self.tag_keys = m.get('tagKeys')
        return self


class UntagResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateAliasHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateAliasRequest(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        description: str = None,
        version_id: str = None,
    ):
        # 额外版本权重
        self.additional_version_weight = additional_version_weight
        # 别名描述
        self.description = description
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.description is not None:
            result['description'] = self.description
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class UpdateAliasResponseBody(TeaModel):
    def __init__(
        self,
        additional_version_weight: Dict[str, float] = None,
        alias_name: str = None,
        created_time: str = None,
        description: str = None,
        last_modified_time: str = None,
        version_id: str = None,
    ):
        # 额外版本权重
        self.additional_version_weight = additional_version_weight
        # 别名名称
        self.alias_name = alias_name
        # 创建时间
        self.created_time = created_time
        # 别名描述
        self.description = description
        # 上次更新时间
        self.last_modified_time = last_modified_time
        # 版本ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class UpdateAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAliasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomDomainHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateCustomDomainRequest(TeaModel):
    def __init__(
        self,
        cert_config: CertConfig = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
    ):
        self.cert_config = cert_config
        self.protocol = protocol
        self.route_config = route_config
        self.tls_config = tls_config

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        return self


class UpdateCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        cert_config: CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: RouteConfig = None,
        tls_config: TLSConfig = None,
    ):
        self.account_id = account_id
        self.api_version = api_version
        self.cert_config = cert_config
        self.created_time = created_time
        self.domain_name = domain_name
        self.last_modified_time = last_modified_time
        self.protocol = protocol
        self.route_config = route_config
        self.tls_config = tls_config

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        return self


class UpdateCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_code_checksum: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # 用于确保实际更改的资源和期望更改的资源是一致的，该值来自Create，Get和Update API的响应
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_code_checksum = x_fc_code_checksum
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(
        self,
        instance_concurrency: int = None,
        ca_port: int = None,
        code: Code = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        layers: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        self.instance_concurrency = instance_concurrency
        # 自定义、自定义容器运行时 HTTP Server 的监听端口
        self.ca_port = ca_port
        self.code = code
        self.custom_container_config = custom_container_config
        # 函数自定义DNS配置
        self.custom_dns = custom_dns
        # Custom Runtime函数详细配置
        self.custom_runtime_config = custom_runtime_config
        # 函数描述
        self.description = description
        # 为函数设置的环境变量，可以在函数中获取环境变量的值
        self.environment_variables = environment_variables
        # function执行的入口，具体格式和语言相关
        self.handler = handler
        # 初始化function运行的超时时间，单位为秒，最小1秒，默认3秒。初始化function超过这个时间后会被终止执行
        self.initialization_timeout = initialization_timeout
        # 初始化 function 执行的入口，具体格式和语言相关
        self.initializer = initializer
        self.instance_lifecycle_config = instance_lifecycle_config
        self.instance_soft_concurrency = instance_soft_concurrency
        self.instance_type = instance_type
        self.layers = layers
        # function的内存规格，单位为MB，为64MB的倍数
        self.memory_size = memory_size
        # runtime
        self.runtime = runtime
        # function运行的超时时间，单位为秒，最小1秒，默认3秒。function超过这个时间后会被终止执行
        self.timeout = timeout

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('code') is not None:
            temp_model = Code()
            self.code = temp_model.from_map(m['code'])
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        ca_port: int = None,
        code_checksum: str = None,
        code_size: int = None,
        created_time: str = None,
        custom_container_config: CustomContainerConfig = None,
        custom_dns: CustomDNS = None,
        custom_runtime_config: CustomRuntimeConfig = None,
        description: str = None,
        environment_variables: Dict[str, str] = None,
        function_id: str = None,
        function_name: str = None,
        handler: str = None,
        initialization_timeout: int = None,
        initializer: str = None,
        instance_lifecycle_config: InstanceLifecycleConfig = None,
        instance_soft_concurrency: int = None,
        instance_type: str = None,
        last_modified_time: str = None,
        layers: List[str] = None,
        memory_size: int = None,
        runtime: str = None,
        timeout: int = None,
    ):
        # 自定义、自定义容器运行时 HTTP Server 的监听端口
        self.ca_port = ca_port
        # function code包的CRC64值
        self.code_checksum = code_checksum
        # 系统返回的function的code包大小，单位为byte Example : 1024
        self.code_size = code_size
        # function创建时间
        self.created_time = created_time
        self.custom_container_config = custom_container_config
        # 函数自定义DNS配置
        self.custom_dns = custom_dns
        # Custom Runtime函数详细配置
        self.custom_runtime_config = custom_runtime_config
        # 函数描述
        self.description = description
        # 为函数设置的环境变量，可以在函数中获取环境变量的值
        self.environment_variables = environment_variables
        # 系统为每个function生成的唯一ID
        self.function_id = function_id
        # 函数名称
        self.function_name = function_name
        # function的执行入口
        self.handler = handler
        # 初始化function运行的超时时间，单位为秒，最小1秒，默认3秒。初始化function超过这个时间后会被终止执行
        self.initialization_timeout = initialization_timeout
        # 初始化 function 执行的入口，具体格式和语言相关
        self.initializer = initializer
        self.instance_lifecycle_config = instance_lifecycle_config
        self.instance_soft_concurrency = instance_soft_concurrency
        self.instance_type = instance_type
        # function上次修改时间
        self.last_modified_time = last_modified_time
        self.layers = layers
        # function设置的内存大小，单位为MB
        self.memory_size = memory_size
        # function运行的语言环境，目前支持nodejs6, nodejs8, python2.7, python3, java8
        self.runtime = runtime
        # 运行的超时时间，单位为秒
        self.timeout = timeout

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.code_size is not None:
            result['codeSize'] = self.code_size
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # 用于确保实际更改的资源和期望更改的资源是一致的，该值来自Create，Get和Update API的响应
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        internet_access: bool = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        role: str = None,
        tracing_config: TracingConfig = None,
        vpc_config: VPCConfig = None,
    ):
        # 服务描述
        self.description = description
        # 公网访问设置
        self.internet_access = internet_access
        self.log_config = log_config
        self.nas_config = nas_config
        # 服务角色
        self.role = role
        self.tracing_config = tracing_config
        self.vpc_config = vpc_config

    def validate(self):
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        internet_access: bool = None,
        last_modified_time: str = None,
        log_config: LogConfig = None,
        nas_config: NASConfig = None,
        role: str = None,
        service_id: str = None,
        service_name: str = None,
        tracing_config: TracingConfig = None,
        vendor_config: VendorConfig = None,
        vpc_config: VPCConfig = None,
    ):
        # 创建时间
        self.created_time = created_time
        # 服务描述
        self.description = description
        # 公网访问设置
        self.internet_access = internet_access
        # 上次更新时间
        self.last_modified_time = last_modified_time
        self.log_config = log_config
        self.nas_config = nas_config
        # 服务角色
        self.role = role
        # 服务ID
        self.service_id = service_id
        # 服务名称
        self.service_name = service_name
        self.tracing_config = tracing_config
        self.vendor_config = vendor_config
        self.vpc_config = vpc_config

    def validate(self):
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vendor_config:
            self.vendor_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vendorConfig') is not None:
            temp_model = VendorConfig()
            self.vendor_config = temp_model.from_map(m['vendorConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        if_match: str = None,
        x_fc_account_id: str = None,
        x_fc_date: str = None,
        x_fc_trace_id: str = None,
    ):
        self.common_headers = common_headers
        # 用于确保实际更改的资源和期望更改的资源是一致的，该值来自Create，Get和Update API的响应
        self.if_match = if_match
        self.x_fc_account_id = x_fc_account_id
        self.x_fc_date = x_fc_date
        self.x_fc_trace_id = x_fc_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateTriggerRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        invocation_role: str = None,
        qualifier: str = None,
        trigger_config: str = None,
    ):
        self.description = description
        # event source，如OSS，使用该role去invoke function
        self.invocation_role = invocation_role
        # service版本
        self.qualifier = qualifier
        # trigger配置，针对不同的trigger类型，trigger配置会有所不同
        self.trigger_config = trigger_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        return self


class UpdateTriggerResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        domain_name: str = None,
        invocation_role: str = None,
        last_modified_time: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        # 创建时间
        self.created_time = created_time
        self.description = description
        # 域名名称，使用域名名称拼接上函数计算域名，可以采用HTTP协议调用到触发器对应版本的函数。例如{domainName}.cn-shanghai.fc.aliyuncs.com
        self.domain_name = domain_name
        # 调用函数使用的RAM角色的ARN
        self.invocation_role = invocation_role
        # 上次修改时间
        self.last_modified_time = last_modified_time
        # service版本
        self.qualifier = qualifier
        # event source的Aliyun Resource Name（ARN
        self.source_arn = source_arn
        # trigger配置对象
        self.trigger_config = trigger_config
        self.trigger_id = trigger_id
        # trigger名称
        self.trigger_name = trigger_name
        # trigger类型，如 oss, log, tablestore, timer, http, cdn_events, mns_topic
        self.trigger_type = trigger_type
        # 公网域名地址。在互联网可以通过HTTP协议或者HTTPS协议访问HTTP Trigger。
        self.url_internet = url_internet
        # 私网域名地址。在VPC可以通过HTTP协议或者HTTPS协议访问HTTP Trigger。
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class UpdateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


