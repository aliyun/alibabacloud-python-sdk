# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStatisticLogsRequest(DaraModel):
    def __init__(
        self,
        columns: str = None,
        distinct: bool = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        sort_by: str = None,
        start_time: int = None,
        stop_time: int = None,
    ):
        # The fields to query. Format: columns=wordsTopPv.
        # 
        # For more information, see [Metrics in statistical reports](https://help.aliyun.com/document_detail/187665.html).
        self.columns = columns
        # Specifies whether to use the distinct clause.
        self.distinct = distinct
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The content of the query clause.
        self.query = query
        # The content of the sort clause.
        self.sort_by = sort_by
        # The beginning of the time range to query. The default value is the timestamp of 00:00:00 on the current day.
        self.start_time = start_time
        # The end of the time range to query. The default value is the timestamp of 24:00:00 on the current day.
        self.stop_time = stop_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['columns'] = self.columns

        if self.distinct is not None:
            result['distinct'] = self.distinct

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query is not None:
            result['query'] = self.query

        if self.sort_by is not None:
            result['sortBy'] = self.sort_by

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.stop_time is not None:
            result['stopTime'] = self.stop_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('distinct') is not None:
            self.distinct = m.get('distinct')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('stopTime') is not None:
            self.stop_time = m.get('stopTime')

        return self

