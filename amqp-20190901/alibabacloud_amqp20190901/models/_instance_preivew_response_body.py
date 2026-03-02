# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class InstancePreivewResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.InstancePreivewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.InstancePreivewResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class InstancePreivewResponseBodyData(DaraModel):
    def __init__(
        self,
        exchange_num: int = None,
        instance_num: int = None,
        instances: main_models.InstancePreivewResponseBodyDataInstances = None,
        queue_num: int = None,
        vhost_num: int = None,
    ):
        self.exchange_num = exchange_num
        self.instance_num = instance_num
        self.instances = instances
        self.queue_num = queue_num
        self.vhost_num = vhost_num

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exchange_num is not None:
            result['ExchangeNum'] = self.exchange_num

        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num

        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.queue_num is not None:
            result['QueueNum'] = self.queue_num

        if self.vhost_num is not None:
            result['VhostNum'] = self.vhost_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExchangeNum') is not None:
            self.exchange_num = m.get('ExchangeNum')

        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')

        if m.get('Instances') is not None:
            temp_model = main_models.InstancePreivewResponseBodyDataInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('QueueNum') is not None:
            self.queue_num = m.get('QueueNum')

        if m.get('VhostNum') is not None:
            self.vhost_num = m.get('VhostNum')

        return self

