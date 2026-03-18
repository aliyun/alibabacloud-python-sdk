# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRdMemberListShrinkRequest(DaraModel):
    def __init__(
        self,
        member_list_shrink: str = None,
    ):
        # The list of the members.
        # 
        # This parameter is required.
        self.member_list_shrink = member_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_list_shrink is not None:
            result['MemberList'] = self.member_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberList') is not None:
            self.member_list_shrink = m.get('MemberList')

        return self

