# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyCatalogKmsResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        hint: str = None,
        kms_key_id: str = None,
        server_side_encryption: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.hint = hint
        self.kms_key_id = kms_key_id
        self.server_side_encryption = server_side_encryption
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.hint is not None:
            result['hint'] = self.hint

        if self.kms_key_id is not None:
            result['kmsKeyId'] = self.kms_key_id

        if self.server_side_encryption is not None:
            result['serverSideEncryption'] = self.server_side_encryption

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('hint') is not None:
            self.hint = m.get('hint')

        if m.get('kmsKeyId') is not None:
            self.kms_key_id = m.get('kmsKeyId')

        if m.get('serverSideEncryption') is not None:
            self.server_side_encryption = m.get('serverSideEncryption')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

