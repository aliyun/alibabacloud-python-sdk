# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiDeployConfig(DaraModel):
    def __init__(
        self,
        auto_deploy: bool = None,
        backend_scene: str = None,
        custom_domain_ids: List[str] = None,
        custom_domain_infos: List[main_models.HttpApiDeployConfigCustomDomainInfos] = None,
        environment_id: str = None,
        gateway_id: str = None,
        gateway_info: main_models.GatewayInfo = None,
        gateway_type: str = None,
        mock: main_models.HttpApiMockContract = None,
        policy_configs: List[main_models.HttpApiDeployConfigPolicyConfigs] = None,
        route_backend: main_models.Backend = None,
        service_configs: List[main_models.HttpApiDeployConfigServiceConfigs] = None,
        sub_domains: List[main_models.HttpApiDeployConfigSubDomains] = None,
    ):
        self.auto_deploy = auto_deploy
        self.backend_scene = backend_scene
        self.custom_domain_ids = custom_domain_ids
        self.custom_domain_infos = custom_domain_infos
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.gateway_info = gateway_info
        self.gateway_type = gateway_type
        self.mock = mock
        self.policy_configs = policy_configs
        self.route_backend = route_backend
        self.service_configs = service_configs
        self.sub_domains = sub_domains

    def validate(self):
        if self.custom_domain_infos:
            for v1 in self.custom_domain_infos:
                 if v1:
                    v1.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.mock:
            self.mock.validate()
        if self.policy_configs:
            for v1 in self.policy_configs:
                 if v1:
                    v1.validate()
        if self.route_backend:
            self.route_backend.validate()
        if self.service_configs:
            for v1 in self.service_configs:
                 if v1:
                    v1.validate()
        if self.sub_domains:
            for v1 in self.sub_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy

        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene

        if self.custom_domain_ids is not None:
            result['customDomainIds'] = self.custom_domain_ids

        result['customDomainInfos'] = []
        if self.custom_domain_infos is not None:
            for k1 in self.custom_domain_infos:
                result['customDomainInfos'].append(k1.to_map() if k1 else None)

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.mock is not None:
            result['mock'] = self.mock.to_map()

        result['policyConfigs'] = []
        if self.policy_configs is not None:
            for k1 in self.policy_configs:
                result['policyConfigs'].append(k1.to_map() if k1 else None)

        if self.route_backend is not None:
            result['routeBackend'] = self.route_backend.to_map()

        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        result['subDomains'] = []
        if self.sub_domains is not None:
            for k1 in self.sub_domains:
                result['subDomains'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')

        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')

        if m.get('customDomainIds') is not None:
            self.custom_domain_ids = m.get('customDomainIds')

        self.custom_domain_infos = []
        if m.get('customDomainInfos') is not None:
            for k1 in m.get('customDomainInfos'):
                temp_model = main_models.HttpApiDeployConfigCustomDomainInfos()
                self.custom_domain_infos.append(temp_model.from_map(k1))

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.GatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('mock') is not None:
            temp_model = main_models.HttpApiMockContract()
            self.mock = temp_model.from_map(m.get('mock'))

        self.policy_configs = []
        if m.get('policyConfigs') is not None:
            for k1 in m.get('policyConfigs'):
                temp_model = main_models.HttpApiDeployConfigPolicyConfigs()
                self.policy_configs.append(temp_model.from_map(k1))

        if m.get('routeBackend') is not None:
            temp_model = main_models.Backend()
            self.route_backend = temp_model.from_map(m.get('routeBackend'))

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.HttpApiDeployConfigServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k1 in m.get('subDomains'):
                temp_model = main_models.HttpApiDeployConfigSubDomains()
                self.sub_domains.append(temp_model.from_map(k1))

        return self

class HttpApiDeployConfigSubDomains(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        network_type: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.network_type = network_type
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.name is not None:
            result['name'] = self.name

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class HttpApiDeployConfigServiceConfigs(DaraModel):
    def __init__(
        self,
        intent_code: str = None,
        match: main_models.HttpApiBackendMatchConditions = None,
        model_name: str = None,
        model_name_pattern: str = None,
        service_id: str = None,
        weight: int = None,
    ):
        self.intent_code = intent_code
        self.match = match
        self.model_name = model_name
        self.model_name_pattern = model_name_pattern
        self.service_id = service_id
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intent_code is not None:
            result['intentCode'] = self.intent_code

        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_name_pattern is not None:
            result['modelNamePattern'] = self.model_name_pattern

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intentCode') is not None:
            self.intent_code = m.get('intentCode')

        if m.get('match') is not None:
            temp_model = main_models.HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelNamePattern') is not None:
            self.model_name_pattern = m.get('modelNamePattern')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class HttpApiDeployConfigPolicyConfigs(DaraModel):
    def __init__(
        self,
        ai_fallback_config: main_models.HttpApiDeployConfigPolicyConfigsAiFallbackConfig = None,
        ai_security_guard_config: main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfig = None,
        ai_token_rate_limit_config: main_models.HttpApiDeployConfigPolicyConfigsAiTokenRateLimitConfig = None,
        enable: bool = None,
        type: str = None,
    ):
        self.ai_fallback_config = ai_fallback_config
        self.ai_security_guard_config = ai_security_guard_config
        self.ai_token_rate_limit_config = ai_token_rate_limit_config
        self.enable = enable
        self.type = type

    def validate(self):
        if self.ai_fallback_config:
            self.ai_fallback_config.validate()
        if self.ai_security_guard_config:
            self.ai_security_guard_config.validate()
        if self.ai_token_rate_limit_config:
            self.ai_token_rate_limit_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_fallback_config is not None:
            result['aiFallbackConfig'] = self.ai_fallback_config.to_map()

        if self.ai_security_guard_config is not None:
            result['aiSecurityGuardConfig'] = self.ai_security_guard_config.to_map()

        if self.ai_token_rate_limit_config is not None:
            result['aiTokenRateLimitConfig'] = self.ai_token_rate_limit_config.to_map()

        if self.enable is not None:
            result['enable'] = self.enable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiFallbackConfig') is not None:
            temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiFallbackConfig()
            self.ai_fallback_config = temp_model.from_map(m.get('aiFallbackConfig'))

        if m.get('aiSecurityGuardConfig') is not None:
            temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfig()
            self.ai_security_guard_config = temp_model.from_map(m.get('aiSecurityGuardConfig'))

        if m.get('aiTokenRateLimitConfig') is not None:
            temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiTokenRateLimitConfig()
            self.ai_token_rate_limit_config = temp_model.from_map(m.get('aiTokenRateLimitConfig'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HttpApiDeployConfigPolicyConfigsAiTokenRateLimitConfig(DaraModel):
    def __init__(
        self,
        enable_global_rules: bool = None,
        global_rules: List[main_models.HttpApiDeployConfigPolicyConfigsAiTokenRateLimitConfigGlobalRules] = None,
        rules: List[main_models.HttpApiDeployConfigPolicyConfigsAiTokenRateLimitConfigRules] = None,
    ):
        self.enable_global_rules = enable_global_rules
        self.global_rules = global_rules
        self.rules = rules

    def validate(self):
        if self.global_rules:
            for v1 in self.global_rules:
                 if v1:
                    v1.validate()
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
                temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiTokenRateLimitConfigGlobalRules()
                self.global_rules.append(temp_model.from_map(k1))

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiTokenRateLimitConfigRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class HttpApiDeployConfigPolicyConfigsAiTokenRateLimitConfigRules(DaraModel):
    def __init__(
        self,
        limit_mode: str = None,
        limit_type: str = None,
        limit_value: int = None,
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

class HttpApiDeployConfigPolicyConfigsAiTokenRateLimitConfigGlobalRules(DaraModel):
    def __init__(
        self,
        limit_mode: str = None,
        limit_type: str = None,
        limit_value: int = None,
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

class HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfig(DaraModel):
    def __init__(
        self,
        buffer_limit: int = None,
        check_request: bool = None,
        check_request_image: bool = None,
        check_response: bool = None,
        check_response_image: bool = None,
        consumer_request_check_service: List[main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigConsumerRequestCheckService] = None,
        consumer_response_check_service: List[main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigConsumerResponseCheckService] = None,
        consumer_risk_level: List[main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigConsumerRiskLevel] = None,
        request_check_service: str = None,
        request_image_check_service: str = None,
        response_check_service: str = None,
        response_image_check_service: str = None,
        risk_alert_level: str = None,
        risk_config: List[main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigRiskConfig] = None,
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
                temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigConsumerRequestCheckService()
                self.consumer_request_check_service.append(temp_model.from_map(k1))

        self.consumer_response_check_service = []
        if m.get('consumerResponseCheckService') is not None:
            for k1 in m.get('consumerResponseCheckService'):
                temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigConsumerResponseCheckService()
                self.consumer_response_check_service.append(temp_model.from_map(k1))

        self.consumer_risk_level = []
        if m.get('consumerRiskLevel') is not None:
            for k1 in m.get('consumerRiskLevel'):
                temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigConsumerRiskLevel()
                self.consumer_risk_level.append(temp_model.from_map(k1))

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
                temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigRiskConfig()
                self.risk_config.append(temp_model.from_map(k1))

        if m.get('serviceAddress') is not None:
            self.service_address = m.get('serviceAddress')

        return self

class HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigRiskConfig(DaraModel):
    def __init__(
        self,
        consumer_rules: main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigRiskConfigConsumerRules = None,
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
            temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigRiskConfigConsumerRules()
            self.consumer_rules = temp_model.from_map(m.get('consumerRules'))

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigRiskConfigConsumerRules(DaraModel):
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

class HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigConsumerRiskLevel(DaraModel):
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

class HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigConsumerResponseCheckService(DaraModel):
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

class HttpApiDeployConfigPolicyConfigsAiSecurityGuardConfigConsumerRequestCheckService(DaraModel):
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

class HttpApiDeployConfigPolicyConfigsAiFallbackConfig(DaraModel):
    def __init__(
        self,
        service_configs: List[main_models.HttpApiDeployConfigPolicyConfigsAiFallbackConfigServiceConfigs] = None,
    ):
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
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.HttpApiDeployConfigPolicyConfigsAiFallbackConfigServiceConfigs()
                self.service_configs.append(temp_model.from_map(k1))

        return self

class HttpApiDeployConfigPolicyConfigsAiFallbackConfigServiceConfigs(DaraModel):
    def __init__(
        self,
        service_id: str = None,
        target_model_name: str = None,
    ):
        self.service_id = service_id
        self.target_model_name = target_model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.target_model_name is not None:
            result['targetModelName'] = self.target_model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('targetModelName') is not None:
            self.target_model_name = m.get('targetModelName')

        return self

class HttpApiDeployConfigCustomDomainInfos(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

