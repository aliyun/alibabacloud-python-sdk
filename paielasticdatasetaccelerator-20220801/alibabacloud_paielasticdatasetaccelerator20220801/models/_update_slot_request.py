# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from darabonba.model import DaraModel

class UpdateSlotRequest(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        description: str = None,
        life_cycle: main_models.SlotLifeCycle = None,
        name: str = None,
        storage_type: str = None,
        storage_uri: str = None,
        tags: List[main_models.UpdateSlotRequestTags] = None,
    ):
        # This parameter is required.
        self.capacity = capacity
        self.description = description
        self.life_cycle = life_cycle
        self.name = name
        # This parameter is required.
        self.storage_type = storage_type
        # This parameter is required.
        self.storage_uri = storage_uri
        self.tags = tags

    def validate(self):
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
                temp_model = main_models.UpdateSlotRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class UpdateSlotRequestTags(DaraModel):
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

