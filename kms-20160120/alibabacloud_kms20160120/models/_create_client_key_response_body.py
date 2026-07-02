# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClientKeyResponseBody(DaraModel):
    def __init__(
        self,
        client_key_id: str = None,
        key_algorithm: str = None,
        not_after: str = None,
        not_before: str = None,
        private_key_data: str = None,
        request_id: str = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.client_key_id = client_key_id
        # The ID of the client key.
        self.key_algorithm = key_algorithm
        # The beginning of the validity period of the client key.
        self.not_after = not_after
        # The private key of the client key.
        self.not_before = not_before
        # The algorithm that is used to encrypt the private key of the client key. Currently, only RSA_2048 is supported.
        self.private_key_data = private_key_data
        # The beginning of the validity period of the client key.
        # 
        # Specify the time in the ISO 8601 standard. The time must be in UTC. The time must be in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # > 
        # 
        # *   If you do not configure NotBefore, the default value is the time when the client key was created.
        # *   If you configure NotBefore, you must configure NotAfter.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_key_id is not None:
            result['ClientKeyId'] = self.client_key_id

        if self.key_algorithm is not None:
            result['KeyAlgorithm'] = self.key_algorithm

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.private_key_data is not None:
            result['PrivateKeyData'] = self.private_key_data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientKeyId') is not None:
            self.client_key_id = m.get('ClientKeyId')

        if m.get('KeyAlgorithm') is not None:
            self.key_algorithm = m.get('KeyAlgorithm')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('PrivateKeyData') is not None:
            self.private_key_data = m.get('PrivateKeyData')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

