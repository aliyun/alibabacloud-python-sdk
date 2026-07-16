# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDohSubDomainStatisticsSummaryRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_date: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        sub_domain: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The end date of the query. The format is YYYY-MM-DD.
        # 
        # The default value is the current day.
        self.end_date = end_date
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The current page number. The value starts from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. Maximum value: 100. Default value: 20.
        self.page_size = page_size
        # The start date of the query. The format is YYYY-MM-DD.
        # 
        # You can query data only from the last 90 days. StartDate must be greater than or equal to `Now - 90`.
        self.start_date = start_date
        # The subdomain.
        self.sub_domain = sub_domain

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

        return self

