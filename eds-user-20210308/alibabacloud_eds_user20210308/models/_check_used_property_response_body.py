# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckUsedPropertyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        use_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The number of convenience users that are associated with the property.
        self.use_count = use_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.use_count is not None:
            result['UseCount'] = self.use_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')

        return self

