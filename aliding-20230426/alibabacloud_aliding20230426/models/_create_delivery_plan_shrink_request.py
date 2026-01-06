# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeliveryPlanShrinkRequest(DaraModel):
    def __init__(
        self,
        content_shrink: str = None,
        end_time: int = None,
        res_id: str = None,
        start_time: int = None,
        tenant_context_shrink: str = None,
        user_id_list_shrink: str = None,
    ):
        self.content_shrink = content_shrink
        self.end_time = end_time
        self.res_id = res_id
        self.start_time = start_time
        self.tenant_context_shrink = tenant_context_shrink
        self.user_id_list_shrink = user_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.res_id is not None:
            result['ResId'] = self.res_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.user_id_list_shrink is not None:
            result['UserIdList'] = self.user_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ResId') is not None:
            self.res_id = m.get('ResId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('UserIdList') is not None:
            self.user_id_list_shrink = m.get('UserIdList')

        return self

