# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListDeviceBasicInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, main_models.ResultValue] = None,
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
            for v1 in self.result.values():
                 if v1:
                    v1.validate()

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

        result['Result'] = {}
        if self.result is not None:
            for k1, v1 in self.result.items():
                result['Result'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = {}
        if m.get('Result') is not None:
            for k1, v1 in m.get('Result').items():
                temp_model = main_models.ResultValue()
                self.result[k1] = temp_model.from_map(v1)

        return self

