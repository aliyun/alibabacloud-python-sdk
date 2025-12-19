# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class OAuth2ProviderConfig(DaraModel):
    def __init__(
        self,
        custom_oauth2_provider_config: main_models.CustomOAuth2ProviderConfig = None,
        included_oauth2_provider_config: main_models.IncludedOAuth2ProviderConfig = None,
    ):
        self.custom_oauth2_provider_config = custom_oauth2_provider_config
        self.included_oauth2_provider_config = included_oauth2_provider_config

    def validate(self):
        if self.custom_oauth2_provider_config:
            self.custom_oauth2_provider_config.validate()
        if self.included_oauth2_provider_config:
            self.included_oauth2_provider_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_oauth2_provider_config is not None:
            result['CustomOAuth2ProviderConfig'] = self.custom_oauth2_provider_config.to_map()

        if self.included_oauth2_provider_config is not None:
            result['IncludedOAuth2ProviderConfig'] = self.included_oauth2_provider_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomOAuth2ProviderConfig') is not None:
            temp_model = main_models.CustomOAuth2ProviderConfig()
            self.custom_oauth2_provider_config = temp_model.from_map(m.get('CustomOAuth2ProviderConfig'))

        if m.get('IncludedOAuth2ProviderConfig') is not None:
            temp_model = main_models.IncludedOAuth2ProviderConfig()
            self.included_oauth2_provider_config = temp_model.from_map(m.get('IncludedOAuth2ProviderConfig'))

        return self

