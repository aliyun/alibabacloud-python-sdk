# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AiSecurityGuardConfig(DaraModel):
    def __init__(
        self,
        buffer_limit: int = None,
        check_request: bool = None,
        check_request_image: bool = None,
        check_response: bool = None,
        check_response_image: bool = None,
        consumer_request_check_service: List[main_models.AiSecurityGuardConfigConsumerRequestCheckService] = None,
        consumer_response_check_service: List[main_models.AiSecurityGuardConfigConsumerResponseCheckService] = None,
        consumer_risk_level: List[main_models.AiSecurityGuardConfigConsumerRiskLevel] = None,
        plugin_status: main_models.AiPluginStatus = None,
        request_check_service: str = None,
        request_image_check_service: str = None,
        response_check_service: str = None,
        response_image_check_service: str = None,
        risk_alert_level: str = None,
        risk_config: List[main_models.AiSecurityGuardConfigRiskConfig] = None,
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
                temp_model = main_models.AiSecurityGuardConfigConsumerRequestCheckService()
                self.consumer_request_check_service.append(temp_model.from_map(k1))

        self.consumer_response_check_service = []
        if m.get('consumerResponseCheckService') is not None:
            for k1 in m.get('consumerResponseCheckService'):
                temp_model = main_models.AiSecurityGuardConfigConsumerResponseCheckService()
                self.consumer_response_check_service.append(temp_model.from_map(k1))

        self.consumer_risk_level = []
        if m.get('consumerRiskLevel') is not None:
            for k1 in m.get('consumerRiskLevel'):
                temp_model = main_models.AiSecurityGuardConfigConsumerRiskLevel()
                self.consumer_risk_level.append(temp_model.from_map(k1))

        if m.get('pluginStatus') is not None:
            temp_model = main_models.AiPluginStatus()
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
                temp_model = main_models.AiSecurityGuardConfigRiskConfig()
                self.risk_config.append(temp_model.from_map(k1))

        if m.get('serviceAddress') is not None:
            self.service_address = m.get('serviceAddress')

        return self

class AiSecurityGuardConfigRiskConfig(DaraModel):
    def __init__(
        self,
        consumer_rules: main_models.AiSecurityGuardConfigRiskConfigConsumerRules = None,
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
            temp_model = main_models.AiSecurityGuardConfigRiskConfigConsumerRules()
            self.consumer_rules = temp_model.from_map(m.get('consumerRules'))

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class AiSecurityGuardConfigRiskConfigConsumerRules(DaraModel):
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

class AiSecurityGuardConfigConsumerRiskLevel(DaraModel):
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

class AiSecurityGuardConfigConsumerResponseCheckService(DaraModel):
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

class AiSecurityGuardConfigConsumerRequestCheckService(DaraModel):
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

