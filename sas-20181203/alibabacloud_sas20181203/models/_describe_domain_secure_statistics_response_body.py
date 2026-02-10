# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainSecureStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        no_ssl_count: int = None,
        request_id: str = None,
        risk_count: int = None,
        total_domain_count: int = None,
        vul_count: int = None,
    ):
        # The number of domain names that trigger security alerts.
        self.alarm_count = alarm_count
        # The number of the websites for which no certificates are installed.
        self.no_ssl_count = no_ssl_count
        # The request ID.
        self.request_id = request_id
        # The number of the domain names that have security risks.
        self.risk_count = risk_count
        # The total number of domain names.
        self.total_domain_count = total_domain_count
        # The number of the domain names that have vulnerabilities.
        self.vul_count = vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count

        if self.no_ssl_count is not None:
            result['NoSslCount'] = self.no_ssl_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.total_domain_count is not None:
            result['TotalDomainCount'] = self.total_domain_count

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')

        if m.get('NoSslCount') is not None:
            self.no_ssl_count = m.get('NoSslCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('TotalDomainCount') is not None:
            self.total_domain_count = m.get('TotalDomainCount')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

