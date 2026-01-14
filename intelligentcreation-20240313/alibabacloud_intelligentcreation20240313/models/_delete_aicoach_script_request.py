# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAICoachScriptRequest(DaraModel):
    def __init__(
        self,
        script_id: str = None,
    ):
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script_id is not None:
            result['scriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scriptId') is not None:
            self.script_id = m.get('scriptId')

        return self

