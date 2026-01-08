# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMemberInfoResponseBody(DaraModel):
    def __init__(
        self,
        admin_name: str = None,
        admin_uid: str = None,
        is_member: bool = None,
        member_uid: str = None,
        request_id: str = None,
    ):
        self.admin_name = admin_name
        self.admin_uid = admin_uid
        self.is_member = is_member
        self.member_uid = member_uid
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name

        if self.admin_uid is not None:
            result['AdminUid'] = self.admin_uid

        if self.is_member is not None:
            result['IsMember'] = self.is_member

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')

        if m.get('AdminUid') is not None:
            self.admin_uid = m.get('AdminUid')

        if m.get('IsMember') is not None:
            self.is_member = m.get('IsMember')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

