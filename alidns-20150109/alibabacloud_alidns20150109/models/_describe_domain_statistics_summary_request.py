# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainStatisticsSummaryRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        search_mode: str = None,
        start_date: str = None,
        threshold: int = None,
    ):
        # The end of the time range to query. Specify the time in the **YYYY-MM-DD** format.
        # 
        # The default value is the day when you perform the operation.
        self.end_date = end_date
        # The keyword for searches in %KeyWord% mode. The value is not case-sensitive.
        self.keyword = keyword
        # The language type.
        self.lang = lang
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **20**.
        self.page_size = page_size
        # The search mode of the keyword. Valid values:
        # 
        # *   **LIKE**: fuzzy match (default).
        # *   **EXACT**: exact match.
        self.search_mode = search_mode
        # The beginning of the time range to query. Specify the time in the **YYYY-MM-DD** format.
        # 
        # You can only query DNS records of the last 90 days.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The threshold of query volume that can be obtained. You can also obtain data about a domain name with the query volume less than or equal to the threshold. For example, if you set this parameter to 100, you can query domain names with less than 100 queries.
        self.threshold = threshold

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

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.threshold is not None:
            result['Threshold'] = self.threshold

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

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

