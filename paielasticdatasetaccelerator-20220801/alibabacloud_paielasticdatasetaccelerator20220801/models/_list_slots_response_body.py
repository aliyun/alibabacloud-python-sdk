# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from darabonba.model import DaraModel

class ListSlotsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        slots: List[main_models.ListSlotsResponseBodySlots] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.slots = slots
        self.total_count = total_count

    def validate(self):
        if self.slots:
            for v1 in self.slots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Slots'] = []
        if self.slots is not None:
            for k1 in self.slots:
                result['Slots'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.slots = []
        if m.get('Slots') is not None:
            for k1 in m.get('Slots'):
                temp_model = main_models.ListSlotsResponseBodySlots()
                self.slots.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSlotsResponseBodySlots(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        description: str = None,
        endpoints: List[main_models.ListSlotsResponseBodySlotsEndpoints] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        io_type: str = None,
        life_cycle: main_models.SlotLifeCycle = None,
        name: str = None,
        owner_id: str = None,
        status: main_models.SlotStatus = None,
        storage_type: str = None,
        storage_uri: str = None,
        tags: List[main_models.ListSlotsResponseBodySlotsTags] = None,
        user_id: str = None,
        uuid: str = None,
    ):
        self.capacity = capacity
        self.description = description
        self.endpoints = endpoints
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.instance_id = instance_id
        # 数据集加速槽的读写类型。
        self.io_type = io_type
        self.life_cycle = life_cycle
        self.name = name
        self.owner_id = owner_id
        self.status = status
        self.storage_type = storage_type
        self.storage_uri = storage_uri
        self.tags = tags
        self.user_id = user_id
        self.uuid = uuid

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.life_cycle:
            self.life_cycle.validate()
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

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.io_type is not None:
            result['IoType'] = self.io_type

        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.status is not None:
            result['Status'] = self.status.to_map()

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_uri is not None:
            result['StorageUri'] = self.storage_uri

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.ListSlotsResponseBodySlotsEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IoType') is not None:
            self.io_type = m.get('IoType')

        if m.get('LifeCycle') is not None:
            temp_model = main_models.SlotLifeCycle()
            self.life_cycle = temp_model.from_map(m.get('LifeCycle'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Status') is not None:
            temp_model = main_models.SlotStatus()
            self.status = temp_model.from_map(m.get('Status'))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUri') is not None:
            self.storage_uri = m.get('StorageUri')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListSlotsResponseBodySlotsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class ListSlotsResponseBodySlotsTags(DaraModel):
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

class ListSlotsResponseBodySlotsEndpoints(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        owner_id: str = None,
        status: main_models.EndpointStatus = None,
        type: str = None,
        user_id: str = None,
        uuid: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.owner_id = owner_id
        self.status = status
        self.type = type
        self.user_id = user_id
        self.uuid = uuid
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.status is not None:
            result['Status'] = self.status.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Status') is not None:
            temp_model = main_models.EndpointStatus()
            self.status = temp_model.from_map(m.get('Status'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

