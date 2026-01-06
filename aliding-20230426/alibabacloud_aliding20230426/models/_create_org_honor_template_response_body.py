# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrgHonorTemplateResponseBody(DaraModel):
    def __init__(
        self,
        honor_id: str = None,
        request_id: str = None,
    ):
        self.honor_id = honor_id
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.honor_id is not None:
            result['honorId'] = self.honor_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('honorId') is not None:
            self.honor_id = m.get('honorId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

