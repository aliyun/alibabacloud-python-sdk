# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListNodeGroupsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_ids: List[str] = None,
        node_group_names: List[str] = None,
        node_group_states: List[str] = None,
        node_group_types: List[str] = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The maximum number of records to return in a single request. Valid values: 1 to 100.
        self.max_results = max_results
        # The token that marks the start of the query. Leave this parameter empty to start from the beginning.
        self.next_token = next_token
        # A list of node group IDs. The number of array elements N can range from 1 to 100.
        self.node_group_ids = node_group_ids
        # A list of node group names. The number of array elements N can range from 1 to 100.
        self.node_group_names = node_group_names
        # The state of the node group. The number of array elements N can range from 1 to 100.
        self.node_group_states = node_group_states
        # A list of node group types. The number of array elements N can range from 1 to 100.
        self.node_group_types = node_group_types
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

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

        if self.node_group_names is not None:
            result['NodeGroupNames'] = self.node_group_names

        if self.node_group_states is not None:
            result['NodeGroupStates'] = self.node_group_states

        if self.node_group_types is not None:
            result['NodeGroupTypes'] = self.node_group_types

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

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

        if m.get('NodeGroupNames') is not None:
            self.node_group_names = m.get('NodeGroupNames')

        if m.get('NodeGroupStates') is not None:
            self.node_group_states = m.get('NodeGroupStates')

        if m.get('NodeGroupTypes') is not None:
            self.node_group_types = m.get('NodeGroupTypes')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

