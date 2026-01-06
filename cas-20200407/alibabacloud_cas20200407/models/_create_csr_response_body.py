# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCsrResponseBody(DaraModel):
    def __init__(
        self,
        csr: str = None,
        csr_id: int = None,
        request_id: str = None,
    ):
        # The content of the CSR.
        self.csr = csr
        # The unique identifier of the CSR. You can use this value to obtain the content of the CSR. For more information about the operation that you can call to obtain the content of a CSR, see [GetCsrDetail](https://help.aliyun.com/document_detail/2709720.html).
        self.csr_id = csr_id
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

        if self.csr_id is not None:
            result['CsrId'] = self.csr_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('CsrId') is not None:
            self.csr_id = m.get('CsrId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

