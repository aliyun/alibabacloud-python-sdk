# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateMacRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        dry_run: str = None,
        key_id: str = None,
        message: str = None,
    ):
        # The algorithm that is used to generate the message authentication code. Valid values vary based on the key specification:  
        # 
        # - HMAC_SM3
        # 
        # - HMAC_SHA_224
        # 
        # - HMAC_SHA_256
        # 
        # - HMAC_SHA_384
        # 
        # - HMAC_SHA_512
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # Specifies whether to enable DryRun mode.
        # 
        # - true: enabled
        # - false (default): disabled
        # 
        # DryRun mode is used to test API calls and verify whether you have the required permissions on the corresponding resources and whether the request parameters are correctly configured. When DryRun mode is enabled, KMS always returns a failure and provides the failure reason. Failure reasons include:
        # 
        # - DryRunOperationError: The request would succeed without the DryRun parameter.
        # - ValidationError: The parameters specified in the request are invalid.
        # - AccessDeniedError: You are not authorized to perform this operation on the KMS resource.
        self.dry_run = dry_run
        # The ID of the key. You can also specify a key alias or a key Amazon Resource Name (ARN). For more information about aliases, refer to [Manage key aliases](https://help.aliyun.com/document_detail/480655.html).
        # >When you access a key that belongs to a different Alibaba Cloud account, you must specify the key ARN. The format of a key ARN is `acs:kms:${region}:${account}:key/${keyid}`.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The data for which you want to generate a message authentication code.  
        # 
        # The value is Base64-encoded. For example, if the hexadecimal data is `[0x31, 0x32, 0x33, 0x34]`, the corresponding Base64-encoded value is `MTIzNA==`.
        # 
        # This parameter is required.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

