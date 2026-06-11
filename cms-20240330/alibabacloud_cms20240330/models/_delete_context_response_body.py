# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContextResponseBody(DaraModel):
    def __init__(
        self,
        context_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The unique identifier of the deleted context.
        self.context_id = context_id
        # The request ID.
        self.request_id = request_id
        # The deletion status. For example, deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_id is not None:
            result['contextId'] = self.context_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contextId') is not None:
            self.context_id = m.get('contextId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

