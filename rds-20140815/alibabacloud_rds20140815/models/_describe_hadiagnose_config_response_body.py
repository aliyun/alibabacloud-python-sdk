# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHADiagnoseConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tcp_connection_type: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The availability check method of the instance. Valid values:
        # 
        # *   **LONG**: Alibaba Cloud uses persistent connections to check the availability of the instance.
        # *   **SHORT**: Alibaba Cloud uses short-lived connections to check the availability of the instance.
        self.tcp_connection_type = tcp_connection_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tcp_connection_type is not None:
            result['TcpConnectionType'] = self.tcp_connection_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TcpConnectionType') is not None:
            self.tcp_connection_type = m.get('TcpConnectionType')

        return self

