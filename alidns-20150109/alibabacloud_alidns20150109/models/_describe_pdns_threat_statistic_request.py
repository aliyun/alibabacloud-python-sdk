# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePdnsThreatStatisticRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        lang: str = None,
        start_date: str = None,
        threat_source_ip: str = None,
    ):
        self.end_date = end_date
        self.lang = lang
        self.start_date = start_date
        self.threat_source_ip = threat_source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.threat_source_ip is not None:
            result['ThreatSourceIp'] = self.threat_source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('ThreatSourceIp') is not None:
            self.threat_source_ip = m.get('ThreatSourceIp')

        return self

