# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOutgoingRiskDomainAndIpCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_domain_count: int = None,
        risk_ip_count: int = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.risk_domain_count = risk_domain_count
        self.risk_ip_count = risk_ip_count
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_domain_count is not None:
            result['RiskDomainCount'] = self.risk_domain_count

        if self.risk_ip_count is not None:
            result['RiskIpCount'] = self.risk_ip_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskDomainCount') is not None:
            self.risk_domain_count = m.get('RiskDomainCount')

        if m.get('RiskIpCount') is not None:
            self.risk_ip_count = m.get('RiskIpCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

