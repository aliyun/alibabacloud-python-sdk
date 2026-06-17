# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSystemEventCountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        system_event_counts: main_models.DescribeSystemEventCountResponseBodySystemEventCounts = None,
    ):
        # The status code.
        # >A value of 200 indicates success.
        self.code = code
        # The returned message.
        # 
        # If the request is successful, a success message is returned. If the request fails, the failure reason is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # - true: The operation is successful.
        # 
        # - false: The operation failed.
        self.success = success
        self.system_event_counts = system_event_counts

    def validate(self):
        if self.system_event_counts:
            self.system_event_counts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.system_event_counts is not None:
            result['SystemEventCounts'] = self.system_event_counts.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('SystemEventCounts') is not None:
            temp_model = main_models.DescribeSystemEventCountResponseBodySystemEventCounts()
            self.system_event_counts = temp_model.from_map(m.get('SystemEventCounts'))

        return self

class DescribeSystemEventCountResponseBodySystemEventCounts(DaraModel):
    def __init__(
        self,
        system_event_count: List[main_models.DescribeSystemEventCountResponseBodySystemEventCountsSystemEventCount] = None,
    ):
        self.system_event_count = system_event_count

    def validate(self):
        if self.system_event_count:
            for v1 in self.system_event_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SystemEventCount'] = []
        if self.system_event_count is not None:
            for k1 in self.system_event_count:
                result['SystemEventCount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_event_count = []
        if m.get('SystemEventCount') is not None:
            for k1 in m.get('SystemEventCount'):
                temp_model = main_models.DescribeSystemEventCountResponseBodySystemEventCountsSystemEventCount()
                self.system_event_count.append(temp_model.from_map(k1))

        return self

class DescribeSystemEventCountResponseBodySystemEventCountsSystemEventCount(DaraModel):
    def __init__(
        self,
        content: str = None,
        group_id: str = None,
        instance_name: str = None,
        level: str = None,
        name: str = None,
        num: int = None,
        product: str = None,
        region_id: str = None,
        resource_id: str = None,
        status: str = None,
        time: int = None,
    ):
        self.content = content
        self.group_id = group_id
        self.instance_name = instance_name
        self.level = level
        self.name = name
        self.num = num
        self.product = product
        self.region_id = region_id
        self.resource_id = resource_id
        self.status = status
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.num is not None:
            result['Num'] = self.num

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

