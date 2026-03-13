# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class UserQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.UserQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.UserQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class UserQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        items: List[main_models.UserQueryResponseBodyModuleItems] = None,
        page_token: str = None,
        total: int = None,
    ):
        self.has_more = has_more
        self.items = items
        self.page_token = page_token
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['has_more'] = self.has_more

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_token is not None:
            result['page_token'] = self.page_token

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('has_more') is not None:
            self.has_more = m.get('has_more')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.UserQueryResponseBodyModuleItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class UserQueryResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        employee_nick: str = None,
        leave_status: int = None,
        third_part_employee_id: str = None,
        third_part_job_no: str = None,
    ):
        self.employee_nick = employee_nick
        self.leave_status = leave_status
        self.third_part_employee_id = third_part_employee_id
        self.third_part_job_no = third_part_job_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.employee_nick is not None:
            result['employee_nick'] = self.employee_nick

        if self.leave_status is not None:
            result['leave_status'] = self.leave_status

        if self.third_part_employee_id is not None:
            result['third_part_employee_id'] = self.third_part_employee_id

        if self.third_part_job_no is not None:
            result['third_part_job_no'] = self.third_part_job_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('employee_nick') is not None:
            self.employee_nick = m.get('employee_nick')

        if m.get('leave_status') is not None:
            self.leave_status = m.get('leave_status')

        if m.get('third_part_employee_id') is not None:
            self.third_part_employee_id = m.get('third_part_employee_id')

        if m.get('third_part_job_no') is not None:
            self.third_part_job_no = m.get('third_part_job_no')

        return self

