# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from darabonba.model import DaraModel

class CreateSlotRequest(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        description: str = None,
        endpoint_ids: str = None,
        endpoints: List[main_models.CreateSlotRequestEndpoints] = None,
        instance_id: str = None,
        io_type: str = None,
        life_cycle: main_models.SlotLifeCycle = None,
        name: str = None,
        storage_type: str = None,
        storage_uri: str = None,
        tags: List[main_models.CreateSlotRequestTags] = None,
    ):
        # This parameter is required.
        self.capacity = capacity
        self.description = description
        self.endpoint_ids = endpoint_ids
        self.endpoints = endpoints
        # This parameter is required.
        self.instance_id = instance_id
        self.io_type = io_type
        self.life_cycle = life_cycle
        self.name = name
        # This parameter is required.
        self.storage_type = storage_type
        # This parameter is required.
        self.storage_uri = storage_uri
        self.tags = tags

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.life_cycle:
            self.life_cycle.validate()
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

        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.io_type is not None:
            result['IoType'] = self.io_type

        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_uri is not None:
            result['StorageUri'] = self.storage_uri

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.CreateSlotRequestEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IoType') is not None:
            self.io_type = m.get('IoType')

        if m.get('LifeCycle') is not None:
            temp_model = main_models.SlotLifeCycle()
            self.life_cycle = temp_model.from_map(m.get('LifeCycle'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageUri') is not None:
            self.storage_uri = m.get('StorageUri')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateSlotRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateSlotRequestTags(DaraModel):
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

class CreateSlotRequestEndpoints(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.name = name
        self.type = type
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

