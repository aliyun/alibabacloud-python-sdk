# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListComponentInstancesRequest(DaraModel):
    def __init__(
        self,
        application_names: List[str] = None,
        cluster_id: str = None,
        component_names: List[str] = None,
        component_states: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        node_ids: List[str] = None,
        node_names: List[str] = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The list of component names.
        self.application_names = application_names
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The list of component names.
        self.component_names = component_names
        # The list of component status.
        self.component_states = component_states
        # The maximum number of entries returned.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The list of instance IDs.
        self.node_ids = node_ids
        # The instance IDs.
        self.node_names = node_names
        # The region ID. You can call the [ListRegions](url) view.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_names is not None:
            result['ApplicationNames'] = self.application_names

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.component_names is not None:
            result['ComponentNames'] = self.component_names

        if self.component_states is not None:
            result['ComponentStates'] = self.component_states

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationNames') is not None:
            self.application_names = m.get('ApplicationNames')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComponentNames') is not None:
            self.component_names = m.get('ComponentNames')

        if m.get('ComponentStates') is not None:
            self.component_states = m.get('ComponentStates')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

