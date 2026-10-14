# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetGpuClusterTopologyRequest(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        cluster_id: str = None,
        communication_id: str = None,
        instance_id_list: Any = None,
        pod_list: Any = None,
        start_time: str = None,
        task_id_list: Any = None,
        topo_type: str = None,
    ):
        # Used when viewing collective communication topology. Specifies the topology relationship for a given channel ID within a communication group, such as the inter-rank communication topology (tree or ring topology). Must be used together with communication_id and topo_type.
        # 
        # ⚠️ Use the channel filter parameter of the GetGpuClusterArgsOptions operation to retrieve the list of channel_id values for a specified communication_id.
        self.channel_id = channel_id
        # The cluster name. Select a cluster from the cluster list returned by the GetListGpuCluster operation.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Used when viewing collective communication topology. Specifies the topology relationship for a given communication group ID, such as the inter-rank communication topology (tree or ring topology) within a communication group. Must be used together with channel_id and topo_type.
        # 
        # ⚠️ Use the communication filter type of the GetGpuClusterArgsOptions operation to retrieve the list of communication_id values.
        self.communication_id = communication_id
        # The GPU topology information for the specified list of instances.
        self.instance_id_list = instance_id_list
        # The GPU topology information for the specified list of pods.
        self.pod_list = pod_list
        # The timestamp for the query. Defaults to the current time. Must be a second-level timestamp.
        self.start_time = start_time
        # The GPU topology information for the specified list of nodes.
        self.task_id_list = task_id_list
        # Used when viewing collective communication topology. Specifies the topology relationship for a given topology type within a communication group and channel, such as the inter-rank communication topology (tree or ring topology). Must be used together with communication_id and channel_id.
        # 
        # ⚠️ Use the topoType filter parameter of the GetGpuClusterArgsOptions operation to retrieve the list of topo_type values for a specified communication_id and channel_id.
        self.topo_type = topo_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['channelId'] = self.channel_id

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.communication_id is not None:
            result['communicationId'] = self.communication_id

        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list

        if self.pod_list is not None:
            result['podList'] = self.pod_list

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.task_id_list is not None:
            result['taskIdList'] = self.task_id_list

        if self.topo_type is not None:
            result['topoType'] = self.topo_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('communicationId') is not None:
            self.communication_id = m.get('communicationId')

        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')

        if m.get('podList') is not None:
            self.pod_list = m.get('podList')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('taskIdList') is not None:
            self.task_id_list = m.get('taskIdList')

        if m.get('topoType') is not None:
            self.topo_type = m.get('topoType')

        return self

