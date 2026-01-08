# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class AddInstanceMembersRequest(DaraModel):
    def __init__(
        self,
        members: List[main_models.AddInstanceMembersRequestMembers] = None,
    ):
        # The members.
        # 
        # This parameter is required.
        self.members = members

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.AddInstanceMembersRequestMembers()
                self.members.append(temp_model.from_map(k1))

        return self

class AddInstanceMembersRequestMembers(DaraModel):
    def __init__(
        self,
        member_desc: str = None,
        member_uid: int = None,
    ):
        # The remarks of the member. The value must be 1 to 256 characters in length.
        self.member_desc = member_desc
        # The UID of the member. You can add up to 20 members to Cloud Firewall at a time.
        # 
        # This parameter is required.
        self.member_uid = member_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        return self

