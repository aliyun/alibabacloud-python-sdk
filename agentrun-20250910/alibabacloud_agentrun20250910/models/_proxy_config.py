# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ProxyConfig(DaraModel):
    def __init__(
        self,
        endpoints: List[main_models.ProxyConfigEndpoints] = None,
        policies: main_models.ProxyConfigPolicies = None,
    ):
        self.endpoints = endpoints
        self.policies = policies

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['endpoints'].append(k1.to_map() if k1 else None)

        if self.policies is not None:
            result['policies'] = self.policies.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('endpoints') is not None:
            for k1 in m.get('endpoints'):
                temp_model = main_models.ProxyConfigEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('policies') is not None:
            temp_model = main_models.ProxyConfigPolicies()
            self.policies = temp_model.from_map(m.get('policies'))

        return self

class ProxyConfigPolicies(DaraModel):
    def __init__(
        self,
        ai_guardrail_config: main_models.ProxyConfigPoliciesAiGuardrailConfig = None,
        cache: bool = None,
        concurrency_limit: int = None,
        fallbacks: List[main_models.ProxyConfigPoliciesFallbacks] = None,
        num_retries: int = None,
        request_timeout: int = None,
        token_rate_limiter: main_models.ProxyConfigPoliciesTokenRateLimiter = None,
    ):
        self.ai_guardrail_config = ai_guardrail_config
        self.cache = cache
        self.concurrency_limit = concurrency_limit
        self.fallbacks = fallbacks
        self.num_retries = num_retries
        self.request_timeout = request_timeout
        self.token_rate_limiter = token_rate_limiter

    def validate(self):
        if self.ai_guardrail_config:
            self.ai_guardrail_config.validate()
        if self.fallbacks:
            for v1 in self.fallbacks:
                 if v1:
                    v1.validate()
        if self.token_rate_limiter:
            self.token_rate_limiter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_guardrail_config is not None:
            result['aiGuardrailConfig'] = self.ai_guardrail_config.to_map()

        if self.cache is not None:
            result['cache'] = self.cache

        if self.concurrency_limit is not None:
            result['concurrencyLimit'] = self.concurrency_limit

        result['fallbacks'] = []
        if self.fallbacks is not None:
            for k1 in self.fallbacks:
                result['fallbacks'].append(k1.to_map() if k1 else None)

        if self.num_retries is not None:
            result['numRetries'] = self.num_retries

        if self.request_timeout is not None:
            result['requestTimeout'] = self.request_timeout

        if self.token_rate_limiter is not None:
            result['tokenRateLimiter'] = self.token_rate_limiter.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiGuardrailConfig') is not None:
            temp_model = main_models.ProxyConfigPoliciesAiGuardrailConfig()
            self.ai_guardrail_config = temp_model.from_map(m.get('aiGuardrailConfig'))

        if m.get('cache') is not None:
            self.cache = m.get('cache')

        if m.get('concurrencyLimit') is not None:
            self.concurrency_limit = m.get('concurrencyLimit')

        self.fallbacks = []
        if m.get('fallbacks') is not None:
            for k1 in m.get('fallbacks'):
                temp_model = main_models.ProxyConfigPoliciesFallbacks()
                self.fallbacks.append(temp_model.from_map(k1))

        if m.get('numRetries') is not None:
            self.num_retries = m.get('numRetries')

        if m.get('requestTimeout') is not None:
            self.request_timeout = m.get('requestTimeout')

        if m.get('tokenRateLimiter') is not None:
            temp_model = main_models.ProxyConfigPoliciesTokenRateLimiter()
            self.token_rate_limiter = temp_model.from_map(m.get('tokenRateLimiter'))

        return self

