# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EncryptionConfig(DaraModel):
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

