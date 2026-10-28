# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAccountInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. Valid values:
        # - 200: OK.
        # - 1109: A system error occurred.
        # - 3030: The account nickname exceeds the maximum length of 150 bytes.
        # - 3031: The remark exceeds the maximum length of 3000 bytes.
        self.code = code
        # The message returned.
        self.message = message
        # The request ID. Alibaba Cloud uses this ID for error tracking.
        self.request_id = request_id
        # Valid values: True and False. Indicates whether the current API call itself is successful. This does not indicate the success of subsequent business operations.
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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

