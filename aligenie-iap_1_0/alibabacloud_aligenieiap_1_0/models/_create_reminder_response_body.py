# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReminderResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        model: int = None,
        success: bool = None,
    ):
        # Error code.
        self.error_code = error_code
        # Detailed description of the error message.
        self.error_msg = error_msg
        # The ID of the created reminder.
        self.model = model
        # Indicates the result of the API call. true indicates success, and false indicates failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.model is not None:
            result['Model'] = self.model

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

