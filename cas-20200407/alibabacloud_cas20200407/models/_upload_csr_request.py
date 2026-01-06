# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadCsrRequest(DaraModel):
    def __init__(
        self,
        csr: str = None,
        key: str = None,
        name: str = None,
    ):
        # The content of the CSR.
        # 
        # This parameter is required.
        self.csr = csr
        # The private key content of the certificate in the PEM format.
        self.key = key
        # The name of the CSR.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csr is not None:
            result['Csr'] = self.csr

        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

