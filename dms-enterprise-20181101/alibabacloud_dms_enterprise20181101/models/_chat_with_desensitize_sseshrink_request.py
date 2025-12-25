# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatWithDesensitizeSSEShrinkRequest(DaraModel):
    def __init__(
        self,
        audio_json: str = None,
        desensitization_rule: str = None,
        dimensions: int = None,
        enable_code_interpreter: bool = None,
        enable_search: bool = None,
        enable_thinking: bool = None,
        include_usage: bool = None,
        input: str = None,
        instance_id: int = None,
        logprobs: bool = None,
        max_tokens: int = None,
        messages_shrink: str = None,
        modalities_list_shrink: str = None,
        model: str = None,
        need_desensitization: bool = None,
        parameters: str = None,
        presence_penalty: str = None,
        response_format: str = None,
        search_options_shrink: str = None,
        seed: int = None,
        stop_shrink: str = None,
        stream: bool = None,
        temperature: str = None,
        thinking_budget: int = None,
        top_k: int = None,
        top_logprobs: int = None,
        top_p: str = None,
        vl_high_resolution_images: bool = None,
        xdash_scope_data_inspection: str = None,
    ):
        self.audio_json = audio_json
        self.desensitization_rule = desensitization_rule
        self.dimensions = dimensions
        self.enable_code_interpreter = enable_code_interpreter
        self.enable_search = enable_search
        self.enable_thinking = enable_thinking
        self.include_usage = include_usage
        self.input = input
        # This parameter is required.
        self.instance_id = instance_id
        self.logprobs = logprobs
        self.max_tokens = max_tokens
        self.messages_shrink = messages_shrink
        self.modalities_list_shrink = modalities_list_shrink
        self.model = model
        self.need_desensitization = need_desensitization
        self.parameters = parameters
        self.presence_penalty = presence_penalty
        self.response_format = response_format
        self.search_options_shrink = search_options_shrink
        self.seed = seed
        self.stop_shrink = stop_shrink
        self.stream = stream
        self.temperature = temperature
        self.thinking_budget = thinking_budget
        self.top_k = top_k
        self.top_logprobs = top_logprobs
        self.top_p = top_p
        self.vl_high_resolution_images = vl_high_resolution_images
        self.xdash_scope_data_inspection = xdash_scope_data_inspection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_json is not None:
            result['AudioJson'] = self.audio_json

        if self.desensitization_rule is not None:
            result['DesensitizationRule'] = self.desensitization_rule

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.enable_code_interpreter is not None:
            result['EnableCodeInterpreter'] = self.enable_code_interpreter

        if self.enable_search is not None:
            result['EnableSearch'] = self.enable_search

        if self.enable_thinking is not None:
            result['EnableThinking'] = self.enable_thinking

        if self.include_usage is not None:
            result['IncludeUsage'] = self.include_usage

        if self.input is not None:
            result['Input'] = self.input

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logprobs is not None:
            result['Logprobs'] = self.logprobs

        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        if self.messages_shrink is not None:
            result['Messages'] = self.messages_shrink

        if self.modalities_list_shrink is not None:
            result['ModalitiesList'] = self.modalities_list_shrink

        if self.model is not None:
            result['Model'] = self.model

        if self.need_desensitization is not None:
            result['NeedDesensitization'] = self.need_desensitization

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.presence_penalty is not None:
            result['PresencePenalty'] = self.presence_penalty

        if self.response_format is not None:
            result['ResponseFormat'] = self.response_format

        if self.search_options_shrink is not None:
            result['SearchOptions'] = self.search_options_shrink

        if self.seed is not None:
            result['Seed'] = self.seed

        if self.stop_shrink is not None:
            result['Stop'] = self.stop_shrink

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        if self.thinking_budget is not None:
            result['ThinkingBudget'] = self.thinking_budget

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.top_logprobs is not None:
            result['TopLogprobs'] = self.top_logprobs

        if self.top_p is not None:
            result['TopP'] = self.top_p

        if self.vl_high_resolution_images is not None:
            result['VlHighResolutionImages'] = self.vl_high_resolution_images

        if self.xdash_scope_data_inspection is not None:
            result['XDashScopeDataInspection'] = self.xdash_scope_data_inspection

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioJson') is not None:
            self.audio_json = m.get('AudioJson')

        if m.get('DesensitizationRule') is not None:
            self.desensitization_rule = m.get('DesensitizationRule')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EnableCodeInterpreter') is not None:
            self.enable_code_interpreter = m.get('EnableCodeInterpreter')

        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')

        if m.get('EnableThinking') is not None:
            self.enable_thinking = m.get('EnableThinking')

        if m.get('IncludeUsage') is not None:
            self.include_usage = m.get('IncludeUsage')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Logprobs') is not None:
            self.logprobs = m.get('Logprobs')

        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        if m.get('Messages') is not None:
            self.messages_shrink = m.get('Messages')

        if m.get('ModalitiesList') is not None:
            self.modalities_list_shrink = m.get('ModalitiesList')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NeedDesensitization') is not None:
            self.need_desensitization = m.get('NeedDesensitization')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PresencePenalty') is not None:
            self.presence_penalty = m.get('PresencePenalty')

        if m.get('ResponseFormat') is not None:
            self.response_format = m.get('ResponseFormat')

        if m.get('SearchOptions') is not None:
            self.search_options_shrink = m.get('SearchOptions')

        if m.get('Seed') is not None:
            self.seed = m.get('Seed')

        if m.get('Stop') is not None:
            self.stop_shrink = m.get('Stop')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        if m.get('ThinkingBudget') is not None:
            self.thinking_budget = m.get('ThinkingBudget')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('TopLogprobs') is not None:
            self.top_logprobs = m.get('TopLogprobs')

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        if m.get('VlHighResolutionImages') is not None:
            self.vl_high_resolution_images = m.get('VlHighResolutionImages')

        if m.get('XDashScopeDataInspection') is not None:
            self.xdash_scope_data_inspection = m.get('XDashScopeDataInspection')

        return self

