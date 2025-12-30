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
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The type of the domain name. The parameter value is not case-sensitive. Valid values:
        # 
        # *   PUBLIC (default): hosted public domain name
        # *   CACHE: cache-accelerated domain name
        self.domain_type = domain_type
        # The end date of the query. Specify the end date in the **YYYY-MM-DD** format.
        # 
        # The default value is the day when you query the data.
        self.end_date = end_date
        # The language.
        self.lang = lang
        # The hostname. If you want to resolve www.dns-exmaple.top, set Rr to www.
        # 
        # This parameter is required.
        self.rr = rr
        # The start date of the query. Specify the start date in the **YYYY-MM-DD** format.
        # 
        # You can only query the DNS records within the last 90 days.``
        # 
        # If the time range is less than or equal to seven days, data is returned on an hourly basis.````
        # 
        # If the time range is greater than seven days, data is returned on a daily basis.````
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

