# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class LookupResourceGroupEventsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_category: str = None,
        lookup_attributes: List[main_models.LookupResourceGroupEventsRequestLookupAttributes] = None,
        max_results: str = None,
        next_token: str = None,
        resource_group_display_name: str = None,
        resource_group_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. The time is displayed in UTC.
        self.end_time = end_time
        # The event type.
        # 
        # This parameter is required.
        self.event_category = event_category
        # The attributes used for advanced search.
        self.lookup_attributes = lookup_attributes
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The resource group name.
        self.resource_group_display_name = resource_group_display_name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.lookup_attributes:
            for v1 in self.lookup_attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_category is not None:
            result['EventCategory'] = self.event_category

        result['LookupAttributes'] = []
        if self.lookup_attributes is not None:
            for k1 in self.lookup_attributes:
                result['LookupAttributes'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_display_name is not None:
            result['ResourceGroupDisplayName'] = self.resource_group_display_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventCategory') is not None:
            self.event_category = m.get('EventCategory')

        self.lookup_attributes = []
        if m.get('LookupAttributes') is not None:
            for k1 in m.get('LookupAttributes'):
                temp_model = main_models.LookupResourceGroupEventsRequestLookupAttributes()
                self.lookup_attributes.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupDisplayName') is not None:
            self.resource_group_display_name = m.get('ResourceGroupDisplayName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class LookupResourceGroupEventsRequestLookupAttributes(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the attribute.
        self.key = key
        # The value of the attribute.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

