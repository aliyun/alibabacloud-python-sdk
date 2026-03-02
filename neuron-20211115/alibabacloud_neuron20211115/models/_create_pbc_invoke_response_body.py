# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePbcInvokeResponseBody(DaraModel):
    def __init__(
        self,
        pbc_invoke_id: int = None,
        request_id: str = None,
    ):
        self.pbc_invoke_id = pbc_invoke_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pbc_invoke_id is not None:
            result['pbcInvokeId'] = self.pbc_invoke_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pbcInvokeId') is not None:
            self.pbc_invoke_id = m.get('pbcInvokeId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

