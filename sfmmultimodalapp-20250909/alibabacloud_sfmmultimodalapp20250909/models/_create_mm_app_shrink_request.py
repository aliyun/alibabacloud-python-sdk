# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMmAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        binding_config_shrink: str = None,
        conversation_config_shrink: str = None,
        model_config_shrink: str = None,
        prompt: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.binding_config_shrink = binding_config_shrink
        self.conversation_config_shrink = conversation_config_shrink
        self.model_config_shrink = model_config_shrink
        self.prompt = prompt
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.binding_config_shrink is not None:
            result['BindingConfig'] = self.binding_config_shrink

        if self.conversation_config_shrink is not None:
            result['ConversationConfig'] = self.conversation_config_shrink

        if self.model_config_shrink is not None:
            result['ModelConfig'] = self.model_config_shrink

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BindingConfig') is not None:
            self.binding_config_shrink = m.get('BindingConfig')

        if m.get('ConversationConfig') is not None:
            self.conversation_config_shrink = m.get('ConversationConfig')

        if m.get('ModelConfig') is not None:
            self.model_config_shrink = m.get('ModelConfig')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

