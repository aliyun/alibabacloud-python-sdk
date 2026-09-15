# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maasqiservice20260831 import models as main_models
from darabonba.model import DaraModel

class GuiChatCompletionStreamRequest(DaraModel):
    def __init__(
        self,
        allowed_token_ids: List[int] = None,
        bad_words: List[str] = None,
        chat_template_kwargs: main_models.GuiChatCompletionStreamRequestChatTemplateKwargs = None,
        frequency_penalty: float = None,
        ignore_eos: bool = None,
        include_reasoning: bool = None,
        logprobs: bool = None,
        max_completion_tokens: int = None,
        max_tokens: int = None,
        messages: List[main_models.GuiChatCompletionStreamRequestMessages] = None,
        metadata: main_models.GuiChatCompletionStreamRequestMetadata = None,
        min_p: float = None,
        min_tokens: int = None,
        mm_processor_kwargs: main_models.GuiChatCompletionStreamRequestMmProcessorKwargs = None,
        model: str = None,
        n: int = None,
        parallel_tool_calls: bool = None,
        presence_penalty: float = None,
        prompt_logprobs: int = None,
        reasoning_effort: str = None,
        repetition_penalty: float = None,
        response_format: main_models.GuiChatCompletionStreamRequestResponseFormat = None,
        seed: int = None,
        skip_special_tokens: bool = None,
        stop: List[str] = None,
        stop_token_ids: List[int] = None,
        stream: bool = None,
        stream_options: main_models.GuiChatCompletionStreamRequestStreamOptions = None,
        structured_outputs: main_models.GuiChatCompletionStreamRequestStructuredOutputs = None,
        temperature: float = None,
        top_k: int = None,
        top_logprobs: int = None,
        top_p: float = None,
    ):
        self.allowed_token_ids = allowed_token_ids
        self.bad_words = bad_words
        self.chat_template_kwargs = chat_template_kwargs
        self.frequency_penalty = frequency_penalty
        self.ignore_eos = ignore_eos
        self.include_reasoning = include_reasoning
        self.logprobs = logprobs
        self.max_completion_tokens = max_completion_tokens
        self.max_tokens = max_tokens
        # This parameter is required.
        self.messages = messages
        self.metadata = metadata
        self.min_p = min_p
        self.min_tokens = min_tokens
        self.mm_processor_kwargs = mm_processor_kwargs
        self.model = model
        self.n = n
        self.parallel_tool_calls = parallel_tool_calls
        self.presence_penalty = presence_penalty
        self.prompt_logprobs = prompt_logprobs
        self.reasoning_effort = reasoning_effort
        self.repetition_penalty = repetition_penalty
        self.response_format = response_format
        self.seed = seed
        self.skip_special_tokens = skip_special_tokens
        self.stop = stop
        self.stop_token_ids = stop_token_ids
        # This parameter is required.
        self.stream = stream
        self.stream_options = stream_options
        self.structured_outputs = structured_outputs
        self.temperature = temperature
        self.top_k = top_k
        self.top_logprobs = top_logprobs
        self.top_p = top_p

    def validate(self):
        if self.chat_template_kwargs:
            self.chat_template_kwargs.validate()
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.metadata:
            self.metadata.validate()
        if self.mm_processor_kwargs:
            self.mm_processor_kwargs.validate()
        if self.response_format:
            self.response_format.validate()
        if self.stream_options:
            self.stream_options.validate()
        if self.structured_outputs:
            self.structured_outputs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_token_ids is not None:
            result['allowedTokenIds'] = self.allowed_token_ids

        if self.bad_words is not None:
            result['badWords'] = self.bad_words

        if self.chat_template_kwargs is not None:
            result['chatTemplateKwargs'] = self.chat_template_kwargs.to_map()

        if self.frequency_penalty is not None:
            result['frequencyPenalty'] = self.frequency_penalty

        if self.ignore_eos is not None:
            result['ignoreEos'] = self.ignore_eos

        if self.include_reasoning is not None:
            result['includeReasoning'] = self.include_reasoning

        if self.logprobs is not None:
            result['logprobs'] = self.logprobs

        if self.max_completion_tokens is not None:
            result['maxCompletionTokens'] = self.max_completion_tokens

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.min_p is not None:
            result['minP'] = self.min_p

        if self.min_tokens is not None:
            result['minTokens'] = self.min_tokens

        if self.mm_processor_kwargs is not None:
            result['mmProcessorKwargs'] = self.mm_processor_kwargs.to_map()

        if self.model is not None:
            result['model'] = self.model

        if self.n is not None:
            result['n'] = self.n

        if self.parallel_tool_calls is not None:
            result['parallelToolCalls'] = self.parallel_tool_calls

        if self.presence_penalty is not None:
            result['presencePenalty'] = self.presence_penalty

        if self.prompt_logprobs is not None:
            result['promptLogprobs'] = self.prompt_logprobs

        if self.reasoning_effort is not None:
            result['reasoningEffort'] = self.reasoning_effort

        if self.repetition_penalty is not None:
            result['repetitionPenalty'] = self.repetition_penalty

        if self.response_format is not None:
            result['responseFormat'] = self.response_format.to_map()

        if self.seed is not None:
            result['seed'] = self.seed

        if self.skip_special_tokens is not None:
            result['skipSpecialTokens'] = self.skip_special_tokens

        if self.stop is not None:
            result['stop'] = self.stop

        if self.stop_token_ids is not None:
            result['stopTokenIds'] = self.stop_token_ids

        if self.stream is not None:
            result['stream'] = self.stream

        if self.stream_options is not None:
            result['streamOptions'] = self.stream_options.to_map()

        if self.structured_outputs is not None:
            result['structuredOutputs'] = self.structured_outputs.to_map()

        if self.temperature is not None:
            result['temperature'] = self.temperature

        if self.top_k is not None:
            result['topK'] = self.top_k

        if self.top_logprobs is not None:
            result['topLogprobs'] = self.top_logprobs

        if self.top_p is not None:
            result['topP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedTokenIds') is not None:
            self.allowed_token_ids = m.get('allowedTokenIds')

        if m.get('badWords') is not None:
            self.bad_words = m.get('badWords')

        if m.get('chatTemplateKwargs') is not None:
            temp_model = main_models.GuiChatCompletionStreamRequestChatTemplateKwargs()
            self.chat_template_kwargs = temp_model.from_map(m.get('chatTemplateKwargs'))

        if m.get('frequencyPenalty') is not None:
            self.frequency_penalty = m.get('frequencyPenalty')

        if m.get('ignoreEos') is not None:
            self.ignore_eos = m.get('ignoreEos')

        if m.get('includeReasoning') is not None:
            self.include_reasoning = m.get('includeReasoning')

        if m.get('logprobs') is not None:
            self.logprobs = m.get('logprobs')

        if m.get('maxCompletionTokens') is not None:
            self.max_completion_tokens = m.get('maxCompletionTokens')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.GuiChatCompletionStreamRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('metadata') is not None:
            temp_model = main_models.GuiChatCompletionStreamRequestMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('minP') is not None:
            self.min_p = m.get('minP')

        if m.get('minTokens') is not None:
            self.min_tokens = m.get('minTokens')

        if m.get('mmProcessorKwargs') is not None:
            temp_model = main_models.GuiChatCompletionStreamRequestMmProcessorKwargs()
            self.mm_processor_kwargs = temp_model.from_map(m.get('mmProcessorKwargs'))

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('n') is not None:
            self.n = m.get('n')

        if m.get('parallelToolCalls') is not None:
            self.parallel_tool_calls = m.get('parallelToolCalls')

        if m.get('presencePenalty') is not None:
            self.presence_penalty = m.get('presencePenalty')

        if m.get('promptLogprobs') is not None:
            self.prompt_logprobs = m.get('promptLogprobs')

        if m.get('reasoningEffort') is not None:
            self.reasoning_effort = m.get('reasoningEffort')

        if m.get('repetitionPenalty') is not None:
            self.repetition_penalty = m.get('repetitionPenalty')

        if m.get('responseFormat') is not None:
            temp_model = main_models.GuiChatCompletionStreamRequestResponseFormat()
            self.response_format = temp_model.from_map(m.get('responseFormat'))

        if m.get('seed') is not None:
            self.seed = m.get('seed')

        if m.get('skipSpecialTokens') is not None:
            self.skip_special_tokens = m.get('skipSpecialTokens')

        if m.get('stop') is not None:
            self.stop = m.get('stop')

        if m.get('stopTokenIds') is not None:
            self.stop_token_ids = m.get('stopTokenIds')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('streamOptions') is not None:
            temp_model = main_models.GuiChatCompletionStreamRequestStreamOptions()
            self.stream_options = temp_model.from_map(m.get('streamOptions'))

        if m.get('structuredOutputs') is not None:
            temp_model = main_models.GuiChatCompletionStreamRequestStructuredOutputs()
            self.structured_outputs = temp_model.from_map(m.get('structuredOutputs'))

        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        if m.get('topLogprobs') is not None:
            self.top_logprobs = m.get('topLogprobs')

        if m.get('topP') is not None:
            self.top_p = m.get('topP')

        return self

