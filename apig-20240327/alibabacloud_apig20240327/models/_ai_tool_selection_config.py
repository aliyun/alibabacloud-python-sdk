# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AiToolSelectionConfig(DaraModel):
    def __init__(
        self,
        enable_conditions: main_models.AiToolSelectionConfigEnableConditions = None,
        plugin_status: main_models.AiPluginStatus = None,
        query_rewriting: main_models.AiToolSelectionConfigQueryRewriting = None,
        tool_reranking: main_models.AiToolSelectionConfigToolReranking = None,
    ):
        # Conditions for activating the tool selection feature.
        self.enable_conditions = enable_conditions
        # The status of the AI tool selection plugin.
        self.plugin_status = plugin_status
        # Configuration for query rewriting, which optimizes user queries before tool selection.
        self.query_rewriting = query_rewriting
        # Configuration for tool reranking, which controls how tools are scored and filtered.
        self.tool_reranking = tool_reranking

    def validate(self):
        if self.enable_conditions:
            self.enable_conditions.validate()
        if self.plugin_status:
            self.plugin_status.validate()
        if self.query_rewriting:
            self.query_rewriting.validate()
        if self.tool_reranking:
            self.tool_reranking.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_conditions is not None:
            result['enableConditions'] = self.enable_conditions.to_map()

        if self.plugin_status is not None:
            result['pluginStatus'] = self.plugin_status.to_map()

        if self.query_rewriting is not None:
            result['queryRewriting'] = self.query_rewriting.to_map()

        if self.tool_reranking is not None:
            result['toolReranking'] = self.tool_reranking.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableConditions') is not None:
            temp_model = main_models.AiToolSelectionConfigEnableConditions()
            self.enable_conditions = temp_model.from_map(m.get('enableConditions'))

        if m.get('pluginStatus') is not None:
            temp_model = main_models.AiPluginStatus()
            self.plugin_status = temp_model.from_map(m.get('pluginStatus'))

        if m.get('queryRewriting') is not None:
            temp_model = main_models.AiToolSelectionConfigQueryRewriting()
            self.query_rewriting = temp_model.from_map(m.get('queryRewriting'))

        if m.get('toolReranking') is not None:
            temp_model = main_models.AiToolSelectionConfigToolReranking()
            self.tool_reranking = temp_model.from_map(m.get('toolReranking'))

        return self

class AiToolSelectionConfigToolReranking(DaraModel):
    def __init__(
        self,
        fallback_strategy: str = None,
        filtering_method: str = None,
        model_service: main_models.AiToolSelectionConfigToolRerankingModelService = None,
        score_threshold: float = None,
        top_kpercent: int = None,
        top_ncount: int = None,
    ):
        # The fallback strategy used if tool reranking fails or returns no results.
        self.fallback_strategy = fallback_strategy
        # The method for filtering tools after reranking.
        self.filtering_method = filtering_method
        # Model service configuration for tool reranking.
        self.model_service = model_service
        # The minimum score a tool must have to be selected. Tools with scores below this threshold are filtered out.
        self.score_threshold = score_threshold
        # The percentage of top-ranked tools to select. This parameter only applies when `filteringMethod` is set to a percentage-based method.
        self.top_kpercent = top_kpercent
        # The number of top-ranked tools to select. This parameter only applies when `filteringMethod` is set to a count-based method.
        self.top_ncount = top_ncount

    def validate(self):
        if self.model_service:
            self.model_service.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fallback_strategy is not None:
            result['fallbackStrategy'] = self.fallback_strategy

        if self.filtering_method is not None:
            result['filteringMethod'] = self.filtering_method

        if self.model_service is not None:
            result['modelService'] = self.model_service.to_map()

        if self.score_threshold is not None:
            result['scoreThreshold'] = self.score_threshold

        if self.top_kpercent is not None:
            result['topKPercent'] = self.top_kpercent

        if self.top_ncount is not None:
            result['topNCount'] = self.top_ncount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fallbackStrategy') is not None:
            self.fallback_strategy = m.get('fallbackStrategy')

        if m.get('filteringMethod') is not None:
            self.filtering_method = m.get('filteringMethod')

        if m.get('modelService') is not None:
            temp_model = main_models.AiToolSelectionConfigToolRerankingModelService()
            self.model_service = temp_model.from_map(m.get('modelService'))

        if m.get('scoreThreshold') is not None:
            self.score_threshold = m.get('scoreThreshold')

        if m.get('topKPercent') is not None:
            self.top_kpercent = m.get('topKPercent')

        if m.get('topNCount') is not None:
            self.top_ncount = m.get('topNCount')

        return self

class AiToolSelectionConfigToolRerankingModelService(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        service_id: str = None,
        timeout_millisecond: int = None,
    ):
        # The name of the model used for reranking.
        self.model_name = model_name
        # The ID of the model service used for reranking.
        self.service_id = service_id
        # The request timeout in milliseconds for the reranking model service.
        self.timeout_millisecond = timeout_millisecond

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.timeout_millisecond is not None:
            result['timeoutMillisecond'] = self.timeout_millisecond

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('timeoutMillisecond') is not None:
            self.timeout_millisecond = m.get('timeoutMillisecond')

        return self

