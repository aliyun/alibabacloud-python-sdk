# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKMSEncryptionRequest(DaraModel):
    def __init__(
        self,
        disable_encryption: bool = None,
        kms_key_id: str = None,
    ):
        # Specifies whether to disable the Secret encryption at rest feature.
        # 
        # * `true`: Disables the encryption at rest feature.
        # * `false`: Enables the encryption at rest feature.
        self.disable_encryption = disable_encryption
        # The key ID of the KMS key used by the Secret encryption at rest feature.
        # 
        # >Notice: You cannot use a service key. Use only a master key or a customer master key (CMK). The key type must be `Aliyun_AES_256`, and the key usage must be `ENCRYPT/DECRYPT`.
        # 
        # 
        # 
        # 
        # >Warning: During the procedure of enabling or shutdown of encryption at rest and after the feature is enabled, do not disable or delete the KMS key in the KMS console or through OpenAPI. Otherwise, the cluster API Server becomes not active, which prevents normal retrieval of objects such as Secrets and ServiceAccounts and affects the normal operation of business applications.
        self.kms_key_id = kms_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_encryption is not None:
            result['disable_encryption'] = self.disable_encryption

        if self.kms_key_id is not None:
            result['kms_key_id'] = self.kms_key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disable_encryption') is not None:
            self.disable_encryption = m.get('disable_encryption')

        if m.get('kms_key_id') is not None:
            self.kms_key_id = m.get('kms_key_id')

        return self

