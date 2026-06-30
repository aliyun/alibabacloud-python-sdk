# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class DeleteRuleV4ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: main_models.DeleteRuleV4ResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. **200** indicates success. Other values indicate failure. Callers can use this field to determine the cause of failure.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Provides error details if an error occurs. If successful, the value is **successful**.
        self.message = message
        self.messages = messages
        # Request ID
        self.request_id = request_id
        # Indicates whether the request was successful. Callers can use this field to determine if the request succeeded: true means success; false/null means failure.
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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Messages') is not None:
            temp_model = main_models.DeleteRuleV4ResponseBodyMessages()
            self.messages = temp_model.from_map(m.get('Messages'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteRuleV4ResponseBodyMessages(DaraModel):
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

