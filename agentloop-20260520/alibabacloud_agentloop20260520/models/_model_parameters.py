# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ModelParameters(DaraModel):
    def __init__(
        self,
        enable_cache_control: bool = None,
        enable_thinking: bool = None,
        extra_body: str = None,
        frequency_penalty: float = None,
        max_completion_tokens: int = None,
        max_tokens: int = None,
        presence_penalty: float = None,
        reasoning_effort: str = None,
        repetition_penalty: float = None,
        response_format: main_models.ModelParametersResponseFormat = None,
        seed: int = None,
        stop_sequences: List[str] = None,
        temperature: float = None,
        thinking_budget: int = None,
        top_k: int = None,
        top_p: float = None,
    ):
        # Specifies whether to enable explicit caching for system messages.
        self.enable_cache_control = enable_cache_control
        # Specifies whether to enable thinking mode. This takes effect only for hybrid thinking models and defaults to false if not specified.
        self.enable_thinking = enable_thinking
        # The extended parameters, which are a serialized string of a JSON object. These are merged into the top level of the model request body to pass through other Model Studio parameters.
        self.extra_body = extra_body
        # The frequency penalty where positive values reduce repetition, with a range of -2.0 to 2.0.
        self.frequency_penalty = frequency_penalty
        # The maximum number of output tokens, including the chain-of-thought and the response. This is recommended for thinking models.
        self.max_completion_tokens = max_completion_tokens
        # The maximum number of output tokens.
        self.max_tokens = max_tokens
        # The presence penalty where positive values encourage new topics, with a range of -2.0 to 2.0.
        self.presence_penalty = presence_penalty
        # The reasoning effort level. This takes effect only when thinking mode is enabled. For the Qwen3.8 series, valid values are low, medium, and xhigh. This cannot be set simultaneously with thinkingBudget.
        self.reasoning_effort = reasoning_effort
        # The repetition penalty that controls the repetition of consecutive sequences. The value must be greater than 0. A value of 1.0 indicates no penalty, and a larger value results in less repetition.
        self.repetition_penalty = repetition_penalty
        # The response content format, which defaults to text if not specified.
        self.response_format = response_format
        # The random seed, with a range of 0 to 2147483647, which attempts to return the same result for the same input and parameters.
        self.seed = seed
        # The stop sequences that immediately halt generation when encountered.
        self.stop_sequences = stop_sequences
        # The temperature parameter that controls the randomness of the output, with a range of 0 to 2.
        self.temperature = temperature
        # The maximum number of tokens for the thinking process. This takes effect only when thinking mode is enabled and cannot be set simultaneously with reasoningEffort.
        self.thinking_budget = thinking_budget
        # The Top K sampling parameter, with a range of 1 to 100.
        self.top_k = top_k
        # The Top P sampling parameter, with a range of 0 to 1.
        self.top_p = top_p

    def validate(self):
        if self.response_format:
            self.response_format.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_cache_control is not None:
            result['enableCacheControl'] = self.enable_cache_control

        if self.enable_thinking is not None:
            result['enableThinking'] = self.enable_thinking

        if self.extra_body is not None:
            result['extraBody'] = self.extra_body

        if self.frequency_penalty is not None:
            result['frequencyPenalty'] = self.frequency_penalty

        if self.max_completion_tokens is not None:
            result['maxCompletionTokens'] = self.max_completion_tokens

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        if self.presence_penalty is not None:
            result['presencePenalty'] = self.presence_penalty

        if self.reasoning_effort is not None:
            result['reasoningEffort'] = self.reasoning_effort

        if self.repetition_penalty is not None:
            result['repetitionPenalty'] = self.repetition_penalty

        if self.response_format is not None:
            result['responseFormat'] = self.response_format.to_map()

        if self.seed is not None:
            result['seed'] = self.seed

        if self.stop_sequences is not None:
            result['stopSequences'] = self.stop_sequences

        if self.temperature is not None:
            result['temperature'] = self.temperature

        if self.thinking_budget is not None:
            result['thinkingBudget'] = self.thinking_budget

        if self.top_k is not None:
            result['topK'] = self.top_k

        if self.top_p is not None:
            result['topP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableCacheControl') is not None:
            self.enable_cache_control = m.get('enableCacheControl')

        if m.get('enableThinking') is not None:
            self.enable_thinking = m.get('enableThinking')

        if m.get('extraBody') is not None:
            self.extra_body = m.get('extraBody')

        if m.get('frequencyPenalty') is not None:
            self.frequency_penalty = m.get('frequencyPenalty')

        if m.get('maxCompletionTokens') is not None:
            self.max_completion_tokens = m.get('maxCompletionTokens')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        if m.get('presencePenalty') is not None:
            self.presence_penalty = m.get('presencePenalty')

        if m.get('reasoningEffort') is not None:
            self.reasoning_effort = m.get('reasoningEffort')

        if m.get('repetitionPenalty') is not None:
            self.repetition_penalty = m.get('repetitionPenalty')

        if m.get('responseFormat') is not None:
            temp_model = main_models.ModelParametersResponseFormat()
            self.response_format = temp_model.from_map(m.get('responseFormat'))

        if m.get('seed') is not None:
            self.seed = m.get('seed')

        if m.get('stopSequences') is not None:
            self.stop_sequences = m.get('stopSequences')

        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        if m.get('thinkingBudget') is not None:
            self.thinking_budget = m.get('thinkingBudget')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        if m.get('topP') is not None:
            self.top_p = m.get('topP')

        return self

class ModelParametersResponseFormat(DaraModel):
    def __init__(
        self,
        json_schema: main_models.ModelParametersResponseFormatJsonSchema = None,
        type: str = None,
    ):
        # The JSON Schema constraint, which is required when the type is json_schema.
        self.json_schema = json_schema
        # The format type. Valid values: text, json_object, and json_schema. When using json_object, the prompt must explicitly request JSON output.
        self.type = type

    def validate(self):
        if self.json_schema:
            self.json_schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.json_schema is not None:
            result['jsonSchema'] = self.json_schema.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jsonSchema') is not None:
            temp_model = main_models.ModelParametersResponseFormatJsonSchema()
            self.json_schema = temp_model.from_map(m.get('jsonSchema'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ModelParametersResponseFormatJsonSchema(DaraModel):
    def __init__(
        self,
        name: str = None,
        schema: str = None,
        strict: bool = None,
    ):
        # The schema name.
        self.name = name
        # The JSON Schema definition, which is a serialized string of a JSON object.
        self.schema = schema
        # Specifies whether to strictly adhere to the schema structure. Set this to true.
        self.strict = strict

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.schema is not None:
            result['schema'] = self.schema

        if self.strict is not None:
            result['strict'] = self.strict

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        if m.get('strict') is not None:
            self.strict = m.get('strict')

        return self

