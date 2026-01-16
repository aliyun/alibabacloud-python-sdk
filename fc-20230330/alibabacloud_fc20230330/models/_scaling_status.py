# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScalingStatus(DaraModel):
    def __init__(
        self,
        current_error: str = None,
        resource_count: int = None,
    ):
        self.current_error = current_error
        self.resource_count = resource_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_error is not None:
            result['currentError'] = self.current_error

        if self.resource_count is not None:
            result['resourceCount'] = self.resource_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')

        if m.get('resourceCount') is not None:
            self.resource_count = m.get('resourceCount')

        return self

