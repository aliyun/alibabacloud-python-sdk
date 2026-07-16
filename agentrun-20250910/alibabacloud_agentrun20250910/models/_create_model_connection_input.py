# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateModelConnectionInput(DaraModel):
    def __init__(
        self,
        consumer_api_keys: List[main_models.CreateModelConnectionInputConsumerApiKeys] = None,
        description: str = None,
        model_connection_name: str = None,
        model_info_configs: List[main_models.ModelInfoConfig] = None,
        provider: str = None,
        provider_settings: main_models.ModelConnectionProviderSettings = None,
        workspace_id: str = None,
    ):
        # A list of consumer API keys for the model connection. If this list is empty, the connection enters open mode.
        self.consumer_api_keys = consumer_api_keys
        # A description of the model connection.
        self.description = description
        # A unique name for the model connection.
        # 
        # This parameter is required.
        self.model_connection_name = model_connection_name
        # A list of model metadata configurations.
        self.model_info_configs = model_info_configs
        # The model provider name.
        # 
        # This parameter is required.
        self.provider = provider
        # Configuration settings for the model provider, such as the base URL and a list of models.
        # 
        # This parameter is required.
        self.provider_settings = provider_settings
        # The ID of the workspace containing the model connection.
        self.workspace_id = workspace_id

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

        if self.model_connection_name is not None:
            result['modelConnectionName'] = self.model_connection_name

        result['modelInfoConfigs'] = []
        if self.model_info_configs is not None:
            for k1 in self.model_info_configs:
                result['modelInfoConfigs'].append(k1.to_map() if k1 else None)

        if self.provider is not None:
            result['provider'] = self.provider

        if self.provider_settings is not None:
            result['providerSettings'] = self.provider_settings.to_map()

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumer_api_keys = []
        if m.get('consumerApiKeys') is not None:
            for k1 in m.get('consumerApiKeys'):
                temp_model = main_models.CreateModelConnectionInputConsumerApiKeys()
                self.consumer_api_keys.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('modelConnectionName') is not None:
            self.model_connection_name = m.get('modelConnectionName')

        self.model_info_configs = []
        if m.get('modelInfoConfigs') is not None:
            for k1 in m.get('modelInfoConfigs'):
                temp_model = main_models.ModelInfoConfig()
                self.model_info_configs.append(temp_model.from_map(k1))

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('providerSettings') is not None:
            temp_model = main_models.ModelConnectionProviderSettings()
            self.provider_settings = temp_model.from_map(m.get('providerSettings'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateModelConnectionInputConsumerApiKeys(DaraModel):
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

