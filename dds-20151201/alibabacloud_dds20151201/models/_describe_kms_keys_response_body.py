# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeKmsKeysResponseBody(DaraModel):
    def __init__(
        self,
        kms_keys: List[main_models.DescribeKmsKeysResponseBodyKmsKeys] = None,
        request_id: str = None,
    ):
        # The KMS keys.
        self.kms_keys = kms_keys
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.kms_keys:
            for v1 in self.kms_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KmsKeys'] = []
        if self.kms_keys is not None:
            for k1 in self.kms_keys:
                result['KmsKeys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kms_keys = []
        if m.get('KmsKeys') is not None:
            for k1 in m.get('KmsKeys'):
                temp_model = main_models.DescribeKmsKeysResponseBodyKmsKeys()
                self.kms_keys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeKmsKeysResponseBodyKmsKeys(DaraModel):
    def __init__(
        self,
        key_alias: str = None,
        key_id: str = None,
    ):
        # The alias of the key.
        self.key_alias = key_alias
        # The key ID.
        self.key_id = key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_alias is not None:
            result['KeyAlias'] = self.key_alias

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyAlias') is not None:
            self.key_alias = m.get('KeyAlias')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        return self

