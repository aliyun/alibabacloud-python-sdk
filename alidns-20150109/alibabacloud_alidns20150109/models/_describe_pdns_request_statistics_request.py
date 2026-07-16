# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePdnsRequestStatisticsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_date: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        sub_domain: str = None,
        type: str = None,
    ):
        # The primary domain name to query.
        self.domain_name = domain_name
        # The end date of the query. Use the YYYY-MM-DD format.
        # 
        # The default value is the current date.
        self.end_date = end_date
        # The language of the request and response. The default value is **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The page number. The value starts from **1**. The default value is **1**.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. The maximum value is 100. The default value is 20.
        self.page_size = page_size
        # The start date of the query. Use the YYYY-MM-DD format.
        # 
        # You can query data from the last 90 days only.
        self.start_date = start_date
        # The subdomain for which to view statistics.
        self.sub_domain = sub_domain
        # The type of request statistics to query. Valid values:
        # 
        # - DOMAIN: queries statistics by domain name.
        # 
        # - SUB_DOMAIN: queries statistics by subdomain.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

