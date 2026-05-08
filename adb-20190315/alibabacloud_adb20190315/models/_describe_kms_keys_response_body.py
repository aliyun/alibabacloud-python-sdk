# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeKmsKeysResponseBody(DaraModel):
    def __init__(
        self,
        kms_keys: main_models.DescribeKmsKeysResponseBodyKmsKeys = None,
        request_id: str = None,
    ):
        self.kms_keys = kms_keys
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.kms_keys:
            self.kms_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kms_keys is not None:
            result['KmsKeys'] = self.kms_keys.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KmsKeys') is not None:
            temp_model = main_models.DescribeKmsKeysResponseBodyKmsKeys()
            self.kms_keys = temp_model.from_map(m.get('KmsKeys'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeKmsKeysResponseBodyKmsKeys(DaraModel):
    def __init__(
        self,
        kms_key: List[main_models.DescribeKmsKeysResponseBodyKmsKeysKmsKey] = None,
    ):
        self.kms_key = kms_key

    def validate(self):
        if self.kms_key:
            for v1 in self.kms_key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KmsKey'] = []
        if self.kms_key is not None:
            for k1 in self.kms_key:
                result['KmsKey'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kms_key = []
        if m.get('KmsKey') is not None:
            for k1 in m.get('KmsKey'):
                temp_model = main_models.DescribeKmsKeysResponseBodyKmsKeysKmsKey()
                self.kms_key.append(temp_model.from_map(k1))

        return self

class DescribeKmsKeysResponseBodyKmsKeysKmsKey(DaraModel):
    def __init__(
        self,
        key_alias: str = None,
        key_id: str = None,
    ):
        self.key_alias = key_alias
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

