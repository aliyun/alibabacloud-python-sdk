# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainStatisticsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_type: str = None,
        end_date: str = None,
        lang: str = None,
        start_date: str = None,
    ):
        # The domain name. You can call the [DescribeDomains](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomains?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to obtain the domain name.
        self.domain_name = domain_name
        # The type of the domain name. Valid values:
        # 
        # *   PUBLIC (default): hosted public domain name
        # *   CACHE: cached public domain name
        self.domain_type = domain_type
        # The end date of the query. Specify the end date in the **YYYY-MM-DD** format.
        # 
        # The default value is the day when you query the data.
        self.end_date = end_date
        # The language of the content within the request and response.
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The start date of the query. Specify the start date in the **YYYY-MM-DD** format.
        # 
        # You can only query the DNS records within the last 90 days.``
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

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

