# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateCredentialInput(DaraModel):
    def __init__(
        self,
        credential_auth_type: str = None,
        credential_name: str = None,
        credential_public_config: main_models.CredentialPublicConfig = None,
        credential_secret: str = None,
        credential_source_type: str = None,
        description: str = None,
        enabled: bool = None,
    ):
        # This parameter is required.
        self.credential_auth_type = credential_auth_type
        # This parameter is required.
        self.credential_name = credential_name
        self.credential_public_config = credential_public_config
        self.credential_secret = credential_secret
        # This parameter is required.
        self.credential_source_type = credential_source_type
        self.description = description
        self.enabled = enabled

    def validate(self):
        if self.credential_public_config:
            self.credential_public_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_auth_type is not None:
            result['credentialAuthType'] = self.credential_auth_type

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.credential_public_config is not None:
            result['credentialPublicConfig'] = self.credential_public_config.to_map()

        if self.credential_secret is not None:
            result['credentialSecret'] = self.credential_secret

        if self.credential_source_type is not None:
            result['credentialSourceType'] = self.credential_source_type

        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialAuthType') is not None:
            self.credential_auth_type = m.get('credentialAuthType')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('credentialPublicConfig') is not None:
            temp_model = main_models.CredentialPublicConfig()
            self.credential_public_config = temp_model.from_map(m.get('credentialPublicConfig'))

        if m.get('credentialSecret') is not None:
            self.credential_secret = m.get('credentialSecret')

        if m.get('credentialSourceType') is not None:
            self.credential_source_type = m.get('credentialSourceType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

