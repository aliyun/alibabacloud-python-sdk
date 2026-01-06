# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCsrDetailResponseBody(DaraModel):
    def __init__(
        self,
        csr: str = None,
        private_key: str = None,
        request_id: str = None,
    ):
        # The content of the CSR.
        self.csr = csr
        # The private key. Specify a Base64-encoded string.
        self.private_key = private_key
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csr is not None:
            result['Csr'] = self.csr

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

