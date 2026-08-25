# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListGroupMembersResponseBody(DaraModel):
    def __init__(
        self,
        group_members: List[main_models.ListGroupMembersResponseBodyGroupMembers] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # The users in the group.
        self.group_members = group_members
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
        if self.group_members:
            for v1 in self.group_members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GroupMembers'] = []
        if self.group_members is not None:
            for k1 in self.group_members:
                result['GroupMembers'].append(k1.to_map() if k1 else None)

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
        self.group_members = []
        if m.get('GroupMembers') is not None:
            for k1 in m.get('GroupMembers'):
                temp_model = main_models.ListGroupMembersResponseBodyGroupMembers()
                self.group_members.append(temp_model.from_map(k1))

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

class ListGroupMembersResponseBodyGroupMembers(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        email: str = None,
        group_id: str = None,
        join_time: str = None,
        provision_type: str = None,
        status: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The description of the user.
        self.description = description
        # The display name of the user.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The ID of the group.
        self.group_id = group_id
        # The time when the user was added to the group.
        self.join_time = join_time
        # The type of the user. Valid values:
        # 
        # *   Manual: The user is manually created.
        # *   Synchronized: The user is synchronized from an external identity provider (IdP).
        self.provision_type = provision_type
        # The status of the user. Valid values:
        # 
        # *   Enabled: The logon of the user is enabled.
        # *   Disabled: The logon of the user is disabled.
        self.status = status
        # The ID of the user.
        self.user_id = user_id
        # The name of the user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

