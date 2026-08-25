# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListGroupsResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[main_models.ListGroupsResponseBodyGroups] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # The groups.
        self.groups = groups
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        # 
        # >  This parameter is returned only when the value of the `IsTruncated` parameter is `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_counts = total_counts

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.ListGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ListGroupsResponseBodyGroups(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        provision_type: str = None,
        update_time: str = None,
    ):
        # The time when the group was created.
        self.create_time = create_time
        # The description of the group.
        self.description = description
        # The ID of the group.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The type of the group. Valid values:
        # 
        # *   Manual: The group is manually created.
        # *   Synchronized: The group is synchronized from an external IdP.
        self.provision_type = provision_type
        # The time when the information about the group was modified.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

