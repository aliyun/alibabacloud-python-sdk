# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChatSessionRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        session_id: str = None,
        tenant_id: str = None,
    ):
        # The maximum number of resources to return. If not specified, the default value is 20. The maximum value is 100. The actual number of returned results may be less than the specified value but will not exceed it.
        self.limit = limit
        # The SessionId value to filter by. If specified, all Active/Expired status information associated with this session is returned.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The effective tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

