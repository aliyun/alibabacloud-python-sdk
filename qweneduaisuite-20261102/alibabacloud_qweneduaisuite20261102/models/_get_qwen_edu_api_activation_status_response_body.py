# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qweneduaisuite20261102 import models as main_models
from darabonba.model import DaraModel

class GetQwenEduApiActivationStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetQwenEduApiActivationStatusResponseBodyData = None,
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
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetQwenEduApiActivationStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetQwenEduApiActivationStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_code: str = None,
        fail_message: str = None,
        status: str = None,
    ):
        self.fail_code = fail_code
        self.fail_message = fail_message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_code is not None:
            result['failCode'] = self.fail_code

        if self.fail_message is not None:
            result['failMessage'] = self.fail_message

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failCode') is not None:
            self.fail_code = m.get('failCode')

        if m.get('failMessage') is not None:
            self.fail_message = m.get('failMessage')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

