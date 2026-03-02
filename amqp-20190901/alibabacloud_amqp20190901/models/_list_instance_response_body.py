# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class ListInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListInstanceResponseBodyData = None,
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
            temp_model = main_models.ListInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstanceResponseBodyDataInstances] = None,
    ):
        self.instances = instances

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstanceResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k1))

        return self

class ListInstanceResponseBodyDataInstances(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        classic_endpoint: str = None,
        expire: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        max_eiptps: int = None,
        max_queue: int = None,
        max_tps: int = None,
        max_vhost: int = None,
        order_create: int = None,
        order_type: str = None,
        private_endpoint: str = None,
        public_endpoint: str = None,
        status: str = None,
        storage_size: int = None,
        support_eip: bool = None,
        tags: main_models.ListInstanceResponseBodyDataInstancesTags = None,
    ):
        self.auto_renew = auto_renew
        self.classic_endpoint = classic_endpoint
        self.expire = expire
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.max_eiptps = max_eiptps
        self.max_queue = max_queue
        self.max_tps = max_tps
        self.max_vhost = max_vhost
        self.order_create = order_create
        self.order_type = order_type
        self.private_endpoint = private_endpoint
        self.public_endpoint = public_endpoint
        self.status = status
        self.storage_size = storage_size
        self.support_eip = support_eip
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.classic_endpoint is not None:
            result['ClassicEndpoint'] = self.classic_endpoint

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_eiptps is not None:
            result['MaxEIPTPS'] = self.max_eiptps

        if self.max_queue is not None:
            result['MaxQueue'] = self.max_queue

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

        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.support_eip is not None:
            result['SupportEIP'] = self.support_eip

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClassicEndpoint') is not None:
            self.classic_endpoint = m.get('ClassicEndpoint')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxEIPTPS') is not None:
            self.max_eiptps = m.get('MaxEIPTPS')

        if m.get('MaxQueue') is not None:
            self.max_queue = m.get('MaxQueue')

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

        if m.get('PublicEndpoint') is not None:
            self.public_endpoint = m.get('PublicEndpoint')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SupportEIP') is not None:
            self.support_eip = m.get('SupportEIP')

        if m.get('Tags') is not None:
            temp_model = main_models.ListInstanceResponseBodyDataInstancesTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class ListInstanceResponseBodyDataInstancesTags(DaraModel):
    def __init__(
        self,
        tags: List[main_models.ListInstanceResponseBodyDataInstancesTagsTags] = None,
    ):
        self.tags = tags

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
        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListInstanceResponseBodyDataInstancesTagsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListInstanceResponseBodyDataInstancesTagsTags(DaraModel):
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

