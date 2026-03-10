# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModelParameters(DaraModel):
    def __init__(
        self,
        frequency_penalty: float = None,
        max_tokens: int = None,
        presence_penalty: float = None,
        stop_sequences: List[str] = None,
        temperature: float = None,
        top_k: int = None,
        top_p: float = None,
    ):
        self.frequency_penalty = frequency_penalty
        self.max_tokens = max_tokens
        self.presence_penalty = presence_penalty
        self.stop_sequences = stop_sequences
        self.temperature = temperature
        self.top_k = top_k
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frequency_penalty is not None:
            result['frequencyPenalty'] = self.frequency_penalty

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        if self.presence_penalty is not None:
            result['presencePenalty'] = self.presence_penalty

        if self.stop_sequences is not None:
            result['stopSequences'] = self.stop_sequences

        if self.temperature is not None:
            result['temperature'] = self.temperature

        if self.top_k is not None:
            result['topK'] = self.top_k

        if self.top_p is not None:
            result['topP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('frequencyPenalty') is not None:
            self.frequency_penalty = m.get('frequencyPenalty')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        if m.get('presencePenalty') is not None:
            self.presence_penalty = m.get('presencePenalty')

        if m.get('stopSequences') is not None:
            self.stop_sequences = m.get('stopSequences')

        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        if m.get('topP') is not None:
            self.top_p = m.get('topP')

        return self

