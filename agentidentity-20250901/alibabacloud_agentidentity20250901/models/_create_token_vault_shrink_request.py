# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTokenVaultShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        encryption_config_shrink: str = None,
        role_arn: str = None,
        token_vault_name: str = None,
    ):
        self.description = description
        self.encryption_config_shrink = encryption_config_shrink
        self.role_arn = role_arn
        self.token_vault_name = token_vault_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.encryption_config_shrink is not None:
            result['EncryptionConfig'] = self.encryption_config_shrink

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.token_vault_name is not None:
            result['TokenVaultName'] = self.token_vault_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptionConfig') is not None:
            self.encryption_config_shrink = m.get('EncryptionConfig')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('TokenVaultName') is not None:
            self.token_vault_name = m.get('TokenVaultName')

        return self

