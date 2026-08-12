# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel



class AgenticFSVolumeConfig(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        server_addr: str = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.server_addr = server_addr
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupID'] = self.group_id

        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr

        if self.user_id is not None:
            result['userID'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupID') is not None:
            self.group_id = m.get('groupID')

        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        return self

