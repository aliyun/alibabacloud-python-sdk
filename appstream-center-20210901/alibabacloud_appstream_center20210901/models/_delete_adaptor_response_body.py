# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAdaptorResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This field is returned when the request fails. A successful response may not contain this field.
        self.code = code
        # Indicates whether the operation was successful. A value of true indicates that the operation was successful.
        self.data = data
        # The error message or result prompt. This field describes the cause when the request fails. A successful response may not contain this field.
        self.message = message
        # The unique identifier of the request. You can provide this value when troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the request was processed successfully. A value of true indicates that the request was processed successfully. To check whether the asynchronous task is completed, query the task status separately.
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

