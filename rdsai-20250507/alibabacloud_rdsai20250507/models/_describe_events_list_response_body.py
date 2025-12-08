# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeEventsListResponseBody(DaraModel):
    def __init__(
        self,
        event_code_counts: str = None,
        events: List[main_models.DescribeEventsListResponseBodyEvents] = None,
        page_count: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_pages: int = None,
    ):
        self.event_code_counts = event_code_counts
        self.events = events
        self.page_count = page_count
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_pages = total_pages

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code_counts is not None:
            result['EventCodeCounts'] = self.event_code_counts

        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCodeCounts') is not None:
            self.event_code_counts = m.get('EventCodeCounts')

        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.DescribeEventsListResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeEventsListResponseBodyEvents(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_status: str = None,
        event_time_list: List[str] = None,
        instance_description: str = None,
        instance_id: str = None,
        recovery_time: str = None,
    ):
        self.event_code = event_code
        self.event_status = event_status
        self.event_time_list = event_time_list
        self.instance_description = instance_description
        self.instance_id = instance_id
        self.recovery_time = recovery_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.event_time_list is not None:
            result['EventTimeList'] = self.event_time_list

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('EventTimeList') is not None:
            self.event_time_list = m.get('EventTimeList')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')

        return self

