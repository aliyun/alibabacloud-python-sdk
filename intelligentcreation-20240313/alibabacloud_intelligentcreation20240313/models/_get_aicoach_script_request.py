# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAICoachScriptRequest(DaraModel):
    def __init__(
        self,
        script_record_id: str = None,
    ):
        self.script_record_id = script_record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        return self

