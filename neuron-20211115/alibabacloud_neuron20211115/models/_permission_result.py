# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PermissionResult(DaraModel):
    def __init__(
        self,
        allow: bool = None,
        request_id: str = None,
    ):
        self.allow = allow
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow is not None:
            result['allow'] = self.allow

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allow') is not None:
            self.allow = m.get('allow')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

