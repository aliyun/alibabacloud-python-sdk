# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class NodeSnapshot(DaraModel):
    def __init__(
        self,
        ancestor_quota_workload_num: int = None,
        descendant_quota_workload_num: int = None,
        node_name: str = None,
        request_cpu: str = None,
        request_gpu: str = None,
        request_memory: str = None,
        self_quota_workload_num: int = None,
        workload_num: int = None,
        workloads: List[main_models.NodeSnapshotWorkloads] = None,
    ):
        self.ancestor_quota_workload_num = ancestor_quota_workload_num
        self.descendant_quota_workload_num = descendant_quota_workload_num
        self.node_name = node_name
        self.request_cpu = request_cpu
        self.request_gpu = request_gpu
        self.request_memory = request_memory
        self.self_quota_workload_num = self_quota_workload_num
        self.workload_num = workload_num
        self.workloads = workloads

    def validate(self):
        if self.workloads:
            for v1 in self.workloads:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ancestor_quota_workload_num is not None:
            result['AncestorQuotaWorkloadNum'] = self.ancestor_quota_workload_num

        if self.descendant_quota_workload_num is not None:
            result['DescendantQuotaWorkloadNum'] = self.descendant_quota_workload_num

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu

        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu

        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory

        if self.self_quota_workload_num is not None:
            result['SelfQuotaWorkloadNum'] = self.self_quota_workload_num

        if self.workload_num is not None:
            result['WorkloadNum'] = self.workload_num

        result['Workloads'] = []
        if self.workloads is not None:
            for k1 in self.workloads:
                result['Workloads'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AncestorQuotaWorkloadNum') is not None:
            self.ancestor_quota_workload_num = m.get('AncestorQuotaWorkloadNum')

        if m.get('DescendantQuotaWorkloadNum') is not None:
            self.descendant_quota_workload_num = m.get('DescendantQuotaWorkloadNum')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')

        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')

        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')

        if m.get('SelfQuotaWorkloadNum') is not None:
            self.self_quota_workload_num = m.get('SelfQuotaWorkloadNum')

        if m.get('WorkloadNum') is not None:
            self.workload_num = m.get('WorkloadNum')

        self.workloads = []
        if m.get('Workloads') is not None:
            for k1 in m.get('Workloads'):
                temp_model = main_models.NodeSnapshotWorkloads()
                self.workloads.append(temp_model.from_map(k1))

        return self

class NodeSnapshotWorkloads(DaraModel):
    def __init__(
        self,
        name: str = None,
        workload_id: str = None,
        workload_type: str = None,
    ):
        self.name = name
        self.workload_id = workload_id
        self.workload_type = workload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        return self

