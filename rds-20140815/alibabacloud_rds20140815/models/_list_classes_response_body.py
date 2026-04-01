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
        # The list of instance specifications.
        self.items = items
        # The ID of the region.
        self.region_id = region_id
        # The ID of the request.
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
        # The code of the instance type. For more information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html) and [Read-only ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/145759.html).
        self.class_code = class_code
        # The instance family. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/57184.html).
        self.class_group = class_group
        # The number of CPU cores that are supported by the instance type. Unit: cores.
        self.cpu = cpu
        # The size of the encrypted memory that is supported by the security-enhanced instance type. Unit: GB.
        self.encrypted_memory = encrypted_memory
        # The architecture of the instance type. Valid values:
        # 
        # *   If the architecture of the instance type is **x86**, an empty string is returned by default.
        # *   If the architecture of the instance type is **ARM**, **arm** is returned.
        self.instruction_set_arch = instruction_set_arch
        # The maximum number of connections that are supported by the instance type. Unit: connections.
        self.max_connections = max_connections
        # The maximum I/O bandwidth that is supported by the instance type. Unit: Mbit/s.
        self.max_iombps = max_iombps
        # The maximum input/output operations per second (IOPS) that is supported by the instance type. Unit: operations per second.
        self.max_iops = max_iops
        # The memory size that is supported by the instance type. Unit: GB.
        self.memory_class = memory_class
        # The fee that you must pay for the instance type.
        # 
        # *   Unit: cents (USD).
        # 
        # > *   If you set **CommodityCode** to a value that indicates the pay-as-you-go billing method, the ReferencePrice parameter specifies the hourly fee that you must pay.
        # > *   If you set **CommodityCode** to a value that indicates the subscription billing method, the ReferencePrice parameter specifies the monthly fee that you must pay.
        self.reference_price = reference_price
        # The RDS edition of the instance. Valid values:
        # 
        # *   Regular instance
        # 
        #     *   **Basic**: RDS Basic Edition
        #     *   **HighAvailability**: RDS High-availability Edition
        #     *   **cluster**: RDS Cluster Edition for ApsaraDB RDS for MySQL or PostgreSQL
        #     *   **AlwaysOn**: RDS Cluster Edition for ApsaraDB RDS for SQL Server
        #     *   **Finance**: RDS Basic Edition for serverless instances
        # 
        # *   Serverless instance
        # 
        #     *   **serverless_basic**: RDS Basic Edition for serverless instances. This edition is available only for instances that run MySQL and PostgreSQL.
        #     *   **serverless_standard**: RDS High-availability Edition for serverless instances. This edition is available only for instances that run MySQL and PostgreSQL.
        #     *   **serverless_ha**: RDS High-availability Edition for serverless instances. This edition is available only for instances that run SQL Server.
        self.category = category
        # The storage type of the instance.
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

