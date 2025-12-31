# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCertificatePrivateKeyResponseBody(DaraModel):
    def __init__(
        self,
        encrypted_data: str = None,
        request_id: str = None,
    ):
        # The content of the encrypted private key.
        self.encrypted_data = encrypted_data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted_data is not None:
            result['EncryptedData'] = self.encrypted_data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedData') is not None:
            self.encrypted_data = m.get('EncryptedData')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

