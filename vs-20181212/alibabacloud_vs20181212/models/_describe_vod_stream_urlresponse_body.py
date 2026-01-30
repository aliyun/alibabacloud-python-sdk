# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodStreamURLResponseBody(DaraModel):
    def __init__(
        self,
        out_protocol: str = None,
        port: int = None,
        request_id: str = None,
        url: str = None,
    ):
        self.out_protocol = out_protocol
        self.port = port
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol

        if self.port is not None:
            result['Port'] = self.port

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

