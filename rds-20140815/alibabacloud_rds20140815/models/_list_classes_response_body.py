# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ListClassesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListClassesResponseBodyItems] = None,
        region_id: str = None,
        request_id: str = None,
    ):
        self.items = items
        self.region_id = region_id
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListClassesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClassesResponseBodyItems(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        class_group: str = None,
        cpu: str = None,
        encrypted_memory: str = None,
        instruction_set_arch: str = None,
        max_connections: str = None,
        max_iombps: str = None,
        max_iops: str = None,
        memory_class: str = None,
        reference_price: str = None,
        category: str = None,
        storage_type: str = None,
    ):
        self.class_code = class_code
        self.class_group = class_group
        self.cpu = cpu
        self.encrypted_memory = encrypted_memory
        self.instruction_set_arch = instruction_set_arch
        self.max_connections = max_connections
        self.max_iombps = max_iombps
        self.max_iops = max_iops
        self.memory_class = memory_class
        self.reference_price = reference_price
        self.category = category
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.class_group is not None:
            result['ClassGroup'] = self.class_group

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.encrypted_memory is not None:
            result['EncryptedMemory'] = self.encrypted_memory

        if self.instruction_set_arch is not None:
            result['InstructionSetArch'] = self.instruction_set_arch

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iombps is not None:
            result['MaxIOMBPS'] = self.max_iombps

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.memory_class is not None:
            result['MemoryClass'] = self.memory_class

        if self.reference_price is not None:
            result['ReferencePrice'] = self.reference_price

        if self.category is not None:
            result['category'] = self.category

        if self.storage_type is not None:
            result['storageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('ClassGroup') is not None:
            self.class_group = m.get('ClassGroup')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('EncryptedMemory') is not None:
            self.encrypted_memory = m.get('EncryptedMemory')

        if m.get('InstructionSetArch') is not None:
            self.instruction_set_arch = m.get('InstructionSetArch')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIOMBPS') is not None:
            self.max_iombps = m.get('MaxIOMBPS')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('MemoryClass') is not None:
            self.memory_class = m.get('MemoryClass')

        if m.get('ReferencePrice') is not None:
            self.reference_price = m.get('ReferencePrice')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')

        return self

