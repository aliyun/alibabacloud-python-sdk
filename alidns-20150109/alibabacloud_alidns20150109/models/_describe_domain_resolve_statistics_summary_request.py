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
        # The sort direction. Valid values:
        # 
        # - DESC: descending
        # 
        # - ASC: ascending
        self.direction = direction
        # The end date. The format is yyyy-MM-dd. For example, 2023-03-13.
        self.end_date = end_date
        # The keyword. This parameter is used with SearchMode.
        self.keyword = keyword
        # The language. Valid values: zh, en, and ja.
        self.lang = lang
        # The page number. The value starts from 1. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. The maximum value is 1000. The minimum value is 1.
        self.page_size = page_size
        # The search mode of the keyword. Valid values:
        # 
        # - LIKE: fuzzy search (default)
        # 
        # - EXACT: exact match
        self.search_mode = search_mode
        # The start date. The format is yyyy-MM-dd. For example, 2023-03-01.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The threshold for the number of DNS queries. This parameter filters domain names by query volume.
        # 
        # If you do not specify this parameter, the operation returns domain names with more than zero queries.
        # 
        # If you specify a value less than 0, the operation returns all domain names.
        # 
        # If you specify 0, the operation returns domain names with zero queries.
        # 
        # If you specify a value greater than 0, the operation returns domain names with a query volume up to this value.
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

