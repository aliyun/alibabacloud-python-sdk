# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class CapacityPlanResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CapacityPlanResponseBodyResult = None,
    ):
        # ID of the current request.
        self.request_id = request_id
        # Returned result of the request.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CapacityPlanResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CapacityPlanResponseBodyResult(DaraModel):
    def __init__(
        self,
        extend_configs: List[main_models.CapacityPlanResponseBodyResultExtendConfigs] = None,
        instance_category: str = None,
        node_configurations: List[main_models.CapacityPlanResponseBodyResultNodeConfigurations] = None,
        oversized_cluster: bool = None,
    ):
        # Extended configuration information.
        self.extend_configs = extend_configs
        # Edition type, with values meaning as follows:
        # 
        # - advanced: Enhanced Edition
        # 
        # - x-pack: Commercial Edition
        # 
        # - community: Community Edition
        self.instance_category = instance_category
        # Node information.
        self.node_configurations = node_configurations
        # Based on the capacity planning calculation, there is no default value. The meanings of the values are as follows:
        # 
        # - true: Represents an oversized cluster, indicating that the number of data nodes calculated by the capacity planning exceeds the threshold of 50.
        # 
        # - false: The number of data nodes calculated by the capacity planning is within 50.
        self.oversized_cluster = oversized_cluster

    def validate(self):
        if self.extend_configs:
            for v1 in self.extend_configs:
                 if v1:
                    v1.validate()
        if self.node_configurations:
            for v1 in self.node_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExtendConfigs'] = []
        if self.extend_configs is not None:
            for k1 in self.extend_configs:
                result['ExtendConfigs'].append(k1.to_map() if k1 else None)

        if self.instance_category is not None:
            result['InstanceCategory'] = self.instance_category

        result['NodeConfigurations'] = []
        if self.node_configurations is not None:
            for k1 in self.node_configurations:
                result['NodeConfigurations'].append(k1.to_map() if k1 else None)

        if self.oversized_cluster is not None:
            result['OversizedCluster'] = self.oversized_cluster

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extend_configs = []
        if m.get('ExtendConfigs') is not None:
            for k1 in m.get('ExtendConfigs'):
                temp_model = main_models.CapacityPlanResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k1))

        if m.get('InstanceCategory') is not None:
            self.instance_category = m.get('InstanceCategory')

        self.node_configurations = []
        if m.get('NodeConfigurations') is not None:
            for k1 in m.get('NodeConfigurations'):
                temp_model = main_models.CapacityPlanResponseBodyResultNodeConfigurations()
                self.node_configurations.append(temp_model.from_map(k1))

        if m.get('OversizedCluster') is not None:
            self.oversized_cluster = m.get('OversizedCluster')

        return self

class CapacityPlanResponseBodyResultNodeConfigurations(DaraModel):
    def __init__(
        self,
        amount: int = None,
        cpu: int = None,
        disk: int = None,
        disk_type: str = None,
        memory: int = None,
        node_type: str = None,
    ):
        # Number of nodes.
        self.amount = amount
        # Number of CPUs.
        self.cpu = cpu
        # Disk size, in GiB.
        self.disk = disk
        # Disk type, with meanings as follows:
        # 
        # - cloud_essd: ESSD Cloud Disk
        # 
        # - cloud_ssd: SSD Cloud Disk
        # 
        # - cloud_efficiency: Efficient Cloud Disk
        # 
        # - local_ssd: Local SSD Disk
        # 
        # - local_efficiency: Local Efficient Disk
        self.disk_type = disk_type
        # Specified memory size for the current node role.
        self.memory = memory
        # Node type, with supported types as follows:
        # 
        # - WORKER: Data Node
        # 
        # - WORKER_WARM: Cold Data Node
        # 
        # - MASTER: Dedicated Master Node
        # 
        # - KIBANA: Kibana Node
        # 
        # - COORDINATING: Coordinator Node
        # 
        # - ELASTIC_WORKER: Elastic Node
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.disk is not None:
            result['Disk'] = self.disk

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Disk') is not None:
            self.disk = m.get('Disk')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

class CapacityPlanResponseBodyResultExtendConfigs(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        disk: int = None,
        disk_type: str = None,
    ):
        # Configuration type, with a single value: sharedDisk.
        # 
        # > This extendConfigs attribute may appear when the planned instance type is Advanced.
        self.config_type = config_type
        # Disk size, in GiB.
        self.disk = disk
        # Disk type, with a single value: CPFS_PREMIUM.
        # 
        # > This extendConfigs attribute may appear when the planned instance type is Advanced.
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.disk is not None:
            result['Disk'] = self.disk

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('Disk') is not None:
            self.disk = m.get('Disk')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        return self

