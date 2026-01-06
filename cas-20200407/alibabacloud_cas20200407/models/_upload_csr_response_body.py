# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadCsrResponseBody(DaraModel):
    def __init__(
        self,
        csr_id: int = None,
        request_id: str = None,
    ):
        # The ID of the CSR.
        self.csr_id = csr_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csr_id is not None:
            result['CsrId'] = self.csr_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsrId') is not None:
            self.csr_id = m.get('CsrId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

