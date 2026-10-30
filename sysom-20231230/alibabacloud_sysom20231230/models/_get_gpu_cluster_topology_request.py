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
        # The ID of the channel. Used to view the collective communication topology and the topology relationships of a specified channel ID under a specified communication group, such as the communication, tree, or ring topology among ranks within a communication group. This parameter must be used together with communication_id and topo_type. You can call the GetGpuClusterArgsOptions operation with the channel filter parameter to obtain the list of channel_id values under a specified communication_id.
        self.channel_id = channel_id
        # The name of the cluster. You can select a cluster from the cluster list obtained by calling the GetListGpuCluster operation.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the communication group. Used to view the collective communication topology and the topology relationships of a specified communication group ID, such as the communication, tree, or ring topology among ranks within a communication group. This parameter must be used together with channel_id and topo_type. You can call the GetGpuClusterArgsOptions operation with the communication filter type to obtain the list of communication_id values.
        self.communication_id = communication_id
        # The list of instances for which to query GPU topology information.
        self.instance_id_list = instance_id_list
        # The list of pods for which to query GPU topology information.
        self.pod_list = pod_list
        # The query timestamp. Default value: the current time. The timestamp must be accurate to seconds.
        self.start_time = start_time
        # The list of tasks for which to query GPU topology information.
        self.task_id_list = task_id_list
        # The topology type. Used to view the collective communication topology and the topology relationships of a specified topology type under a specified communication group and channel ID, such as the communication, tree, or ring topology among ranks within a communication group. This parameter must be used together with communication_id and channel_id. You can call the GetGpuClusterArgsOptions operation with the topoType filter parameter to obtain the list of topo_type values under a specified communication_id and channel_id.
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

