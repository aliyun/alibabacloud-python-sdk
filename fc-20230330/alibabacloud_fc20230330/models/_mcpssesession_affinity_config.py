# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MCPSSESessionAffinityConfig(DaraModel):
    def __init__(
        self,
        session_concurrency_per_instance: int = None,
        sse_endpoint_path: str = None,
    ):
        self.session_concurrency_per_instance = session_concurrency_per_instance
        self.sse_endpoint_path = sse_endpoint_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_concurrency_per_instance is not None:
            result['sessionConcurrencyPerInstance'] = self.session_concurrency_per_instance

        if self.sse_endpoint_path is not None:
            result['sseEndpointPath'] = self.sse_endpoint_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionConcurrencyPerInstance') is not None:
            self.session_concurrency_per_instance = m.get('sessionConcurrencyPerInstance')

        if m.get('sseEndpointPath') is not None:
            self.sse_endpoint_path = m.get('sseEndpointPath')

        return self

