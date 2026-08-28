# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSyncMCPServerRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        namespace: str = None,
        source_id: str = None,
    ):
        self.gateway_id = gateway_id
        self.namespace = namespace
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        return self

