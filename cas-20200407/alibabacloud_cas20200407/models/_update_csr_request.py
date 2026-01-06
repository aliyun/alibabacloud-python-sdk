# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCsrRequest(DaraModel):
    def __init__(
        self,
        csr_id: int = None,
        key: str = None,
    ):
        # The ID of the CSR.
        # 
        # This parameter is required.
        self.csr_id = csr_id
        # The private key content of the certificate in the PEM format.
        # 
        # This parameter is required.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csr_id is not None:
            result['CsrId'] = self.csr_id

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsrId') is not None:
            self.csr_id = m.get('CsrId')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

