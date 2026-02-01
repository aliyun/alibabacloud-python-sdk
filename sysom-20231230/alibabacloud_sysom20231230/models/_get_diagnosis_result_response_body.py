# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetDiagnosisResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDiagnosisResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['request_id'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetDiagnosisResultResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        return self

class GetDiagnosisResultResponseBodyData(DaraModel):
    def __init__(
        self,
        code: int = None,
        command: Any = None,
        created_at: str = None,
        err_msg: str = None,
        params: Any = None,
        result: Any = None,
        service_name: str = None,
        status: str = None,
        task_id: str = None,
        updated_at: str = None,
        url: str = None,
    ):
        self.code = code
        self.command = command
        self.created_at = created_at
        self.err_msg = err_msg
        self.params = params
        self.result = result
        self.service_name = service_name
        self.status = status
        self.task_id = task_id
        self.updated_at = updated_at
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.command is not None:
            result['command'] = self.command

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.err_msg is not None:
            result['err_msg'] = self.err_msg

        if self.params is not None:
            result['params'] = self.params

        if self.result is not None:
            result['result'] = self.result

        if self.service_name is not None:
            result['service_name'] = self.service_name

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['task_id'] = self.task_id

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('err_msg') is not None:
            self.err_msg = m.get('err_msg')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

