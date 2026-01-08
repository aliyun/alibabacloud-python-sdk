# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteInstanceMembersRequest(DaraModel):
    def __init__(
        self,
        member_uids: List[int] = None,
    ):
        # The UIDs of the members.
        # 
        # This parameter is required.
        self.member_uids = member_uids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_uids is not None:
            result['MemberUids'] = self.member_uids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberUids') is not None:
            self.member_uids = m.get('MemberUids')

        return self

