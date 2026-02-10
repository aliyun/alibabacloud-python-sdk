# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AnalyzeConversationResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_info: str = None,
        finish_reason: str = None,
        input_tokens: str = None,
        output_tokens: str = None,
        request_id: str = None,
        success: bool = None,
        text: str = None,
        total_tokens: str = None,
    ):
        self.error_code = error_code
        self.error_info = error_info
        self.finish_reason = finish_reason
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.request_id = request_id
        self.success = success
        self.text = text
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_info is not None:
            result['errorInfo'] = self.error_info

        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.text is not None:
            result['text'] = self.text

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorInfo') is not None:
            self.error_info = m.get('errorInfo')

        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

