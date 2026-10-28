# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetWarningThresholdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. Valid values:
        # - 200: OK.
        # - 1109: System error.
        # - 3040: The sub-account is frozen and the operation cannot be completed.
        # - 3044: The alert percentage value is not a number.
        # - 3045: The alert percentage value must be from 1 to 100.
        self.code = code
        # The message that corresponds to the Code parameter value.
        self.message = message
        # The request ID. A unique identifier that Alibaba Cloud generates for the request.
        self.request_id = request_id
        # Indicates whether the current API call was successful. Valid values: True and False. This does not indicate whether the subsequent business operation was successful.
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

