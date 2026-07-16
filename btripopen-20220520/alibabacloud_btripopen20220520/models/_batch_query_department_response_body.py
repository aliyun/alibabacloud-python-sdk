# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class BatchQueryDepartmentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        module: main_models.BatchQueryDepartmentResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
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

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

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

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.BatchQueryDepartmentResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class BatchQueryDepartmentResponseBodyModule(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        items: List[main_models.BatchQueryDepartmentResponseBodyModuleItems] = None,
        next_cursor_token: str = None,
        total: int = None,
    ):
        self.has_more = has_more
        self.items = items
        self.next_cursor_token = next_cursor_token
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

        if self.next_cursor_token is not None:
            result['next_cursor_token'] = self.next_cursor_token

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
                temp_model = main_models.BatchQueryDepartmentResponseBodyModuleItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('next_cursor_token') is not None:
            self.next_cursor_token = m.get('next_cursor_token')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class BatchQueryDepartmentResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        dept_name: str = None,
        manager_employee_id_list: List[str] = None,
        out_dept_id: str = None,
    ):
        self.dept_name = dept_name
        self.manager_employee_id_list = manager_employee_id_list
        self.out_dept_id = out_dept_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_name is not None:
            result['dept_name'] = self.dept_name

        if self.manager_employee_id_list is not None:
            result['manager_employee_id_list'] = self.manager_employee_id_list

        if self.out_dept_id is not None:
            result['out_dept_id'] = self.out_dept_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dept_name') is not None:
            self.dept_name = m.get('dept_name')

        if m.get('manager_employee_id_list') is not None:
            self.manager_employee_id_list = m.get('manager_employee_id_list')

        if m.get('out_dept_id') is not None:
            self.out_dept_id = m.get('out_dept_id')

        return self

