# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maasqiservice20260831 import models as main_models
from darabonba.model import DaraModel

class PaChatCompletionStreamRequest(DaraModel):
    def __init__(
        self,
        allowed_token_ids: List[int] = None,
        bad_words: List[str] = None,
        chat_template_kwargs: main_models.PaChatCompletionStreamRequestChatTemplateKwargs = None,
        frequency_penalty: float = None,
        ignore_eos: bool = None,
        include_reasoning: bool = None,
        logprobs: bool = None,
        max_completion_tokens: int = None,
        max_tokens: int = None,
        messages: List[main_models.PaChatCompletionStreamRequestMessages] = None,
        min_p: float = None,
        min_tokens: int = None,
        mm_processor_kwargs: main_models.PaChatCompletionStreamRequestMmProcessorKwargs = None,
        model: str = None,
        n: int = None,
        parallel_tool_calls: bool = None,
        presence_penalty: float = None,
        prompt_logprobs: int = None,
        reasoning_effort: str = None,
        repetition_penalty: float = None,
        response_format: main_models.PaChatCompletionStreamRequestResponseFormat = None,
        seed: int = None,
        skip_special_tokens: bool = None,
        stop: List[str] = None,
        stop_token_ids: List[int] = None,
        stream: bool = None,
        stream_options: main_models.PaChatCompletionStreamRequestStreamOptions = None,
        structured_outputs: main_models.PaChatCompletionStreamRequestStructuredOutputs = None,
        temperature: float = None,
        tool_choice: str = None,
        tools: List[main_models.PaChatCompletionStreamRequestTools] = None,
        top_k: int = None,
        top_logprobs: int = None,
        top_p: float = None,
    ):
        # The whitelist of token IDs allowed for generation.
        self.allowed_token_ids = allowed_token_ids
        # The list of words or strings prohibited from generation.
        self.bad_words = bad_words
        # The vLLM/OpenAI-Compatible template parameter object. Request values are merged with model defaults, with request keys taking precedence, and passed to the model as-is.
        self.chat_template_kwargs = chat_template_kwargs
        # The frequency penalty parameter passed through to the Mobile Planner Agent model.
        self.frequency_penalty = frequency_penalty
        # Specifies whether to ignore EOS and continue generation.
        self.ignore_eos = ignore_eos
        # Specifies whether to request reasoning content from the upstream. The actual capability depends on the model.
        self.include_reasoning = include_reasoning
        # A model-compatible parameter with the JSON field name logprobs. Whether it is accepted and takes effect depends on the model used by the instance. The current Agent response does not provide token log probability details.
        self.logprobs = logprobs
        # The maximum number of completion tokens. Must be greater than 0 if provided, and is passed as an OpenAI-compatible model parameter.
        self.max_completion_tokens = max_completion_tokens
        # The OpenAI-compatible maximum number of generated tokens. Must be greater than 0 if provided.
        self.max_tokens = max_tokens
        # The list of conversation messages. The first call can submit one turn or an existing multi-turn conversation. When continuing with an existing session ID, retain the complete and unmodified historical message prefix and append the current turn messages. Tool results are associated through role=tool and the corresponding tool_call_id.
        # 
        # This parameter is required.
        self.messages = messages
        # The vLLM Min-P sampling parameter.
        self.min_p = min_p
        # The minimum number of tokens to generate.
        self.min_tokens = min_tokens
        # The multimodal preprocessor parameters passed through to vLLM as-is by key.
        self.mm_processor_kwargs = mm_processor_kwargs
        # Reserved for OpenAI client compatibility. Ignored during routing. The actual model is determined by the published instance configuration. The model field in the response is always an empty string.
        self.model = model
        # Set this parameter to 1. Whether the model accepts this parameter depends on the model. The current Mobile Planner Agent response does not return multiple candidate results. Do not use this parameter for multiple-candidate responses.
        self.n = n
        # Specifies whether the model is allowed to generate multiple tool calling requests in parallel. The model invokes tools concurrently when this parameter is enabled.
        self.parallel_tool_calls = parallel_tool_calls
        # The presence penalty parameter, passed through to the Mobile Planner Agent model.
        self.presence_penalty = presence_penalty
        # A model compatibility parameter. The JSON field is prompt_logprobs. Whether the model accepts this parameter depends on the model. The current Agent response does not return probability details for input tokens.
        self.prompt_logprobs = prompt_logprobs
        # The OpenAI-compatible reasoning effort level, such as low, medium, or high.
        self.reasoning_effort = reasoning_effort
        # The vLLM repetition penalty parameter.
        self.repetition_penalty = repetition_penalty
        # The structured response format, such as json_object or json_schema.
        self.response_format = response_format
        # The random seed.
        self.seed = seed
        # Specifies whether to skip special tokens.
        self.skip_special_tokens = skip_special_tokens
        # The stop sequences. Compatible with a single string or an array of strings. This field is displayed in array format.
        self.stop = stop
        # The vLLM stop token ID list.
        self.stop_token_ids = stop_token_ids
        # Specifies whether to use SSE streaming responses. This parameter must be set to true for this operation.
        # 
        # This parameter is required.
        self.stream = stream
        # The OpenAI-compatible streaming options.
        self.stream_options = stream_options
        # The vLLM structured output constraints.
        self.structured_outputs = structured_outputs
        # The sampling temperature. Passed as an OpenAI-compatible model parameter to override the model default value.
        self.temperature = temperature
        # The tool choice strategy. Valid values: auto, none, required, or a named selection supported by the model.
        self.tool_choice = tool_choice
        # The array of function tool definitions available for this request. Mobile Planner Agent registers each named function in the runtime Toolkit and returns tool_calls in the streaming response.
        self.tools = tools
        # The vLLM Top-K sampling parameter.
        self.top_k = top_k
        # A model compatibility parameter. The JSON field is top_logprobs. Used for models that support this feature. The current Agent response does not provide candidate token probability details.
        self.top_logprobs = top_logprobs
        # Top-P sampling parameter. Passed as an OpenAI-compatible model parameter to override the model default value.
        self.top_p = top_p

    def validate(self):
        if self.chat_template_kwargs:
            self.chat_template_kwargs.validate()
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.mm_processor_kwargs:
            self.mm_processor_kwargs.validate()
        if self.response_format:
            self.response_format.validate()
        if self.stream_options:
            self.stream_options.validate()
        if self.structured_outputs:
            self.structured_outputs.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

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

        if self.tool_choice is not None:
            result['toolChoice'] = self.tool_choice

        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.PaChatCompletionStreamRequestChatTemplateKwargs()
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
                temp_model = main_models.PaChatCompletionStreamRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('minP') is not None:
            self.min_p = m.get('minP')

        if m.get('minTokens') is not None:
            self.min_tokens = m.get('minTokens')

        if m.get('mmProcessorKwargs') is not None:
            temp_model = main_models.PaChatCompletionStreamRequestMmProcessorKwargs()
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
            temp_model = main_models.PaChatCompletionStreamRequestResponseFormat()
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
            temp_model = main_models.PaChatCompletionStreamRequestStreamOptions()
            self.stream_options = temp_model.from_map(m.get('streamOptions'))

        if m.get('structuredOutputs') is not None:
            temp_model = main_models.PaChatCompletionStreamRequestStructuredOutputs()
            self.structured_outputs = temp_model.from_map(m.get('structuredOutputs'))

        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        if m.get('toolChoice') is not None:
            self.tool_choice = m.get('toolChoice')

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.PaChatCompletionStreamRequestTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        if m.get('topLogprobs') is not None:
            self.top_logprobs = m.get('topLogprobs')

        if m.get('topP') is not None:
            self.top_p = m.get('topP')

        return self

