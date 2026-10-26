# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopAgentConversationResponseBody(DaraModel):
    def __init__(
        self,
        stopped: bool = None,
    ):
        self.stopped = stopped

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stopped is not None:
            result['stopped'] = self.stopped

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')

        return self

