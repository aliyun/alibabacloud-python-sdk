# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ModelConnection(DaraModel):
    def __init__(
        self,
        consumer_api_keys: List[main_models.ModelConnectionConsumerAPIKey] = None,
        created_at: str = None,
        description: str = None,
        last_updated_at: str = None,
        model_connection_id: str = None,
        model_connection_name: str = None,
        model_info_configs: List[main_models.ModelInfoConfig] = None,
        provider: str = None,
        provider_settings: main_models.ModelConnectionProviderSettings = None,
        workspace_id: str = None,
    ):
        # A list of consumer API keys bound to this model connection.
        self.consumer_api_keys = consumer_api_keys
        # The time the model connection was created, in ISO 8601 format.
        self.created_at = created_at
        # A description of the model connection.
        self.description = description
        # The time the model connection was last updated, in ISO 8601 format.
        self.last_updated_at = last_updated_at
        # The model connection\\"s unique identifier.
        self.model_connection_id = model_connection_id
        # A unique name identifying the model connection.
        self.model_connection_name = model_connection_name
        # A list of model metadata configurations. Each configuration includes the features and parameter rules for a specific model.
        self.model_info_configs = model_info_configs
        # The model provider\\"s name.
        self.provider = provider
        # The settings for the model provider.
        self.provider_settings = provider_settings
        # The identifier of the workspace containing the model connection.
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

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.model_connection_id is not None:
            result['modelConnectionId'] = self.model_connection_id

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
                temp_model = main_models.ModelConnectionConsumerAPIKey()
                self.consumer_api_keys.append(temp_model.from_map(k1))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('modelConnectionId') is not None:
            self.model_connection_id = m.get('modelConnectionId')

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

