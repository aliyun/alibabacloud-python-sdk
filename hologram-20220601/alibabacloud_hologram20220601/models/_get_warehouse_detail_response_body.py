# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class GetWarehouseDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        warehouse_detail: main_models.GetWarehouseDetailResponseBodyWarehouseDetail = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned values.
        self.warehouse_detail = warehouse_detail

    def validate(self):
        if self.warehouse_detail:
            self.warehouse_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.warehouse_detail is not None:
            result['WarehouseDetail'] = self.warehouse_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WarehouseDetail') is not None:
            temp_model = main_models.GetWarehouseDetailResponseBodyWarehouseDetail()
            self.warehouse_detail = temp_model.from_map(m.get('WarehouseDetail'))

        return self

class GetWarehouseDetailResponseBodyWarehouseDetail(DaraModel):
    def __init__(
        self,
        auto_elastic_cpu: str = None,
        remaining_cpu: str = None,
        reserved_cpu: str = None,
        timed_elastic_cpu: str = None,
        warehouse_list: List[main_models.GetWarehouseDetailResponseBodyWarehouseDetailWarehouseList] = None,
    ):
        self.auto_elastic_cpu = auto_elastic_cpu
        # The remaining unallocated computing resources of the virtual warehouse instance.
        self.remaining_cpu = remaining_cpu
        # The reserved computing resources. The amount of computing resources in all running virtual warehouses in an instance cannot exceed the amount of reserved computing resources in the virtual warehouses.
        self.reserved_cpu = reserved_cpu
        self.timed_elastic_cpu = timed_elastic_cpu
        # The list of virtual warehouses.
        self.warehouse_list = warehouse_list

    def validate(self):
        if self.warehouse_list:
            for v1 in self.warehouse_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_elastic_cpu is not None:
            result['AutoElasticCpu'] = self.auto_elastic_cpu

        if self.remaining_cpu is not None:
            result['RemainingCpu'] = self.remaining_cpu

        if self.reserved_cpu is not None:
            result['ReservedCpu'] = self.reserved_cpu

        if self.timed_elastic_cpu is not None:
            result['TimedElasticCpu'] = self.timed_elastic_cpu

        result['WarehouseList'] = []
        if self.warehouse_list is not None:
            for k1 in self.warehouse_list:
                result['WarehouseList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoElasticCpu') is not None:
            self.auto_elastic_cpu = m.get('AutoElasticCpu')

        if m.get('RemainingCpu') is not None:
            self.remaining_cpu = m.get('RemainingCpu')

        if m.get('ReservedCpu') is not None:
            self.reserved_cpu = m.get('ReservedCpu')

        if m.get('TimedElasticCpu') is not None:
            self.timed_elastic_cpu = m.get('TimedElasticCpu')

        self.warehouse_list = []
        if m.get('WarehouseList') is not None:
            for k1 in m.get('WarehouseList'):
                temp_model = main_models.GetWarehouseDetailResponseBodyWarehouseDetailWarehouseList()
                self.warehouse_list.append(temp_model.from_map(k1))

        return self

class GetWarehouseDetailResponseBodyWarehouseDetailWarehouseList(DaraModel):
    def __init__(
        self,
        auto_scale_type: str = None,
        cluster_count: str = None,
        cluster_cpu: str = None,
        cpu: int = None,
        default_warehouse: bool = None,
        elastic_cpu: int = None,
        elastic_type: str = None,
        id: int = None,
        init_cluster_count: str = None,
        max_cluster_count: str = None,
        mem: int = None,
        name: str = None,
        node_count: int = None,
        rebalance_status: str = None,
        status: str = None,
    ):
        self.auto_scale_type = auto_scale_type
        self.cluster_count = cluster_count
        self.cluster_cpu = cluster_cpu
        # The number of CPU cores.
        self.cpu = cpu
        self.default_warehouse = default_warehouse
        self.elastic_cpu = elastic_cpu
        self.elastic_type = elastic_type
        # The ID.
        self.id = id
        self.init_cluster_count = init_cluster_count
        self.max_cluster_count = max_cluster_count
        # The memory capacity.
        self.mem = mem
        # The name of the virtual warehouse instance.
        self.name = name
        # The number of compute nodes.
        self.node_count = node_count
        self.rebalance_status = rebalance_status
        # The status.
        # 
        # Valid values:
        # 
        # *   kRunning
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kSuspended
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kInit
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   kAllocating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_scale_type is not None:
            result['AutoScaleType'] = self.auto_scale_type

        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count

        if self.cluster_cpu is not None:
            result['ClusterCpu'] = self.cluster_cpu

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.default_warehouse is not None:
            result['DefaultWarehouse'] = self.default_warehouse

        if self.elastic_cpu is not None:
            result['ElasticCpu'] = self.elastic_cpu

        if self.elastic_type is not None:
            result['ElasticType'] = self.elastic_type

        if self.id is not None:
            result['Id'] = self.id

        if self.init_cluster_count is not None:
            result['InitClusterCount'] = self.init_cluster_count

        if self.max_cluster_count is not None:
            result['MaxClusterCount'] = self.max_cluster_count

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.name is not None:
            result['Name'] = self.name

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.rebalance_status is not None:
            result['RebalanceStatus'] = self.rebalance_status

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScaleType') is not None:
            self.auto_scale_type = m.get('AutoScaleType')

        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')

        if m.get('ClusterCpu') is not None:
            self.cluster_cpu = m.get('ClusterCpu')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DefaultWarehouse') is not None:
            self.default_warehouse = m.get('DefaultWarehouse')

        if m.get('ElasticCpu') is not None:
            self.elastic_cpu = m.get('ElasticCpu')

        if m.get('ElasticType') is not None:
            self.elastic_type = m.get('ElasticType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InitClusterCount') is not None:
            self.init_cluster_count = m.get('InitClusterCount')

        if m.get('MaxClusterCount') is not None:
            self.max_cluster_count = m.get('MaxClusterCount')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('RebalanceStatus') is not None:
            self.rebalance_status = m.get('RebalanceStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

