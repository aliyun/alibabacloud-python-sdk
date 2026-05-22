# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserIdByOpenDingtalkIdShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        open_dingtalk_id: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.open_dingtalk_id = open_dingtalk_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.open_dingtalk_id is not None:
            result['openDingtalkId'] = self.open_dingtalk_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('openDingtalkId') is not None:
            self.open_dingtalk_id = m.get('openDingtalkId')

        return self

