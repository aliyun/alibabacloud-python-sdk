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
        # The type of the domain name. This parameter is not case-sensitive. Valid values:
        # 
        # - PUBLIC: authoritative domain name (default)
        # 
        # - CACHE: proxy domain name
        self.domain_type = domain_type
        # The end date of the query. The format is **YYYY-MM-DD**.
        # 
        # The default value is the current day.
        self.end_date = end_date
        # The keyword. The search is performed in the %KeyWord% format and is not case-sensitive.
        self.keyword = keyword
        # The language of the response. Valid values:
        # 
        # - zh: Chinese
        # 
        # - en: English
        # 
        # The default value is en.
        self.lang = lang
        # The page number. The value starts from **1**. The default value is **1**.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is **100**, the minimum value is **1**, and the default value is **20**.
        self.page_size = page_size
        # The search mode for the keyword. Valid values:
        # 
        # - **LIKE**: fuzzy search (default)
        # 
        # - **EXACT**: exact match
        self.search_mode = search_mode
        # The start date of the query. The format is **YYYY-MM-DD**.
        # 
        # You can query data only from the last 90 days. The value of `StartDate` must be greater than or equal to the current date minus 90 days.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The threshold for the number of DNS requests. This operation returns data for subdomains whose request count is less than or equal to this value.
        # 
        # - If you set this parameter to 100, subdomains with a request count from 1 to 100 are returned.
        # 
        # - If you leave this parameter empty, all subdomains that have DNS requests are returned.
        # 
        # - If you set this parameter to 0, subdomains with no DNS requests are returned. If a domain name is added on the current day and has no requests, you can query its data on the next day.
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

