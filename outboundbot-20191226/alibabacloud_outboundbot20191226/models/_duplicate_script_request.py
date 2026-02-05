# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DuplicateScriptRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        source_script_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.source_script_id = source_script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.source_script_id is not None:
            result['SourceScriptId'] = self.source_script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourceScriptId') is not None:
            self.source_script_id = m.get('SourceScriptId')

        return self

