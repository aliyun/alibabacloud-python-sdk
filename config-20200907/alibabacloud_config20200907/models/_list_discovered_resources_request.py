# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDiscoveredResourcesRequest(DaraModel):
    def __init__(
        self,
        end_update_timestamp: int = None,
        exclude_resource_types: str = None,
        max_results: int = None,
        next_token: str = None,
        regions: str = None,
        resource_deleted: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_types: str = None,
        start_update_timestamp: int = None,
    ):
        # The end time of the time range for querying resources. The value is a timestamp in the UTC format. When you specify this parameter, take note of the following limits:
        # 
        # *   The value must be a timestamp in milliseconds.
        # *   The value cannot be less than the value of the StartUpdateTimestamp parameter. The interval between the value and the value of the StartUpdateTimestamp parameter must be less than or equal to 30 days.
        # *   The StartUpdateTimestamp and EndUpdateTimestamp parameters must be specified at the same time or left empty at the same time.
        self.end_update_timestamp = end_update_timestamp
        # The types of resources that are excluded. Separate multiple values with commas (,). If this parameter conflicts with the ResourceTypes parameter, this parameter prevails.
        self.exclude_resource_types = exclude_resource_types
        # The maximum number of entries returned for a single request. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.max_results = max_results
        # The `token` that you want to use to initiate the current request. If the response of the previous request is truncated, you can use this token to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The ID of the region where the resource resides. Separate multiple region IDs with commas (,).
        self.regions = regions
        # The status of the resource. Valid values:
        # 
        # *   0: The resource is deleted. If a resource is deleted from the desired cloud service, **Deleted** is displayed in the resource list in the Cloud Config console.
        # *   1 (default): The resource is retained. If a resource is managed as expected, **Active** is displayed in the resource list in the Cloud Config console.
        self.resource_deleted = resource_deleted
        # The resource ID.
        self.resource_id = resource_id
        self.resource_name = resource_name
        # The type of the resource. Separate multiple resource types with commas (,).
        self.resource_types = resource_types
        # The start time of the time range for querying resources. The value is a timestamp in the UTC format. When you specify this parameter, take note of the following limits:
        # 
        # *   The value must be a timestamp in milliseconds.
        # *   The value cannot be greater than the value of the EndUpdateTimestamp parameter. The interval between the value and the value of the EndUpdateTimestamp parameter must be less than or equal to 30 days.
        # *   The StartUpdateTimestamp and EndUpdateTimestamp parameters must be specified at the same time or left blank at the same time.
        self.start_update_timestamp = start_update_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.resource_deleted is not None:
            result['ResourceDeleted'] = self.resource_deleted

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.start_update_timestamp is not None:
            result['StartUpdateTimestamp'] = self.start_update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('ResourceDeleted') is not None:
            self.resource_deleted = m.get('ResourceDeleted')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('StartUpdateTimestamp') is not None:
            self.start_update_timestamp = m.get('StartUpdateTimestamp')

        return self

