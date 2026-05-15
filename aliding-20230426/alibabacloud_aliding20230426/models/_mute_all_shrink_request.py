# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MuteAllShrinkRequest(DaraModel):
    def __init__(
        self,
        force_mute: bool = None,
        tenant_context_shrink: str = None,
        conference_id: str = None,
        mute_action: str = None,
    ):
        self.force_mute = force_mute
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.conference_id = conference_id
        # This parameter is required.
        self.mute_action = mute_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_mute is not None:
            result['ForceMute'] = self.force_mute

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.mute_action is not None:
            result['muteAction'] = self.mute_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceMute') is not None:
            self.force_mute = m.get('ForceMute')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('muteAction') is not None:
            self.mute_action = m.get('muteAction')

        return self

