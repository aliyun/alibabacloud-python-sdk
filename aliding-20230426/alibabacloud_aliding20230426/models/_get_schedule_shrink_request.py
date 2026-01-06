# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduleShrinkRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        tenant_context_shrink: str = None,
        user_ids_shrink: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.tenant_context_shrink = tenant_context_shrink
        self.user_ids_shrink = user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.user_ids_shrink is not None:
            result['UserIds'] = self.user_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('UserIds') is not None:
            self.user_ids_shrink = m.get('UserIds')

        return self

