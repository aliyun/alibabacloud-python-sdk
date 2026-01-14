# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAvatarResourceRequest(DaraModel):
    def __init__(
        self,
        idempotent_id: str = None,
    ):
        self.idempotent_id = idempotent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')

        return self

