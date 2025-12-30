# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class QueueTemplate(DaraModel):
    def __init__(
        self,
        allocation_strategy: str = None,
        compute_nodes: List[main_models.NodeTemplate] = None,
        enable_scale_in: bool = None,
        enable_scale_out: bool = None,
        hostname_prefix: str = None,
        hostname_suffix: str = None,
        initial_count: int = None,
        inter_connect: str = None,
        keep_alive_nodes: List[str] = None,
        max_count: int = None,
        max_count_per_cycle: int = None,
        min_count: int = None,
        queue_name: str = None,
        ram_role: str = None,
        reserved_node_pool_id: str = None,
        v_switch_ids: List[str] = None,
    ):
        self.allocation_strategy = allocation_strategy
        self.compute_nodes = compute_nodes
        self.enable_scale_in = enable_scale_in
        self.enable_scale_out = enable_scale_out
        self.hostname_prefix = hostname_prefix
        self.hostname_suffix = hostname_suffix
        self.initial_count = initial_count
        self.inter_connect = inter_connect
        self.keep_alive_nodes = keep_alive_nodes
        self.max_count = max_count
        self.max_count_per_cycle = max_count_per_cycle
        self.min_count = min_count
        # This parameter is required.
        self.queue_name = queue_name
        self.ram_role = ram_role
        self.reserved_node_pool_id = reserved_node_pool_id
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.compute_nodes:
            for v1 in self.compute_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_strategy is not None:
            result['AllocationStrategy'] = self.allocation_strategy

        result['ComputeNodes'] = []
        if self.compute_nodes is not None:
            for k1 in self.compute_nodes:
                result['ComputeNodes'].append(k1.to_map() if k1 else None)

        if self.enable_scale_in is not None:
            result['EnableScaleIn'] = self.enable_scale_in

        if self.enable_scale_out is not None:
            result['EnableScaleOut'] = self.enable_scale_out

        if self.hostname_prefix is not None:
            result['HostnamePrefix'] = self.hostname_prefix

        if self.hostname_suffix is not None:
            result['HostnameSuffix'] = self.hostname_suffix

        if self.initial_count is not None:
            result['InitialCount'] = self.initial_count

        if self.inter_connect is not None:
            result['InterConnect'] = self.inter_connect

        if self.keep_alive_nodes is not None:
            result['KeepAliveNodes'] = self.keep_alive_nodes

        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.max_count_per_cycle is not None:
            result['MaxCountPerCycle'] = self.max_count_per_cycle

        if self.min_count is not None:
            result['MinCount'] = self.min_count

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.ram_role is not None:
            result['RamRole'] = self.ram_role

        if self.reserved_node_pool_id is not None:
            result['ReservedNodePoolId'] = self.reserved_node_pool_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')

        self.compute_nodes = []
        if m.get('ComputeNodes') is not None:
            for k1 in m.get('ComputeNodes'):
                temp_model = main_models.NodeTemplate()
                self.compute_nodes.append(temp_model.from_map(k1))

        if m.get('EnableScaleIn') is not None:
            self.enable_scale_in = m.get('EnableScaleIn')

        if m.get('EnableScaleOut') is not None:
            self.enable_scale_out = m.get('EnableScaleOut')

        if m.get('HostnamePrefix') is not None:
            self.hostname_prefix = m.get('HostnamePrefix')

        if m.get('HostnameSuffix') is not None:
            self.hostname_suffix = m.get('HostnameSuffix')

        if m.get('InitialCount') is not None:
            self.initial_count = m.get('InitialCount')

        if m.get('InterConnect') is not None:
            self.inter_connect = m.get('InterConnect')

        if m.get('KeepAliveNodes') is not None:
            self.keep_alive_nodes = m.get('KeepAliveNodes')

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('MaxCountPerCycle') is not None:
            self.max_count_per_cycle = m.get('MaxCountPerCycle')

        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')

        if m.get('ReservedNodePoolId') is not None:
            self.reserved_node_pool_id = m.get('ReservedNodePoolId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

