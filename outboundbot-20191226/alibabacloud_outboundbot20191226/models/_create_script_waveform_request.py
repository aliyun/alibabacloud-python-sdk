# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScriptWaveformRequest(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        instance_id: str = None,
        script_content: str = None,
        script_id: str = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.script_content = script_content
        # This parameter is required.
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_content is not None:
            result['ScriptContent'] = self.script_content

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

