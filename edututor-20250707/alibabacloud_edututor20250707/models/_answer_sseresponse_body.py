# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AnswerSSEResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        finish_reason: str = None,
        http_status_code: int = None,
        input_tokens: int = None,
        message: str = None,
        output_tokens: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.finish_reason = finish_reason
        self.http_status_code = http_status_code
        self.input_tokens = input_tokens
        self.message = message
        self.output_tokens = output_tokens
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data

        if self.finish_reason is not None:
            result['finish_reason'] = self.finish_reason

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.input_tokens is not None:
            result['input_tokens'] = self.input_tokens

        if self.message is not None:
            result['message'] = self.message

        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('finish_reason') is not None:
            self.finish_reason = m.get('finish_reason')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

