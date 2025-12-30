# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainResolveStatisticsSummaryRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        end_date: str = None,
        keyword: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        search_mode: str = None,
        start_date: str = None,
        threshold: int = None,
    ):
        # The order in which you want to sort the returned entries. Valid values:
        # 
        # *   DESC: the descending order
        # *   ASC: the ascending order
        self.direction = direction
        # The end time in the yyyy-MM-dd format, for example, 2023-03-13.
        self.end_date = end_date
        # The keyword. The Keyword parameter is used together with the SearchMode parameter.
        self.keyword = keyword
        # The language. Valid values: zh, en, and ja.
        self.lang = lang
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 1000.
        self.page_size = page_size
        # The search mode of the keyword. Valid values:
        # 
        # *   LIKE (default): fuzzy search
        # *   EXACT: exact search
        self.search_mode = search_mode
        # The start time in the yyyy-MM-dd format, for example, 2023-03-01.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The threshold for the number of Domain Name System (DNS) requests. You can query the domain names at the specified quantity level of DNS requests and query the number of DNS requests for each domain name.
        # 
        # If you do not specify this parameter, the data about the domain names that have DNS requests is obtained.
        # 
        # If you set this parameter to a value less than 0, the data about all domain names is obtained.
        # 
        # If you set this parameter to 0, the data about the domain names that do not have DNS requests is obtained.
        # 
        # If you set this parameter to a value greater than 0, the data about the domain names whose number of DNS requests is less than or equal to the value of this parameter is obtained.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

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
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

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

