# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribePackageDeductionsResponseBody(DaraModel):
    def __init__(
        self,
        deductions: List[main_models.DescribePackageDeductionsResponseBodyDeductions] = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_used_core_time: float = None,
        total_used_time: int = None,
        total_used_time_decimal: str = None,
    ):
        self.deductions = deductions
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_used_core_time = total_used_core_time
        self.total_used_time = total_used_time
        self.total_used_time_decimal = total_used_time_decimal

    def validate(self):
        if self.deductions:
            for v1 in self.deductions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Deductions'] = []
        if self.deductions is not None:
            for k1 in self.deductions:
                result['Deductions'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_used_core_time is not None:
            result['TotalUsedCoreTime'] = self.total_used_core_time

        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time

        if self.total_used_time_decimal is not None:
            result['TotalUsedTimeDecimal'] = self.total_used_time_decimal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deductions = []
        if m.get('Deductions') is not None:
            for k1 in m.get('Deductions'):
                temp_model = main_models.DescribePackageDeductionsResponseBodyDeductions()
                self.deductions.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalUsedCoreTime') is not None:
            self.total_used_core_time = m.get('TotalUsedCoreTime')

        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')

        if m.get('TotalUsedTimeDecimal') is not None:
            self.total_used_time_decimal = m.get('TotalUsedTimeDecimal')

        return self

class DescribePackageDeductionsResponseBodyDeductions(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_type: str = None,
        end_time: str = None,
        group_resource_type: str = None,
        instance_id: str = None,
        instance_state: str = None,
        instance_type: str = None,
        memory: int = None,
        os_type: str = None,
        region_id: str = None,
        resource_type: str = None,
        session_id: str = None,
        sta_time: str = None,
        used_core_time: float = None,
        used_time: int = None,
        used_time_decimal: str = None,
        used_time_with_scale: int = None,
    ):
        self.cpu = cpu
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_type = desktop_type
        self.end_time = end_time
        self.group_resource_type = group_resource_type
        self.instance_id = instance_id
        self.instance_state = instance_state
        self.instance_type = instance_type
        self.memory = memory
        self.os_type = os_type
        self.region_id = region_id
        self.resource_type = resource_type
        self.session_id = session_id
        self.sta_time = sta_time
        self.used_core_time = used_core_time
        self.used_time = used_time
        self.used_time_decimal = used_time_decimal
        self.used_time_with_scale = used_time_with_scale

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_resource_type is not None:
            result['GroupResourceType'] = self.group_resource_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_state is not None:
            result['InstanceState'] = self.instance_state

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.sta_time is not None:
            result['StaTime'] = self.sta_time

        if self.used_core_time is not None:
            result['UsedCoreTime'] = self.used_core_time

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.used_time_decimal is not None:
            result['UsedTimeDecimal'] = self.used_time_decimal

        if self.used_time_with_scale is not None:
            result['UsedTimeWithScale'] = self.used_time_with_scale

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupResourceType') is not None:
            self.group_resource_type = m.get('GroupResourceType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceState') is not None:
            self.instance_state = m.get('InstanceState')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StaTime') is not None:
            self.sta_time = m.get('StaTime')

        if m.get('UsedCoreTime') is not None:
            self.used_core_time = m.get('UsedCoreTime')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('UsedTimeDecimal') is not None:
            self.used_time_decimal = m.get('UsedTimeDecimal')

        if m.get('UsedTimeWithScale') is not None:
            self.used_time_with_scale = m.get('UsedTimeWithScale')

        return self

