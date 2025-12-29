# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GRPCAction(DaraModel):
    def __init__(
        self,
        port: int = None,
        service: str = None,
    ):
        self.port = port
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        if self.service is not None:
            result['service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('service') is not None:
            self.service = m.get('service')

        return self

