# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_bailianmodelonchip20240816 import models as main_models
from darabonba.model import DaraModel

class GetPassThroughAuthInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPassThroughAuthInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetPassThroughAuthInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetPassThroughAuthInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        device_name: str = None,
        pass_through_params: Dict[str, Any] = None,
        task_id: str = None,
    ):
        self.app_id = app_id
        self.device_name = device_name
        self.pass_through_params = pass_through_params
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.device_name is not None:
            result['deviceName'] = self.device_name

        if self.pass_through_params is not None:
            result['passThroughParams'] = self.pass_through_params

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')

        if m.get('passThroughParams') is not None:
            self.pass_through_params = m.get('passThroughParams')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

