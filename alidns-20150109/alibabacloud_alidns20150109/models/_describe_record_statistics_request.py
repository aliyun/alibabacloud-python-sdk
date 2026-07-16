# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordStatisticsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_type: str = None,
        end_date: str = None,
        lang: str = None,
        rr: str = None,
        start_date: str = None,
    ):
        # The primary domain name.
        # <props="china">For more information, see [DescribeDomains](https://help.aliyun.com/document_detail/29751.html).
        # <props="intl">For more information, see [DescribeDomains](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describedomains).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The type of the domain name. This parameter is not case-sensitive. Valid values:
        # 
        # - PUBLIC (default): authoritative domain name
        # 
        # - CACHE: authoritative proxy domain name
        self.domain_type = domain_type
        # The end date of the query. The format is **YYYY-MM-DD**.
        # 
        # The default value is the current date.
        self.end_date = end_date
        # The language of the return value. Valid values:
        # 
        # - zh (default): Chinese
        # 
        # - en: English
        self.lang = lang
        # The host record. For example, to resolve www\\.example.com, set this parameter to www.
        # 
        # This parameter is required.
        self.rr = rr
        # The start date of the query. The format is **YYYY-MM-DD**.
        # 
        # The start date must be within the last 90 days.
        # 
        # If the time range of the query is 7 days or less, data is returned by the hour.
        # 
        # If the time range of the query is more than 7 days, data is returned by the day.
        # 
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

