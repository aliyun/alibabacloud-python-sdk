# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListMembersResponseBody(DaraModel):
    def __init__(
        self,
        members: List[main_models.ListMembersResponseBodyMembers] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The members.
        self.members = members
        # The request ID.
        self.request_id = request_id
        # The number of members that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['Members'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.ListMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMembersResponseBodyMembers(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        display_name: str = None,
        gmt_create_time: str = None,
        member_id: str = None,
        member_name: str = None,
        roles: List[str] = None,
        user_id: str = None,
    ):
        self.account_name = account_name
        self.account_type = account_type
        # The display name of the member.
        self.display_name = display_name
        # The time when the user is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The member ID.
        self.member_id = member_id
        # The username.
        self.member_name = member_name
        # The list of roles.
        self.roles = roles
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

