# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceCLSResponseBody(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        encryption_key: str = None,
        encryption_key_mode: str = None,
        request_id: str = None,
        white_list_mode: bool = None,
    ):
        # The encryption algorithm. Valid values:
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
        self.algorithm = algorithm
        # The custom KMS master key ID.
        # 
        # >  This parameter takes effect only when the column encryption key pattern is set to kms_key. If this parameter is not specified, the current column encryption key settings of the database remain unchanged.
        self.encryption_key = encryption_key
        # The column encryption key mode. Valid values:
        # 
        # - client_key: configures a user-generated random key on the client side.
        # - kms_key: configures a custom key by using Alibaba Cloud Key Management Service (KMS).
        # 
        # >  After an instance is configured to use KMS for key management, you can no longer switch back to the client-side random key mode.
        self.encryption_key_mode = encryption_key_mode
        # The request ID.
        self.request_id = request_id
        # Indicates whether the whitelist mode is enabled.
        self.white_list_mode = white_list_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_key_mode is not None:
            result['EncryptionKeyMode'] = self.encryption_key_mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.white_list_mode is not None:
            result['WhiteListMode'] = self.white_list_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionKeyMode') is not None:
            self.encryption_key_mode = m.get('EncryptionKeyMode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WhiteListMode') is not None:
            self.white_list_mode = m.get('WhiteListMode')

        return self

