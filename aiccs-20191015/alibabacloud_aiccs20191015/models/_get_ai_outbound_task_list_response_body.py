# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetAiOutboundTaskListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAiOutboundTaskListResponseBodyData = None,
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
            temp_model = main_models.GetAiOutboundTaskListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAiOutboundTaskListResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        has_next_page: bool = None,
        list: List[main_models.GetAiOutboundTaskListResponseBodyDataList] = None,
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
                temp_model = main_models.GetAiOutboundTaskListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')

        return self

class GetAiOutboundTaskListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        concurrent_rate: int = None,
        create_time: int = None,
        description: str = None,
        finish_count: int = None,
        finish_rate: float = None,
        handler_id: int = None,
        handler_name: str = None,
        name: str = None,
        status: int = None,
        status_desc: str = None,
        task_id: int = None,
        total_count: int = None,
    ):
        self.concurrent_rate = concurrent_rate
        self.create_time = create_time
        self.description = description
        self.finish_count = finish_count
        self.finish_rate = finish_rate
        self.handler_id = handler_id
        self.handler_name = handler_name
        self.name = name
        self.status = status
        self.status_desc = status_desc
        self.task_id = task_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrent_rate is not None:
            result['ConcurrentRate'] = self.concurrent_rate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.finish_rate is not None:
            result['FinishRate'] = self.finish_rate

        if self.handler_id is not None:
            result['HandlerId'] = self.handler_id

        if self.handler_name is not None:
            result['HandlerName'] = self.handler_name

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrentRate') is not None:
            self.concurrent_rate = m.get('ConcurrentRate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('FinishRate') is not None:
            self.finish_rate = m.get('FinishRate')

        if m.get('HandlerId') is not None:
            self.handler_id = m.get('HandlerId')

        if m.get('HandlerName') is not None:
            self.handler_name = m.get('HandlerName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

