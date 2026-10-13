# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomScriptTemplateRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        labels_json: str = None,
        model: str = None,
        name: str = None,
        prompt: str = None,
        prompt_json: str = None,
        script_id: str = None,
    ):
        # The description of the custom scenario.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The label descriptions in JSON array format.
        self.labels_json = labels_json
        # The ID of the model used to create the template.
        self.model = model
        # The name of the custom scenario.
        self.name = name
        # The prompt for professional mode.
        self.prompt = prompt
        # The agent configuration in JSON format.
        self.prompt_json = prompt_json
        # The script ID.
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.labels_json is not None:
            result['LabelsJson'] = self.labels_json

        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.prompt_json is not None:
            result['PromptJson'] = self.prompt_json

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LabelsJson') is not None:
            self.labels_json = m.get('LabelsJson')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PromptJson') is not None:
            self.prompt_json = m.get('PromptJson')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

