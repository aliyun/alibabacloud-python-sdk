# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_contactcenterai20240603 import models as main_models
from darabonba.model import DaraModel

class RunCompletionResponseBody(DaraModel):
    def __init__(
        self,
        finish_reason: str = None,
        request_id: str = None,
        text: str = None,
        input_tokens: str = None,
        output_tokens: str = None,
        rag_status: str = None,
        total_tokens: str = None,
        usage: main_models.RunCompletionResponseBodyUsage = None,
    ):
        self.finish_reason = finish_reason
        self.request_id = request_id
        self.text = text
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.rag_status = rag_status
        self.total_tokens = total_tokens
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_reason is not None:
            result['FinishReason'] = self.finish_reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.text is not None:
            result['Text'] = self.text

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.rag_status is not None:
            result['ragStatus'] = self.rag_status

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('ragStatus') is not None:
            self.rag_status = m.get('ragStatus')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        if m.get('usage') is not None:
            temp_model = main_models.RunCompletionResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class RunCompletionResponseBodyUsage(DaraModel):
    def __init__(
        self,
        rag: main_models.RunCompletionResponseBodyUsageRag = None,
    ):
        self.rag = rag

    def validate(self):
        if self.rag:
            self.rag.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rag is not None:
            result['rag'] = self.rag.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rag') is not None:
            temp_model = main_models.RunCompletionResponseBodyUsageRag()
            self.rag = temp_model.from_map(m.get('rag'))

        return self

class RunCompletionResponseBodyUsageRag(DaraModel):
    def __init__(
        self,
        adaptive: main_models.RunCompletionResponseBodyUsageRagAdaptive = None,
        dialog_summary: main_models.RunCompletionResponseBodyUsageRagDialogSummary = None,
    ):
        self.adaptive = adaptive
        self.dialog_summary = dialog_summary

    def validate(self):
        if self.adaptive:
            self.adaptive.validate()
        if self.dialog_summary:
            self.dialog_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptive is not None:
            result['adaptive'] = self.adaptive.to_map()

        if self.dialog_summary is not None:
            result['dialogSummary'] = self.dialog_summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adaptive') is not None:
            temp_model = main_models.RunCompletionResponseBodyUsageRagAdaptive()
            self.adaptive = temp_model.from_map(m.get('adaptive'))

        if m.get('dialogSummary') is not None:
            temp_model = main_models.RunCompletionResponseBodyUsageRagDialogSummary()
            self.dialog_summary = temp_model.from_map(m.get('dialogSummary'))

        return self

class RunCompletionResponseBodyUsageRagDialogSummary(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        invoke_count: int = None,
        output_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.invoke_count = invoke_count
        self.output_tokens = output_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.invoke_count is not None:
            result['invokeCount'] = self.invoke_count

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('invokeCount') is not None:
            self.invoke_count = m.get('invokeCount')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        return self

class RunCompletionResponseBodyUsageRagAdaptive(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        invoke_count: int = None,
        output_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.invoke_count = invoke_count
        self.output_tokens = output_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.invoke_count is not None:
            result['invokeCount'] = self.invoke_count

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('invokeCount') is not None:
            self.invoke_count = m.get('invokeCount')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        return self

