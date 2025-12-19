# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class CustomOAuth2ProviderConfig(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        oauth2_discovery: main_models.OAuth2Discovery = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth2_discovery = oauth2_discovery

    def validate(self):
        if self.oauth2_discovery:
            self.oauth2_discovery.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.oauth2_discovery is not None:
            result['OAuth2Discovery'] = self.oauth2_discovery.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('OAuth2Discovery') is not None:
            temp_model = main_models.OAuth2Discovery()
            self.oauth2_discovery = temp_model.from_map(m.get('OAuth2Discovery'))

        return self

