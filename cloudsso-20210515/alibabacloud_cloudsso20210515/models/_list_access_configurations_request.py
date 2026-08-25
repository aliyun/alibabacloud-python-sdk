# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListAccessConfigurationsRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        status_notifications: str = None,
        tags: List[main_models.ListAccessConfigurationsRequestTags] = None,
    ):
        # The directory ID.
        self.directory_id = directory_id
        # The filter condition.
        # 
        # Format: <Attribute> <Operator> <Value>. The filter is case-insensitive. Currently, <Attribute> supports only AccessConfigurationName, and <Operator> supports only eq (Equals) and sw (Start With).
        # 
        # Example: Filter = "AccessConfigurationName sw test" queries all access configurations whose names start with test. Filter = "AccessConfigurationName eq TestAccessConfiguration" queries the access configuration named TestAccessConfiguration.
        self.filter = filter
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token for the next page of results. You do not need to specify `NextToken` for the first API call.
        # 
        # When you call this API operation for the first time, if the total number of results exceeds the `MaxResults` limit, the results are truncated and only `MaxResults` entries are returned. In this case, the `IsTruncated` parameter is set to `true` and a `NextToken` is returned. You can use the `NextToken` returned from the previous call to continue calling this API operation while keeping other request parameters unchanged to query the truncated results. You can repeat this process until `IsTruncated` is `false`, which indicates that all data has been retrieved.
        self.next_token = next_token
        # The status notification information, which is used as a filter condition for the query.
        # 
        # Valid values: ReprovisionRequired, which queries access configurations that need to be reprovisioned.
        self.status_notifications = status_notifications
        # The list of tags.
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
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.status_notifications is not None:
            result['StatusNotifications'] = self.status_notifications

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('StatusNotifications') is not None:
            self.status_notifications = m.get('StatusNotifications')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListAccessConfigurationsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListAccessConfigurationsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

