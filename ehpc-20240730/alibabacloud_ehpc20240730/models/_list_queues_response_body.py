# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListQueuesResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        queues: List[main_models.ListQueuesResponseBodyQueues] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        self.cluster_id = cluster_id
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The information about the queues.
        self.queues = queues
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.queues:
            for v1 in self.queues:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Queues'] = []
        if self.queues is not None:
            for k1 in self.queues:
                result['Queues'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.queues = []
        if m.get('Queues') is not None:
            for k1 in m.get('Queues'):
                temp_model = main_models.ListQueuesResponseBodyQueues()
                self.queues.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQueuesResponseBodyQueues(DaraModel):
    def __init__(
        self,
        compute_nodes: List[main_models.NodeTemplate] = None,
        create_time: str = None,
        enable_scale_in: bool = None,
        enable_scale_out: bool = None,
        max_count: int = None,
        max_count_per_cycle: int = None,
        min_count: int = None,
        nodes: main_models.ListQueuesResponseBodyQueuesNodes = None,
        queue_name: str = None,
        total_cores: int = None,
        update_time: str = None,
        v_switch_ids: List[str] = None,
    ):
        # The hardware configurations of the compute nodes that are added in auto scale-outs. Up to five nodes are displayed.
        self.compute_nodes = compute_nodes
        # The time when the queue was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.create_time = create_time
        # Indicates whether auto scale-in is enabled for the queue. Valid values:
        # 
        # *   true
        # *   false
        self.enable_scale_in = enable_scale_in
        # Indicates whether auto scale-out is enabled for the queue. Valid values:
        # 
        # *   true
        # *   false
        self.enable_scale_out = enable_scale_out
        # The maximum number of compute nodes that the queue can contain.
        self.max_count = max_count
        # The minimum number of compute nodes that are added to the queue in each auto scale-out.
        self.max_count_per_cycle = max_count_per_cycle
        # The minimum number of compute nodes that the queue must contain.
        self.min_count = min_count
        # The statistics about the compute nodes in the queue.
        self.nodes = nodes
        # The queue name.
        self.queue_name = queue_name
        # The total number of vCPUs that are used by all compute nodes in the queue.
        self.total_cores = total_cores
        # The time when the queue was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.update_time = update_time
        # The vSwitches that can be used for added nodes during auto scale-outs. Up to three vSwitches are displayed.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.compute_nodes:
            for v1 in self.compute_nodes:
                 if v1:
                    v1.validate()
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComputeNodes'] = []
        if self.compute_nodes is not None:
            for k1 in self.compute_nodes:
                result['ComputeNodes'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable_scale_in is not None:
            result['EnableScaleIn'] = self.enable_scale_in

        if self.enable_scale_out is not None:
            result['EnableScaleOut'] = self.enable_scale_out

        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.max_count_per_cycle is not None:
            result['MaxCountPerCycle'] = self.max_count_per_cycle

        if self.min_count is not None:
            result['MinCount'] = self.min_count

        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.total_cores is not None:
            result['TotalCores'] = self.total_cores

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compute_nodes = []
        if m.get('ComputeNodes') is not None:
            for k1 in m.get('ComputeNodes'):
                temp_model = main_models.NodeTemplate()
                self.compute_nodes.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableScaleIn') is not None:
            self.enable_scale_in = m.get('EnableScaleIn')

        if m.get('EnableScaleOut') is not None:
            self.enable_scale_out = m.get('EnableScaleOut')

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('MaxCountPerCycle') is not None:
            self.max_count_per_cycle = m.get('MaxCountPerCycle')

        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')

        if m.get('Nodes') is not None:
            temp_model = main_models.ListQueuesResponseBodyQueuesNodes()
            self.nodes = temp_model.from_map(m.get('Nodes'))

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('TotalCores') is not None:
            self.total_cores = m.get('TotalCores')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class ListQueuesResponseBodyQueuesNodes(DaraModel):
    def __init__(
        self,
        creating_counts: int = None,
        exception_counts: int = None,
        running_counts: int = None,
    ):
        # The number of compute nodes that are not ready.
        self.creating_counts = creating_counts
        # The number of malfunctioning compute nodes.
        self.exception_counts = exception_counts
        # The number of running compute nodes.
        self.running_counts = running_counts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creating_counts is not None:
            result['CreatingCounts'] = self.creating_counts

        if self.exception_counts is not None:
            result['ExceptionCounts'] = self.exception_counts

        if self.running_counts is not None:
            result['RunningCounts'] = self.running_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatingCounts') is not None:
            self.creating_counts = m.get('CreatingCounts')

        if m.get('ExceptionCounts') is not None:
            self.exception_counts = m.get('ExceptionCounts')

        if m.get('RunningCounts') is not None:
            self.running_counts = m.get('RunningCounts')

        return self

