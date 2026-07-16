# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetTokenVaultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        token_vault: main_models.GetTokenVaultResponseBodyTokenVault = None,
    ):
        self.request_id = request_id
        self.token_vault = token_vault

    def validate(self):
        if self.token_vault:
            self.token_vault.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token_vault is not None:
            result['TokenVault'] = self.token_vault.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TokenVault') is not None:
            temp_model = main_models.GetTokenVaultResponseBodyTokenVault()
            self.token_vault = temp_model.from_map(m.get('TokenVault'))

        return self

class GetTokenVaultResponseBodyTokenVault(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        encryption_config: main_models.GetTokenVaultResponseBodyTokenVaultEncryptionConfig = None,
        role_arn: str = None,
        token_vault_arn: str = None,
        token_vault_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.encryption_config = encryption_config
        self.role_arn = role_arn
        self.token_vault_arn = token_vault_arn
        self.token_vault_name = token_vault_name
        self.update_time = update_time

    def validate(self):
        if self.encryption_config:
            self.encryption_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.encryption_config is not None:
            result['EncryptionConfig'] = self.encryption_config.to_map()

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.token_vault_arn is not None:
            result['TokenVaultArn'] = self.token_vault_arn

        if self.token_vault_name is not None:
            result['TokenVaultName'] = self.token_vault_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptionConfig') is not None:
            temp_model = main_models.GetTokenVaultResponseBodyTokenVaultEncryptionConfig()
            self.encryption_config = temp_model.from_map(m.get('EncryptionConfig'))

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('TokenVaultArn') is not None:
            self.token_vault_arn = m.get('TokenVaultArn')

        if m.get('TokenVaultName') is not None:
            self.token_vault_name = m.get('TokenVaultName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetTokenVaultResponseBodyTokenVaultEncryptionConfig(DaraModel):
    def __init__(
        self,
        key_type: str = None,
        kms_key_arn: str = None,
    ):
        self.key_type = key_type
        self.kms_key_arn = kms_key_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.kms_key_arn is not None:
            result['KmsKeyArn'] = self.kms_key_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('KmsKeyArn') is not None:
            self.kms_key_arn = m.get('KmsKeyArn')

        return self

