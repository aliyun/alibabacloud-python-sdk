# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSortScriptRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        scope: str = None,
        script_name: str = None,
        type: str = None,
    ):
        self.description = description
        # The sort phase to which the script applies.
        self.scope = scope
        # The script name.
        self.script_name = script_name
        # The script type. Set the value to cava_script.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.scope is not None:
            result['scope'] = self.scope

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

