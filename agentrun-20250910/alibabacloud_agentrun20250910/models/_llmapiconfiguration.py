# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class LLMAPIConfiguration(DaraModel):
    def __init__(
        self,
        ai_protocols: List[str] = None,
        attach_policy_configs: List[main_models.AttachPolicyConfig] = None,
        base_path: str = None,
        deploy_configs: List[main_models.LLMDeployConfig] = None,
        model_category: str = None,
        remove_base_path_on_forward: bool = None,
        type: str = None,
    ):
        self.ai_protocols = ai_protocols
        self.attach_policy_configs = attach_policy_configs
        self.base_path = base_path
        self.deploy_configs = deploy_configs
        self.model_category = model_category
        self.remove_base_path_on_forward = remove_base_path_on_forward
        self.type = type

    def validate(self):
        if self.attach_policy_configs:
            for v1 in self.attach_policy_configs:
                 if v1:
                    v1.validate()
        if self.deploy_configs:
            for v1 in self.deploy_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_protocols is not None:
            result['aiProtocols'] = self.ai_protocols

        result['attachPolicyConfigs'] = []
        if self.attach_policy_configs is not None:
            for k1 in self.attach_policy_configs:
                result['attachPolicyConfigs'].append(k1.to_map() if k1 else None)

        if self.base_path is not None:
            result['basePath'] = self.base_path

        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k1 in self.deploy_configs:
                result['deployConfigs'].append(k1.to_map() if k1 else None)

        if self.model_category is not None:
            result['modelCategory'] = self.model_category

        if self.remove_base_path_on_forward is not None:
            result['removeBasePathOnForward'] = self.remove_base_path_on_forward

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiProtocols') is not None:
            self.ai_protocols = m.get('aiProtocols')

        self.attach_policy_configs = []
        if m.get('attachPolicyConfigs') is not None:
            for k1 in m.get('attachPolicyConfigs'):
                temp_model = main_models.AttachPolicyConfig()
                self.attach_policy_configs.append(temp_model.from_map(k1))

        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')

        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k1 in m.get('deployConfigs'):
                temp_model = main_models.LLMDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k1))

        if m.get('modelCategory') is not None:
            self.model_category = m.get('modelCategory')

        if m.get('removeBasePathOnForward') is not None:
            self.remove_base_path_on_forward = m.get('removeBasePathOnForward')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

