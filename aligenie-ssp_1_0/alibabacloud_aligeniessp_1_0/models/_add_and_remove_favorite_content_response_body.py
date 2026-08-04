# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAndRemoveFavoriteContentResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: str = None,
    ):
        # Return code of the invocation
        self.code = code
        # Additional information. In common scenarios, this provides a brief description of a failed invocation to help the caller identify the issue.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Actual return result of the service
        self.result = result
        # Indicates whether the invocation succeeded. The value true indicates success, and false indicates failure. When the value is false, check the Message field for details.
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

        if self.result is not None:
            result['Result'] = self.result

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

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

