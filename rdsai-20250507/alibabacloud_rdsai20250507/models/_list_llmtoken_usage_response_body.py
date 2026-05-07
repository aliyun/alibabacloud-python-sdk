# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListLLMTokenUsageResponseBody(DaraModel):
    def __init__(
        self,
        completion_tokens: int = None,
        explicit_cached_tokens: int = None,
        implicit_cached_tokens: int = None,
        prompt_tokens: int = None,
        request_id: str = None,
        token_usages: List[main_models.ListLLMTokenUsageResponseBodyTokenUsages] = None,
        total_tokens: int = None,
    ):
        self.completion_tokens = completion_tokens
        self.explicit_cached_tokens = explicit_cached_tokens
        self.implicit_cached_tokens = implicit_cached_tokens
        self.prompt_tokens = prompt_tokens
        # Id of the request
        self.request_id = request_id
        self.token_usages = token_usages
        self.total_tokens = total_tokens

    def validate(self):
        if self.token_usages:
            for v1 in self.token_usages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_tokens is not None:
            result['CompletionTokens'] = self.completion_tokens

        if self.explicit_cached_tokens is not None:
            result['ExplicitCachedTokens'] = self.explicit_cached_tokens

        if self.implicit_cached_tokens is not None:
            result['ImplicitCachedTokens'] = self.implicit_cached_tokens

        if self.prompt_tokens is not None:
            result['PromptTokens'] = self.prompt_tokens

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TokenUsages'] = []
        if self.token_usages is not None:
            for k1 in self.token_usages:
                result['TokenUsages'].append(k1.to_map() if k1 else None)

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletionTokens') is not None:
            self.completion_tokens = m.get('CompletionTokens')

        if m.get('ExplicitCachedTokens') is not None:
            self.explicit_cached_tokens = m.get('ExplicitCachedTokens')

        if m.get('ImplicitCachedTokens') is not None:
            self.implicit_cached_tokens = m.get('ImplicitCachedTokens')

        if m.get('PromptTokens') is not None:
            self.prompt_tokens = m.get('PromptTokens')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.token_usages = []
        if m.get('TokenUsages') is not None:
            for k1 in m.get('TokenUsages'):
                temp_model = main_models.ListLLMTokenUsageResponseBodyTokenUsages()
                self.token_usages.append(temp_model.from_map(k1))

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class ListLLMTokenUsageResponseBodyTokenUsages(DaraModel):
    def __init__(
        self,
        completion_reasoning_tokens: int = None,
        completion_tokens: int = None,
        end_time: str = None,
        explicit_cached_tokens: int = None,
        implicit_cached_tokens: int = None,
        model: str = None,
        prompt_tokens: int = None,
        start_time: str = None,
        total_tokens: int = None,
    ):
        self.completion_reasoning_tokens = completion_reasoning_tokens
        self.completion_tokens = completion_tokens
        self.end_time = end_time
        self.explicit_cached_tokens = explicit_cached_tokens
        self.implicit_cached_tokens = implicit_cached_tokens
        self.model = model
        self.prompt_tokens = prompt_tokens
        self.start_time = start_time
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_reasoning_tokens is not None:
            result['CompletionReasoningTokens'] = self.completion_reasoning_tokens

        if self.completion_tokens is not None:
            result['CompletionTokens'] = self.completion_tokens

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.explicit_cached_tokens is not None:
            result['ExplicitCachedTokens'] = self.explicit_cached_tokens

        if self.implicit_cached_tokens is not None:
            result['ImplicitCachedTokens'] = self.implicit_cached_tokens

        if self.model is not None:
            result['Model'] = self.model

        if self.prompt_tokens is not None:
            result['PromptTokens'] = self.prompt_tokens

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletionReasoningTokens') is not None:
            self.completion_reasoning_tokens = m.get('CompletionReasoningTokens')

        if m.get('CompletionTokens') is not None:
            self.completion_tokens = m.get('CompletionTokens')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExplicitCachedTokens') is not None:
            self.explicit_cached_tokens = m.get('ExplicitCachedTokens')

        if m.get('ImplicitCachedTokens') is not None:
            self.implicit_cached_tokens = m.get('ImplicitCachedTokens')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('PromptTokens') is not None:
            self.prompt_tokens = m.get('PromptTokens')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

