# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunClusterCheckResponseBody(DaraModel):
    def __init__(
        self,
        check_id: str = None,
        request_id: str = None,
    ):
        # The ID of the cluster check task.
        self.check_id = check_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['check_id'] = self.check_id

        if self.request_id is not None:
            result['request_id'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_id') is not None:
            self.check_id = m.get('check_id')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        return self

