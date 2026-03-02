# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Member(DaraModel):
    def __init__(
        self,
        member: str = None,
        role: str = None,
    ):
        # The member ID.
        # 
        # This parameter is required.
        self.member = member
        # The role of the member.
        # 
        # Valid values:
        # 
        # *   EDITOR
        # *   VIEWER
        # *   ADMIN
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member is not None:
            result['member'] = self.member

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('member') is not None:
            self.member = m.get('member')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

