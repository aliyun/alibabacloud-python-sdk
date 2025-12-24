# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class ListAlarmEventResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListAlarmEventResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListAlarmEventResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAlarmEventResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListAlarmEventResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListAlarmEventResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListAlarmEventResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        alarm_channel: str = None,
        alarm_contacts: str = None,
        alarm_message: str = None,
        alarm_status: str = None,
        alarm_type: str = None,
        app_name: str = None,
        job_name: str = None,
        time: str = None,
    ):
        self.alarm_channel = alarm_channel
        self.alarm_contacts = alarm_contacts
        self.alarm_message = alarm_message
        self.alarm_status = alarm_status
        self.alarm_type = alarm_type
        self.app_name = app_name
        self.job_name = job_name
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_channel is not None:
            result['AlarmChannel'] = self.alarm_channel

        if self.alarm_contacts is not None:
            result['AlarmContacts'] = self.alarm_contacts

        if self.alarm_message is not None:
            result['AlarmMessage'] = self.alarm_message

        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status

        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmChannel') is not None:
            self.alarm_channel = m.get('AlarmChannel')

        if m.get('AlarmContacts') is not None:
            self.alarm_contacts = m.get('AlarmContacts')

        if m.get('AlarmMessage') is not None:
            self.alarm_message = m.get('AlarmMessage')

        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')

        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

