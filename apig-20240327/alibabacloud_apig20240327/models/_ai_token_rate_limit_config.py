# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AiTokenRateLimitConfig(DaraModel):
    def __init__(
        self,
        enable_global_rules: bool = None,
        global_rules: List[main_models.AiTokenRateLimitConfigRule] = None,
        plugin_status: main_models.AiPluginStatus = None,
        redis_config: main_models.AiPolicyRedisConfig = None,
        rules: List[main_models.AiTokenRateLimitConfigRule] = None,
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
                temp_model = main_models.AiTokenRateLimitConfigRule()
                self.global_rules.append(temp_model.from_map(k1))

        if m.get('pluginStatus') is not None:
            temp_model = main_models.AiPluginStatus()
            self.plugin_status = temp_model.from_map(m.get('pluginStatus'))

        if m.get('redisConfig') is not None:
            temp_model = main_models.AiPolicyRedisConfig()
            self.redis_config = temp_model.from_map(m.get('redisConfig'))

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.AiTokenRateLimitConfigRule()
                self.rules.append(temp_model.from_map(k1))

        return self

