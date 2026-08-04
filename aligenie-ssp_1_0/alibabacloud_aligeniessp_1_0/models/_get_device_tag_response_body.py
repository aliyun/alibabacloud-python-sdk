# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetDeviceTagResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetDeviceTagResponseBodyResult = None,
    ):
        # The error code returned. A value of 200 indicates that the call succeeded.
        self.code = code
        # The return result of invoking this API.
        self.message = message
        # The request ID.
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
            temp_model = main_models.GetDeviceTagResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetDeviceTagResponseBodyResult(DaraModel):
    def __init__(
        self,
        device_tags: Dict[str, Any] = None,
    ):
        # Tag information of the device.
        self.device_tags = device_tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')

        return self

