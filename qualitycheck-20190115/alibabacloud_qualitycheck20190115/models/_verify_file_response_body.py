# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: float = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Result code. **200** indicates success. Other values indicate failure. Callers can determine the failure reason using this field.
        self.code = code
        # Current detection accuracy: Number of incorrect characters in verified files / Total number of characters in verified files.
        self.data = data
        # Error details when an error occurs. Successful when successful.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Callers can determine if the request was successful using this field: true indicates success; false/null indicates failure.
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

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

