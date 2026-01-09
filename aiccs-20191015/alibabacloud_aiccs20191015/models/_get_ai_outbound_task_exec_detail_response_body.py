# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetAiOutboundTaskExecDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAiOutboundTaskExecDetailResponseBodyData = None,
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
            temp_model = main_models.GetAiOutboundTaskExecDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAiOutboundTaskExecDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        has_next_page: bool = None,
        list: List[main_models.GetAiOutboundTaskExecDetailResponseBodyDataList] = None,
        page_size: int = None,
        total_results: int = None,
    ):
        self.current_page = current_page
        self.has_next_page = has_next_page
        self.list = list
        self.page_size = page_size
        self.total_results = total_results

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.has_next_page is not None:
            result['HasNextPage'] = self.has_next_page

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_results is not None:
            result['TotalResults'] = self.total_results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HasNextPage') is not None:
            self.has_next_page = m.get('HasNextPage')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetAiOutboundTaskExecDetailResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')

        return self

class GetAiOutboundTaskExecDetailResponseBodyDataList(DaraModel):
    def __init__(
        self,
        batch_version: int = None,
        biz_data: str = None,
        call_count: int = None,
        case_id: int = None,
        create_time: int = None,
        last_call_result: str = None,
        phone_num: str = None,
        status: int = None,
        status_desc: int = None,
    ):
        self.batch_version = batch_version
        self.biz_data = biz_data
        self.call_count = call_count
        self.case_id = case_id
        self.create_time = create_time
        self.last_call_result = last_call_result
        self.phone_num = phone_num
        self.status = status
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_version is not None:
            result['BatchVersion'] = self.batch_version

        if self.biz_data is not None:
            result['BizData'] = self.biz_data

        if self.call_count is not None:
            result['CallCount'] = self.call_count

        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_call_result is not None:
            result['LastCallResult'] = self.last_call_result

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        if self.status is not None:
            result['Status'] = self.status

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchVersion') is not None:
            self.batch_version = m.get('BatchVersion')

        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')

        if m.get('CallCount') is not None:
            self.call_count = m.get('CallCount')

        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastCallResult') is not None:
            self.last_call_result = m.get('LastCallResult')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        return self

