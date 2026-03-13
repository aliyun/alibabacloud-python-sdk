# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai20240521 import models as main_models
from darabonba.model import DaraModel

class Node(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        bound_quotas: List[main_models.QuotaIdName] = None,
        cpu: str = None,
        creator_id: str = None,
        gpu: str = None,
        gputype: str = None,
        gmt_create_time: str = None,
        gmt_expired_time: str = None,
        gmt_modified_time: str = None,
        is_bound: bool = None,
        limit_cpu: str = None,
        limit_gpu: str = None,
        limit_memory: str = None,
        machine_group_id: str = None,
        memory: str = None,
        node_name: str = None,
        node_status: str = None,
        node_type: str = None,
        order_status: str = None,
        pod_num: int = None,
        reason_code: str = None,
        reason_message: str = None,
        request_cpu: str = None,
        request_gpu: str = None,
        request_memory: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        sub_nodes: List[str] = None,
        users: List[main_models.UserInfo] = None,
        workload_num: int = None,
    ):
        self.accelerator_type = accelerator_type
        self.bound_quotas = bound_quotas
        self.cpu = cpu
        self.creator_id = creator_id
        self.gpu = gpu
        self.gputype = gputype
        self.gmt_create_time = gmt_create_time
        self.gmt_expired_time = gmt_expired_time
        self.gmt_modified_time = gmt_modified_time
        self.is_bound = is_bound
        self.limit_cpu = limit_cpu
        self.limit_gpu = limit_gpu
        self.limit_memory = limit_memory
        self.machine_group_id = machine_group_id
        self.memory = memory
        self.node_name = node_name
        self.node_status = node_status
        self.node_type = node_type
        self.order_status = order_status
        self.pod_num = pod_num
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.request_cpu = request_cpu
        self.request_gpu = request_gpu
        self.request_memory = request_memory
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.sub_nodes = sub_nodes
        self.users = users
        self.workload_num = workload_num

    def validate(self):
        if self.bound_quotas:
            for v1 in self.bound_quotas:
                 if v1:
                    v1.validate()
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        result['BoundQuotas'] = []
        if self.bound_quotas is not None:
            for k1 in self.bound_quotas:
                result['BoundQuotas'].append(k1.to_map() if k1 else None)

        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_expired_time is not None:
            result['GmtExpiredTime'] = self.gmt_expired_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.is_bound is not None:
            result['IsBound'] = self.is_bound

        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu

        if self.limit_gpu is not None:
            result['LimitGPU'] = self.limit_gpu

        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory

        if self.machine_group_id is not None:
            result['MachineGroupId'] = self.machine_group_id

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.pod_num is not None:
            result['PodNum'] = self.pod_num

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu

        if self.request_gpu is not None:
            result['RequestGPU'] = self.request_gpu

        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.sub_nodes is not None:
            result['SubNodes'] = self.sub_nodes

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        if self.workload_num is not None:
            result['WorkloadNum'] = self.workload_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        self.bound_quotas = []
        if m.get('BoundQuotas') is not None:
            for k1 in m.get('BoundQuotas'):
                temp_model = main_models.QuotaIdName()
                self.bound_quotas.append(temp_model.from_map(k1))

        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtExpiredTime') is not None:
            self.gmt_expired_time = m.get('GmtExpiredTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('IsBound') is not None:
            self.is_bound = m.get('IsBound')

        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')

        if m.get('LimitGPU') is not None:
            self.limit_gpu = m.get('LimitGPU')

        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')

        if m.get('MachineGroupId') is not None:
            self.machine_group_id = m.get('MachineGroupId')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('PodNum') is not None:
            self.pod_num = m.get('PodNum')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')

        if m.get('RequestGPU') is not None:
            self.request_gpu = m.get('RequestGPU')

        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('SubNodes') is not None:
            self.sub_nodes = m.get('SubNodes')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.UserInfo()
                self.users.append(temp_model.from_map(k1))

        if m.get('WorkloadNum') is not None:
            self.workload_num = m.get('WorkloadNum')

        return self

