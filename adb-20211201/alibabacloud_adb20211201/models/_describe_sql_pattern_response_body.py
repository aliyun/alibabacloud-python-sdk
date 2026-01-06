# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlPatternResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeSqlPatternResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried SQL pattern.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSqlPatternResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSqlPatternResponseBodyItems(DaraModel):
    def __init__(
        self,
        access_ip: str = None,
        avg_cpu_time: str = None,
        avg_peak_memory: str = None,
        avg_scan_size: str = None,
        avg_stage_count: str = None,
        avg_task_count: str = None,
        instance_name: str = None,
        max_cpu_time: str = None,
        max_peak_memory: str = None,
        max_scan_size: str = None,
        max_stage_count: str = None,
        max_task_count: str = None,
        pattern: str = None,
        query_count: str = None,
        report_date: str = None,
        user: str = None,
    ):
        # The IP address of the client.
        # 
        # >  This parameter is returned only when **Type** is set to **accessip**.
        self.access_ip = access_ip
        # The average execution duration of the SQL pattern within the query time range. Unit: milliseconds.
        self.avg_cpu_time = avg_cpu_time
        # The average peak memory usage of the SQL pattern within the query time range. Unit: KB.
        self.avg_peak_memory = avg_peak_memory
        # The average amount of data scanned based on the SQL pattern within the query time range. Unit: KB.
        self.avg_scan_size = avg_scan_size
        # The average number of scanned rows.
        self.avg_stage_count = avg_stage_count
        # The average number of tasks.
        self.avg_task_count = avg_task_count
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        self.instance_name = instance_name
        # The maximum execution duration of the SQL pattern within the query time range. Unit: milliseconds.
        self.max_cpu_time = max_cpu_time
        # The maximum peak memory usage of the SQL pattern within the query time range. Unit: KB.
        self.max_peak_memory = max_peak_memory
        # The maximum amount of data scanned based on the SQL pattern within the query time range. Unit: KB.
        self.max_scan_size = max_scan_size
        # The maximum number of stages.
        self.max_stage_count = max_stage_count
        # The maximum number of tasks.
        self.max_task_count = max_task_count
        # The SQL pattern.
        self.pattern = pattern
        # The number of queries performed in association with the SQL pattern within the query time range.
        self.query_count = query_count
        # The start date of the query.
        self.report_date = report_date
        # The username.
        # 
        # >  This parameter is returned only when **Type** is left empty or set to **user**.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ip is not None:
            result['AccessIP'] = self.access_ip

        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time

        if self.avg_peak_memory is not None:
            result['AvgPeakMemory'] = self.avg_peak_memory

        if self.avg_scan_size is not None:
            result['AvgScanSize'] = self.avg_scan_size

        if self.avg_stage_count is not None:
            result['AvgStageCount'] = self.avg_stage_count

        if self.avg_task_count is not None:
            result['AvgTaskCount'] = self.avg_task_count

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time

        if self.max_peak_memory is not None:
            result['MaxPeakMemory'] = self.max_peak_memory

        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size

        if self.max_stage_count is not None:
            result['MaxStageCount'] = self.max_stage_count

        if self.max_task_count is not None:
            result['MaxTaskCount'] = self.max_task_count

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.query_count is not None:
            result['QueryCount'] = self.query_count

        if self.report_date is not None:
            result['ReportDate'] = self.report_date

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIP') is not None:
            self.access_ip = m.get('AccessIP')

        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')

        if m.get('AvgPeakMemory') is not None:
            self.avg_peak_memory = m.get('AvgPeakMemory')

        if m.get('AvgScanSize') is not None:
            self.avg_scan_size = m.get('AvgScanSize')

        if m.get('AvgStageCount') is not None:
            self.avg_stage_count = m.get('AvgStageCount')

        if m.get('AvgTaskCount') is not None:
            self.avg_task_count = m.get('AvgTaskCount')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')

        if m.get('MaxPeakMemory') is not None:
            self.max_peak_memory = m.get('MaxPeakMemory')

        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')

        if m.get('MaxStageCount') is not None:
            self.max_stage_count = m.get('MaxStageCount')

        if m.get('MaxTaskCount') is not None:
            self.max_task_count = m.get('MaxTaskCount')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')

        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