class PaChatCompletionStreamRequestTools(DaraModel):
    def __init__(
        self,
        function: main_models.PaChatCompletionStreamRequestToolsFunction = None,
        type: str = None,
    ):
        # The function tool definition, including the name, description, and JSON Schema parameters.
        self.function = function
        # The tool type. This parameter must be set to function.
        self.type = type

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['function'] = self.function.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function') is not None:
            temp_model = main_models.PaChatCompletionStreamRequestToolsFunction()
            self.function = temp_model.from_map(m.get('function'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class PaChatCompletionStreamRequestToolsFunction(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        parameters: main_models.PaChatCompletionStreamRequestToolsFunctionParameters = None,
        strict: bool = None,
    ):
        # The description of the function purpose. The model uses this to determine when to call the tool.
        self.description = description
        # The function name. This parameter is required. Used to match assistant.tool_calls with subsequent tool results.
        self.name = name
        # The JSON Schema for function parameters, passed to the model as raw JSON. If not provided, an empty object Schema is used.
        self.parameters = parameters
        # Specifies whether the model must strictly follow the function parameter JSON Schema.
        self.strict = strict

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()

        if self.strict is not None:
            result['strict'] = self.strict

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parameters') is not None:
            temp_model = main_models.PaChatCompletionStreamRequestToolsFunctionParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('strict') is not None:
            self.strict = m.get('strict')

        return self

class PaChatCompletionStreamRequestToolsFunctionParameters(DaraModel):
    def __init__(
        self,
        properties: main_models.PaChatCompletionStreamRequestToolsFunctionParametersProperties = None,
        required: List[str] = None,
        type: str = None,
    ):
        # The property definitions of the JSON Schema.
        self.properties = properties
        # The array of required field names in the JSON Schema.
        self.required = required
        # The root Schema type of the function parameters. Typically set to object.
        self.type = type

    def validate(self):
        if self.properties:
            self.properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.properties is not None:
            result['properties'] = self.properties.to_map()

        if self.required is not None:
            result['required'] = self.required

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            temp_model = main_models.PaChatCompletionStreamRequestToolsFunctionParametersProperties()
            self.properties = temp_model.from_map(m.get('properties'))

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class PaChatCompletionStreamRequestToolsFunctionParametersProperties(DaraModel):
    def __init__(
        self,
        city: main_models.PaChatCompletionStreamRequestToolsFunctionParametersPropertiesCity = None,
    ):
        # The Schema for the sample business parameter city. The actual fields are determined by the caller\\"s tool definition.
        self.city = city

    def validate(self):
        if self.city:
            self.city.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['city'] = self.city.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            temp_model = main_models.PaChatCompletionStreamRequestToolsFunctionParametersPropertiesCity()
            self.city = temp_model.from_map(m.get('city'))

        return self

class PaChatCompletionStreamRequestToolsFunctionParametersPropertiesCity(DaraModel):
    def __init__(
        self,
        description: str = None,
        type: str = None,
    ):
        # The sample parameter description.
        self.description = description
        # The JSON Schema type of the sample city field.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class PaChatCompletionStreamRequestStructuredOutputs(DaraModel):
    def __init__(
        self,
        choice: List[str] = None,
    ):
        # The set of allowed enumeration text values.
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

class PaChatCompletionStreamRequestStreamOptions(DaraModel):
    def __init__(
        self,
        include_usage: bool = None,
    ):
        # Specifies whether to output a usage statistics chunk before data:[DONE].
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

class PaChatCompletionStreamRequestResponseFormat(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The response format type, such as text, json_object, or json_schema.
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

class PaChatCompletionStreamRequestMmProcessorKwargs(DaraModel):
    def __init__(
        self,
        max_dynamic_patch: int = None,
    ):
        # Example: the maximum number of dynamic image patches allowed by the vision model.
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

class PaChatCompletionStreamRequestMessages(DaraModel):
    def __init__(
        self,
        content: List[main_models.PaChatCompletionStreamRequestMessagesContent] = None,
        role: str = None,
        tool_call_id: str = None,
        tool_calls: List[main_models.PaChatCompletionStreamRequestMessagesToolCalls] = None,
    ):
        # The message content. Mobile Planner Agent supports text and multimodal content. Image URLs or base64 Data URLs are passed through to the Mobile Planner Agent model if it supports multimodal input.
        self.content = content
        # The message role: user, assistant, tool, system, or developer. system/developer is used for optional per-turn text instruction overrides. If omitted, the instructions from the instance configuration are used. Tool results use tool and are associated with tool_call_id.
        self.role = role
        # Required when role=tool. Must match an id from the preceding assistant.tool_calls.
        self.tool_call_id = tool_call_id
        # The list of function invocation entries that can be carried when role=assistant. Used for multi-turn tool invocation continuation.
        self.tool_calls = tool_calls

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()
        if self.tool_calls:
            for v1 in self.tool_calls:
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

        result['toolCalls'] = []
        if self.tool_calls is not None:
            for k1 in self.tool_calls:
                result['toolCalls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.PaChatCompletionStreamRequestMessagesContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        self.tool_calls = []
        if m.get('toolCalls') is not None:
            for k1 in m.get('toolCalls'):
                temp_model = main_models.PaChatCompletionStreamRequestMessagesToolCalls()
                self.tool_calls.append(temp_model.from_map(k1))

        return self

class PaChatCompletionStreamRequestMessagesToolCalls(DaraModel):
    def __init__(
        self,
        function: main_models.PaChatCompletionStreamRequestMessagesToolCallsFunction = None,
        id: str = None,
        type: str = None,
    ):
        # The function information of a historical tool invocation entry, including name and arguments as a JSON character string. Retain the actual returned values in subsequent turns.
        self.function = function
        # The tool invocation ID. Subsequent tool messages reference this through tool_call_id.
        self.id = id
        # The tool invocation type. Currently fixed as function.
        self.type = type

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['function'] = self.function.to_map()

        if self.id is not None:
            result['id'] = self.id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function') is not None:
            temp_model = main_models.PaChatCompletionStreamRequestMessagesToolCallsFunction()
            self.function = temp_model.from_map(m.get('function'))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class PaChatCompletionStreamRequestMessagesToolCallsFunction(DaraModel):
    def __init__(
        self,
        arguments: str = None,
        name: str = None,
    ):
        # The JSON object string of function arguments.
        self.arguments = arguments
        # The name of the function to call.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arguments is not None:
            result['arguments'] = self.arguments

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arguments') is not None:
            self.arguments = m.get('arguments')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class PaChatCompletionStreamRequestMessagesContent(DaraModel):
    def __init__(
        self,
        image_url: main_models.PaChatCompletionStreamRequestMessagesContentImageUrl = None,
        text: str = None,
        type: str = None,
    ):
        # The image reference when type=image_url. Supports HTTPS URLs or data:image/...;base64,... format.
        self.image_url = image_url
        # The non-empty text when type=text.
        self.text = text
        # The content part type. Mobile Planner Agent user messages support text or image_url.
        self.type = type

    def validate(self):
        if self.image_url:
            self.image_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['imageUrl'] = self.image_url.to_map()

        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrl') is not None:
            temp_model = main_models.PaChatCompletionStreamRequestMessagesContentImageUrl()
            self.image_url = temp_model.from_map(m.get('imageUrl'))

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class PaChatCompletionStreamRequestMessagesContentImageUrl(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        # The image URL. Remote images must use HTTPS. Base64 Data URLs are also accepted.
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

class PaChatCompletionStreamRequestChatTemplateKwargs(DaraModel):
    def __init__(
        self,
        enable_thinking: bool = None,
        preserve_thinking: bool = None,
    ):
        # Controls whether the model generates reasoning_content through chat_template_kwargs. This value is passed to the model used by the Mobile Planner Agent.
        self.enable_thinking = enable_thinking
        # Specifies whether the model preserves and reuses existing reasoning content in subsequent turns. Passed through as-is per vLLM/Qwen chat_template_kwargs.
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

