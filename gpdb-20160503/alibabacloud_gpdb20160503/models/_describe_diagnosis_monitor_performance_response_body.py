# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosisMonitorPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        performances: List[main_models.DescribeDiagnosisMonitorPerformanceResponseBodyPerformances] = None,
        performances_threshold: int = None,
        performances_truncated: bool = None,
        request_id: str = None,
    ):
        # Details of query execution.
        self.performances = performances
        # The threshold for the number of queries.
        self.performances_threshold = performances_threshold
        # Indicates whether the queries are truncated when the number of queries exceeds the threshold. Valid values:
        # 
        # *   **true**: The queries are truncated.
        # *   **false**: The queries are not truncated.
        self.performances_truncated = performances_truncated
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.performances:
            for v1 in self.performances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Performances'] = []
        if self.performances is not None:
            for k1 in self.performances:
                result['Performances'].append(k1.to_map() if k1 else None)

        if self.performances_threshold is not None:
            result['PerformancesThreshold'] = self.performances_threshold

        if self.performances_truncated is not None:
            result['PerformancesTruncated'] = self.performances_truncated

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performances = []
        if m.get('Performances') is not None:
            for k1 in m.get('Performances'):
                temp_model = main_models.DescribeDiagnosisMonitorPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k1))

        if m.get('PerformancesThreshold') is not None:
            self.performances_threshold = m.get('PerformancesThreshold')

        if m.get('PerformancesTruncated') is not None:
            self.performances_truncated = m.get('PerformancesTruncated')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDiagnosisMonitorPerformanceResponseBodyPerformances(DaraModel):
    def __init__(
        self,
        cost: int = None,
        database: str = None,
        query_id: str = None,
        start_time: int = None,
        status: str = None,
        user: str = None,
    ):
        # The execution duration of the query. Unit: milliseconds.
        self.cost = cost
        # The name of the database.
        self.database = database
        # The ID of the query. It is a unique identifier of the query.
        self.query_id = query_id
        # The start time of the query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The execution state of the query. Valid values:
        # 
        # *   **running**: The query is being executed.
        # *   **finished**: The query is complete.
        self.status = status
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['Cost'] = self.cost

        if self.database is not None:
            result['Database'] = self.database

        if self.query_id is not None:
            result['QueryID'] = self.query_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('QueryID') is not None:
            self.query_id = m.get('QueryID')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

