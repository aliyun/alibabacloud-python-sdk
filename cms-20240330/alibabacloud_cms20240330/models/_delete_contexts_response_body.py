# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContextsResponseBody(DaraModel):
    def __init__(
        self,
        deleted_count: int = None,
        request_id: str = None,
    ):
        self.deleted_count = deleted_count
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted_count is not None:
            result['deletedCount'] = self.deleted_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deletedCount') is not None:
            self.deleted_count = m.get('deletedCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

