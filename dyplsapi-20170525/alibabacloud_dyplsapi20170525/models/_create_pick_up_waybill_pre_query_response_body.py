# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CreatePickUpWaybillPreQueryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreatePickUpWaybillPreQueryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The result set.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The description of the status code.
        self.message = message
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreatePickUpWaybillPreQueryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreatePickUpWaybillPreQueryResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        cp_time_select_list: List[main_models.CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList] = None,
        error_code: str = None,
        error_msg: str = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The list of information about whether courier companies are available for placing orders.
        self.cp_time_select_list = cp_time_select_list
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The response content.
        self.message = message
        # Indicates whether the operation is successful.
        self.success = success

    def validate(self):
        if self.cp_time_select_list:
            for v1 in self.cp_time_select_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['CpTimeSelectList'] = []
        if self.cp_time_select_list is not None:
            for k1 in self.cp_time_select_list:
                result['CpTimeSelectList'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.cp_time_select_list = []
        if m.get('CpTimeSelectList') is not None:
            for k1 in m.get('CpTimeSelectList'):
                temp_model = main_models.CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList()
                self.cp_time_select_list.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList(DaraModel):
    def __init__(
        self,
        appoint_times: List[main_models.CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes] = None,
        pre_price: str = None,
        real_time: main_models.CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime = None,
    ):
        # The available time options for scheduled orders. If the courier company does not support scheduled orders, this field is empty.
        self.appoint_times = appoint_times
        # The estimated price, in CNY, rounded to two decimal places. This field has a value only when the estimated weight is specified in the request parameters.
        self.pre_price = pre_price
        # The available options for real-time orders.
        self.real_time = real_time

    def validate(self):
        if self.appoint_times:
            for v1 in self.appoint_times:
                 if v1:
                    v1.validate()
        if self.real_time:
            self.real_time.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppointTimes'] = []
        if self.appoint_times is not None:
            for k1 in self.appoint_times:
                result['AppointTimes'].append(k1.to_map() if k1 else None)

        if self.pre_price is not None:
            result['PrePrice'] = self.pre_price

        if self.real_time is not None:
            result['RealTime'] = self.real_time.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.appoint_times = []
        if m.get('AppointTimes') is not None:
            for k1 in m.get('AppointTimes'):
                temp_model = main_models.CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes()
                self.appoint_times.append(temp_model.from_map(k1))

        if m.get('PrePrice') is not None:
            self.pre_price = m.get('PrePrice')

        if m.get('RealTime') is not None:
            temp_model = main_models.CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime()
            self.real_time = temp_model.from_map(m.get('RealTime'))

        return self

class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime(DaraModel):
    def __init__(
        self,
        name: str = None,
        select_disable_tip: str = None,
        selectable: bool = None,
    ):
        # The service type name for real-time orders.
        self.name = name
        # The tip message displayed when the option is not selectable.
        self.select_disable_tip = select_disable_tip
        # Indicates whether a real-time order can still be placed after the real-time order placement time has passed.
        self.selectable = selectable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.select_disable_tip is not None:
            result['SelectDisableTip'] = self.select_disable_tip

        if self.selectable is not None:
            result['Selectable'] = self.selectable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SelectDisableTip') is not None:
            self.select_disable_tip = m.get('SelectDisableTip')

        if m.get('Selectable') is not None:
            self.selectable = m.get('Selectable')

        return self

class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes(DaraModel):
    def __init__(
        self,
        date: str = None,
        date_selectable: bool = None,
        time_list: List[main_models.CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList] = None,
    ):
        # The date string in YYYY-MM-DD format.
        self.date = date
        # Indicates whether the date is selectable.
        self.date_selectable = date_selectable
        # The list of available time slots for the day.
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for v1 in self.time_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.date_selectable is not None:
            result['DateSelectable'] = self.date_selectable

        result['TimeList'] = []
        if self.time_list is not None:
            for k1 in self.time_list:
                result['TimeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('DateSelectable') is not None:
            self.date_selectable = m.get('DateSelectable')

        self.time_list = []
        if m.get('TimeList') is not None:
            for k1 in m.get('TimeList'):
                temp_model = main_models.CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList()
                self.time_list.append(temp_model.from_map(k1))

        return self

class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        select_disable_tip: str = None,
        selectable: bool = None,
        start_time: str = None,
    ):
        # The end time of the time slot, in HH:mm:ss format.
        self.end_time = end_time
        # The tip message displayed when the option is not selectable.
        self.select_disable_tip = select_disable_tip
        # Indicates whether the scheduled time slot is selectable.
        self.selectable = selectable
        # The start time of the time slot, in HH:mm:ss format.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.select_disable_tip is not None:
            result['SelectDisableTip'] = self.select_disable_tip

        if self.selectable is not None:
            result['Selectable'] = self.selectable

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('SelectDisableTip') is not None:
            self.select_disable_tip = m.get('SelectDisableTip')

        if m.get('Selectable') is not None:
            self.selectable = m.get('Selectable')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

