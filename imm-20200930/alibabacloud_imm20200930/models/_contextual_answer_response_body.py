# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ContextualAnswerResponseBody(DaraModel):
    def __init__(
        self,
        answer: main_models.Answer = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Content of the response from the large model.
        self.answer = answer
        # Error code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID of the current request.
        self.request_id = request_id

    def validate(self):
        if self.answer:
            self.answer.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            temp_model = main_models.Answer()
            self.answer = temp_model.from_map(m.get('Answer'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

