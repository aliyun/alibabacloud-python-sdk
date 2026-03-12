# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrayPublishRequest(DaraModel):
    def __init__(
        self,
        x_request_change_id: str = None,
    ):
        self.x_request_change_id = x_request_change_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_request_change_id is not None:
            result['X-Request-ChangeId'] = self.x_request_change_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Request-ChangeId') is not None:
            self.x_request_change_id = m.get('X-Request-ChangeId')

        return self

