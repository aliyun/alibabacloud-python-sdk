# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        # This parameter is required.
        self.request_id = request_id
        self.total_count = total_count

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        io_type: str = None,
        max_endpoint: int = None,
        max_slot: int = None,
        name: str = None,
        owner_id: str = None,
        payment_type: str = None,
        provider_type: str = None,
        status: main_models.InstanceStatus = None,
        storage_type: str = None,
        tags: List[main_models.ListInstancesResponseBodyInstancesTags] = None,
        type: str = None,
        user_id: str = None,
        uuid: str = None,
    ):
        self.capacity = capacity
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.io_type = io_type
        # 数据集加速实例的最大挂载点个数。
        self.max_endpoint = max_endpoint
        self.max_slot = max_slot
        self.name = name
        self.owner_id = owner_id
        self.payment_type = payment_type
        # 数据集加速实例的资源提供者类型。
        self.provider_type = provider_type
        self.status = status
        # 数据集加速实例的存储类型。
        self.storage_type = storage_type
        self.tags = tags
        self.type = type
        self.user_id = user_id
        self.uuid = uuid

    def validate(self):
        if self.status:
            self.status.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.io_type is not None:
            result['IoType'] = self.io_type

        if self.max_endpoint is not None:
            result['MaxEndpoint'] = self.max_endpoint

        if self.max_slot is not None:
            result['MaxSlot'] = self.max_slot

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        if self.status is not None:
            result['Status'] = self.status.to_map()

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('IoType') is not None:
            self.io_type = m.get('IoType')

        if m.get('MaxEndpoint') is not None:
            self.max_endpoint = m.get('MaxEndpoint')

        if m.get('MaxSlot') is not None:
            self.max_slot = m.get('MaxSlot')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        if m.get('Status') is not None:
            temp_model = main_models.InstanceStatus()
            self.status = temp_model.from_map(m.get('Status'))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListInstancesResponseBodyInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class ListInstancesResponseBodyInstancesTags(DaraModel):
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

