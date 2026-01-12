# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Member(DaraModel):
    def __init__(
        self,
        member_id: str = None,
        member_type: str = None,
    ):
        self.member_id = member_id
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_type is not None:
            result['MemberType'] = self.member_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')

        return self