class GuiChatCompletionStreamRequestStructuredOutputs(DaraModel):
    def __init__(
        self,
        choice: List[str] = None,
    ):
        self.choice = choice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.choice is not None:
            result['choice'] = self.choice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('choice') is not None:
            self.choice = m.get('choice')

        return self

class GuiChatCompletionStreamRequestStreamOptions(DaraModel):
    def __init__(
        self,
        include_usage: bool = None,
    ):
        self.include_usage = include_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_usage is not None:
            result['includeUsage'] = self.include_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includeUsage') is not None:
            self.include_usage = m.get('includeUsage')

        return self

class GuiChatCompletionStreamRequestResponseFormat(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GuiChatCompletionStreamRequestMmProcessorKwargs(DaraModel):
    def __init__(
        self,
        max_dynamic_patch: int = None,
    ):
        self.max_dynamic_patch = max_dynamic_patch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_dynamic_patch is not None:
            result['maxDynamicPatch'] = self.max_dynamic_patch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxDynamicPatch') is not None:
            self.max_dynamic_patch = m.get('maxDynamicPatch')

        return self

class GuiChatCompletionStreamRequestMetadata(DaraModel):
    def __init__(
        self,
        app_list: List[str] = None,
        available_apps: List[str] = None,
        harness_message: str = None,
        screen_height: int = None,
        screen_width: int = None,
    ):
        self.app_list = app_list
        self.available_apps = available_apps
        self.harness_message = harness_message
        self.screen_height = screen_height
        self.screen_width = screen_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_list is not None:
            result['appList'] = self.app_list

        if self.available_apps is not None:
            result['availableApps'] = self.available_apps

        if self.harness_message is not None:
            result['harnessMessage'] = self.harness_message

        if self.screen_height is not None:
            result['screenHeight'] = self.screen_height

        if self.screen_width is not None:
            result['screenWidth'] = self.screen_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appList') is not None:
            self.app_list = m.get('appList')

        if m.get('availableApps') is not None:
            self.available_apps = m.get('availableApps')

        if m.get('harnessMessage') is not None:
            self.harness_message = m.get('harnessMessage')

        if m.get('screenHeight') is not None:
            self.screen_height = m.get('screenHeight')

        if m.get('screenWidth') is not None:
            self.screen_width = m.get('screenWidth')

        return self

class GuiChatCompletionStreamRequestMessages(DaraModel):
    def __init__(
        self,
        content: List[main_models.GuiChatCompletionStreamRequestMessagesContent] = None,
        role: str = None,
        tool_call_id: str = None,
    ):
        self.content = content
        self.role = role
        self.tool_call_id = tool_call_id

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        if self.role is not None:
            result['role'] = self.role

        if self.tool_call_id is not None:
            result['toolCallId'] = self.tool_call_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.GuiChatCompletionStreamRequestMessagesContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        return self

class GuiChatCompletionStreamRequestMessagesContent(DaraModel):
    def __init__(
        self,
        image_data: str = None,
        image_url: main_models.GuiChatCompletionStreamRequestMessagesContentImageUrl = None,
        text: str = None,
        type: str = None,
    ):
        self.image_data = image_data
        self.image_url = image_url
        self.text = text
        self.type = type

    def validate(self):
        if self.image_url:
            self.image_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_data is not None:
            result['imageData'] = self.image_data

        if self.image_url is not None:
            result['imageUrl'] = self.image_url.to_map()

        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageData') is not None:
            self.image_data = m.get('imageData')

        if m.get('imageUrl') is not None:
            temp_model = main_models.GuiChatCompletionStreamRequestMessagesContentImageUrl()
            self.image_url = temp_model.from_map(m.get('imageUrl'))

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GuiChatCompletionStreamRequestMessagesContentImageUrl(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class GuiChatCompletionStreamRequestChatTemplateKwargs(DaraModel):
    def __init__(
        self,
        enable_thinking: bool = None,
        preserve_thinking: bool = None,
    ):
        self.enable_thinking = enable_thinking
        self.preserve_thinking = preserve_thinking

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_thinking is not None:
            result['enableThinking'] = self.enable_thinking

        if self.preserve_thinking is not None:
            result['preserveThinking'] = self.preserve_thinking

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableThinking') is not None:
            self.enable_thinking = m.get('enableThinking')

        if m.get('preserveThinking') is not None:
            self.preserve_thinking = m.get('preserveThinking')

        return self

