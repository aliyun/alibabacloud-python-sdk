# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePdnsThreatLogsRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        threat_level: str = None,
        threat_source_ip: str = None,
        threat_type: str = None,
    ):
        self.end_date = end_date
        self.keyword = keyword
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.threat_level = threat_level
        self.threat_source_ip = threat_source_ip
        self.threat_type = threat_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.threat_source_ip is not None:
            result['ThreatSourceIp'] = self.threat_source_ip

        if self.threat_type is not None:
            result['ThreatType'] = self.threat_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('ThreatSourceIp') is not None:
            self.threat_source_ip = m.get('ThreatSourceIp')

        if m.get('ThreatType') is not None:
            self.threat_type = m.get('ThreatType')

        return self

