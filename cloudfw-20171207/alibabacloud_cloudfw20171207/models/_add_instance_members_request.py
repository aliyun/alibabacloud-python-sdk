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
        # The list of Cloud Firewall member accounts to add. Call DescribeInstanceRdAccounts to obtain the available MemberUid values. You can add up to 20 members at a time, subject to the instance member quota.
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
        # The description of the Cloud Firewall member account. The description must be 1 to 256 characters in length. You can add up to 20 member accounts.
        self.member_desc = member_desc
        # The UID of the Cloud Firewall member account. You can add up to 20 member accounts.
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

