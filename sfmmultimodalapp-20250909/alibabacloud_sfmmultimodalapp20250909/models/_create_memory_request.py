# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateMemoryRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_update: bool = None,
        content: str = None,
        expiration_time: int = None,
        messages_json: str = None,
        meta_data: Dict[str, str] = None,
        project_id: str = None,
        prompt: str = None,
        user_defined_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.auto_update = auto_update
        self.content = content
        self.expiration_time = expiration_time
        self.messages_json = messages_json
        self.meta_data = meta_data
        self.project_id = project_id
        self.prompt = prompt
        # This parameter is required.
        self.user_defined_id = user_defined_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auto_update is not None:
            result['AutoUpdate'] = self.auto_update

        if self.content is not None:
            result['Content'] = self.content

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.messages_json is not None:
            result['MessagesJson'] = self.messages_json

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.user_defined_id is not None:
            result['UserDefinedId'] = self.user_defined_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AutoUpdate') is not None:
            self.auto_update = m.get('AutoUpdate')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('MessagesJson') is not None:
            self.messages_json = m.get('MessagesJson')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('UserDefinedId') is not None:
            self.user_defined_id = m.get('UserDefinedId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

