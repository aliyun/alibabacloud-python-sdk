# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class DecryptKMSDataKeyResponseBody(DaraModel):
    def __init__(
        self,
        data_key: main_models.DecryptKMSDataKeyResponseBodyDataKey = None,
        request_id: str = None,
    ):
        # The information about the decryption result.
        self.data_key = data_key
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_key:
            self.data_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_key is not None:
            result['DataKey'] = self.data_key.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataKey') is not None:
            temp_model = main_models.DecryptKMSDataKeyResponseBodyDataKey()
            self.data_key = temp_model.from_map(m.get('DataKey'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DecryptKMSDataKeyResponseBodyDataKey(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        plaintext: str = None,
    ):
        # The ID of the customer master key (CMK) that was used to decrypt the ciphertext.
        self.key_id = key_id
        # The plaintext that is generated after decryption.
        self.plaintext = plaintext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')

        return self

