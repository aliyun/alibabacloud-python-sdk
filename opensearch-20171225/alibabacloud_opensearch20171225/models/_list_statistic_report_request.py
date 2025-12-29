# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStatisticReportRequest(DaraModel):
    def __init__(
        self,
        columns: str = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        start_time: int = None,
    ):
        # The fields to query. Set this parameter in the format of columns="pv,uv,ipv". For more information, see [Metrics of statistical reports](https://help.aliyun.com/document_detail/187665.html).
        self.columns = columns
        # The end timestamp of the query. By default, the end time is the current time. Unit: seconds.
        self.end_time = end_time
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The query conditions. Set this parameter in the format of k1:v1,k2:v2. Valid values:
        # 
        # *   experimentSerialNumber: the globally unique sequence number of the test
        # *   sceneTag: the tag of the test scenario
        # *   bizType: the type of the business
        # *   modelId: the ID of the algorithm model
        self.query = query
        # The start timestamp of the query. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['columns'] = self.columns

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query is not None:
            result['query'] = self.query

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

