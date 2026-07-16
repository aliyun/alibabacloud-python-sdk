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
        # The language of the generated script.
        # Recommended values:
        # 
        # zh-CN: Chinese
        # 
        # en-US: English
        # 
        # The default is Chinese.
        self.language = language
        # The prompt for the video script.
        # 
        # This parameter is required.
        self.prompt = prompt
        # The length of the script. Valid values:
        # 
        # 20\\~75: 10 to 15 seconds of normal speaking time.
        # 
        # 75\\~150: 15 to 30 seconds of normal speaking time.
        # 
        # 150\\~300: Approximately 30 to 60 seconds of normal speaking time.
        # 
        # \\>=300: 60 seconds or more of normal speaking time.
        self.script_length = script_length
        # The number of scripts to generate. The default is 1. You can generate a maximum of three scripts at a time.
        # If you specify multiple scripts, the results are returned in parallel streams. The client distinguishes between the streams using different session IDs.
        self.script_number = script_number
        # Specifies whether to use an internet search. If you set this to true, the system performs intention recognition and then searches the internet for relevant reference materials.
        self.use_search = use_search
        # The unique ID of the Alibaba Cloud Model Studio workspace. For more information, see [Get a Workspace ID](https://help.aliyun.com/document_detail/2782167.html).
        # 
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

