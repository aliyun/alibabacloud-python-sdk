# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TCPSocketAction(DaraModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

