# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CloseChatInstanceSessionsRequest(DaraModel):
    def __init__(
        self,
        session_ids: List[str] = None,
    ):
        self.session_ids = session_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_ids is not None:
            result['sessionIds'] = self.session_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionIds') is not None:
            self.session_ids = m.get('sessionIds')

        return self

