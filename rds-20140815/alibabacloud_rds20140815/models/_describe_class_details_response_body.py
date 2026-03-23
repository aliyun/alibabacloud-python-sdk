# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClassDetailsResponseBody(DaraModel):
    def __init__(
        self,
        category: str = None,
        class_code: str = None,
        class_group: str = None,
        cpu: str = None,
        dbinstance_storage_type: str = None,
        instruction_set_arch: str = None,
        max_connections: str = None,
        max_iombps: str = None,
        max_iops: str = None,
        memory_class: str = None,
        reference_price: str = None,
        request_id: str = None,
    ):
        self.category = category
        self.class_code = class_code
        self.class_group = class_group
        self.cpu = cpu
        self.dbinstance_storage_type = dbinstance_storage_type
        self.instruction_set_arch = instruction_set_arch
        self.max_connections = max_connections
        self.max_iombps = max_iombps
        self.max_iops = max_iops
        self.memory_class = memory_class
        self.reference_price = reference_price
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.class_group is not None:
            result['ClassGroup'] = self.class_group

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('ClassGroup') is not None:
            self.class_group = m.get('ClassGroup')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

