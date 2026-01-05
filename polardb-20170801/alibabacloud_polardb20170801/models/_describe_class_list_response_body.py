# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeClassListResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeClassListResponseBodyItems] = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # The cluster specifications.
        self.items = items
        # The region ID of the cluster.
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
                temp_model = main_models.DescribeClassListResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClassListResponseBodyItems(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        class_group: str = None,
        class_type_level: str = None,
        cpu: str = None,
        essd_max_storage_capacity: str = None,
        max_connections: str = None,
        max_iops: str = None,
        max_storage_capacity: str = None,
        memory_class: str = None,
        pl_1max_iops: str = None,
        pl_2max_iops: str = None,
        pl_3max_iops: str = None,
        polar_store_max_storage_capacity: str = None,
        psl_4max_iops: str = None,
        psl_5max_iops: str = None,
        reference_ext_price: str = None,
        reference_price: str = None,
    ):
        # The specifications of the cluster.
        self.class_code = class_code
        # The instance family of the cluster. Valid values:
        # 
        # *   Exclusive package: dedicated
        # *   Exclusive physical machine: dedicated host
        # *   Beginner: starter
        # *   Historical specifications: historical
        self.class_group = class_group
        # The specification type of the cluster.
        self.class_type_level = class_type_level
        # The number of vCPU cores. Unit: cores.
        self.cpu = cpu
        # The maximum ESSD storage capacity. Unit: TB.
        self.essd_max_storage_capacity = essd_max_storage_capacity
        # The maximum number of concurrent connections in the cluster.
        self.max_connections = max_connections
        # The maximum IOPS. Unit: operations per second.
        self.max_iops = max_iops
        # The maximum storage capacity. Unit: TB.
        self.max_storage_capacity = max_storage_capacity
        # The memory size. Unit: GB.
        self.memory_class = memory_class
        # The maximum IOPS of an enhanced SSD (ESSD) of performance level 1 (PL1). Unit: operations per second.
        self.pl_1max_iops = pl_1max_iops
        # The maximum IOPS of an ESSD of performance level 2 (PL2). Unit: operations per second.
        self.pl_2max_iops = pl_2max_iops
        # The maximum IOPS of an ESSD of performance level 3 (PL3). Unit: operations per second.
        self.pl_3max_iops = pl_3max_iops
        # The maximum PSL4/PSL5 storage capacity. Unit: TB.
        self.polar_store_max_storage_capacity = polar_store_max_storage_capacity
        # The maximum Input/output operations per second (IOPS) for PolarStore Level 4 (PSL4). Unit: operations per second.
        self.psl_4max_iops = psl_4max_iops
        # The maximum IOPS for PolarStore Level 5 (PSL5). Unit: operations per second.
        self.psl_5max_iops = psl_5max_iops
        # The additional price.
        # 
        # Unit: cents (USD).
        # 
        # >- If you set MasterHa to cluster or single, the value of ReferenceExtPrice is the same as the value of ReferencePrice.
        # >- If you set MasterHa to cluster or single, the value of ReferenceExtPrice is the price of the single-node cluster.
        self.reference_ext_price = reference_ext_price
        # The price.
        # 
        # Unit: cents (USD).
        # 
        # >- If you set CommodityCode to a commodity that uses the pay-as-you-go billing method, ReferencePrice indicates the hourly fee that you need to pay.
        # >- If you set CommodityCode to a commodity that uses the subscription billing method, ReferencePrice indicates the monthly fee that you need to pay.
        self.reference_price = reference_price

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

        if self.class_type_level is not None:
            result['ClassTypeLevel'] = self.class_type_level

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.essd_max_storage_capacity is not None:
            result['EssdMaxStorageCapacity'] = self.essd_max_storage_capacity

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.max_storage_capacity is not None:
            result['MaxStorageCapacity'] = self.max_storage_capacity

        if self.memory_class is not None:
            result['MemoryClass'] = self.memory_class

        if self.pl_1max_iops is not None:
            result['Pl1MaxIOPS'] = self.pl_1max_iops

        if self.pl_2max_iops is not None:
            result['Pl2MaxIOPS'] = self.pl_2max_iops

        if self.pl_3max_iops is not None:
            result['Pl3MaxIOPS'] = self.pl_3max_iops

        if self.polar_store_max_storage_capacity is not None:
            result['PolarStoreMaxStorageCapacity'] = self.polar_store_max_storage_capacity

        if self.psl_4max_iops is not None:
            result['Psl4MaxIOPS'] = self.psl_4max_iops

        if self.psl_5max_iops is not None:
            result['Psl5MaxIOPS'] = self.psl_5max_iops

        if self.reference_ext_price is not None:
            result['ReferenceExtPrice'] = self.reference_ext_price

        if self.reference_price is not None:
            result['ReferencePrice'] = self.reference_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('ClassGroup') is not None:
            self.class_group = m.get('ClassGroup')

        if m.get('ClassTypeLevel') is not None:
            self.class_type_level = m.get('ClassTypeLevel')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('EssdMaxStorageCapacity') is not None:
            self.essd_max_storage_capacity = m.get('EssdMaxStorageCapacity')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('MaxStorageCapacity') is not None:
            self.max_storage_capacity = m.get('MaxStorageCapacity')

        if m.get('MemoryClass') is not None:
            self.memory_class = m.get('MemoryClass')

        if m.get('Pl1MaxIOPS') is not None:
            self.pl_1max_iops = m.get('Pl1MaxIOPS')

        if m.get('Pl2MaxIOPS') is not None:
            self.pl_2max_iops = m.get('Pl2MaxIOPS')

        if m.get('Pl3MaxIOPS') is not None:
            self.pl_3max_iops = m.get('Pl3MaxIOPS')

        if m.get('PolarStoreMaxStorageCapacity') is not None:
            self.polar_store_max_storage_capacity = m.get('PolarStoreMaxStorageCapacity')

        if m.get('Psl4MaxIOPS') is not None:
            self.psl_4max_iops = m.get('Psl4MaxIOPS')

        if m.get('Psl5MaxIOPS') is not None:
            self.psl_5max_iops = m.get('Psl5MaxIOPS')

        if m.get('ReferenceExtPrice') is not None:
            self.reference_ext_price = m.get('ReferenceExtPrice')

        if m.get('ReferencePrice') is not None:
            self.reference_price = m.get('ReferencePrice')

        return self