class AiToolSelectionConfigQueryRewriting(DaraModel):
    def __init__(
        self,
        context_selection: main_models.AiToolSelectionConfigQueryRewritingContextSelection = None,
        enabled: bool = None,
        fallback_strategy: str = None,
        max_output_tokens: int = None,
        model_service: main_models.AiToolSelectionConfigQueryRewritingModelService = None,
        prompt_config: main_models.AiToolSelectionConfigQueryRewritingPromptConfig = None,
        trigger_conditions: main_models.AiToolSelectionConfigQueryRewritingTriggerConditions = None,
    ):
        # Method for selecting the conversation context for query rewriting.
        self.context_selection = context_selection
        # Whether to enable query rewriting.
        self.enabled = enabled
        # The fallback strategy used if query rewriting fails or returns no results.
        self.fallback_strategy = fallback_strategy
        # The maximum number of tokens to generate for the rewritten query.
        self.max_output_tokens = max_output_tokens
        # Model service configuration for query rewriting.
        self.model_service = model_service
        # Prompt configuration for query rewriting.
        self.prompt_config = prompt_config
        # Conditions for activating query rewriting.
        self.trigger_conditions = trigger_conditions

    def validate(self):
        if self.context_selection:
            self.context_selection.validate()
        if self.model_service:
            self.model_service.validate()
        if self.prompt_config:
            self.prompt_config.validate()
        if self.trigger_conditions:
            self.trigger_conditions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_selection is not None:
            result['contextSelection'] = self.context_selection.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.fallback_strategy is not None:
            result['fallbackStrategy'] = self.fallback_strategy

        if self.max_output_tokens is not None:
            result['maxOutputTokens'] = self.max_output_tokens

        if self.model_service is not None:
            result['modelService'] = self.model_service.to_map()

        if self.prompt_config is not None:
            result['promptConfig'] = self.prompt_config.to_map()

        if self.trigger_conditions is not None:
            result['triggerConditions'] = self.trigger_conditions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contextSelection') is not None:
            temp_model = main_models.AiToolSelectionConfigQueryRewritingContextSelection()
            self.context_selection = temp_model.from_map(m.get('contextSelection'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('fallbackStrategy') is not None:
            self.fallback_strategy = m.get('fallbackStrategy')

        if m.get('maxOutputTokens') is not None:
            self.max_output_tokens = m.get('maxOutputTokens')

        if m.get('modelService') is not None:
            temp_model = main_models.AiToolSelectionConfigQueryRewritingModelService()
            self.model_service = temp_model.from_map(m.get('modelService'))

        if m.get('promptConfig') is not None:
            temp_model = main_models.AiToolSelectionConfigQueryRewritingPromptConfig()
            self.prompt_config = temp_model.from_map(m.get('promptConfig'))

        if m.get('triggerConditions') is not None:
            temp_model = main_models.AiToolSelectionConfigQueryRewritingTriggerConditions()
            self.trigger_conditions = temp_model.from_map(m.get('triggerConditions'))

        return self

class AiToolSelectionConfigQueryRewritingTriggerConditions(DaraModel):
    def __init__(
        self,
        message_count_threshold: int = None,
    ):
        # The minimum number of messages in the conversation history required to activate query rewriting.
        self.message_count_threshold = message_count_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_count_threshold is not None:
            result['messageCountThreshold'] = self.message_count_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageCountThreshold') is not None:
            self.message_count_threshold = m.get('messageCountThreshold')

        return self

class AiToolSelectionConfigQueryRewritingPromptConfig(DaraModel):
    def __init__(
        self,
        custom_prompt: str = None,
        type: str = None,
    ):
        # The custom prompt template for query rewriting. This parameter is required if `type` is set to `custom`.
        self.custom_prompt = custom_prompt
        # The type of prompt, such as default or custom.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class AiToolSelectionConfigQueryRewritingModelService(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        service_id: str = None,
        timeout_millisecond: int = None,
    ):
        # The name of the model used for query rewriting.
        self.model_name = model_name
        # The ID of the model service used for query rewriting.
        self.service_id = service_id
        # The request timeout in milliseconds for the query rewriting model service.
        self.timeout_millisecond = timeout_millisecond

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.timeout_millisecond is not None:
            result['timeoutMillisecond'] = self.timeout_millisecond

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('timeoutMillisecond') is not None:
            self.timeout_millisecond = m.get('timeoutMillisecond')

        return self

class AiToolSelectionConfigQueryRewritingContextSelection(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
    ):
        # The strategy for selecting the conversation context.
        self.type = type
        # The value associated with the context selection strategy, such as the number of messages to include.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class AiToolSelectionConfigEnableConditions(DaraModel):
    def __init__(
        self,
        tool_count_threshold: int = None,
    ):
        # The minimum number of tools required to activate tool selection.
        self.tool_count_threshold = tool_count_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tool_count_threshold is not None:
            result['toolCountThreshold'] = self.tool_count_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('toolCountThreshold') is not None:
            self.tool_count_threshold = m.get('toolCountThreshold')

        return self

