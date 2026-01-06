# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLPatternsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        page_number: int = None,
        page_size: int = None,
        pattern_details: List[main_models.DescribeSQLPatternsResponseBodyPatternDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The queried SQL patterns.
        self.pattern_details = pattern_details
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.pattern_details:
            for v1 in self.pattern_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PatternDetails'] = []
        if self.pattern_details is not None:
            for k1 in self.pattern_details:
                result['PatternDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.pattern_details = []
        if m.get('PatternDetails') is not None:
            for k1 in m.get('PatternDetails'):
                temp_model = main_models.DescribeSQLPatternsResponseBodyPatternDetails()
                self.pattern_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSQLPatternsResponseBodyPatternDetails(DaraModel):
    def __init__(
        self,
        access_ip: str = None,
        average_execution_time: float = None,
        average_operator_cost: float = None,
        average_peak_memory: float = None,
        average_query_time: float = None,
        average_scan_cost: float = None,
        average_scan_size: float = None,
        blockable: bool = None,
        failed_count: int = None,
        max_execution_time: int = None,
        max_operator_cost: float = None,
        max_peak_memory: int = None,
        max_query_time: int = None,
        max_scan_cost: float = None,
        max_scan_size: int = None,
        operator_cost_percentage: float = None,
        operator_cost_sum: float = None,
        pattern_creation_time: str = None,
        pattern_id: str = None,
        peak_memory_percentage: float = None,
        peak_memory_sum: float = None,
        query_count: int = None,
        query_time_percentage: float = None,
        query_time_sum: float = None,
        sqlpattern: str = None,
        scan_cost_percentage: float = None,
        scan_cost_sum: float = None,
        scan_size_percentage: float = None,
        scan_size_sum: float = None,
        tables: str = None,
        user: str = None,
    ):
        # The IP address of the SQL client that commits the SQL pattern.
        self.access_ip = access_ip
        # The average execution duration of the SQL pattern within the query time range. Unit: milliseconds.
        self.average_execution_time = average_execution_time
        self.average_operator_cost = average_operator_cost
        # The average peak memory usage of the SQL pattern within the query time range. Unit: bytes.
        self.average_peak_memory = average_peak_memory
        # The average total amount of time consumed by the SQL pattern within the query time range. Unit: milliseconds.
        self.average_query_time = average_query_time
        self.average_scan_cost = average_scan_cost
        # The average amount of data scanned based on the SQL pattern within the query time range. Unit: bytes.
        self.average_scan_size = average_scan_size
        # Indicates whether the execution of the SQL pattern can be intercepted. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  Only SELECT and INSERT statements can be intercepted.
        self.blockable = blockable
        # The number of failed queries executed in association with the SQL pattern within the query time range.
        self.failed_count = failed_count
        # The maximum execution duration of the SQL pattern within the query time range. Unit: milliseconds.
        self.max_execution_time = max_execution_time
        self.max_operator_cost = max_operator_cost
        # The maximum peak memory usage of the SQL pattern within the query time range. Unit: bytes.
        self.max_peak_memory = max_peak_memory
        # The maximum total amount of time consumed by the SQL pattern within the query time range. Unit: milliseconds.
        self.max_query_time = max_query_time
        self.max_scan_cost = max_scan_cost
        # The maximum amount of data scanned based on the SQL pattern within the query time range. Unit: bytes.
        self.max_scan_size = max_scan_size
        self.operator_cost_percentage = operator_cost_percentage
        self.operator_cost_sum = operator_cost_sum
        # The earliest commit time of the SQL pattern within the query time range.
        self.pattern_creation_time = pattern_creation_time
        # The ID of the SQL pattern.
        self.pattern_id = pattern_id
        self.peak_memory_percentage = peak_memory_percentage
        self.peak_memory_sum = peak_memory_sum
        # The number of queries executed in association with the SQL pattern within the query time range.
        self.query_count = query_count
        self.query_time_percentage = query_time_percentage
        self.query_time_sum = query_time_sum
        # The statement of the SQL pattern.
        self.sqlpattern = sqlpattern
        self.scan_cost_percentage = scan_cost_percentage
        self.scan_cost_sum = scan_cost_sum
        self.scan_size_percentage = scan_size_percentage
        self.scan_size_sum = scan_size_sum
        # The tables scanned based on the SQL pattern.
        self.tables = tables
        # The name of the database account that is used to commit the SQL pattern.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ip is not None:
            result['AccessIp'] = self.access_ip

        if self.average_execution_time is not None:
            result['AverageExecutionTime'] = self.average_execution_time

        if self.average_operator_cost is not None:
            result['AverageOperatorCost'] = self.average_operator_cost

        if self.average_peak_memory is not None:
            result['AveragePeakMemory'] = self.average_peak_memory

        if self.average_query_time is not None:
            result['AverageQueryTime'] = self.average_query_time

        if self.average_scan_cost is not None:
            result['AverageScanCost'] = self.average_scan_cost

        if self.average_scan_size is not None:
            result['AverageScanSize'] = self.average_scan_size

        if self.blockable is not None:
            result['Blockable'] = self.blockable

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.max_execution_time is not None:
            result['MaxExecutionTime'] = self.max_execution_time

        if self.max_operator_cost is not None:
            result['MaxOperatorCost'] = self.max_operator_cost

        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory

        if self.max_query_time is not None:
            result['MaxQueryTime'] = self.max_query_time

        if self.max_scan_cost is not None:
            result['MaxScanCost'] = self.max_scan_cost

        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size

        if self.operator_cost_percentage is not None:
            result['OperatorCostPercentage'] = self.operator_cost_percentage

        if self.operator_cost_sum is not None:
            result['OperatorCostSum'] = self.operator_cost_sum

        if self.pattern_creation_time is not None:
            result['PatternCreationTime'] = self.pattern_creation_time

        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id

        if self.peak_memory_percentage is not None:
            result['PeakMemoryPercentage'] = self.peak_memory_percentage

        if self.peak_memory_sum is not None:
            result['PeakMemorySum'] = self.peak_memory_sum

        if self.query_count is not None:
            result['QueryCount'] = self.query_count

        if self.query_time_percentage is not None:
            result['QueryTimePercentage'] = self.query_time_percentage

        if self.query_time_sum is not None:
            result['QueryTimeSum'] = self.query_time_sum

        if self.sqlpattern is not None:
            result['SQLPattern'] = self.sqlpattern

        if self.scan_cost_percentage is not None:
            result['ScanCostPercentage'] = self.scan_cost_percentage

        if self.scan_cost_sum is not None:
            result['ScanCostSum'] = self.scan_cost_sum

        if self.scan_size_percentage is not None:
            result['ScanSizePercentage'] = self.scan_size_percentage

        if self.scan_size_sum is not None:
            result['ScanSizeSum'] = self.scan_size_sum

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')

        if m.get('AverageExecutionTime') is not None:
            self.average_execution_time = m.get('AverageExecutionTime')

        if m.get('AverageOperatorCost') is not None:
            self.average_operator_cost = m.get('AverageOperatorCost')

        if m.get('AveragePeakMemory') is not None:
            self.average_peak_memory = m.get('AveragePeakMemory')

        if m.get('AverageQueryTime') is not None:
            self.average_query_time = m.get('AverageQueryTime')

        if m.get('AverageScanCost') is not None:
            self.average_scan_cost = m.get('AverageScanCost')

        if m.get('AverageScanSize') is not None:
            self.average_scan_size = m.get('AverageScanSize')

        if m.get('Blockable') is not None:
            self.blockable = m.get('Blockable')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('MaxExecutionTime') is not None:
            self.max_execution_time = m.get('MaxExecutionTime')

        if m.get('MaxOperatorCost') is not None:
            self.max_operator_cost = m.get('MaxOperatorCost')

        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')

        if m.get('MaxQueryTime') is not None:
            self.max_query_time = m.get('MaxQueryTime')

        if m.get('MaxScanCost') is not None:
            self.max_scan_cost = m.get('MaxScanCost')

        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')

        if m.get('OperatorCostPercentage') is not None:
            self.operator_cost_percentage = m.get('OperatorCostPercentage')

        if m.get('OperatorCostSum') is not None:
            self.operator_cost_sum = m.get('OperatorCostSum')

        if m.get('PatternCreationTime') is not None:
            self.pattern_creation_time = m.get('PatternCreationTime')

        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')

        if m.get('PeakMemoryPercentage') is not None:
            self.peak_memory_percentage = m.get('PeakMemoryPercentage')

        if m.get('PeakMemorySum') is not None:
            self.peak_memory_sum = m.get('PeakMemorySum')

        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')

        if m.get('QueryTimePercentage') is not None:
            self.query_time_percentage = m.get('QueryTimePercentage')

        if m.get('QueryTimeSum') is not None:
            self.query_time_sum = m.get('QueryTimeSum')

        if m.get('SQLPattern') is not None:
            self.sqlpattern = m.get('SQLPattern')

        if m.get('ScanCostPercentage') is not None:
            self.scan_cost_percentage = m.get('ScanCostPercentage')

        if m.get('ScanCostSum') is not None:
            self.scan_cost_sum = m.get('ScanCostSum')

        if m.get('ScanSizePercentage') is not None:
            self.scan_size_percentage = m.get('ScanSizePercentage')

        if m.get('ScanSizeSum') is not None:
            self.scan_size_sum = m.get('ScanSizeSum')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

