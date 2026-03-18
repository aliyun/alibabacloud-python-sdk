# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteProjectRequest(DaraModel):
    def __init__(
        self,
        is_logical: bool = None,
    ):
        # Specifies whether to perform a logical deletion. The default value is true. A value of false indicates a physical deletion.
        self.is_logical = is_logical

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_logical is not None:
            result['isLogical'] = self.is_logical

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isLogical') is not None:
            self.is_logical = m.get('isLogical')

        return self

