# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAggregateDiscoveredResourcesRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        end_update_timestamp: int = None,
        exclude_resource_types: str = None,
        max_results: int = None,
        next_token: str = None,
        regions: str = None,
        resource_account_id: int = None,
        resource_deleted: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_owner_id: int = None,
        resource_types: str = None,
        start_update_timestamp: int = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The end of the time range to query. This is a standard UTC timestamp. The following limits apply:
        # 
        # - The value must be a timestamp in milliseconds.
        # 
        # - The value cannot be earlier than StartUpdateTimestamp. The interval between StartUpdateTimestamp and EndUpdateTimestamp cannot exceed 30 days.
        # 
        # - You must specify both StartUpdateTimestamp and EndUpdateTimestamp, or leave both empty.
        self.end_update_timestamp = end_update_timestamp
        # The resource types to exclude. Separate multiple resource types with commas (,). This parameter has a higher priority than the ResourceTypes parameter.
        self.exclude_resource_types = exclude_resource_types
        # The maximum number of entries to return for a single request. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.max_results = max_results
        # If the response is truncated, use the `NextToken` to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region where the resource resides. Separate multiple region IDs with commas (,).
        self.regions = regions
        # The ID of the Alibaba Cloud account to which the resources to be queried belong. The account is a member of the account group.
        self.resource_account_id = resource_account_id
        # The status of the resource. Valid values:
        # 
        # - 0: The resource is deleted. A resource is displayed as Deleted in Cloud Config after it is deleted from the source Alibaba Cloud service.
        # 
        # - 1 (Default): The resource is active. A resource is displayed as Active in Cloud Config if it is properly managed.
        self.resource_deleted = resource_deleted
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        self.resource_owner_id = resource_owner_id
        # The resource type. Separate multiple resource types with commas (,).
        self.resource_types = resource_types
        # The start of the time range to query. This is a standard UTC timestamp. The following limits apply:
        # 
        # - The value must be a timestamp in milliseconds.
        # 
        # - The value cannot be later than EndUpdateTimestamp. The interval between StartUpdateTimestamp and EndUpdateTimestamp cannot exceed 30 days.
        # 
        # - You must specify both StartUpdateTimestamp and EndUpdateTimestamp, or leave both empty.
        self.start_update_timestamp = start_update_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.end_update_timestamp is not None:
            result['EndUpdateTimestamp'] = self.end_update_timestamp

        if self.exclude_resource_types is not None:
            result['ExcludeResourceTypes'] = self.exclude_resource_types

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.regions is not None:
            result['Regions'] = self.regions

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.start_update_timestamp is not None:
            result['StartUpdateTimestamp'] = self.start_update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('EndUpdateTimestamp') is not None:
            self.end_update_timestamp = m.get('EndUpdateTimestamp')

        if m.get('ExcludeResourceTypes') is not None:
            self.exclude_resource_types = m.get('ExcludeResourceTypes')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Regions') is not None:
            self.regions = m.get('Regions')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('StartUpdateTimestamp') is not None:
            self.start_update_timestamp = m.get('StartUpdateTimestamp')

        return self

