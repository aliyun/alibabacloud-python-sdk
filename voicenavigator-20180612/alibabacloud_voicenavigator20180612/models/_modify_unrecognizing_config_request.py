# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUnrecognizingConfigRequest(DaraModel):
    def __init__(
        self,
        final_action: str = None,
        final_action_params: str = None,
        final_prompt: str = None,
        instance_id: str = None,
        prompt: str = None,
        threshold: int = None,
    ):
        # This parameter is required.
        self.final_action = final_action
        self.final_action_params = final_action_params
        # This parameter is required.
        self.final_prompt = final_prompt
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.prompt = prompt
        # This parameter is required.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.final_action is not None:
            result['FinalAction'] = self.final_action

        if self.final_action_params is not None:
            result['FinalActionParams'] = self.final_action_params

        if self.final_prompt is not None:
            result['FinalPrompt'] = self.final_prompt

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinalAction') is not None:
            self.final_action = m.get('FinalAction')

        if m.get('FinalActionParams') is not None:
            self.final_action_params = m.get('FinalActionParams')

        if m.get('FinalPrompt') is not None:
            self.final_prompt = m.get('FinalPrompt')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

