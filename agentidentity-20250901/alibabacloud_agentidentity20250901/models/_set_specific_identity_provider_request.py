# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSpecificIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        idpmetadata: str = None,
        identity_provider_type: str = None,
        ssostatus: str = None,
        user_pool_name: str = None,
    ):
        # The IdP metadata. For the DingTalk type, the metadata is in JSON format and includes fields such as corpId, appKey, appSecret, encryptKey, verificationToken, and syncCallbackStatus.
        self.idpmetadata = idpmetadata
        # The type of the identity provider. Currently, only DingTalk is supported.
        self.identity_provider_type = identity_provider_type
        # The SSO enabling status. Valid values:
        # - Enabled: Enabled.
        # - Disabled: Disabled.
        self.ssostatus = ssostatus
        # The name of the user pool.
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idpmetadata is not None:
            result['IDPMetadata'] = self.idpmetadata

        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.ssostatus is not None:
            result['SSOStatus'] = self.ssostatus

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IDPMetadata') is not None:
            self.idpmetadata = m.get('IDPMetadata')

        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('SSOStatus') is not None:
            self.ssostatus = m.get('SSOStatus')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

