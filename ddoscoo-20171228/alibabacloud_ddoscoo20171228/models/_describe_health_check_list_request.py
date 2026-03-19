# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHealthCheckListRequest(DaraModel):
    def __init__(
        self,
        listeners: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners is not None:
            result['Listeners'] = self.listeners

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

