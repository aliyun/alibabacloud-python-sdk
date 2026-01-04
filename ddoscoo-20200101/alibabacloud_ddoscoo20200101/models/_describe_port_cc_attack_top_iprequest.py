# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePortCcAttackTopIPRequest(DaraModel):
    def __init__(
        self,
        ip: str = None,
        limit: int = None,
        port: str = None,
        start_timestamp: int = None,
    ):
        # The IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance to query.
        # 
        # This parameter is required.
        self.ip = ip
        # The maximum number of entries to return.
        self.limit = limit
        # The attacked port.
        # 
        # This parameter is required.
        self.port = port
        # The beginning of the time range to query. Unit: seconds.
        # 
        # This parameter is required.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.port is not None:
            result['Port'] = self.port

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

