# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunVideoScriptGenerateRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        prompt: str = None,
        script_length: str = None,
        script_number: int = None,
        use_search: bool = None,
        workspace_id: str = None,
    ):
        self.language = language
        # This parameter is required.
        self.prompt = prompt
        self.script_length = script_length
        self.script_number = script_number
        self.use_search = use_search
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.script_length is not None:
            result['ScriptLength'] = self.script_length

        if self.script_number is not None:
            result['ScriptNumber'] = self.script_number

        if self.use_search is not None:
            result['UseSearch'] = self.use_search

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('ScriptLength') is not None:
            self.script_length = m.get('ScriptLength')

        if m.get('ScriptNumber') is not None:
            self.script_number = m.get('ScriptNumber')

        if m.get('UseSearch') is not None:
            self.use_search = m.get('UseSearch')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

