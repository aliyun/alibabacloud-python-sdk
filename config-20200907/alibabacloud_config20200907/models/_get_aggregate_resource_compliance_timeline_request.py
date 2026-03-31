# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAggregateResourceComplianceTimelineRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        end_time: int = None,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_account_id: int = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        start_time: int = None,
    ):
        # The ID of the account group.
        # 
        # For information about how to obtain the ID of the account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The end of the time range to query. The default value indicates the time when the GetAggregateResourceConfigurationTimeline operation is called. Unit: milliseconds.
        self.end_time = end_time
        # The maximum number of entries returned for a single request. Valid values: 1 to 100.
        self.max_results = max_results
        # The `token` that is used to initiate the next request if the response of the current request is truncated. You can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The ID of the region where the resource resides.
        # 
        # For more information about how to obtain the ID of a region, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/265983.html).
        # 
        # This parameter is required.
        self.region = region
        # The ID of the Alibaba Cloud account to which the resources in the account group belong.
        # 
        # > You can use either the ResourceAccountId or ResourceOwnerId parameter. We recommend that you use the ResourceAccountId parameter.
        self.resource_account_id = resource_account_id
        # The resource ID.
        # 
        # For more information about how to query the ID of a resource, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/265983.html).
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        # The resource type.
        # 
        # For more information about how to obtain the type of a resource, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/265983.html).
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The beginning of the time range to query. By default, Cloud Config retrieves the configuration changes in the last 30 days for the specified resource. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