class InstancePreivewResponseBodyDataInstances(DaraModel):
    def __init__(
        self,
        instances_vo: List[main_models.InstancePreivewResponseBodyDataInstancesInstancesVO] = None,
    ):
        self.instances_vo = instances_vo

    def validate(self):
        if self.instances_vo:
            for v1 in self.instances_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstancesVO'] = []
        if self.instances_vo is not None:
            for k1 in self.instances_vo:
                result['InstancesVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances_vo = []
        if m.get('InstancesVO') is not None:
            for k1 in m.get('InstancesVO'):
                temp_model = main_models.InstancePreivewResponseBodyDataInstancesInstancesVO()
                self.instances_vo.append(temp_model.from_map(k1))

        return self

class InstancePreivewResponseBodyDataInstancesInstancesVO(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        cease_status: bool = None,
        classic_endpoint: str = None,
        enable_dlq_ttl: bool = None,
        encrypted: bool = None,
        expire: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        invisible_time: int = None,
        kms_key_id: str = None,
        listener_mode: str = None,
        max_binding_count: int = None,
        max_connection_channel_count: int = None,
        max_connection_count: int = None,
        max_consume_retry_time: int = None,
        max_eiptps: int = None,
        max_exchange_count: int = None,
        max_msg_body_byte: int = None,
        max_msg_delay_hour: int = None,
        max_msg_trace_time: int = None,
        max_queue: int = None,
        max_queue_consumer_count: int = None,
        max_retry_interval: int = None,
        max_retry_times: int = None,
        max_tps: int = None,
        max_vhost: int = None,
        order_create: int = None,
        order_type: str = None,
        private_endpoint: str = None,
        private_endpoint_type: str = None,
        public_endpoint: str = None,
        pvl_params: main_models.InstancePreivewResponseBodyDataInstancesInstancesVOPvlParams = None,
        resource_group_id: str = None,
        serverless_rate: float = None,
        serverless_switch: bool = None,
        status: str = None,
        storage_size: int = None,
        support_eip: bool = None,
        support_msg_trace: bool = None,
        support_open_source_auth: bool = None,
        tags: main_models.InstancePreivewResponseBodyDataInstancesInstancesVOTags = None,
        used_queue: int = None,
        used_vhost: int = None,
        version: int = None,
    ):
        self.auto_renew = auto_renew
        self.cease_status = cease_status
        self.classic_endpoint = classic_endpoint
        self.enable_dlq_ttl = enable_dlq_ttl
        self.encrypted = encrypted
        self.expire = expire
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.invisible_time = invisible_time
        self.kms_key_id = kms_key_id
        self.listener_mode = listener_mode
        self.max_binding_count = max_binding_count
        self.max_connection_channel_count = max_connection_channel_count
        self.max_connection_count = max_connection_count
        self.max_consume_retry_time = max_consume_retry_time
        self.max_eiptps = max_eiptps
        self.max_exchange_count = max_exchange_count
        self.max_msg_body_byte = max_msg_body_byte
        self.max_msg_delay_hour = max_msg_delay_hour
        self.max_msg_trace_time = max_msg_trace_time
        self.max_queue = max_queue
        self.max_queue_consumer_count = max_queue_consumer_count
        self.max_retry_interval = max_retry_interval
        self.max_retry_times = max_retry_times
        self.max_tps = max_tps
        self.max_vhost = max_vhost
        self.order_create = order_create
        self.order_type = order_type
        self.private_endpoint = private_endpoint
        self.private_endpoint_type = private_endpoint_type
        self.public_endpoint = public_endpoint
        self.pvl_params = pvl_params
        self.resource_group_id = resource_group_id
        self.serverless_rate = serverless_rate
        self.serverless_switch = serverless_switch
        self.status = status
        self.storage_size = storage_size
        self.support_eip = support_eip
        self.support_msg_trace = support_msg_trace
        self.support_open_source_auth = support_open_source_auth
        self.tags = tags
        self.used_queue = used_queue
        self.used_vhost = used_vhost
        self.version = version

    def validate(self):
        if self.pvl_params:
            self.pvl_params.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.cease_status is not None:
            result['CeaseStatus'] = self.cease_status

        if self.classic_endpoint is not None:
            result['ClassicEndpoint'] = self.classic_endpoint

        if self.enable_dlq_ttl is not None:
            result['EnableDlqTtl'] = self.enable_dlq_ttl

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.invisible_time is not None:
            result['InvisibleTime'] = self.invisible_time

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.listener_mode is not None:
            result['ListenerMode'] = self.listener_mode

        if self.max_binding_count is not None:
            result['MaxBindingCount'] = self.max_binding_count

        if self.max_connection_channel_count is not None:
            result['MaxConnectionChannelCount'] = self.max_connection_channel_count

        if self.max_connection_count is not None:
            result['MaxConnectionCount'] = self.max_connection_count

        if self.max_consume_retry_time is not None:
            result['MaxConsumeRetryTime'] = self.max_consume_retry_time

        if self.max_eiptps is not None:
            result['MaxEIPTPS'] = self.max_eiptps

        if self.max_exchange_count is not None:
            result['MaxExchangeCount'] = self.max_exchange_count

        if self.max_msg_body_byte is not None:
            result['MaxMsgBodyByte'] = self.max_msg_body_byte

        if self.max_msg_delay_hour is not None:
            result['MaxMsgDelayHour'] = self.max_msg_delay_hour

        if self.max_msg_trace_time is not None:
            result['MaxMsgTraceTime'] = self.max_msg_trace_time

        if self.max_queue is not None:
            result['MaxQueue'] = self.max_queue

        if self.max_queue_consumer_count is not None:
            result['MaxQueueConsumerCount'] = self.max_queue_consumer_count

        if self.max_retry_interval is not None:
            result['MaxRetryInterval'] = self.max_retry_interval

        if self.max_retry_times is not None:
            result['MaxRetryTimes'] = self.max_retry_times

        if self.max_tps is not None:
            result['MaxTPS'] = self.max_tps

        if self.max_vhost is not None:
            result['MaxVhost'] = self.max_vhost

        if self.order_create is not None:
            result['OrderCreate'] = self.order_create

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.private_endpoint is not None:
            result['PrivateEndpoint'] = self.private_endpoint

        if self.private_endpoint_type is not None:
            result['PrivateEndpointType'] = self.private_endpoint_type

        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint

        if self.pvl_params is not None:
            result['PvlParams'] = self.pvl_params.to_map()

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.serverless_rate is not None:
            result['ServerlessRate'] = self.serverless_rate

        if self.serverless_switch is not None:
            result['ServerlessSwitch'] = self.serverless_switch

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.support_eip is not None:
            result['SupportEIP'] = self.support_eip

        if self.support_msg_trace is not None:
            result['SupportMsgTrace'] = self.support_msg_trace

        if self.support_open_source_auth is not None:
            result['SupportOpenSourceAuth'] = self.support_open_source_auth

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.used_queue is not None:
            result['UsedQueue'] = self.used_queue

        if self.used_vhost is not None:
            result['UsedVhost'] = self.used_vhost

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('CeaseStatus') is not None:
            self.cease_status = m.get('CeaseStatus')

        if m.get('ClassicEndpoint') is not None:
            self.classic_endpoint = m.get('ClassicEndpoint')

        if m.get('EnableDlqTtl') is not None:
            self.enable_dlq_ttl = m.get('EnableDlqTtl')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InvisibleTime') is not None:
            self.invisible_time = m.get('InvisibleTime')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('ListenerMode') is not None:
            self.listener_mode = m.get('ListenerMode')

        if m.get('MaxBindingCount') is not None:
            self.max_binding_count = m.get('MaxBindingCount')

        if m.get('MaxConnectionChannelCount') is not None:
            self.max_connection_channel_count = m.get('MaxConnectionChannelCount')

        if m.get('MaxConnectionCount') is not None:
            self.max_connection_count = m.get('MaxConnectionCount')

        if m.get('MaxConsumeRetryTime') is not None:
            self.max_consume_retry_time = m.get('MaxConsumeRetryTime')

        if m.get('MaxEIPTPS') is not None:
            self.max_eiptps = m.get('MaxEIPTPS')

        if m.get('MaxExchangeCount') is not None:
            self.max_exchange_count = m.get('MaxExchangeCount')

        if m.get('MaxMsgBodyByte') is not None:
            self.max_msg_body_byte = m.get('MaxMsgBodyByte')

        if m.get('MaxMsgDelayHour') is not None:
            self.max_msg_delay_hour = m.get('MaxMsgDelayHour')

        if m.get('MaxMsgTraceTime') is not None:
            self.max_msg_trace_time = m.get('MaxMsgTraceTime')

        if m.get('MaxQueue') is not None:
            self.max_queue = m.get('MaxQueue')

        if m.get('MaxQueueConsumerCount') is not None:
            self.max_queue_consumer_count = m.get('MaxQueueConsumerCount')

        if m.get('MaxRetryInterval') is not None:
            self.max_retry_interval = m.get('MaxRetryInterval')

        if m.get('MaxRetryTimes') is not None:
            self.max_retry_times = m.get('MaxRetryTimes')

        if m.get('MaxTPS') is not None:
            self.max_tps = m.get('MaxTPS')

        if m.get('MaxVhost') is not None:
            self.max_vhost = m.get('MaxVhost')

        if m.get('OrderCreate') is not None:
            self.order_create = m.get('OrderCreate')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PrivateEndpoint') is not None:
            self.private_endpoint = m.get('PrivateEndpoint')

        if m.get('PrivateEndpointType') is not None:
            self.private_endpoint_type = m.get('PrivateEndpointType')

        if m.get('PublicEndpoint') is not None:
            self.public_endpoint = m.get('PublicEndpoint')

        if m.get('PvlParams') is not None:
            temp_model = main_models.InstancePreivewResponseBodyDataInstancesInstancesVOPvlParams()
            self.pvl_params = temp_model.from_map(m.get('PvlParams'))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServerlessRate') is not None:
            self.serverless_rate = m.get('ServerlessRate')

        if m.get('ServerlessSwitch') is not None:
            self.serverless_switch = m.get('ServerlessSwitch')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SupportEIP') is not None:
            self.support_eip = m.get('SupportEIP')

        if m.get('SupportMsgTrace') is not None:
            self.support_msg_trace = m.get('SupportMsgTrace')

        if m.get('SupportOpenSourceAuth') is not None:
            self.support_open_source_auth = m.get('SupportOpenSourceAuth')

        if m.get('Tags') is not None:
            temp_model = main_models.InstancePreivewResponseBodyDataInstancesInstancesVOTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UsedQueue') is not None:
            self.used_queue = m.get('UsedQueue')

        if m.get('UsedVhost') is not None:
            self.used_vhost = m.get('UsedVhost')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class InstancePreivewResponseBodyDataInstancesInstancesVOTags(DaraModel):
    def __init__(
        self,
        tags_vo: List[main_models.InstancePreivewResponseBodyDataInstancesInstancesVOTagsTagsVO] = None,
    ):
        self.tags_vo = tags_vo

    def validate(self):
        if self.tags_vo:
            for v1 in self.tags_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagsVO'] = []
        if self.tags_vo is not None:
            for k1 in self.tags_vo:
                result['TagsVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags_vo = []
        if m.get('TagsVO') is not None:
            for k1 in m.get('TagsVO'):
                temp_model = main_models.InstancePreivewResponseBodyDataInstancesInstancesVOTagsTagsVO()
                self.tags_vo.append(temp_model.from_map(k1))

        return self

class InstancePreivewResponseBodyDataInstancesInstancesVOTagsTagsVO(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class InstancePreivewResponseBodyDataInstancesInstancesVOPvlParams(DaraModel):
    def __init__(
        self,
        pvl_vo: List[main_models.InstancePreivewResponseBodyDataInstancesInstancesVOPvlParamsPvlVO] = None,
    ):
        self.pvl_vo = pvl_vo

    def validate(self):
        if self.pvl_vo:
            for v1 in self.pvl_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PvlVO'] = []
        if self.pvl_vo is not None:
            for k1 in self.pvl_vo:
                result['PvlVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pvl_vo = []
        if m.get('PvlVO') is not None:
            for k1 in m.get('PvlVO'):
                temp_model = main_models.InstancePreivewResponseBodyDataInstancesInstancesVOPvlParamsPvlVO()
                self.pvl_vo.append(temp_model.from_map(k1))

        return self

class InstancePreivewResponseBodyDataInstancesInstancesVOPvlParamsPvlVO(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

