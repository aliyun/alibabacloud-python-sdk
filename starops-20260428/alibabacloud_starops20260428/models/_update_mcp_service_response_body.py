# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMcpServiceResponseBody(DaraModel):
    def __init__(
        self,
        mcp_service_name: str = None,
        request_id: str = None,
    ):
        self.mcp_service_name = mcp_service_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mcp_service_name is not None:
            result['mcpServiceName'] = self.mcp_service_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mcpServiceName') is not None:
            self.mcp_service_name = m.get('mcpServiceName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

