# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateCredentialInput(DaraModel):
    def __init__(
        self,
        credential_public_config: main_models.CredentialPublicConfig = None,
        credential_secret: str = None,
        description: str = None,
        enabled: bool = None,
    ):
        self.credential_public_config = credential_public_config
        self.credential_secret = credential_secret
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
        if self.credential_public_config is not None:
            result['credentialPublicConfig'] = self.credential_public_config.to_map()

        if self.credential_secret is not None:
            result['credentialSecret'] = self.credential_secret

        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialPublicConfig') is not None:
            temp_model = main_models.CredentialPublicConfig()
            self.credential_public_config = temp_model.from_map(m.get('credentialPublicConfig'))

        if m.get('credentialSecret') is not None:
            self.credential_secret = m.get('credentialSecret')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

