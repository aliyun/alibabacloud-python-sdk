# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateMemberResponseBody(DaraModel):
    def __init__(
        self,
        members: List[main_models.CreateMemberResponseBodyMembers] = None,
        request_id: str = None,
    ):
        # The returned members.
        self.members = members
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.CreateMemberResponseBodyMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateMemberResponseBodyMembers(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        member_id: str = None,
        roles: List[str] = None,
        user_id: str = None,
    ):
        # The display name.
        self.display_name = display_name
        # The member ID.
        self.member_id = member_id
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
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