class ProxyConfigPoliciesTokenRateLimiter(DaraModel):
    def __init__(
        self,
        tpd: int = None,
        tph: int = None,
        tpm: int = None,
        tps: int = None,
    ):
        self.tpd = tpd
        self.tph = tph
        self.tpm = tpm
        self.tps = tps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tpd is not None:
            result['tpd'] = self.tpd

        if self.tph is not None:
            result['tph'] = self.tph

        if self.tpm is not None:
            result['tpm'] = self.tpm

        if self.tps is not None:
            result['tps'] = self.tps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tpd') is not None:
            self.tpd = m.get('tpd')

        if m.get('tph') is not None:
            self.tph = m.get('tph')

        if m.get('tpm') is not None:
            self.tpm = m.get('tpm')

        if m.get('tps') is not None:
            self.tps = m.get('tps')

        return self

class ProxyConfigPoliciesFallbacks(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        model_service_name: str = None,
    ):
        self.model_name = model_name
        self.model_service_name = model_service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_service_name is not None:
            result['modelServiceName'] = self.model_service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelServiceName') is not None:
            self.model_service_name = m.get('modelServiceName')

        return self

class ProxyConfigPoliciesAiGuardrailConfig(DaraModel):
    def __init__(
        self,
        block_on_content_moderation: bool = None,
        block_on_malicious_url: bool = None,
        block_on_model_hallucination: bool = None,
        block_on_prompt_attack: bool = None,
        block_on_sensitive_data: bool = None,
        check_request: bool = None,
        check_response: bool = None,
        level: str = None,
        max_text_length: int = None,
    ):
        self.block_on_content_moderation = block_on_content_moderation
        self.block_on_malicious_url = block_on_malicious_url
        self.block_on_model_hallucination = block_on_model_hallucination
        self.block_on_prompt_attack = block_on_prompt_attack
        self.block_on_sensitive_data = block_on_sensitive_data
        self.check_request = check_request
        self.check_response = check_response
        self.level = level
        self.max_text_length = max_text_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_on_content_moderation is not None:
            result['blockOnContentModeration'] = self.block_on_content_moderation

        if self.block_on_malicious_url is not None:
            result['blockOnMaliciousUrl'] = self.block_on_malicious_url

        if self.block_on_model_hallucination is not None:
            result['blockOnModelHallucination'] = self.block_on_model_hallucination

        if self.block_on_prompt_attack is not None:
            result['blockOnPromptAttack'] = self.block_on_prompt_attack

        if self.block_on_sensitive_data is not None:
            result['blockOnSensitiveData'] = self.block_on_sensitive_data

        if self.check_request is not None:
            result['checkRequest'] = self.check_request

        if self.check_response is not None:
            result['checkResponse'] = self.check_response

        if self.level is not None:
            result['level'] = self.level

        if self.max_text_length is not None:
            result['maxTextLength'] = self.max_text_length

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('blockOnContentModeration') is not None:
            self.block_on_content_moderation = m.get('blockOnContentModeration')

        if m.get('blockOnMaliciousUrl') is not None:
            self.block_on_malicious_url = m.get('blockOnMaliciousUrl')

        if m.get('blockOnModelHallucination') is not None:
            self.block_on_model_hallucination = m.get('blockOnModelHallucination')

        if m.get('blockOnPromptAttack') is not None:
            self.block_on_prompt_attack = m.get('blockOnPromptAttack')

        if m.get('blockOnSensitiveData') is not None:
            self.block_on_sensitive_data = m.get('blockOnSensitiveData')

        if m.get('checkRequest') is not None:
            self.check_request = m.get('checkRequest')

        if m.get('checkResponse') is not None:
            self.check_response = m.get('checkResponse')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('maxTextLength') is not None:
            self.max_text_length = m.get('maxTextLength')

        return self

class ProxyConfigEndpoints(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        model_names: List[str] = None,
        model_service_name: str = None,
        weight: int = None,
    ):
        self.base_url = base_url
        self.model_names = model_names
        self.model_service_name = model_service_name
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['baseUrl'] = self.base_url

        if self.model_names is not None:
            result['modelNames'] = self.model_names

        if self.model_service_name is not None:
            result['modelServiceName'] = self.model_service_name

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseUrl') is not None:
            self.base_url = m.get('baseUrl')

        if m.get('modelNames') is not None:
            self.model_names = m.get('modelNames')

        if m.get('modelServiceName') is not None:
            self.model_service_name = m.get('modelServiceName')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

