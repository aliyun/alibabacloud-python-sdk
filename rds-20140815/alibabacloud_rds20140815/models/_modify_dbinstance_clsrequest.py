# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceCLSRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        encryption_algorithm: str = None,
        encryption_key: str = None,
        encryption_key_mode: str = None,
        encryption_status: str = None,
        is_rotate: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_arn: str = None,
        white_list_mode: bool = None,
    ):
        # Instance ID
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Encryption algorithm to use. Valid values:
        # 
        # - AES_128_CBC
        # - AES_128_GCM
        # - AES_128_CTR
        # - AES_128_ECB
        # - AES_256_CBC
        # - AES_256_GCM
        # - AES_256_CTR
        # - AES_256_ECB
        # - SM4_128_CBC
        # - SM4_128_GCM
        # - SM4_128_CTR
        # - SM4_128_ECB
        self.encryption_algorithm = encryption_algorithm
        # Encryption key ID. This parameter is required when using a KMS key.
        self.encryption_key = encryption_key
        # Column encryption key mode. Valid values:
        # 
        # - client_key (configure a randomly generated user key on the client side)
        # - kms_key (use a custom key configured via Alibaba Cloud KMS)
        # 
        # Note:
        # Once an instance is configured to use a KMS key, it can no longer use the client-side random key configuration method.
        self.encryption_key_mode = encryption_key_mode
        # Column encryption status. Valid values:
        # - 1 (Enabled)
        # - 0 (Disabled)
        # 
        # This parameter is required.
        self.encryption_status = encryption_status
        # Whether to rotate the key
        self.is_rotate = is_rotate
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Global Resource Descriptor (GRD) of the role used to specify the exact role. For more information, see RAM Role Overview.
        # 
        # Note:
        # This parameter takes effect only when the column encryption key mode is set to kms_key. If not provided, the system uses an internal default value.
        self.role_arn = role_arn
        # Whether to enable whitelist mode. true indicates that only columns in the whitelist are encrypted; false indicates that all columns are encrypted.
        self.white_list_mode = white_list_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.encryption_algorithm is not None:
            result['EncryptionAlgorithm'] = self.encryption_algorithm

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_key_mode is not None:
            result['EncryptionKeyMode'] = self.encryption_key_mode

        if self.encryption_status is not None:
            result['EncryptionStatus'] = self.encryption_status

        if self.is_rotate is not None:
            result['IsRotate'] = self.is_rotate

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.white_list_mode is not None:
            result['WhiteListMode'] = self.white_list_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EncryptionAlgorithm') is not None:
            self.encryption_algorithm = m.get('EncryptionAlgorithm')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionKeyMode') is not None:
            self.encryption_key_mode = m.get('EncryptionKeyMode')

        if m.get('EncryptionStatus') is not None:
            self.encryption_status = m.get('EncryptionStatus')

        if m.get('IsRotate') is not None:
            self.is_rotate = m.get('IsRotate')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('WhiteListMode') is not None:
            self.white_list_mode = m.get('WhiteListMode')

        return self

