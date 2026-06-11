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
        # Indicates whether to enable multi-modal capabilities. If set to `true`, the model can process requests that include multiple data types, such as text and images.
        self.enable_multi_modal = enable_multi_modal
        # Indicates whether to include the model\\"s reasoning process in the response. If set to `true`, the output may contain intermediate steps that show how the model arrived at a conclusion.
        self.enable_thinking = enable_thinking
        # The maximum number of tokens to generate in the response. A token is a unit of text processed by the model.
        self.max_tokens = max_tokens
        # The identifier of the model to use for inference.
        self.model = model
        # Indicates whether to deliver the response as a continuous stream. If set to `true`, results are sent incrementally.
        self.streaming = streaming
        # Controls the randomness of the output. Valid values range from 0 to 1. Higher values, such as 0.8, make the output more random. Lower values, such as 0.2, make the output more deterministic.
        self.temperature = temperature
        # Indicates whether the model can search the web to provide more up-to-date responses.
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

