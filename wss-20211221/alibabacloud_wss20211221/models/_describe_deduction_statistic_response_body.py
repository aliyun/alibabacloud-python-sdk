# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeDeductionStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDeductionStatisticResponseBodyData = None,
        request_id: str = None,
    ):
        # The deduction data.
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
            temp_model = main_models.DescribeDeductionStatisticResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDeductionStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        available_core_packages: List[main_models.DescribeDeductionStatisticResponseBodyDataAvailableCorePackages] = None,
        deductions: List[main_models.DescribeDeductionStatisticResponseBodyDataDeductions] = None,
        usages: List[main_models.DescribeDeductionStatisticResponseBodyDataUsages] = None,
    ):
        # **The available core-hour packages.**
        self.available_core_packages = available_core_packages
        # The deduction details.
        self.deductions = deductions
        # **The usage details.**
        self.usages = usages

    def validate(self):
        if self.available_core_packages:
            for v1 in self.available_core_packages:
                 if v1:
                    v1.validate()
        if self.deductions:
            for v1 in self.deductions:
                 if v1:
                    v1.validate()
        if self.usages:
            for v1 in self.usages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableCorePackages'] = []
        if self.available_core_packages is not None:
            for k1 in self.available_core_packages:
                result['AvailableCorePackages'].append(k1.to_map() if k1 else None)

        result['Deductions'] = []
        if self.deductions is not None:
            for k1 in self.deductions:
                result['Deductions'].append(k1.to_map() if k1 else None)

        result['Usages'] = []
        if self.usages is not None:
            for k1 in self.usages:
                result['Usages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_core_packages = []
        if m.get('AvailableCorePackages') is not None:
            for k1 in m.get('AvailableCorePackages'):
                temp_model = main_models.DescribeDeductionStatisticResponseBodyDataAvailableCorePackages()
                self.available_core_packages.append(temp_model.from_map(k1))

        self.deductions = []
        if m.get('Deductions') is not None:
            for k1 in m.get('Deductions'):
                temp_model = main_models.DescribeDeductionStatisticResponseBodyDataDeductions()
                self.deductions.append(temp_model.from_map(k1))

        self.usages = []
        if m.get('Usages') is not None:
            for k1 in m.get('Usages'):
                temp_model = main_models.DescribeDeductionStatisticResponseBodyDataUsages()
                self.usages.append(temp_model.from_map(k1))

        return self

class DescribeDeductionStatisticResponseBodyDataUsages(DaraModel):
    def __init__(
        self,
        consume_second: int = None,
        period: str = None,
        resource_type: str = None,
    ):
        # **The consumption duration in seconds.**
        self.consume_second = consume_second
        # **The time period.**
        self.period = period
        # **The resource type.**
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_second is not None:
            result['ConsumeSecond'] = self.consume_second

        if self.period is not None:
            result['Period'] = self.period

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeSecond') is not None:
            self.consume_second = m.get('ConsumeSecond')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class DescribeDeductionStatisticResponseBodyDataDeductions(DaraModel):
    def __init__(
        self,
        consume_second: int = None,
        deduction_date: str = None,
        resource_type: str = None,
    ):
        # The consumption duration in seconds.
        self.consume_second = consume_second
        # The deduction date.
        self.deduction_date = deduction_date
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_second is not None:
            result['ConsumeSecond'] = self.consume_second

        if self.deduction_date is not None:
            result['DeductionDate'] = self.deduction_date

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeSecond') is not None:
            self.consume_second = m.get('ConsumeSecond')

        if m.get('DeductionDate') is not None:
            self.deduction_date = m.get('DeductionDate')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class DescribeDeductionStatisticResponseBodyDataAvailableCorePackages(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        create_time: str = None,
        end_time: str = None,
        expired_time: str = None,
        group_id: str = None,
        group_resource_type: str = None,
        no_lx: bool = None,
        no_lx_source: str = None,
        resource_id: str = None,
        resource_type: str = None,
        start_time: str = None,
        status: str = None,
        total_time: int = None,
        used_time: int = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The creation time.
        self.create_time = create_time
        # The end time.
        self.end_time = end_time
        # The expiration time.
        self.expired_time = expired_time
        # The group ID.
        self.group_id = group_id
        # The group resource type.
        self.group_resource_type = group_resource_type
        # Indicates whether the resource is a No-Lx resource.
        self.no_lx = no_lx
        # The source of the No-Lx resource.
        self.no_lx_source = no_lx_source
        # The resource ID.
        self.resource_id = resource_id
        # The group resource type.
        self.resource_type = resource_type
        # The start time.
        self.start_time = start_time
        # The status.
        self.status = status
        # The total duration.
        self.total_time = total_time
        # The used duration.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_resource_type is not None:
            result['GroupResourceType'] = self.group_resource_type

        if self.no_lx is not None:
            result['NoLx'] = self.no_lx

        if self.no_lx_source is not None:
            result['NoLxSource'] = self.no_lx_source

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupResourceType') is not None:
            self.group_resource_type = m.get('GroupResourceType')

        if m.get('NoLx') is not None:
            self.no_lx = m.get('NoLx')

        if m.get('NoLxSource') is not None:
            self.no_lx_source = m.get('NoLxSource')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

