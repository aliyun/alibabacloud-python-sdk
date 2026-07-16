# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePdnsRequestStatisticRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_date: str = None,
        lang: str = None,
        start_date: str = None,
        sub_domain: str = None,
        type: str = None,
    ):
        # The primary domain name for which you want to query statistics.
        self.domain_name = domain_name
        # The end date of the query in the **YYYY-MM-DD** format.
        # 
        # The default value is the current day.
        self.end_date = end_date
        # The language of the request and response. The default value is **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The start date of the query in the **YYYY-MM-DD** format.
        # 
        # You can query data from the last 90 days.
        self.start_date = start_date
        # The subdomain for which you want to query statistics.
        self.sub_domain = sub_domain
        # The dimension for statistics. Valid values:
        # 
        # - **ACCOUNT**: queries statistics by account.
        # 
        # - **DOMAIN**: queries statistics by domain name. The DomainName parameter is required.
        # 
        # - **SUB_DOMAIN**: queries statistics by subdomain. The DomainName and SubDomain parameters are required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

