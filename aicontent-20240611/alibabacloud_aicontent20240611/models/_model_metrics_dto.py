# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelMetricsDTO(DaraModel):
    def __init__(
        self,
        avg_response_time: float = None,
        input_tokens: int = None,
        output_tokens: int = None,
        success_rate: float = None,
        total_calls: int = None,
    ):
        self.avg_response_time = avg_response_time
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.success_rate = success_rate
        self.total_calls = total_calls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_response_time is not None:
            result['avgResponseTime'] = self.avg_response_time

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.success_rate is not None:
            result['successRate'] = self.success_rate

        if self.total_calls is not None:
            result['totalCalls'] = self.total_calls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avgResponseTime') is not None:
            self.avg_response_time = m.get('avgResponseTime')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('successRate') is not None:
            self.success_rate = m.get('successRate')

        if m.get('totalCalls') is not None:
            self.total_calls = m.get('totalCalls')

        return self

