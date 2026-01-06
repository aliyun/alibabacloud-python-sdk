# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeComputeResourceUsageResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeComputeResourceUsageResponseBodyData = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The queried resource usage.
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeComputeResourceUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeComputeResourceUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        acu_info: List[main_models.DescribeComputeResourceUsageResponseBodyDataAcuInfo] = None,
        dbcluster_id: str = None,
        end_time: str = None,
        resource_group_name: str = None,
        resource_group_type: str = None,
        start_time: str = None,
    ):
        # The AnalyticDB compute unit (ACU) usage of the cluster.
        self.acu_info = acu_info
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The end time of the query. The time follows the ISO 8601 standard in the *yyyy-MM-ddTHH:mm:ssZ* format. The time is displayed in UTC.
        self.end_time = end_time
        # The name of the resource group.
        self.resource_group_name = resource_group_name
        # The type of the resource group.
        self.resource_group_type = resource_group_type
        # The start time of the query. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.acu_info:
            for v1 in self.acu_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AcuInfo'] = []
        if self.acu_info is not None:
            for k1 in self.acu_info:
                result['AcuInfo'].append(k1.to_map() if k1 else None)

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.resource_group_type is not None:
            result['ResourceGroupType'] = self.resource_group_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acu_info = []
        if m.get('AcuInfo') is not None:
            for k1 in m.get('AcuInfo'):
                temp_model = main_models.DescribeComputeResourceUsageResponseBodyDataAcuInfo()
                self.acu_info.append(temp_model.from_map(k1))

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('ResourceGroupType') is not None:
            self.resource_group_type = m.get('ResourceGroupType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeComputeResourceUsageResponseBodyDataAcuInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        # The resource usage metric. Valid values:
        # 
        # *   `TotalAcuNumber`: the total number of ACUs.
        # *   `ReservedAcuNumber`: the number of ACUs for the reserved resources.
        # *   `ReservedAcuUsageNumber`: the number of ACUs for the reserved resources that are used.
        self.name = name
        # The values of the metric at specific points in time.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

