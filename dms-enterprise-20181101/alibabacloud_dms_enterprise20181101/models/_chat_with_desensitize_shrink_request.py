# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatWithDesensitizeShrinkRequest(DaraModel):
    def __init__(
        self,
        audio_json: str = None,
        desensitization_rule: str = None,
        enable_code_interpreter: bool = None,
        enable_search: bool = None,
        enable_thinking: bool = None,
        instance_id: int = None,
        logprobs: bool = None,
        max_tokens: int = None,
        messages_shrink: str = None,
        modalities_list_shrink: str = None,
        model: str = None,
        need_desensitization: bool = None,
        presence_penalty: str = None,
        response_format: str = None,
        search_options_shrink: str = None,
        seed: int = None,
        stop_shrink: str = None,
        temperature: str = None,
        thinking_budget: int = None,
        top_k: int = None,
        top_logprobs: int = None,
        top_p: str = None,
        vl_high_resolution_images: bool = None,
        xdash_scope_data_inspection: str = None,
    ):
        # Output audio voice and format; only applicable to the Qwen-Omni model, provided that the modalities parameter is set to ["text", "audio"].
        self.audio_json = audio_json
        # Masking category. Required when needDataMasking is true.
        self.desensitization_rule = desensitization_rule
        # Specifies whether to enable the code interpreter feature. Takes effect only when model is qwen3-max-preview and enable_thinking is true.
        self.enable_code_interpreter = enable_code_interpreter
        # Whether to enable web search.
        self.enable_search = enable_search
        # Specifies whether to enable Thinking Mode when using hybrid thinking models.
        self.enable_thinking = enable_thinking
        # The ID of the instance, used to specify the corresponding data masking rules. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) or [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to query the ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to return the log probabilities of the output tokens.
        self.logprobs = logprobs
        # Limits the maximum number of tokens the model can generate. If the output exceeds this value, generation will be truncated. Suitable for scenarios where you need to control the output length.
        self.max_tokens = max_tokens
        # The conversation context passed to the model, arranged in chronological order.
        self.messages_shrink = messages_shrink
        # Output data modality; only applicable to the Qwen-Omni model.
        self.modalities_list_shrink = modalities_list_shrink
        # The model name. Supported Models: Qwen series text-only Large Language Models (Commercial and Open-source). Multi-modal models are not supported.
        self.model = model
        # Whether to enable data masking. Defaults to false.
        self.need_desensitization = need_desensitization
        # Controls the degree of repetition in generated text. Valid values: [-2.0, 2.0]. Positive values decrease repetition, while negative values increase it.
        self.presence_penalty = presence_penalty
        # The format of the returned content. Valid values: text: Plain text response; json_object: Standardized JSON string.
        self.response_format = response_format
        # Web search strategy.
        self.search_options_shrink = search_options_shrink
        # Random seed. Used to ensure the reproducibility of results under the same input and parameters. Valid values: [0, 2^31−1].
        self.seed = seed
        # Stop sequences.
        self.stop_shrink = stop_shrink
        # The sampling temperature controls the diversity of the generated text. The higher the temperature, the more diverse the generated text, and conversely, the more deterministic the generated text. Valid values: [0, 2).
        self.temperature = temperature
        # The maximum number of tokens allowed for the model\\"s internal reasoning process.
        self.thinking_budget = thinking_budget
        # Specifies the number of candidate tokens to consider during sampling. Higher values increase randomness, while lower values make the output more deterministic. Set to null or a value greater than 100 to disable.
        self.top_k = top_k
        # Specifies the number of most likely candidate tokens to return at each generation step. Valid values: [0, 5].
        self.top_logprobs = top_logprobs
        # The probability threshold for nucleus sampling, used to control the diversity of the generated text. Higher Top-P values result in more diverse generated text. Valid values: (0,1.0].
        self.top_p = top_p
        # Specifies whether to increase the maximum pixel limit of input images to the equivalent of 16,384 tokens.
        self.vl_high_resolution_images = vl_high_resolution_images
        # Specifies whether to further identify non-compliant information in both input and output content, building upon the built-in content safety capabilities of the Tongyi Qianwen API.
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

        if self.enable_code_interpreter is not None:
            result['EnableCodeInterpreter'] = self.enable_code_interpreter

        if self.enable_search is not None:
            result['EnableSearch'] = self.enable_search

        if self.enable_thinking is not None:
            result['EnableThinking'] = self.enable_thinking

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

        if m.get('EnableCodeInterpreter') is not None:
            self.enable_code_interpreter = m.get('EnableCodeInterpreter')

        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')

        if m.get('EnableThinking') is not None:
            self.enable_thinking = m.get('EnableThinking')

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

