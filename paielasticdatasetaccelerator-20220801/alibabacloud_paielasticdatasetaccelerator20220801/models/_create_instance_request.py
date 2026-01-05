# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        description: str = None,
        max_endpoint: str = None,
        max_slot: str = None,
        name: str = None,
        payment_type: str = None,
        provider_type: str = None,
        storage_type: str = None,
        tags: List[main_models.CreateInstanceRequestTags] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.capacity = capacity
        self.description = description
        self.max_endpoint = max_endpoint
        self.max_slot = max_slot
        self.name = name
        # This parameter is required.
        self.payment_type = payment_type
        self.provider_type = provider_type
        self.storage_type = storage_type
        self.tags = tags
        # This parameter is required.
        self.type = type

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
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.description is not None:
            result['Description'] = self.description

        if self.max_endpoint is not None:
            result['MaxEndpoint'] = self.max_endpoint

        if self.max_slot is not None:
            result['MaxSlot'] = self.max_slot

        if self.name is not None:
            result['Name'] = self.name

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaxEndpoint') is not None:
            self.max_endpoint = m.get('MaxEndpoint')

        if m.get('MaxSlot') is not None:
            self.max_slot = m.get('MaxSlot')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self



class CreateInstanceRequestTags(DaraModel):
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

