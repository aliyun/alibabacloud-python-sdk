# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDialogLogRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        session_id: str = None,
    ):
        self.id = id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

