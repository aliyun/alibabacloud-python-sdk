# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeProcessListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeProcessListResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
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
            temp_model = main_models.DescribeProcessListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeProcessListResponseBodyData(DaraModel):
    def __init__(
        self,
        dbinstance_id: int = None,
        dbinstance_name: str = None,
        result_set: List[main_models.DescribeProcessListResponseBodyDataResultSet] = None,
        total_count: int = None,
    ):
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The cluster name.
        self.dbinstance_name = dbinstance_name
        # The result sets.
        self.result_set = result_set
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

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
                temp_model = main_models.DescribeProcessListResponseBodyDataResultSet()
                self.result_set.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeProcessListResponseBodyDataResultSet(DaraModel):
    def __init__(
        self,
        initial_address: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        query: str = None,
        query_duration_ms: int = None,
        query_start_time: str = None,
    ):
        # The address to which the query statement is sent.
        self.initial_address = initial_address
        # The query ID.
        self.initial_query_id = initial_query_id
        # The user who executes the query statement.
        self.initial_user = initial_user
        # The query statement that is running.
        self.query = query
        # The minimum query duration. Minimum value: **1000**. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # The beginning of the time range to query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.query_start_time = query_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.initial_address is not None:
            result['InitialAddress'] = self.initial_address

        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id

        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user

        if self.query is not None:
            result['Query'] = self.query

        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialAddress') is not None:
            self.initial_address = m.get('InitialAddress')

        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')

        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        return self

