# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePdnsThreatStatisticsRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        domain_name: str = None,
        end_date: str = None,
        lang: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        sub_domain: str = None,
        threat_level: str = None,
        threat_source_ip: str = None,
        threat_type: str = None,
        type: str = None,
    ):
        self.direction = direction
        self.domain_name = domain_name
        self.end_date = end_date
        self.lang = lang
        self.order_by = order_by
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.sub_domain = sub_domain
        self.threat_level = threat_level
        self.threat_source_ip = threat_source_ip
        self.threat_type = threat_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.threat_source_ip is not None:
            result['ThreatSourceIp'] = self.threat_source_ip

        if self.threat_type is not None:
            result['ThreatType'] = self.threat_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('ThreatSourceIp') is not None:
            self.threat_source_ip = m.get('ThreatSourceIp')

        if m.get('ThreatType') is not None:
            self.threat_type = m.get('ThreatType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

