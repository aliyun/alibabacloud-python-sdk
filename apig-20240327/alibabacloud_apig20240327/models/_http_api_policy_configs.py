# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiPolicyConfigs(DaraModel):
    def __init__(
        self,
        ai_cache_config: main_models.AiCacheConfig = None,
        ai_fallback_config: main_models.AiFallbackConfig = None,
        ai_network_search_config: main_models.AiNetworkSearchConfig = None,
        ai_security_guard_config: main_models.AiSecurityGuardConfig = None,
        ai_statistics_config: main_models.AiStatisticsConfig = None,
        ai_token_rate_limit_config: main_models.AiTokenRateLimitConfig = None,
        ai_tool_selection_config: main_models.AiToolSelectionConfig = None,
        enable: bool = None,
        semantic_router_config: main_models.HttpApiPolicyConfigsSemanticRouterConfig = None,
        type: str = None,
    ):
        # AiCacheConfig
        self.ai_cache_config = ai_cache_config
        # AiFallbackConfig
        self.ai_fallback_config = ai_fallback_config
        # AiNetworkSearchConfig
        self.ai_network_search_config = ai_network_search_config
        # AiSecurityGuardConfig
        self.ai_security_guard_config = ai_security_guard_config
        # AiStatisticsConfig
        self.ai_statistics_config = ai_statistics_config
        # AiTokenRateLimitConfig
        self.ai_token_rate_limit_config = ai_token_rate_limit_config
        # AiToolSelectionConfig
        self.ai_tool_selection_config = ai_tool_selection_config
        # Policy Enable
        self.enable = enable
        # SemanticRouterConfig
        self.semantic_router_config = semantic_router_config
        # Policy Type
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
            temp_model = main_models.AiCacheConfig()
            self.ai_cache_config = temp_model.from_map(m.get('aiCacheConfig'))

        if m.get('aiFallbackConfig') is not None:
            temp_model = main_models.AiFallbackConfig()
            self.ai_fallback_config = temp_model.from_map(m.get('aiFallbackConfig'))

        if m.get('aiNetworkSearchConfig') is not None:
            temp_model = main_models.AiNetworkSearchConfig()
            self.ai_network_search_config = temp_model.from_map(m.get('aiNetworkSearchConfig'))

        if m.get('aiSecurityGuardConfig') is not None:
            temp_model = main_models.AiSecurityGuardConfig()
            self.ai_security_guard_config = temp_model.from_map(m.get('aiSecurityGuardConfig'))

        if m.get('aiStatisticsConfig') is not None:
            temp_model = main_models.AiStatisticsConfig()
            self.ai_statistics_config = temp_model.from_map(m.get('aiStatisticsConfig'))

        if m.get('aiTokenRateLimitConfig') is not None:
            temp_model = main_models.AiTokenRateLimitConfig()
            self.ai_token_rate_limit_config = temp_model.from_map(m.get('aiTokenRateLimitConfig'))

        if m.get('aiToolSelectionConfig') is not None:
            temp_model = main_models.AiToolSelectionConfig()
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
        # Timeout in milliseconds
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

