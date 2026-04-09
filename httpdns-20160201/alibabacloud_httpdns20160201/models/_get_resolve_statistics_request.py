# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResolveStatisticsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        granularity: str = None,
        protocol_name: str = None,
        time_span: int = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.granularity = granularity
        self.protocol_name = protocol_name
        # This parameter is required.
        self.time_span = time_span

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        if self.time_span is not None:
            result['TimeSpan'] = self.time_span

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('TimeSpan') is not None:
            self.time_span = m.get('TimeSpan')

        return self

