# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelScheduleConferenceShrinkRequest(DaraModel):
    def __init__(
        self,
        schedule_conference_id: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.schedule_conference_id = schedule_conference_id
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schedule_conference_id is not None:
            result['ScheduleConferenceId'] = self.schedule_conference_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleConferenceId') is not None:
            self.schedule_conference_id = m.get('ScheduleConferenceId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

