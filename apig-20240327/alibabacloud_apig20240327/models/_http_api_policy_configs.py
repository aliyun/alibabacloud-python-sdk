# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiPolicyConfigs(DaraModel):
    def __init__(
        self,
        ai_cache_config: main_models.HttpApiPolicyConfigsAiCacheConfig = None,
        ai_fallback_config: main_models.HttpApiPolicyConfigsAiFallbackConfig = None,
        ai_network_search_config: main_models.HttpApiPolicyConfigsAiNetworkSearchConfig = None,
        ai_security_guard_config: main_models.HttpApiPolicyConfigsAiSecurityGuardConfig = None,
        ai_statistics_config: main_models.HttpApiPolicyConfigsAiStatisticsConfig = None,
        ai_token_rate_limit_config: main_models.HttpApiPolicyConfigsAiTokenRateLimitConfig = None,
        ai_tool_selection_config: main_models.HttpApiPolicyConfigsAiToolSelectionConfig = None,
        enable: bool = None,
        semantic_router_config: main_models.HttpApiPolicyConfigsSemanticRouterConfig = None,
        type: str = None,
    ):
        self.ai_cache_config = ai_cache_config
        self.ai_fallback_config = ai_fallback_config
        self.ai_network_search_config = ai_network_search_config
        self.ai_security_guard_config = ai_security_guard_config
        self.ai_statistics_config = ai_statistics_config
        self.ai_token_rate_limit_config = ai_token_rate_limit_config
        self.ai_tool_selection_config = ai_tool_selection_config
        self.enable = enable
        self.semantic_router_config = semantic_router_config
        self.type = type

    def validate(self):
        if self.ai_cache_config:
            self.ai_cache_config.validate()
        if self.ai_fallback_config:
            self.ai_fallback_config.validate()
        if self.ai_network_search_config:
            self.ai_network_search_config.validate()
        if self.ai_security_guard_config:
            self.ai_security_guard_config.validate()
        if self.ai_statistics_config:
            self.ai_statistics_config.validate()
        if self.ai_token_rate_limit_config:
            self.ai_token_rate_limit_config.validate()
        if self.ai_tool_selection_config:
            self.ai_tool_selection_config.validate()
        if self.semantic_router_config:
            self.semantic_router_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_cache_config is not None:
            result['aiCacheConfig'] = self.ai_cache_config.to_map()

        if self.ai_fallback_config is not None:
            result['aiFallbackConfig'] = self.ai_fallback_config.to_map()

        if self.ai_network_search_config is not None:
            result['aiNetworkSearchConfig'] = self.ai_network_search_config.to_map()

        if self.ai_security_guard_config is not None:
            result['aiSecurityGuardConfig'] = self.ai_security_guard_config.to_map()

        if self.ai_statistics_config is not None:
            result['aiStatisticsConfig'] = self.ai_statistics_config.to_map()

        if self.ai_token_rate_limit_config is not None:
            result['aiTokenRateLimitConfig'] = self.ai_token_rate_limit_config.to_map()

        if self.ai_tool_selection_config is not None:
            result['aiToolSelectionConfig'] = self.ai_tool_selection_config.to_map()

        if self.enable is not None:
            result['enable'] = self.enable

        if self.semantic_router_config is not None:
            result['semanticRouterConfig'] = self.semantic_router_config.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiCacheConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiCacheConfig()
            self.ai_cache_config = temp_model.from_map(m.get('aiCacheConfig'))

        if m.get('aiFallbackConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiFallbackConfig()
            self.ai_fallback_config = temp_model.from_map(m.get('aiFallbackConfig'))

        if m.get('aiNetworkSearchConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiNetworkSearchConfig()
            self.ai_network_search_config = temp_model.from_map(m.get('aiNetworkSearchConfig'))

        if m.get('aiSecurityGuardConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiSecurityGuardConfig()
            self.ai_security_guard_config = temp_model.from_map(m.get('aiSecurityGuardConfig'))

        if m.get('aiStatisticsConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiStatisticsConfig()
            self.ai_statistics_config = temp_model.from_map(m.get('aiStatisticsConfig'))

        if m.get('aiTokenRateLimitConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiTokenRateLimitConfig()
            self.ai_token_rate_limit_config = temp_model.from_map(m.get('aiTokenRateLimitConfig'))

        if m.get('aiToolSelectionConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfig()
            self.ai_tool_selection_config = temp_model.from_map(m.get('aiToolSelectionConfig'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('semanticRouterConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsSemanticRouterConfig()
            self.semantic_router_config = temp_model.from_map(m.get('semanticRouterConfig'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HttpApiPolicyConfigsSemanticRouterConfig(DaraModel):
    def __init__(
        self,
        timeout_millisecond: int = None,
    ):
        self.timeout_millisecond = timeout_millisecond

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timeout_millisecond is not None:
            result['timeoutMillisecond'] = self.timeout_millisecond

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeoutMillisecond') is not None:
            self.timeout_millisecond = m.get('timeoutMillisecond')

        return self

class HttpApiPolicyConfigsAiToolSelectionConfig(DaraModel):
    def __init__(
        self,
        enable_conditions: main_models.HttpApiPolicyConfigsAiToolSelectionConfigEnableConditions = None,
        plugin_status: main_models.HttpApiPolicyConfigsAiToolSelectionConfigPluginStatus = None,
        query_rewriting: main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewriting = None,
        tool_reranking: main_models.HttpApiPolicyConfigsAiToolSelectionConfigToolReranking = None,
    ):
        self.enable_conditions = enable_conditions
        self.plugin_status = plugin_status
        self.query_rewriting = query_rewriting
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
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfigEnableConditions()
            self.enable_conditions = temp_model.from_map(m.get('enableConditions'))

        if m.get('pluginStatus') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfigPluginStatus()
            self.plugin_status = temp_model.from_map(m.get('pluginStatus'))

        if m.get('queryRewriting') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewriting()
            self.query_rewriting = temp_model.from_map(m.get('queryRewriting'))

        if m.get('toolReranking') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfigToolReranking()
            self.tool_reranking = temp_model.from_map(m.get('toolReranking'))

        return self

class HttpApiPolicyConfigsAiToolSelectionConfigToolReranking(DaraModel):
    def __init__(
        self,
        fallback_strategy: str = None,
        filtering_method: str = None,
        model_service: main_models.HttpApiPolicyConfigsAiToolSelectionConfigToolRerankingModelService = None,
        score_threshold: float = None,
        top_kpercent: int = None,
        top_ncount: int = None,
    ):
        self.fallback_strategy = fallback_strategy
        self.filtering_method = filtering_method
        self.model_service = model_service
        self.score_threshold = score_threshold
        self.top_kpercent = top_kpercent
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
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfigToolRerankingModelService()
            self.model_service = temp_model.from_map(m.get('modelService'))

        if m.get('scoreThreshold') is not None:
            self.score_threshold = m.get('scoreThreshold')

        if m.get('topKPercent') is not None:
            self.top_kpercent = m.get('topKPercent')

        if m.get('topNCount') is not None:
            self.top_ncount = m.get('topNCount')

        return self

class HttpApiPolicyConfigsAiToolSelectionConfigToolRerankingModelService(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        service_id: str = None,
        timeout_millisecond: int = None,
    ):
        self.model_name = model_name
        self.service_id = service_id
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

class HttpApiPolicyConfigsAiToolSelectionConfigQueryRewriting(DaraModel):
    def __init__(
        self,
        context_selection: main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingContextSelection = None,
        enabled: bool = None,
        fallback_strategy: str = None,
        max_output_tokens: int = None,
        model_service: main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingModelService = None,
        prompt_config: main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingPromptConfig = None,
        trigger_conditions: main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingTriggerConditions = None,
    ):
        self.context_selection = context_selection
        self.enabled = enabled
        self.fallback_strategy = fallback_strategy
        self.max_output_tokens = max_output_tokens
        self.model_service = model_service
        self.prompt_config = prompt_config
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
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingContextSelection()
            self.context_selection = temp_model.from_map(m.get('contextSelection'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('fallbackStrategy') is not None:
            self.fallback_strategy = m.get('fallbackStrategy')

        if m.get('maxOutputTokens') is not None:
            self.max_output_tokens = m.get('maxOutputTokens')

        if m.get('modelService') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingModelService()
            self.model_service = temp_model.from_map(m.get('modelService'))

        if m.get('promptConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingPromptConfig()
            self.prompt_config = temp_model.from_map(m.get('promptConfig'))

        if m.get('triggerConditions') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingTriggerConditions()
            self.trigger_conditions = temp_model.from_map(m.get('triggerConditions'))

        return self

class HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingTriggerConditions(DaraModel):
    def __init__(
        self,
        message_count_threshold: int = None,
    ):
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

class HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingPromptConfig(DaraModel):
    def __init__(
        self,
        custom_prompt: str = None,
        type: str = None,
    ):
        self.custom_prompt = custom_prompt
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

class HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingModelService(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        service_id: str = None,
        timeout_millisecond: int = None,
    ):
        self.model_name = model_name
        self.service_id = service_id
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

class HttpApiPolicyConfigsAiToolSelectionConfigQueryRewritingContextSelection(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
    ):
        self.type = type
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

class HttpApiPolicyConfigsAiToolSelectionConfigPluginStatus(DaraModel):
    def __init__(
        self,
        error_logs: Dict[str, str] = None,
        plugin_id: str = None,
        service_healthy: bool = None,
    ):
        self.error_logs = error_logs
        self.plugin_id = plugin_id
        self.service_healthy = service_healthy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_logs is not None:
            result['errorLogs'] = self.error_logs

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.service_healthy is not None:
            result['serviceHealthy'] = self.service_healthy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorLogs') is not None:
            self.error_logs = m.get('errorLogs')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('serviceHealthy') is not None:
            self.service_healthy = m.get('serviceHealthy')

        return self

class HttpApiPolicyConfigsAiToolSelectionConfigEnableConditions(DaraModel):
    def __init__(
        self,
        tool_count_threshold: int = None,
    ):
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

class HttpApiPolicyConfigsAiTokenRateLimitConfig(DaraModel):
    def __init__(
        self,
        enable_global_rules: bool = None,
        global_rules: List[main_models.HttpApiPolicyConfigsAiTokenRateLimitConfigGlobalRules] = None,
        plugin_status: main_models.HttpApiPolicyConfigsAiTokenRateLimitConfigPluginStatus = None,
        redis_config: main_models.HttpApiPolicyConfigsAiTokenRateLimitConfigRedisConfig = None,
        rules: List[main_models.HttpApiPolicyConfigsAiTokenRateLimitConfigRules] = None,
    ):
        self.enable_global_rules = enable_global_rules
        self.global_rules = global_rules
        self.plugin_status = plugin_status
        self.redis_config = redis_config
        self.rules = rules

    def validate(self):
        if self.global_rules:
            for v1 in self.global_rules:
                 if v1:
                    v1.validate()
        if self.plugin_status:
            self.plugin_status.validate()
        if self.redis_config:
            self.redis_config.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_global_rules is not None:
            result['enableGlobalRules'] = self.enable_global_rules

        result['globalRules'] = []
        if self.global_rules is not None:
            for k1 in self.global_rules:
                result['globalRules'].append(k1.to_map() if k1 else None)

        if self.plugin_status is not None:
            result['pluginStatus'] = self.plugin_status.to_map()

        if self.redis_config is not None:
            result['redisConfig'] = self.redis_config.to_map()

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableGlobalRules') is not None:
            self.enable_global_rules = m.get('enableGlobalRules')

        self.global_rules = []
        if m.get('globalRules') is not None:
            for k1 in m.get('globalRules'):
                temp_model = main_models.HttpApiPolicyConfigsAiTokenRateLimitConfigGlobalRules()
                self.global_rules.append(temp_model.from_map(k1))

        if m.get('pluginStatus') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiTokenRateLimitConfigPluginStatus()
            self.plugin_status = temp_model.from_map(m.get('pluginStatus'))

        if m.get('redisConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiTokenRateLimitConfigRedisConfig()
            self.redis_config = temp_model.from_map(m.get('redisConfig'))

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.HttpApiPolicyConfigsAiTokenRateLimitConfigRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class HttpApiPolicyConfigsAiTokenRateLimitConfigRules(DaraModel):
    def __init__(
        self,
        limit_mode: str = None,
        limit_type: str = None,
        limit_value: str = None,
        match_key: str = None,
        match_type: str = None,
        match_value: str = None,
    ):
        self.limit_mode = limit_mode
        self.limit_type = limit_type
        self.limit_value = limit_value
        self.match_key = match_key
        self.match_type = match_type
        self.match_value = match_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit_mode is not None:
            result['limitMode'] = self.limit_mode

        if self.limit_type is not None:
            result['limitType'] = self.limit_type

        if self.limit_value is not None:
            result['limitValue'] = self.limit_value

        if self.match_key is not None:
            result['matchKey'] = self.match_key

        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.match_value is not None:
            result['matchValue'] = self.match_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limitMode') is not None:
            self.limit_mode = m.get('limitMode')

        if m.get('limitType') is not None:
            self.limit_type = m.get('limitType')

        if m.get('limitValue') is not None:
            self.limit_value = m.get('limitValue')

        if m.get('matchKey') is not None:
            self.match_key = m.get('matchKey')

        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('matchValue') is not None:
            self.match_value = m.get('matchValue')

        return self

class HttpApiPolicyConfigsAiTokenRateLimitConfigRedisConfig(DaraModel):
    def __init__(
        self,
        database_number: int = None,
        host: str = None,
        password: str = None,
        port: int = None,
        timeout: int = None,
        username: str = None,
    ):
        self.database_number = database_number
        self.host = host
        self.password = password
        self.port = port
        self.timeout = timeout
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_number is not None:
            result['databaseNumber'] = self.database_number

        if self.host is not None:
            result['host'] = self.host

        if self.password is not None:
            result['password'] = self.password

        if self.port is not None:
            result['port'] = self.port

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseNumber') is not None:
            self.database_number = m.get('databaseNumber')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

class HttpApiPolicyConfigsAiTokenRateLimitConfigPluginStatus(DaraModel):
    def __init__(
        self,
        error_logs: Dict[str, str] = None,
        plugin_id: str = None,
        service_healthy: bool = None,
    ):
        self.error_logs = error_logs
        self.plugin_id = plugin_id
        self.service_healthy = service_healthy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_logs is not None:
            result['errorLogs'] = self.error_logs

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.service_healthy is not None:
            result['serviceHealthy'] = self.service_healthy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorLogs') is not None:
            self.error_logs = m.get('errorLogs')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('serviceHealthy') is not None:
            self.service_healthy = m.get('serviceHealthy')

        return self

class HttpApiPolicyConfigsAiTokenRateLimitConfigGlobalRules(DaraModel):
    def __init__(
        self,
        limit_mode: str = None,
        limit_type: str = None,
        limit_value: str = None,
        match_key: str = None,
        match_type: str = None,
        match_value: str = None,
    ):
        self.limit_mode = limit_mode
        self.limit_type = limit_type
        self.limit_value = limit_value
        self.match_key = match_key
        self.match_type = match_type
        self.match_value = match_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit_mode is not None:
            result['limitMode'] = self.limit_mode

        if self.limit_type is not None:
            result['limitType'] = self.limit_type

        if self.limit_value is not None:
            result['limitValue'] = self.limit_value

        if self.match_key is not None:
            result['matchKey'] = self.match_key

        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.match_value is not None:
            result['matchValue'] = self.match_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limitMode') is not None:
            self.limit_mode = m.get('limitMode')

        if m.get('limitType') is not None:
            self.limit_type = m.get('limitType')

        if m.get('limitValue') is not None:
            self.limit_value = m.get('limitValue')

        if m.get('matchKey') is not None:
            self.match_key = m.get('matchKey')

        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('matchValue') is not None:
            self.match_value = m.get('matchValue')

        return self

class HttpApiPolicyConfigsAiStatisticsConfig(DaraModel):
    def __init__(
        self,
        log_request_content: bool = None,
        log_response_content: bool = None,
    ):
        self.log_request_content = log_request_content
        self.log_response_content = log_response_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_request_content is not None:
            result['logRequestContent'] = self.log_request_content

        if self.log_response_content is not None:
            result['logResponseContent'] = self.log_response_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logRequestContent') is not None:
            self.log_request_content = m.get('logRequestContent')

        if m.get('logResponseContent') is not None:
            self.log_response_content = m.get('logResponseContent')

        return self

class HttpApiPolicyConfigsAiSecurityGuardConfig(DaraModel):
    def __init__(
        self,
        buffer_limit: int = None,
        check_request: bool = None,
        check_request_image: bool = None,
        check_response: bool = None,
        check_response_image: bool = None,
        consumer_request_check_service: List[main_models.HttpApiPolicyConfigsAiSecurityGuardConfigConsumerRequestCheckService] = None,
        consumer_response_check_service: List[main_models.HttpApiPolicyConfigsAiSecurityGuardConfigConsumerResponseCheckService] = None,
        consumer_risk_level: List[main_models.HttpApiPolicyConfigsAiSecurityGuardConfigConsumerRiskLevel] = None,
        plugin_status: main_models.HttpApiPolicyConfigsAiSecurityGuardConfigPluginStatus = None,
        request_check_service: str = None,
        request_image_check_service: str = None,
        response_check_service: str = None,
        response_image_check_service: str = None,
        risk_alert_level: str = None,
        risk_config: List[main_models.HttpApiPolicyConfigsAiSecurityGuardConfigRiskConfig] = None,
        service_address: str = None,
    ):
        self.buffer_limit = buffer_limit
        self.check_request = check_request
        self.check_request_image = check_request_image
        self.check_response = check_response
        self.check_response_image = check_response_image
        self.consumer_request_check_service = consumer_request_check_service
        self.consumer_response_check_service = consumer_response_check_service
        self.consumer_risk_level = consumer_risk_level
        self.plugin_status = plugin_status
        self.request_check_service = request_check_service
        self.request_image_check_service = request_image_check_service
        self.response_check_service = response_check_service
        self.response_image_check_service = response_image_check_service
        self.risk_alert_level = risk_alert_level
        self.risk_config = risk_config
        self.service_address = service_address

    def validate(self):
        if self.consumer_request_check_service:
            for v1 in self.consumer_request_check_service:
                 if v1:
                    v1.validate()
        if self.consumer_response_check_service:
            for v1 in self.consumer_response_check_service:
                 if v1:
                    v1.validate()
        if self.consumer_risk_level:
            for v1 in self.consumer_risk_level:
                 if v1:
                    v1.validate()
        if self.plugin_status:
            self.plugin_status.validate()
        if self.risk_config:
            for v1 in self.risk_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buffer_limit is not None:
            result['bufferLimit'] = self.buffer_limit

        if self.check_request is not None:
            result['checkRequest'] = self.check_request

        if self.check_request_image is not None:
            result['checkRequestImage'] = self.check_request_image

        if self.check_response is not None:
            result['checkResponse'] = self.check_response

        if self.check_response_image is not None:
            result['checkResponseImage'] = self.check_response_image

        result['consumerRequestCheckService'] = []
        if self.consumer_request_check_service is not None:
            for k1 in self.consumer_request_check_service:
                result['consumerRequestCheckService'].append(k1.to_map() if k1 else None)

        result['consumerResponseCheckService'] = []
        if self.consumer_response_check_service is not None:
            for k1 in self.consumer_response_check_service:
                result['consumerResponseCheckService'].append(k1.to_map() if k1 else None)

        result['consumerRiskLevel'] = []
        if self.consumer_risk_level is not None:
            for k1 in self.consumer_risk_level:
                result['consumerRiskLevel'].append(k1.to_map() if k1 else None)

        if self.plugin_status is not None:
            result['pluginStatus'] = self.plugin_status.to_map()

        if self.request_check_service is not None:
            result['requestCheckService'] = self.request_check_service

        if self.request_image_check_service is not None:
            result['requestImageCheckService'] = self.request_image_check_service

        if self.response_check_service is not None:
            result['responseCheckService'] = self.response_check_service

        if self.response_image_check_service is not None:
            result['responseImageCheckService'] = self.response_image_check_service

        if self.risk_alert_level is not None:
            result['riskAlertLevel'] = self.risk_alert_level

        result['riskConfig'] = []
        if self.risk_config is not None:
            for k1 in self.risk_config:
                result['riskConfig'].append(k1.to_map() if k1 else None)

        if self.service_address is not None:
            result['serviceAddress'] = self.service_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bufferLimit') is not None:
            self.buffer_limit = m.get('bufferLimit')

        if m.get('checkRequest') is not None:
            self.check_request = m.get('checkRequest')

        if m.get('checkRequestImage') is not None:
            self.check_request_image = m.get('checkRequestImage')

        if m.get('checkResponse') is not None:
            self.check_response = m.get('checkResponse')

        if m.get('checkResponseImage') is not None:
            self.check_response_image = m.get('checkResponseImage')

        self.consumer_request_check_service = []
        if m.get('consumerRequestCheckService') is not None:
            for k1 in m.get('consumerRequestCheckService'):
                temp_model = main_models.HttpApiPolicyConfigsAiSecurityGuardConfigConsumerRequestCheckService()
                self.consumer_request_check_service.append(temp_model.from_map(k1))

        self.consumer_response_check_service = []
        if m.get('consumerResponseCheckService') is not None:
            for k1 in m.get('consumerResponseCheckService'):
                temp_model = main_models.HttpApiPolicyConfigsAiSecurityGuardConfigConsumerResponseCheckService()
                self.consumer_response_check_service.append(temp_model.from_map(k1))

        self.consumer_risk_level = []
        if m.get('consumerRiskLevel') is not None:
            for k1 in m.get('consumerRiskLevel'):
                temp_model = main_models.HttpApiPolicyConfigsAiSecurityGuardConfigConsumerRiskLevel()
                self.consumer_risk_level.append(temp_model.from_map(k1))

        if m.get('pluginStatus') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiSecurityGuardConfigPluginStatus()
            self.plugin_status = temp_model.from_map(m.get('pluginStatus'))

        if m.get('requestCheckService') is not None:
            self.request_check_service = m.get('requestCheckService')

        if m.get('requestImageCheckService') is not None:
            self.request_image_check_service = m.get('requestImageCheckService')

        if m.get('responseCheckService') is not None:
            self.response_check_service = m.get('responseCheckService')

        if m.get('responseImageCheckService') is not None:
            self.response_image_check_service = m.get('responseImageCheckService')

        if m.get('riskAlertLevel') is not None:
            self.risk_alert_level = m.get('riskAlertLevel')

        self.risk_config = []
        if m.get('riskConfig') is not None:
            for k1 in m.get('riskConfig'):
                temp_model = main_models.HttpApiPolicyConfigsAiSecurityGuardConfigRiskConfig()
                self.risk_config.append(temp_model.from_map(k1))

        if m.get('serviceAddress') is not None:
            self.service_address = m.get('serviceAddress')

        return self

class HttpApiPolicyConfigsAiSecurityGuardConfigRiskConfig(DaraModel):
    def __init__(
        self,
        consumer_rules: main_models.HttpApiPolicyConfigsAiSecurityGuardConfigRiskConfigConsumerRules = None,
        level: str = None,
        type: str = None,
    ):
        self.consumer_rules = consumer_rules
        self.level = level
        self.type = type

    def validate(self):
        if self.consumer_rules:
            self.consumer_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_rules is not None:
            result['consumerRules'] = self.consumer_rules.to_map()

        if self.level is not None:
            result['level'] = self.level

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerRules') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiSecurityGuardConfigRiskConfigConsumerRules()
            self.consumer_rules = temp_model.from_map(m.get('consumerRules'))

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HttpApiPolicyConfigsAiSecurityGuardConfigRiskConfigConsumerRules(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        pattern: str = None,
    ):
        self.match_type = match_type
        self.pattern = pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.pattern is not None:
            result['pattern'] = self.pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('pattern') is not None:
            self.pattern = m.get('pattern')

        return self

class HttpApiPolicyConfigsAiSecurityGuardConfigPluginStatus(DaraModel):
    def __init__(
        self,
        error_logs: Dict[str, str] = None,
        plugin_id: str = None,
        service_healthy: bool = None,
    ):
        self.error_logs = error_logs
        self.plugin_id = plugin_id
        self.service_healthy = service_healthy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_logs is not None:
            result['errorLogs'] = self.error_logs

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.service_healthy is not None:
            result['serviceHealthy'] = self.service_healthy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorLogs') is not None:
            self.error_logs = m.get('errorLogs')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('serviceHealthy') is not None:
            self.service_healthy = m.get('serviceHealthy')

        return self

class HttpApiPolicyConfigsAiSecurityGuardConfigConsumerRiskLevel(DaraModel):
    def __init__(
        self,
        level: str = None,
        match_type: str = None,
        name: str = None,
        type: str = None,
    ):
        self.level = level
        self.match_type = match_type
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['level'] = self.level

        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HttpApiPolicyConfigsAiSecurityGuardConfigConsumerResponseCheckService(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        modality_type: str = None,
        name: str = None,
        response_check_service: str = None,
        response_image_check_service: str = None,
    ):
        self.match_type = match_type
        self.modality_type = modality_type
        self.name = name
        self.response_check_service = response_check_service
        self.response_image_check_service = response_image_check_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.modality_type is not None:
            result['modalityType'] = self.modality_type

        if self.name is not None:
            result['name'] = self.name

        if self.response_check_service is not None:
            result['responseCheckService'] = self.response_check_service

        if self.response_image_check_service is not None:
            result['responseImageCheckService'] = self.response_image_check_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('modalityType') is not None:
            self.modality_type = m.get('modalityType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('responseCheckService') is not None:
            self.response_check_service = m.get('responseCheckService')

        if m.get('responseImageCheckService') is not None:
            self.response_image_check_service = m.get('responseImageCheckService')

        return self

class HttpApiPolicyConfigsAiSecurityGuardConfigConsumerRequestCheckService(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        modality_type: str = None,
        name: str = None,
        request_check_service: str = None,
        request_image_check_service: str = None,
    ):
        self.match_type = match_type
        self.modality_type = modality_type
        self.name = name
        self.request_check_service = request_check_service
        self.request_image_check_service = request_image_check_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.modality_type is not None:
            result['modalityType'] = self.modality_type

        if self.name is not None:
            result['name'] = self.name

        if self.request_check_service is not None:
            result['requestCheckService'] = self.request_check_service

        if self.request_image_check_service is not None:
            result['requestImageCheckService'] = self.request_image_check_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('modalityType') is not None:
            self.modality_type = m.get('modalityType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestCheckService') is not None:
            self.request_check_service = m.get('requestCheckService')

        if m.get('requestImageCheckService') is not None:
            self.request_image_check_service = m.get('requestImageCheckService')

        return self

class HttpApiPolicyConfigsAiNetworkSearchConfig(DaraModel):
    def __init__(
        self,
        default_enable: bool = None,
        default_lang: str = None,
        need_reference: bool = None,
        plugin_status: main_models.HttpApiPolicyConfigsAiNetworkSearchConfigPluginStatus = None,
        reference_format: str = None,
        reference_location: str = None,
        search_engine_config: main_models.HttpApiPolicyConfigsAiNetworkSearchConfigSearchEngineConfig = None,
        search_from: List[main_models.HttpApiPolicyConfigsAiNetworkSearchConfigSearchFrom] = None,
        search_rewrite: main_models.HttpApiPolicyConfigsAiNetworkSearchConfigSearchRewrite = None,
    ):
        self.default_enable = default_enable
        self.default_lang = default_lang
        self.need_reference = need_reference
        self.plugin_status = plugin_status
        self.reference_format = reference_format
        self.reference_location = reference_location
        self.search_engine_config = search_engine_config
        self.search_from = search_from
        self.search_rewrite = search_rewrite

    def validate(self):
        if self.plugin_status:
            self.plugin_status.validate()
        if self.search_engine_config:
            self.search_engine_config.validate()
        if self.search_from:
            for v1 in self.search_from:
                 if v1:
                    v1.validate()
        if self.search_rewrite:
            self.search_rewrite.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_enable is not None:
            result['defaultEnable'] = self.default_enable

        if self.default_lang is not None:
            result['defaultLang'] = self.default_lang

        if self.need_reference is not None:
            result['needReference'] = self.need_reference

        if self.plugin_status is not None:
            result['pluginStatus'] = self.plugin_status.to_map()

        if self.reference_format is not None:
            result['referenceFormat'] = self.reference_format

        if self.reference_location is not None:
            result['referenceLocation'] = self.reference_location

        if self.search_engine_config is not None:
            result['searchEngineConfig'] = self.search_engine_config.to_map()

        result['searchFrom'] = []
        if self.search_from is not None:
            for k1 in self.search_from:
                result['searchFrom'].append(k1.to_map() if k1 else None)

        if self.search_rewrite is not None:
            result['searchRewrite'] = self.search_rewrite.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultEnable') is not None:
            self.default_enable = m.get('defaultEnable')

        if m.get('defaultLang') is not None:
            self.default_lang = m.get('defaultLang')

        if m.get('needReference') is not None:
            self.need_reference = m.get('needReference')

        if m.get('pluginStatus') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiNetworkSearchConfigPluginStatus()
            self.plugin_status = temp_model.from_map(m.get('pluginStatus'))

        if m.get('referenceFormat') is not None:
            self.reference_format = m.get('referenceFormat')

        if m.get('referenceLocation') is not None:
            self.reference_location = m.get('referenceLocation')

        if m.get('searchEngineConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiNetworkSearchConfigSearchEngineConfig()
            self.search_engine_config = temp_model.from_map(m.get('searchEngineConfig'))

        self.search_from = []
        if m.get('searchFrom') is not None:
            for k1 in m.get('searchFrom'):
                temp_model = main_models.HttpApiPolicyConfigsAiNetworkSearchConfigSearchFrom()
                self.search_from.append(temp_model.from_map(k1))

        if m.get('searchRewrite') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiNetworkSearchConfigSearchRewrite()
            self.search_rewrite = temp_model.from_map(m.get('searchRewrite'))

        return self

class HttpApiPolicyConfigsAiNetworkSearchConfigSearchRewrite(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        max_count: int = None,
        model_name: str = None,
        service_id: str = None,
        timeout_millisecond: int = None,
    ):
        self.enable = enable
        self.max_count = max_count
        self.model_name = model_name
        self.service_id = service_id
        self.timeout_millisecond = timeout_millisecond

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.max_count is not None:
            result['maxCount'] = self.max_count

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.timeout_millisecond is not None:
            result['timeoutMillisecond'] = self.timeout_millisecond

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('maxCount') is not None:
            self.max_count = m.get('maxCount')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('timeoutMillisecond') is not None:
            self.timeout_millisecond = m.get('timeoutMillisecond')

        return self

class HttpApiPolicyConfigsAiNetworkSearchConfigSearchFrom(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        content_mode: str = None,
        count: int = None,
        endpoint: str = None,
        industry: str = None,
        option_args: Dict[str, str] = None,
        start: int = None,
        time_range: str = None,
        timeout_millisecond: int = None,
        type: str = None,
    ):
        self.api_key = api_key
        self.content_mode = content_mode
        self.count = count
        self.endpoint = endpoint
        self.industry = industry
        self.option_args = option_args
        self.start = start
        self.time_range = time_range
        self.timeout_millisecond = timeout_millisecond
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.content_mode is not None:
            result['contentMode'] = self.content_mode

        if self.count is not None:
            result['count'] = self.count

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.industry is not None:
            result['industry'] = self.industry

        if self.option_args is not None:
            result['optionArgs'] = self.option_args

        if self.start is not None:
            result['start'] = self.start

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        if self.timeout_millisecond is not None:
            result['timeoutMillisecond'] = self.timeout_millisecond

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('contentMode') is not None:
            self.content_mode = m.get('contentMode')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('optionArgs') is not None:
            self.option_args = m.get('optionArgs')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        if m.get('timeoutMillisecond') is not None:
            self.timeout_millisecond = m.get('timeoutMillisecond')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HttpApiPolicyConfigsAiNetworkSearchConfigSearchEngineConfig(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        content_mode: str = None,
        count: int = None,
        endpoint: str = None,
        industry: str = None,
        option_args: Dict[str, str] = None,
        start: int = None,
        time_range: str = None,
        timeout_millisecond: int = None,
        type: str = None,
    ):
        self.api_key = api_key
        self.content_mode = content_mode
        self.count = count
        self.endpoint = endpoint
        self.industry = industry
        self.option_args = option_args
        self.start = start
        self.time_range = time_range
        self.timeout_millisecond = timeout_millisecond
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.content_mode is not None:
            result['contentMode'] = self.content_mode

        if self.count is not None:
            result['count'] = self.count

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.industry is not None:
            result['industry'] = self.industry

        if self.option_args is not None:
            result['optionArgs'] = self.option_args

        if self.start is not None:
            result['start'] = self.start

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        if self.timeout_millisecond is not None:
            result['timeoutMillisecond'] = self.timeout_millisecond

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('contentMode') is not None:
            self.content_mode = m.get('contentMode')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('optionArgs') is not None:
            self.option_args = m.get('optionArgs')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        if m.get('timeoutMillisecond') is not None:
            self.timeout_millisecond = m.get('timeoutMillisecond')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HttpApiPolicyConfigsAiNetworkSearchConfigPluginStatus(DaraModel):
    def __init__(
        self,
        error_logs: Dict[str, str] = None,
        plugin_id: str = None,
        service_healthy: bool = None,
    ):
        self.error_logs = error_logs
        self.plugin_id = plugin_id
        self.service_healthy = service_healthy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_logs is not None:
            result['errorLogs'] = self.error_logs

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.service_healthy is not None:
            result['serviceHealthy'] = self.service_healthy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorLogs') is not None:
            self.error_logs = m.get('errorLogs')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('serviceHealthy') is not None:
            self.service_healthy = m.get('serviceHealthy')

        return self

class HttpApiPolicyConfigsAiFallbackConfig(DaraModel):
    def __init__(
        self,
        only_redirect_upstream_code: bool = None,
        route_embedded: bool = None,
        service_configs: List[main_models.HttpApiPolicyConfigsAiFallbackConfigServiceConfigs] = None,
    ):
        self.only_redirect_upstream_code = only_redirect_upstream_code
        self.route_embedded = route_embedded
        self.service_configs = service_configs

    def validate(self):
        if self.service_configs:
            for v1 in self.service_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.only_redirect_upstream_code is not None:
            result['onlyRedirectUpstreamCode'] = self.only_redirect_upstream_code

        if self.route_embedded is not None:
            result['routeEmbedded'] = self.route_embedded

        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onlyRedirectUpstreamCode') is not None:
            self.only_redirect_upstream_code = m.get('onlyRedirectUpstreamCode')

        if m.get('routeEmbedded') is not None:
            self.route_embedded = m.get('routeEmbedded')

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.HttpApiPolicyConfigsAiFallbackConfigServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        return self

class HttpApiPolicyConfigsAiFallbackConfigServiceConfigs(DaraModel):
    def __init__(
        self,
        name: str = None,
        pass_through_model_name: bool = None,
        service_id: str = None,
        target_model_name: str = None,
    ):
        self.name = name
        self.pass_through_model_name = pass_through_model_name
        self.service_id = service_id
        self.target_model_name = target_model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.pass_through_model_name is not None:
            result['passThroughModelName'] = self.pass_through_model_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.target_model_name is not None:
            result['targetModelName'] = self.target_model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('passThroughModelName') is not None:
            self.pass_through_model_name = m.get('passThroughModelName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('targetModelName') is not None:
            self.target_model_name = m.get('targetModelName')

        return self

class HttpApiPolicyConfigsAiCacheConfig(DaraModel):
    def __init__(
        self,
        cache_key_strategy: str = None,
        cache_mode: str = None,
        cache_ttl: int = None,
        embedding_config: main_models.HttpApiPolicyConfigsAiCacheConfigEmbeddingConfig = None,
        plugin_status: main_models.HttpApiPolicyConfigsAiCacheConfigPluginStatus = None,
        redis_config: main_models.HttpApiPolicyConfigsAiCacheConfigRedisConfig = None,
        vector_config: main_models.HttpApiPolicyConfigsAiCacheConfigVectorConfig = None,
    ):
        self.cache_key_strategy = cache_key_strategy
        self.cache_mode = cache_mode
        self.cache_ttl = cache_ttl
        self.embedding_config = embedding_config
        self.plugin_status = plugin_status
        self.redis_config = redis_config
        self.vector_config = vector_config

    def validate(self):
        if self.embedding_config:
            self.embedding_config.validate()
        if self.plugin_status:
            self.plugin_status.validate()
        if self.redis_config:
            self.redis_config.validate()
        if self.vector_config:
            self.vector_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_key_strategy is not None:
            result['cacheKeyStrategy'] = self.cache_key_strategy

        if self.cache_mode is not None:
            result['cacheMode'] = self.cache_mode

        if self.cache_ttl is not None:
            result['cacheTTL'] = self.cache_ttl

        if self.embedding_config is not None:
            result['embeddingConfig'] = self.embedding_config.to_map()

        if self.plugin_status is not None:
            result['pluginStatus'] = self.plugin_status.to_map()

        if self.redis_config is not None:
            result['redisConfig'] = self.redis_config.to_map()

        if self.vector_config is not None:
            result['vectorConfig'] = self.vector_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cacheKeyStrategy') is not None:
            self.cache_key_strategy = m.get('cacheKeyStrategy')

        if m.get('cacheMode') is not None:
            self.cache_mode = m.get('cacheMode')

        if m.get('cacheTTL') is not None:
            self.cache_ttl = m.get('cacheTTL')

        if m.get('embeddingConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiCacheConfigEmbeddingConfig()
            self.embedding_config = temp_model.from_map(m.get('embeddingConfig'))

        if m.get('pluginStatus') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiCacheConfigPluginStatus()
            self.plugin_status = temp_model.from_map(m.get('pluginStatus'))

        if m.get('redisConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiCacheConfigRedisConfig()
            self.redis_config = temp_model.from_map(m.get('redisConfig'))

        if m.get('vectorConfig') is not None:
            temp_model = main_models.HttpApiPolicyConfigsAiCacheConfigVectorConfig()
            self.vector_config = temp_model.from_map(m.get('vectorConfig'))

        return self

class HttpApiPolicyConfigsAiCacheConfigVectorConfig(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        collection_id: str = None,
        service_host: str = None,
        threshold: float = None,
        timeout: int = None,
        type: str = None,
    ):
        self.api_key = api_key
        self.collection_id = collection_id
        self.service_host = service_host
        self.threshold = threshold
        self.timeout = timeout
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.collection_id is not None:
            result['collectionId'] = self.collection_id

        if self.service_host is not None:
            result['serviceHost'] = self.service_host

        if self.threshold is not None:
            result['threshold'] = self.threshold

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('collectionId') is not None:
            self.collection_id = m.get('collectionId')

        if m.get('serviceHost') is not None:
            self.service_host = m.get('serviceHost')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HttpApiPolicyConfigsAiCacheConfigRedisConfig(DaraModel):
    def __init__(
        self,
        database_number: int = None,
        host: str = None,
        password: str = None,
        port: int = None,
        timeout: int = None,
        username: str = None,
    ):
        self.database_number = database_number
        self.host = host
        self.password = password
        self.port = port
        self.timeout = timeout
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_number is not None:
            result['databaseNumber'] = self.database_number

        if self.host is not None:
            result['host'] = self.host

        if self.password is not None:
            result['password'] = self.password

        if self.port is not None:
            result['port'] = self.port

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseNumber') is not None:
            self.database_number = m.get('databaseNumber')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

class HttpApiPolicyConfigsAiCacheConfigPluginStatus(DaraModel):
    def __init__(
        self,
        error_logs: Dict[str, str] = None,
        plugin_id: str = None,
        service_healthy: bool = None,
    ):
        self.error_logs = error_logs
        self.plugin_id = plugin_id
        self.service_healthy = service_healthy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_logs is not None:
            result['errorLogs'] = self.error_logs

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.service_healthy is not None:
            result['serviceHealthy'] = self.service_healthy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorLogs') is not None:
            self.error_logs = m.get('errorLogs')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('serviceHealthy') is not None:
            self.service_healthy = m.get('serviceHealthy')

        return self

class HttpApiPolicyConfigsAiCacheConfigEmbeddingConfig(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        service_id: str = None,
        timeout: int = None,
        type: str = None,
    ):
        self.model_name = model_name
        self.service_id = service_id
        self.timeout = timeout
        self.type = type

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

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

