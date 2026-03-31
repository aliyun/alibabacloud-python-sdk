# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceComplianceTimelineRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_id: str = None,
        resource_type: str = None,
        start_time: int = None,
    ):
        # The timestamp that specifies the end of the time range to query. The default value is the time when the GetResourceComplianceTimeline operation is called. Unit: milliseconds.
        self.end_time = end_time
        # The maximum number of entries to return for a single request. Valid values: 1 to 100.
        self.max_results = max_results
        # The token that is used to initiate the next request. If the response of the current request is truncated, this token is used to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The ID of the region where the resource resides.
        # 
        # This parameter is required.
        self.region = region
        # The ID of the resource.
        # 
        # For more information about how to obtain the ID of a resource, see [ListDiscoveredResources](https://help.aliyun.com/document_detail/169620.html).
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # For more information about how to obtain the type of a resource, see [ListDiscoveredResources](https://help.aliyun.com/document_detail/169620.html).
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The timestamp that specifies the beginning of the time range to query. By default, Cloud Config retrieves the compliance evaluations in the last 30 days for the specified resource. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

