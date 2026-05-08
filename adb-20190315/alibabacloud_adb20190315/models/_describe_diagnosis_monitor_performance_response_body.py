# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosisMonitorPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        performances: List[main_models.DescribeDiagnosisMonitorPerformanceResponseBodyPerformances] = None,
        performances_threshold: int = None,
        performances_truncated: bool = None,
        request_id: str = None,
    ):
        # The monitoring information about queries displayed in Gantt charts.
        self.performances = performances
        # The threshold for the number of queries displayed in a Gantt chart. Default value: 10000.
        # 
        # >  Up to 10,000 queries can be displayed in a Gantt chart even if more queries exist.
        self.performances_threshold = performances_threshold
        # Indicates whether all queries are returned. Valid values:
        # 
        # *   true
        # *   false
        self.performances_truncated = performances_truncated
        # The request ID.
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
        peak_memory: int = None,
        process_id: str = None,
        rc_host: str = None,
        scan_rows: int = None,
        scan_size: int = None,
        start_time: int = None,
        status: str = None,
        user_name: str = None,
    ):
        # The total execution duration. Unit: milliseconds.
        # 
        # >  This value is the cumulative value of the `QueuedTime`, `TotalPlanningTime`, and `ExecutionTime` parameters.
        self.cost = cost
        # The peak memory of the query. Unit: bytes.
        self.peak_memory = peak_memory
        # The query ID.
        self.process_id = process_id
        # The IP address of the AnalyticDB for MySQL frontend node on which the SQL statement is executed.
        self.rc_host = rc_host
        # The number of rows scanned.
        self.scan_rows = scan_rows
        # The amount of scanned data. Unit: bytes.
        self.scan_size = scan_size
        # The execution start time of the SQL statement. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The status of the SQL statement. Valid values:
        # 
        # *   **running**
        # *   **finished**
        # *   **failed**
        self.status = status
        # The database account that is used to submit the query.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['Cost'] = self.cost

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.rc_host is not None:
            result['RcHost'] = self.rc_host

        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows

        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('RcHost') is not None:
            self.rc_host = m.get('RcHost')

        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')

        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

