# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertDirectConversationToWorkRequest(DaraModel):
    def __init__(
        self,
        session_id: str = None,
        tenant_id: str = None,
    ):
        # 源会话 ID；首次调用建立转换，后续使用同一 ID 查询或继续原转换
        # 
        # This parameter is required.
        self.session_id = session_id
        # 租户 ID，公共参数，缺省时使用调用方默认租户；仍需通过源会话归属及权限校验
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

