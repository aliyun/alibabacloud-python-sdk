# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAgentJobRequest(DaraModel):
    def __init__(
        self,
        model: str = None,
        notify_url: str = None,
        prompt: str = None,
        skill: str = None,
        user_data: str = None,
        workspace_id: str = None,
    ):
        # The large language model (LLM) used to execute the agent task.
        self.model = model
        # The callback URL. Currently, only HTTP and HTTPS addresses are supported.
        self.notify_url = notify_url
        # The prompt. Defined by the business as needed.
        # 
        # This parameter is required.
        self.prompt = prompt
        # The skill identifier, provided by the skill provider.
        self.skill = skill
        # The custom user data. This value is returned as-is in the callback.
        self.user_data = user_data
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['Model'] = self.model

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.skill is not None:
            result['Skill'] = self.skill

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Skill') is not None:
            self.skill = m.get('Skill')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

