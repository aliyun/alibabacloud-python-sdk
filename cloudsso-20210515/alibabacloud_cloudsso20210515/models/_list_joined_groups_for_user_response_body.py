# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListJoinedGroupsForUserResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        joined_groups: List[main_models.ListJoinedGroupsForUserResponseBodyJoinedGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # Indicates whether the queried entries are truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The groups to which the user is added.
        self.joined_groups = joined_groups
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        # 
        # >  This parameter is returned only when the `IsTruncated` parameter is `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_counts = total_counts

    def validate(self):
        if self.joined_groups:
            for v1 in self.joined_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        result['JoinedGroups'] = []
        if self.joined_groups is not None:
            for k1 in self.joined_groups:
                result['JoinedGroups'].append(k1.to_map() if k1 else None)

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
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        self.joined_groups = []
        if m.get('JoinedGroups') is not None:
            for k1 in m.get('JoinedGroups'):
                temp_model = main_models.ListJoinedGroupsForUserResponseBodyJoinedGroups()
                self.joined_groups.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ListJoinedGroupsForUserResponseBodyJoinedGroups(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        join_time: str = None,
        provision_type: str = None,
        user_id: str = None,
    ):
        # The description of the group.
        self.description = description
        # The ID of the group.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The time when the user was added to the group.
        self.join_time = join_time
        # The type of the group. Valid values:
        # 
        # *   Manual: The group is manually created.
        # *   Synchronized: The group is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

