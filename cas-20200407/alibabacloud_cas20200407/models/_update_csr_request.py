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
        # The unique identifier of the CSR. The CsrId is generated when you upload the CSR. You can obtain this value by querying the CSR list. For more information, see [ListCsr](https://help.aliyun.com/document_detail/2709717.html).
        # 
        # This parameter is required.
        self.csr_id = csr_id
        # The certificate private key content in PEM format. This private key must match the public key cryptography contained in the CSR referenced by CsrId. Otherwise, the API returns the NotMatch.CsrAndPrivateKey error.
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

