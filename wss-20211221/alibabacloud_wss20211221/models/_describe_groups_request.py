# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeGroupsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        group_resource_types: List[str] = None,
        group_type: str = None,
        instance_ids: List[str] = None,
        max_results: str = None,
        next_token: str = None,
        resource_ids: List[str] = None,
        start_time: int = None,
        states: List[str] = None,
        time_using_period: bool = None,
    ):
        # The end time of the period.
        self.end_time = end_time
        # The list of group resource types.
        self.group_resource_types = group_resource_types
        # The group type.
        # 
        # This parameter is required.
        self.group_type = group_type
        # The Lingxiao instance ID.
        self.instance_ids = instance_ids
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token. Leave this parameter empty for the first request. For subsequent requests, use the `nextToken` value returned in the previous response.
        self.next_token = next_token
        # The list of resource IDs.
        self.resource_ids = resource_ids
        # The start time of the period.
        self.start_time = start_time
        # The list of states.
        self.states = states
        # The effective period used for the query.
        self.time_using_period = time_using_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_resource_types is not None:
            result['GroupResourceTypes'] = self.group_resource_types

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.states is not None:
            result['States'] = self.states

        if self.time_using_period is not None:
            result['TimeUsingPeriod'] = self.time_using_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupResourceTypes') is not None:
            self.group_resource_types = m.get('GroupResourceTypes')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('States') is not None:
            self.states = m.get('States')

        if m.get('TimeUsingPeriod') is not None:
            self.time_using_period = m.get('TimeUsingPeriod')

        return self

