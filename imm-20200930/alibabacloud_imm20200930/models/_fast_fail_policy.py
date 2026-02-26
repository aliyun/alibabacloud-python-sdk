# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FastFailPolicy(DaraModel):
    def __init__(
        self,
        action: str = None,
    ):
        # The action when the batch processor or trigger encounters an error.
        # 
        # Enumerated values:
        # 
        # *   abort: stops running.
        # *   ignore: ignores the error and keeps running.
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        return self

