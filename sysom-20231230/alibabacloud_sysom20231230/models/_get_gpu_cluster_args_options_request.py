# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetGpuClusterArgsOptionsRequest(DaraModel):
    def __init__(
        self,
        filter_type: str = None,
        filter_values: Any = None,
    ):
        # 1. Query the machine list of a cluster
        # Set the retrieval type to comm_instance_id_list or instance_id_list.
        # comm_instance_id_list: retrieves only the machines that participate in collective communication in the specified cluster.
        # instance_id_list: retrieves all machines in the specified cluster.
        # 
        # 2. Query the AI task list of a cluster
        # Set the retrieval type to comm_task_id_list or task_id_list.
        # comm_task_id_list: retrieves only the tasks that involve collective communication in the specified cluster.
        # task_id_list: retrieves all tasks in the specified cluster.
        # 
        # 3. Query the AI job pod list of a cluster
        # Set the retrieval type to comm_pod_list or pod_list.
        # comm_pod_list: retrieves only the pods that participate in collective communication in the specified cluster.
        # pod_list: retrieves all pods in the specified cluster.
        # 
        # 4. Query the collective communication topology
        # communication: retrieves all communication group IDs.
        # channel: retrieves the channel list under the specified communication group ID.
        # topoType: retrieves the topology type under the specified channel of the specified communication group ID.
        # 
        # This parameter is required.
        self.filter_type = filter_type
        # The filter conditions. The value is a JSON object. The cluster_id field is required. The following optional filter conditions are supported:
        # - instance_id_list
        # - comm_instance_id_list
        # - pod_list
        # - comm_pod_list
        # - communication
        # - task_id_list
        # - comm_task_id_list
        # - channel
        # - topoType
        self.filter_values = filter_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_type is not None:
            result['filterType'] = self.filter_type

        if self.filter_values is not None:
            result['filterValues'] = self.filter_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')

        if m.get('filterValues') is not None:
            self.filter_values = m.get('filterValues')

        return self

