# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateModelConnectionInput(DaraModel):
    def __init__(
        self,
        consumer_api_keys: List[main_models.UpdateModelConnectionInputConsumerApiKeys] = None,
        description: str = None,
        model_info_configs: List[main_models.ModelInfoConfig] = None,
        provider_settings: main_models.ModelConnectionProviderSettings = None,
    ):
        # 更新绑定的消费者API密钥列表
        self.consumer_api_keys = consumer_api_keys
        # 更新后的描述信息
        self.description = description
        # 更新后的模型元数据配置列表
        self.model_info_configs = model_info_configs
        # 更新后的模型提供商配置信息
        self.provider_settings = provider_settings

    def validate(self):
        if self.consumer_api_keys:
            for v1 in self.consumer_api_keys:
                 if v1:
                    v1.validate()
        if self.model_info_configs:
            for v1 in self.model_info_configs:
                 if v1:
                    v1.validate()
        if self.provider_settings:
            self.provider_settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['consumerApiKeys'] = []
        if self.consumer_api_keys is not None:
            for k1 in self.consumer_api_keys:
                result['consumerApiKeys'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        result['modelInfoConfigs'] = []
        if self.model_info_configs is not None:
            for k1 in self.model_info_configs:
                result['modelInfoConfigs'].append(k1.to_map() if k1 else None)

        if self.provider_settings is not None:
            result['providerSettings'] = self.provider_settings.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumer_api_keys = []
        if m.get('consumerApiKeys') is not None:
            for k1 in m.get('consumerApiKeys'):
                temp_model = main_models.UpdateModelConnectionInputConsumerApiKeys()
                self.consumer_api_keys.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        self.model_info_configs = []
        if m.get('modelInfoConfigs') is not None:
            for k1 in m.get('modelInfoConfigs'):
                temp_model = main_models.ModelInfoConfig()
                self.model_info_configs.append(temp_model.from_map(k1))

        if m.get('providerSettings') is not None:
            temp_model = main_models.ModelConnectionProviderSettings()
            self.provider_settings = temp_model.from_map(m.get('providerSettings'))

        return self

class UpdateModelConnectionInputConsumerApiKeys(DaraModel):
    def __init__(
        self,
        api_key_id: str = None,
        value: str = None,
    ):
        self.api_key_id = api_key_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyId') is not None:
            self.api_key_id = m.get('apiKeyId')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

