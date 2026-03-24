# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLgfResponseBody(DaraModel):
    def __init__(
        self,
        lgf_id: int = None,
        request_id: str = None,
    ):
        # LGF ID
        self.lgf_id = lgf_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

