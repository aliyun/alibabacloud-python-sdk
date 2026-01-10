# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateModelServiceInput(DaraModel):
    def __init__(
        self,
        credential_name: str = None,
        description: str = None,
        model_info_configs: List[main_models.ModelInfoConfig] = None,
        model_service_name: str = None,
        model_type: str = None,
        network_configuration: main_models.NetworkConfiguration = None,
        provider: str = None,
        provider_settings: main_models.ProviderSettings = None,
    ):
        self.credential_name = credential_name
        self.description = description
        self.model_info_configs = model_info_configs
        # This parameter is required.
        self.model_service_name = model_service_name
        # This parameter is required.
        self.model_type = model_type
        self.network_configuration = network_configuration
        # This parameter is required.
        self.provider = provider
        # This parameter is required.
        self.provider_settings = provider_settings

    def validate(self):
        if self.model_info_configs:
            for v1 in self.model_info_configs:
                 if v1:
                    v1.validate()
        if self.network_configuration:
            self.network_configuration.validate()
        if self.provider_settings:
            self.provider_settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.description is not None:
            result['description'] = self.description

        result['modelInfoConfigs'] = []
        if self.model_info_configs is not None:
            for k1 in self.model_info_configs:
                result['modelInfoConfigs'].append(k1.to_map() if k1 else None)

        if self.model_service_name is not None:
            result['modelServiceName'] = self.model_service_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.provider is not None:
            result['provider'] = self.provider

        if self.provider_settings is not None:
            result['providerSettings'] = self.provider_settings.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.model_info_configs = []
        if m.get('modelInfoConfigs') is not None:
            for k1 in m.get('modelInfoConfigs'):
                temp_model = main_models.ModelInfoConfig()
                self.model_info_configs.append(temp_model.from_map(k1))

        if m.get('modelServiceName') is not None:
            self.model_service_name = m.get('modelServiceName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('providerSettings') is not None:
            temp_model = main_models.ProviderSettings()
            self.provider_settings = temp_model.from_map(m.get('providerSettings'))

        return self

