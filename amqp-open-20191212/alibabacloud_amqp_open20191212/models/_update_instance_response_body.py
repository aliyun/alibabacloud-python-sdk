# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class UpdateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        status_code: str = None,
        success: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned data, which includes orderId and instanceId. Sample returned data:
        # 
        # ```json
        # "Data": {
        #     "instanceId": "amqp-cn-xxxxx",
        #     "orderId": 22222
        #   }
        # ```
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response code.
        self.status_code = status_code
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

