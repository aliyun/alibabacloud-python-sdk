# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ListTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListTaskDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
            temp_model = main_models.ListTaskDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTaskDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        record: List[main_models.ListTaskDetailResponseBodyDataRecord] = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.record = record
        self.total = total

    def validate(self):
        if self.record:
            for v1 in self.record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Record'] = []
        if self.record is not None:
            for k1 in self.record:
                result['Record'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.record = []
        if m.get('Record') is not None:
            for k1 in m.get('Record'):
                temp_model = main_models.ListTaskDetailResponseBodyDataRecord()
                self.record.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListTaskDetailResponseBodyDataRecord(DaraModel):
    def __init__(
        self,
        called: str = None,
        caller: str = None,
        direction: str = None,
        duration: int = None,
        end_time: str = None,
        id: int = None,
        retry_cur_times: int = None,
        retry_times: int = None,
        start_time: str = None,
        status: str = None,
        status_code: str = None,
        status_code_desc: str = None,
        tags: str = None,
    ):
        self.called = called
        self.caller = caller
        self.direction = direction
        self.duration = duration
        self.end_time = end_time
        self.id = id
        self.retry_cur_times = retry_cur_times
        self.retry_times = retry_times
        self.start_time = start_time
        self.status = status
        self.status_code = status_code
        self.status_code_desc = status_code_desc
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called is not None:
            result['Called'] = self.called

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.retry_cur_times is not None:
            result['RetryCurTimes'] = self.retry_cur_times

        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.status_code_desc is not None:
            result['StatusCodeDesc'] = self.status_code_desc

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Called') is not None:
            self.called = m.get('Called')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RetryCurTimes') is not None:
            self.retry_cur_times = m.get('RetryCurTimes')

        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('StatusCodeDesc') is not None:
            self.status_code_desc = m.get('StatusCodeDesc')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

