# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HiMarketModelFeature(DaraModel):
    def __init__(
        self,
        enable_multi_modal: bool = None,
        enable_thinking: bool = None,
        max_tokens: int = None,
        model: str = None,
        streaming: bool = None,
        temperature: float = None,
        web_search: bool = None,
    ):
        self.enable_multi_modal = enable_multi_modal
        self.enable_thinking = enable_thinking
        self.max_tokens = max_tokens
        self.model = model
        self.streaming = streaming
        self.temperature = temperature
        self.web_search = web_search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_multi_modal is not None:
            result['enableMultiModal'] = self.enable_multi_modal

        if self.enable_thinking is not None:
            result['enableThinking'] = self.enable_thinking

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        if self.model is not None:
            result['model'] = self.model

        if self.streaming is not None:
            result['streaming'] = self.streaming

        if self.temperature is not None:
            result['temperature'] = self.temperature

        if self.web_search is not None:
            result['webSearch'] = self.web_search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableMultiModal') is not None:
            self.enable_multi_modal = m.get('enableMultiModal')

        if m.get('enableThinking') is not None:
            self.enable_thinking = m.get('enableThinking')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('streaming') is not None:
            self.streaming = m.get('streaming')

        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        if m.get('webSearch') is not None:
            self.web_search = m.get('webSearch')

        return self

