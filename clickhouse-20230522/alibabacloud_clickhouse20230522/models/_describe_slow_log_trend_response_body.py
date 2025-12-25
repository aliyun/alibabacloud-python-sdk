# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogTrendResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSlowLogTrendResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSlowLogTrendResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSlowLogTrendResponseBodyData(DaraModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        result_set: List[main_models.DescribeSlowLogTrendResponseBodyDataResultSet] = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The result sets.
        self.result_set = result_set

    def validate(self):
        if self.result_set:
            for v1 in self.result_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        result['ResultSet'] = []
        if self.result_set is not None:
            for k1 in self.result_set:
                result['ResultSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        self.result_set = []
        if m.get('ResultSet') is not None:
            for k1 in m.get('ResultSet'):
                temp_model = main_models.DescribeSlowLogTrendResponseBodyDataResultSet()
                self.result_set.append(temp_model.from_map(k1))

        return self

class DescribeSlowLogTrendResponseBodyDataResultSet(DaraModel):
    def __init__(
        self,
        avg_query_duration_ms: int = None,
        cnt: int = None,
        max_query_duration_ms: int = None,
        min_query_duration_ms: int = None,
        query_start_time: str = None,
    ):
        # The average execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.avg_query_duration_ms = avg_query_duration_ms
        # The total number of SQL queries within the specified time range.
        self.cnt = cnt
        # The maximum execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.max_query_duration_ms = max_query_duration_ms
        # The minimum execution duration of slow SQL queries. Minimum value: **1000**. Unit: milliseconds.
        self.min_query_duration_ms = min_query_duration_ms
        # The beginning of the time range to query. The time is in the yyyy-MM-dd hh:mm:ss format. The time is displayed in UTC.
        self.query_start_time = query_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_query_duration_ms is not None:
            result['AvgQueryDurationMs'] = self.avg_query_duration_ms

        if self.cnt is not None:
            result['Cnt'] = self.cnt

        if self.max_query_duration_ms is not None:
            result['MaxQueryDurationMs'] = self.max_query_duration_ms

        if self.min_query_duration_ms is not None:
            result['MinQueryDurationMs'] = self.min_query_duration_ms

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgQueryDurationMs') is not None:
            self.avg_query_duration_ms = m.get('AvgQueryDurationMs')

        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')

        if m.get('MaxQueryDurationMs') is not None:
            self.max_query_duration_ms = m.get('MaxQueryDurationMs')

        if m.get('MinQueryDurationMs') is not None:
            self.min_query_duration_ms = m.get('MinQueryDurationMs')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        return self

