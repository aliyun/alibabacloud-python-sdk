# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunLegalAdviceConsultationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response_markdown: str = None,
        round: int = None,
        status: str = None,
        success: bool = None,
        usage: main_models.RunLegalAdviceConsultationResponseBodyUsage = None,
        contents: str = None,
        extra: str = None,
        http_status_code: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.response_markdown = response_markdown
        self.round = round
        self.status = status
        self.success = success
        self.usage = usage
        self.contents = contents
        self.extra = extra
        self.http_status_code = http_status_code

    def validate(self):
        if self.usage:
            self.usage.validate()

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

        if self.response_markdown is not None:
            result['ResponseMarkdown'] = self.response_markdown

        if self.round is not None:
            result['Round'] = self.round

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        if self.contents is not None:
            result['contents'] = self.contents

        if self.extra is not None:
            result['extra'] = self.extra

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResponseMarkdown') is not None:
            self.response_markdown = m.get('ResponseMarkdown')

        if m.get('Round') is not None:
            self.round = m.get('Round')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Usage') is not None:
            temp_model = main_models.RunLegalAdviceConsultationResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        if m.get('contents') is not None:
            self.contents = m.get('contents')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        return self

class RunLegalAdviceConsultationResponseBodyUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

