# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class DescribeAdvancedQueryHistoryResponseBody(DaraModel):
    def __init__(
        self,
        query_history_list: List[main_models.DescribeAdvancedQueryHistoryResponseBodyQueryHistoryList] = None,
        request_id: str = None,
    ):
        # The list of advanced query records.
        self.query_history_list = query_history_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.query_history_list:
            for v1 in self.query_history_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QueryHistoryList'] = []
        if self.query_history_list is not None:
            for k1 in self.query_history_list:
                result['QueryHistoryList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_history_list = []
        if m.get('QueryHistoryList') is not None:
            for k1 in m.get('QueryHistoryList'):
                temp_model = main_models.DescribeAdvancedQueryHistoryResponseBodyQueryHistoryList()
                self.query_history_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class DescribeAdvancedQueryHistoryResponseBodyQueryHistoryList(DaraModel):
    def __init__(
        self,
        query_id: str = None,
        query_sql: str = None,
        simple_query: bool = None,
        time_stamp: str = None,
    ):
        # The ID of the advanced query record.
        self.query_id = query_id
        # The conditional statement for the query.
        self.query_sql = query_sql
        # Indicates whether simple query mode is enabled.
        self.simple_query = simple_query
        # The time when the advanced query record was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.query_sql is not None:
            result['QuerySql'] = self.query_sql

        if self.simple_query is not None:
            result['SimpleQuery'] = self.simple_query

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('QuerySql') is not None:
            self.query_sql = m.get('QuerySql')

        if m.get('SimpleQuery') is not None:
            self.simple_query = m.get('SimpleQuery')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

