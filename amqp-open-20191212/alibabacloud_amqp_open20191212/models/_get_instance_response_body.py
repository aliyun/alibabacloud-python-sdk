# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_renew_instance: bool = None,
        classic_endpoint: str = None,
        edition: str = None,
        encrypted_instance: bool = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        kms_key_id: str = None,
        max_connections: int = None,
        max_eip_tps: int = None,
        max_queue: int = None,
        max_tps: int = None,
        max_vhost: int = None,
        order_create_time: int = None,
        order_type: str = None,
        private_endpoint: str = None,
        provisioned_capacity: int = None,
        public_endpoint: str = None,
        resource_group_id: str = None,
        status: str = None,
        storage_size: int = None,
        support_eip: bool = None,
        support_tracing: bool = None,
        tags: List[main_models.GetInstanceResponseBodyDataTags] = None,
        tracing_storage_time: int = None,
    ):
        self.auto_renew_instance = auto_renew_instance
        self.classic_endpoint = classic_endpoint
        self.edition = edition
        self.encrypted_instance = encrypted_instance
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.kms_key_id = kms_key_id
        self.max_connections = max_connections
        self.max_eip_tps = max_eip_tps
        self.max_queue = max_queue
        self.max_tps = max_tps
        self.max_vhost = max_vhost
        self.order_create_time = order_create_time
        self.order_type = order_type
        self.private_endpoint = private_endpoint
        self.provisioned_capacity = provisioned_capacity
        self.public_endpoint = public_endpoint
        self.resource_group_id = resource_group_id
        self.status = status
        self.storage_size = storage_size
        self.support_eip = support_eip
        self.support_tracing = support_tracing
        self.tags = tags
        self.tracing_storage_time = tracing_storage_time

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew_instance is not None:
            result['AutoRenewInstance'] = self.auto_renew_instance

        if self.classic_endpoint is not None:
            result['ClassicEndpoint'] = self.classic_endpoint

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.encrypted_instance is not None:
            result['EncryptedInstance'] = self.encrypted_instance

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_eip_tps is not None:
            result['MaxEipTps'] = self.max_eip_tps

        if self.max_queue is not None:
            result['MaxQueue'] = self.max_queue

        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps

        if self.max_vhost is not None:
            result['MaxVhost'] = self.max_vhost

        if self.order_create_time is not None:
            result['OrderCreateTime'] = self.order_create_time

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.private_endpoint is not None:
            result['PrivateEndpoint'] = self.private_endpoint

        if self.provisioned_capacity is not None:
            result['ProvisionedCapacity'] = self.provisioned_capacity

        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.support_eip is not None:
            result['SupportEIP'] = self.support_eip

        if self.support_tracing is not None:
            result['SupportTracing'] = self.support_tracing

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tracing_storage_time is not None:
            result['TracingStorageTime'] = self.tracing_storage_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewInstance') is not None:
            self.auto_renew_instance = m.get('AutoRenewInstance')

        if m.get('ClassicEndpoint') is not None:
            self.classic_endpoint = m.get('ClassicEndpoint')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('EncryptedInstance') is not None:
            self.encrypted_instance = m.get('EncryptedInstance')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxEipTps') is not None:
            self.max_eip_tps = m.get('MaxEipTps')

        if m.get('MaxQueue') is not None:
            self.max_queue = m.get('MaxQueue')

        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')

        if m.get('MaxVhost') is not None:
            self.max_vhost = m.get('MaxVhost')

        if m.get('OrderCreateTime') is not None:
            self.order_create_time = m.get('OrderCreateTime')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PrivateEndpoint') is not None:
            self.private_endpoint = m.get('PrivateEndpoint')

        if m.get('ProvisionedCapacity') is not None:
            self.provisioned_capacity = m.get('ProvisionedCapacity')

        if m.get('PublicEndpoint') is not None:
            self.public_endpoint = m.get('PublicEndpoint')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SupportEIP') is not None:
            self.support_eip = m.get('SupportEIP')

        if m.get('SupportTracing') is not None:
            self.support_tracing = m.get('SupportTracing')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetInstanceResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TracingStorageTime') is not None:
            self.tracing_storage_time = m.get('TracingStorageTime')

        return self

class GetInstanceResponseBodyDataTags(DaraModel):
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

