# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListNodesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_ids: List[str] = None,
        node_ids: List[str] = None,
        node_names: List[str] = None,
        node_states: List[str] = None,
        private_ips: List[str] = None,
        public_ips: List[str] = None,
        region_id: str = None,
        tags: List[main_models.Tag] = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The number of maximum number of records to obtain at a time. Valid values: 1 to 100.
        self.max_results = max_results
        # Marks the current position where reading starts. If you set this value to null, you can start from the beginning.
        self.next_token = next_token
        # The IDs of node groups.
        self.node_group_ids = node_group_ids
        # An array that consists of information about the ID of the node.
        self.node_ids = node_ids
        # The names of the nodes.
        self.node_names = node_names
        # The status of the node.
        self.node_states = node_states
        # The private IP address.
        self.private_ips = private_ips
        # The public IP address.
        self.public_ips = public_ips
        # The ID of the region in which you want to create the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_group_ids is not None:
            result['NodeGroupIds'] = self.node_group_ids

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        if self.node_states is not None:
            result['NodeStates'] = self.node_states

        if self.private_ips is not None:
            result['PrivateIps'] = self.private_ips

        if self.public_ips is not None:
            result['PublicIps'] = self.public_ips

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeGroupIds') is not None:
            self.node_group_ids = m.get('NodeGroupIds')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        if m.get('NodeStates') is not None:
            self.node_states = m.get('NodeStates')

        if m.get('PrivateIps') is not None:
            self.private_ips = m.get('PrivateIps')

        if m.get('PublicIps') is not None:
            self.public_ips = m.get('PublicIps')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        return self

