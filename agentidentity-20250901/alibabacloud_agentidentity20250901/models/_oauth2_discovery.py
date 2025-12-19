# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class OAuth2Discovery(DaraModel):
    def __init__(
        self,
        authorization_server_metadata: main_models.AuthorizationServerMetadata = None,
        discovery_url: str = None,
    ):
        self.authorization_server_metadata = authorization_server_metadata
        self.discovery_url = discovery_url

    def validate(self):
        if self.authorization_server_metadata:
            self.authorization_server_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_server_metadata is not None:
            result['AuthorizationServerMetadata'] = self.authorization_server_metadata.to_map()

        if self.discovery_url is not None:
            result['DiscoveryURL'] = self.discovery_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationServerMetadata') is not None:
            temp_model = main_models.AuthorizationServerMetadata()
            self.authorization_server_metadata = temp_model.from_map(m.get('AuthorizationServerMetadata'))

        if m.get('DiscoveryURL') is not None:
            self.discovery_url = m.get('DiscoveryURL')

        return self

