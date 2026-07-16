# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        identity_provider_type: str = None,
        idp_metadata: str = None,
        instance_id: str = None,
        login_enabled: bool = None,
        sync_enabled: bool = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.identity_provider_type = identity_provider_type
        self.idp_metadata = idp_metadata
        # This parameter is required.
        self.instance_id = instance_id
        self.login_enabled = login_enabled
        self.sync_enabled = sync_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.idp_metadata is not None:
            result['IdpMetadata'] = self.idp_metadata

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_enabled is not None:
            result['LoginEnabled'] = self.login_enabled

        if self.sync_enabled is not None:
            result['SyncEnabled'] = self.sync_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('IdpMetadata') is not None:
            self.idp_metadata = m.get('IdpMetadata')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginEnabled') is not None:
            self.login_enabled = m.get('LoginEnabled')

        if m.get('SyncEnabled') is not None:
            self.sync_enabled = m.get('SyncEnabled')

        return self

