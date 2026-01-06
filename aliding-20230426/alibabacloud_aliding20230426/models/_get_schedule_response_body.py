# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetScheduleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        schedule_information: List[main_models.GetScheduleResponseBodyScheduleInformation] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.schedule_information = schedule_information
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.schedule_information:
            for v1 in self.schedule_information:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['scheduleInformation'] = []
        if self.schedule_information is not None:
            for k1 in self.schedule_information:
                result['scheduleInformation'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.schedule_information = []
        if m.get('scheduleInformation') is not None:
            for k1 in m.get('scheduleInformation'):
                temp_model = main_models.GetScheduleResponseBodyScheduleInformation()
                self.schedule_information.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetScheduleResponseBodyScheduleInformation(DaraModel):
    def __init__(
        self,
        error: str = None,
        schedule_items: List[main_models.GetScheduleResponseBodyScheduleInformationScheduleItems] = None,
        user_id: str = None,
    ):
        self.error = error
        self.schedule_items = schedule_items
        self.user_id = user_id

    def validate(self):
        if self.schedule_items:
            for v1 in self.schedule_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        result['ScheduleItems'] = []
        if self.schedule_items is not None:
            for k1 in self.schedule_items:
                result['ScheduleItems'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        self.schedule_items = []
        if m.get('ScheduleItems') is not None:
            for k1 in m.get('ScheduleItems'):
                temp_model = main_models.GetScheduleResponseBodyScheduleInformationScheduleItems()
                self.schedule_items.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetScheduleResponseBodyScheduleInformationScheduleItems(DaraModel):
    def __init__(
        self,
        end: main_models.GetScheduleResponseBodyScheduleInformationScheduleItemsEnd = None,
        start: main_models.GetScheduleResponseBodyScheduleInformationScheduleItemsStart = None,
        status: str = None,
    ):
        self.end = end
        self.start = start
        self.status = status

    def validate(self):
        if self.end:
            self.end.validate()
        if self.start:
            self.start.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end.to_map()

        if self.start is not None:
            result['Start'] = self.start.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            temp_model = main_models.GetScheduleResponseBodyScheduleInformationScheduleItemsEnd()
            self.end = temp_model.from_map(m.get('End'))

        if m.get('Start') is not None:
            temp_model = main_models.GetScheduleResponseBodyScheduleInformationScheduleItemsStart()
            self.start = temp_model.from_map(m.get('Start'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetScheduleResponseBodyScheduleInformationScheduleItemsStart(DaraModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

class GetScheduleResponseBodyScheduleInformationScheduleItemsEnd(DaraModel):
    def __init__(
        self,
        date: str = None,
        date_time: str = None,
        time_zone: str = None,
    ):
        self.date = date
        self.date_time = date_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

