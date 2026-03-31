# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridCloudUnsupportPortsResponseBody(DaraModel):
    def __init__(
        self,
        http_ports: str = None,
        https_ports: str = None,
        request_id: str = None,
    ):
        # The HTTP ports. The value is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.http_ports = http_ports
        # The HTTPS ports. The value is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.https_ports = https_ports
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

