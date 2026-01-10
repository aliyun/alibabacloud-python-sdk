# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateModelServiceInput(DaraModel):
    def __init__(
        self,
        credential_name: str = None,
        description: str = None,
        model_info_configs: List[main_models.ModelInfoConfig] = None,
        network_configuration: main_models.NetworkConfiguration = None,
        provider_settings: main_models.ProviderSettings = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.credential_name = credential_name
        self.description = description
        self.model_info_configs = model_info_configs
        self.network_configuration = network_configuration
        self.provider_settings = provider_settings
        self.status = status
        self.status_reason = status_reason

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

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.provider_settings is not None:
            result['providerSettings'] = self.provider_settings.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

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

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('providerSettings') is not None:
            temp_model = main_models.ProviderSettings()
            self.provider_settings = temp_model.from_map(m.get('providerSettings'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        return self

