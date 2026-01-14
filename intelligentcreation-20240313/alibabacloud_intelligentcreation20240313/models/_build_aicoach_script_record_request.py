# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BuildAICoachScriptRecordRequest(DaraModel):
    def __init__(
        self,
        script_json_url: str = None,
    ):
        self.script_json_url = script_json_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script_json_url is not None:
            result['scriptJsonUrl'] = self.script_json_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scriptJsonUrl') is not None:
            self.script_json_url = m.get('scriptJsonUrl')

        return self

