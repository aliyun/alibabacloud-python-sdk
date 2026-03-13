# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class QueryEmployeeDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        module: main_models.QueryEmployeeDetailResponseBodyModule = None,
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
            temp_model = main_models.QueryEmployeeDetailResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class QueryEmployeeDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        email: str = None,
        is_leave: bool = None,
        job_number: str = None,
        nick_name: str = None,
        out_dept_id: str = None,
        out_dept_id_list: List[str] = None,
        out_employee_id: str = None,
        phone_no: str = None,
        real_name: str = None,
        real_name_en: str = None,
    ):
        self.email = email
        self.is_leave = is_leave
        self.job_number = job_number
        self.nick_name = nick_name
        self.out_dept_id = out_dept_id
        self.out_dept_id_list = out_dept_id_list
        self.out_employee_id = out_employee_id
        self.phone_no = phone_no
        self.real_name = real_name
        self.real_name_en = real_name_en

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.is_leave is not None:
            result['is_leave'] = self.is_leave

        if self.job_number is not None:
            result['job_number'] = self.job_number

        if self.nick_name is not None:
            result['nick_name'] = self.nick_name

        if self.out_dept_id is not None:
            result['out_dept_id'] = self.out_dept_id

        if self.out_dept_id_list is not None:
            result['out_dept_id_list'] = self.out_dept_id_list

        if self.out_employee_id is not None:
            result['out_employee_id'] = self.out_employee_id

        if self.phone_no is not None:
            result['phone_no'] = self.phone_no

        if self.real_name is not None:
            result['real_name'] = self.real_name

        if self.real_name_en is not None:
            result['real_name_en'] = self.real_name_en

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('is_leave') is not None:
            self.is_leave = m.get('is_leave')

        if m.get('job_number') is not None:
            self.job_number = m.get('job_number')

        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')

        if m.get('out_dept_id') is not None:
            self.out_dept_id = m.get('out_dept_id')

        if m.get('out_dept_id_list') is not None:
            self.out_dept_id_list = m.get('out_dept_id_list')

        if m.get('out_employee_id') is not None:
            self.out_employee_id = m.get('out_employee_id')

        if m.get('phone_no') is not None:
            self.phone_no = m.get('phone_no')

        if m.get('real_name') is not None:
            self.real_name = m.get('real_name')

        if m.get('real_name_en') is not None:
            self.real_name_en = m.get('real_name_en')

        return self

