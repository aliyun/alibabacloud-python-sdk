# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeResubmitConfigResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        request_id: str = None,
        rules: List[main_models.DescribeResubmitConfigResponseBodyRules] = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The job resubmission rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeResubmitConfigResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeResubmitConfigResponseBodyRules(DaraModel):
    def __init__(
        self,
        exceed_memory_exception: bool = None,
        group_name: str = None,
        peak_memory: str = None,
        query_time: str = None,
        target_group_name: str = None,
    ):
        # Indicates whether out-of-memory (OOM) check is configured.
        self.exceed_memory_exception = exceed_memory_exception
        # The name of the source resource group.
        self.group_name = group_name
        # The peak memory usage.
        self.peak_memory = peak_memory
        # The duration of the SQL statement. Unit: milliseconds.
        self.query_time = query_time
        # The name of the destination resource group.
        self.target_group_name = target_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exceed_memory_exception is not None:
            result['ExceedMemoryException'] = self.exceed_memory_exception

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.query_time is not None:
            result['QueryTime'] = self.query_time

        if self.target_group_name is not None:
            result['TargetGroupName'] = self.target_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceedMemoryException') is not None:
            self.exceed_memory_exception = m.get('ExceedMemoryException')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('TargetGroupName') is not None:
            self.target_group_name = m.get('TargetGroupName')

        return self

