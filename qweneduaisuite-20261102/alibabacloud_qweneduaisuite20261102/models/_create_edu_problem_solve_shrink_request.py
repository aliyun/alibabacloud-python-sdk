# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEduProblemSolveShrinkRequest(DaraModel):
    def __init__(
        self,
        query_shrink: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.query_shrink = query_shrink
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_shrink is not None:
            result['query'] = self.query_shrink

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query_shrink = m.get('query')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

