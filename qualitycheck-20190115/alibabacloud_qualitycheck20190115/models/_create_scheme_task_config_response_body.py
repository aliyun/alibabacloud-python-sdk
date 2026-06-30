# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class CreateSchemeTaskConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        messages: main_models.CreateSchemeTaskConfigResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Result code. **200** indicates success. Any other value indicates failure. The caller can use this field to determine the cause of failure.
        self.code = code
        # ID of the newly created quality inspection job.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # When an error occurs, this field provides error details. When the operation succeeds, the value is "successful".
        self.message = message
        self.messages = messages
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded. The caller can use this field to determine the request outcome: true indicates success; false or null indicates failure.
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.messages is not None:
            result['Messages'] = self.messages.to_map()

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Messages') is not None:
            temp_model = main_models.CreateSchemeTaskConfigResponseBodyMessages()
            self.messages = temp_model.from_map(m.get('Messages'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateSchemeTaskConfigResponseBodyMessages(DaraModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

