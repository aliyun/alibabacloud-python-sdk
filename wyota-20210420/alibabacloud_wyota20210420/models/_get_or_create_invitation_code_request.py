# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOrCreateInvitationCodeRequest(DaraModel):
    def __init__(
        self,
        expire_days: int = None,
        expire_minutes: int = None,
        terminal_group_id: str = None,
        type: int = None,
    ):
        self.expire_days = expire_days
        self.expire_minutes = expire_minutes
        self.terminal_group_id = terminal_group_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_days is not None:
            result['ExpireDays'] = self.expire_days

        if self.expire_minutes is not None:
            result['ExpireMinutes'] = self.expire_minutes

        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireDays') is not None:
            self.expire_days = m.get('ExpireDays')

        if m.get('ExpireMinutes') is not None:
            self.expire_minutes = m.get('ExpireMinutes')

        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

