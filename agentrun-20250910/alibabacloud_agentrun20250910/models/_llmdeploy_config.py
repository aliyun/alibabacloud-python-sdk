# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class LLMDeployConfig(DaraModel):
    def __init__(
        self,
        auto_deploy: bool = None,
        backend_scene: str = None,
        custom_domain_ids: List[str] = None,
        gateway_type: str = None,
        policy_configs: List[main_models.PolicyConfig] = None,
        service_configs: List[main_models.TargetServiceConfig] = None,
    ):
        self.auto_deploy = auto_deploy
        self.backend_scene = backend_scene
        self.custom_domain_ids = custom_domain_ids
        self.gateway_type = gateway_type
        self.policy_configs = policy_configs
        self.service_configs = service_configs

    def validate(self):
        if self.policy_configs:
            for v1 in self.policy_configs:
                 if v1:
                    v1.validate()
        if self.service_configs:
            for v1 in self.service_configs:
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

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        result['policyConfigs'] = []
        if self.policy_configs is not None:
            for k1 in self.policy_configs:
                result['policyConfigs'].append(k1.to_map() if k1 else None)

        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k1 in self.service_configs:
                result['serviceConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')

        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')

        if m.get('customDomainIds') is not None:
            self.custom_domain_ids = m.get('customDomainIds')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        self.policy_configs = []
        if m.get('policyConfigs') is not None:
            for k1 in m.get('policyConfigs'):
                temp_model = main_models.PolicyConfig()
                self.policy_configs.append(temp_model.from_map(k1))

        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k1 in m.get('serviceConfigs'):
                temp_model = main_models.TargetServiceConfig()
                self.service_configs.append(temp_model.from_map(k1))

        return self

