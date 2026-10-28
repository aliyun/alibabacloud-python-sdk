# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResendEmailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code.
        # Error code. Valid values:
        # - 200: OK.
        # - 1109: System error.
        # - 3058: Emails are sent too frequently. A maximum of 10 emails can be sent within 5 minutes.
        # - 3057: InviteId is empty.
        # - 3060: No sending record found for the specified InviteId.
        # - 3061: The registration URL has expired and the email cannot be resent.
        self.code = code
        # The result message.
        self.message = message
        # The request ID. A unique identifier that Alibaba Cloud generates for the request.
        self.request_id = request_id
        # Valid values: True/False. Indicates whether the current API call itself is successful. This does not indicate the success of subsequent business operations.
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

