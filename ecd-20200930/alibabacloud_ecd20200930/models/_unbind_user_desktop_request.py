# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnbindUserDesktopRequest(DaraModel):
    def __init__(
        self,
        desktop_agent_ids: List[str] = None,
        desktop_group_id: str = None,
        desktop_ids: List[str] = None,
        force: bool = None,
        reason: str = None,
        user_desktop_ids: List[str] = None,
    ):
        self.desktop_agent_ids = desktop_agent_ids
        self.desktop_group_id = desktop_group_id
        self.desktop_ids = desktop_ids
        self.force = force
        self.reason = reason
        self.user_desktop_ids = user_desktop_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_agent_ids is not None:
            result['DesktopAgentIds'] = self.desktop_agent_ids

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.force is not None:
            result['Force'] = self.force

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.user_desktop_ids is not None:
            result['UserDesktopIds'] = self.user_desktop_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopAgentIds') is not None:
            self.desktop_agent_ids = m.get('DesktopAgentIds')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('UserDesktopIds') is not None:
            self.user_desktop_ids = m.get('UserDesktopIds')

        return self

