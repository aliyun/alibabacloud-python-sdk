# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSessionRequest(DaraModel):
    def __init__(
        self,
        qualifier: str = None,
    ):
        # The function alias or version associated with the session to be deleted.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        return self

