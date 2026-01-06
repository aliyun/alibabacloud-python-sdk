# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartMinutesShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        conference_id: str = None,
        owner_user_id: str = None,
        record_audio: bool = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.conference_id = conference_id
        # This parameter is required.
        self.owner_user_id = owner_user_id
        self.record_audio = record_audio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id

        if self.record_audio is not None:
            result['recordAudio'] = self.record_audio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')

        if m.get('recordAudio') is not None:
            self.record_audio = m.get('recordAudio')

        return self

