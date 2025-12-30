# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordStatisticsSummaryRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_type: str = None,
        end_date: str = None,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        search_mode: str = None,
        start_date: str = None,
        threshold: int = None,
    ):
        # The domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The type of the domain name. The parameter value is not case-sensitive. Valid values:
        # 
        # *   PUBLIC (default): hosted public domain name
        # *   CACHE: cache-accelerated domain name
        self.domain_type = domain_type
        # The end date of the query. Specify the start date in the **YYYY-MM-DD** format.
        # 
        # The default value is the day when you query the data.
        self.end_date = end_date
        # The keyword for searches in %KeyWord% mode. The value is not case-sensitive.
        self.keyword = keyword
        # The language.
        self.lang = lang
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **20**.
        self.page_size = page_size
        # The search mode of the keyword. Valid values:
        # 
        # *   **LIKE** (default): fuzzy search
        # *   **EXACT**: exact search
        self.search_mode = search_mode
        # The start date of the query. Specify the start date in the **YYYY-MM-DD** format.
        # 
        # You can only query the DNS records within the last 90 days.``
        # 
        # This parameter is required.
        self.start_date = start_date
        # The maximum number of DNS requests that you can obtain. You can obtain data about a domain name with DNS request volume less than or equal to the maximum number. For example, if you set this parameter to 100, you can query domain names with less than 100 DNS requests.
        self.threshold = threshold

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

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

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

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

