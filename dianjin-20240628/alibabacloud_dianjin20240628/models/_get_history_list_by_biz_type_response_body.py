# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetHistoryListByBizTypeResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetHistoryListByBizTypeResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('data') is not None:
            temp_model = main_models.GetHistoryListByBizTypeResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class GetHistoryListByBizTypeResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[main_models.GetHistoryListByBizTypeResponseBodyDataRecords] = None,
        total_pages: int = None,
        total_records: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.records = records
        self.total_pages = total_pages
        self.total_records = total_records

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
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        if self.total_pages is not None:
            result['totalPages'] = self.total_pages

        if self.total_records is not None:
            result['totalRecords'] = self.total_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.GetHistoryListByBizTypeResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')

        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')

        return self

class GetHistoryListByBizTypeResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        extra_message: Any = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        llm_answer: str = None,
        llm_prompt: str = None,
        llm_type: str = None,
        session_id: str = None,
        user_query: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.extra_message = extra_message
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.llm_answer = llm_answer
        self.llm_prompt = llm_prompt
        self.llm_type = llm_type
        self.session_id = session_id
        self.user_query = user_query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.extra_message is not None:
            result['extraMessage'] = self.extra_message

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.llm_answer is not None:
            result['llmAnswer'] = self.llm_answer

        if self.llm_prompt is not None:
            result['llmPrompt'] = self.llm_prompt

        if self.llm_type is not None:
            result['llmType'] = self.llm_type

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_query is not None:
            result['userQuery'] = self.user_query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('extraMessage') is not None:
            self.extra_message = m.get('extraMessage')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('llmAnswer') is not None:
            self.llm_answer = m.get('llmAnswer')

        if m.get('llmPrompt') is not None:
            self.llm_prompt = m.get('llmPrompt')

        if m.get('llmType') is not None:
            self.llm_type = m.get('llmType')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userQuery') is not None:
            self.user_query = m.get('userQuery')

        return self

