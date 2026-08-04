# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ScanCodeBindResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ScanCodeBindResponseBodyResult = None,
    ):
        # The returned error code. A value of 200 indicates that the invocation succeeded.
        self.code = code
        # Result message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Detailed information returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ScanCodeBindResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ScanCodeBindResponseBodyResult(DaraModel):
    def __init__(
        self,
        biz_group: str = None,
        biz_type: str = None,
        device_open_id: str = None,
        user_open_id: str = None,
    ):
        # Product group
        self.biz_group = biz_group
        # Product categorization
        self.biz_type = biz_type
        # A963*0158
        self.device_open_id = device_open_id
        # DAFE****ce3ej=
        self.user_open_id = user_open_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_group is not None:
            result['BizGroup'] = self.biz_group

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id

        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroup') is not None:
            self.biz_group = m.get('BizGroup')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')

        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')

        return self

