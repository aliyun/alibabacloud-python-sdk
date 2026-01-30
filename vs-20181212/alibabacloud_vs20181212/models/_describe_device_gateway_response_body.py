# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDeviceGatewayResponseBody(DaraModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        protocol: str = None,
        request_id: str = None,
        token: str = None,
    ):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.request_id = request_id
        self.token = token

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

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

