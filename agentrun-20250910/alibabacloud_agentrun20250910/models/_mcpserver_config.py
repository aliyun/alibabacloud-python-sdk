# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MCPServerConfig(DaraModel):
    def __init__(
        self,
        server_url: str = None,
        sse_path: str = None,
        transport_type: str = None,
    ):
        self.server_url = server_url
        self.sse_path = sse_path
        self.transport_type = transport_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server_url is not None:
            result['serverUrl'] = self.server_url

        if self.sse_path is not None:
            result['ssePath'] = self.sse_path

        if self.transport_type is not None:
            result['transportType'] = self.transport_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serverUrl') is not None:
            self.server_url = m.get('serverUrl')

        if m.get('ssePath') is not None:
            self.sse_path = m.get('ssePath')

        if m.get('transportType') is not None:
            self.transport_type = m.get('transportType')

        return self

