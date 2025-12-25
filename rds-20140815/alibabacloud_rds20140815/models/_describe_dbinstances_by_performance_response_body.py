# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesByPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstancesByPerformanceResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The details about the instance.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstancesByPerformanceResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstancesByPerformanceResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance_performance: List[main_models.DescribeDBInstancesByPerformanceResponseBodyItemsDBInstancePerformance] = None,
    ):
        self.dbinstance_performance = dbinstance_performance

    def validate(self):
        if self.dbinstance_performance:
            for v1 in self.dbinstance_performance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstancePerformance'] = []
        if self.dbinstance_performance is not None:
            for k1 in self.dbinstance_performance:
                result['DBInstancePerformance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_performance = []
        if m.get('DBInstancePerformance') is not None:
            for k1 in m.get('DBInstancePerformance'):
                temp_model = main_models.DescribeDBInstancesByPerformanceResponseBodyItemsDBInstancePerformance()
                self.dbinstance_performance.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesByPerformanceResponseBodyItemsDBInstancePerformance(DaraModel):
    def __init__(
        self,
        cpuusage: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        disk_usage: str = None,
        iopsusage: str = None,
        session_usage: str = None,
    ):
        # The CPU utilization of the instance in percentage.
        self.cpuusage = cpuusage
        # The name of the instance.
        self.dbinstance_description = dbinstance_description
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The disk usage of the instance in percentage.
        self.disk_usage = disk_usage
        # The IOPS usage of the instance in percentage.
        self.iopsusage = iopsusage
        # The number of sessions.
        self.session_usage = session_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpuusage is not None:
            result['CPUUsage'] = self.cpuusage

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage

        if self.iopsusage is not None:
            result['IOPSUsage'] = self.iopsusage

        if self.session_usage is not None:
            result['SessionUsage'] = self.session_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPUUsage') is not None:
            self.cpuusage = m.get('CPUUsage')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')

        if m.get('IOPSUsage') is not None:
            self.iopsusage = m.get('IOPSUsage')

        if m.get('SessionUsage') is not None:
            self.session_usage = m.get('SessionUsage')

        return self

