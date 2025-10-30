# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDBInstancePerformanceResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        engine: str = None,
        performance_keys: List[str] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The end time of the query.
        self.end_time = end_time
        # The database engine of the instance.
        self.engine = engine
        # The queried performance metrics.
        self.performance_keys = performance_keys
        # The request ID.
        self.request_id = request_id
        # The start time of the query.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('PerformanceKeys') is not None:
            self.performance_keys = m.get('PerformanceKeys')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

