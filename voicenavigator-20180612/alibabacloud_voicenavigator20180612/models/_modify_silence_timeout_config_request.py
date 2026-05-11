# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySilenceTimeoutConfigRequest(DaraModel):
    def __init__(
        self,
        final_action: str = None,
        final_action_params: str = None,
        final_prompt: str = None,
        instance_id: str = None,
        intent_trigger: str = None,
        prompt: str = None,
        source_type: str = None,
        threshold: int = None,
        timeout: int = None,
    ):
        # This parameter is required.
        self.final_action = final_action
        self.final_action_params = final_action_params
        # This parameter is required.
        self.final_prompt = final_prompt
        # This parameter is required.
        self.instance_id = instance_id
        self.intent_trigger = intent_trigger
        # This parameter is required.
        self.prompt = prompt
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required.
        self.threshold = threshold
        # This parameter is required.
        self.timeout = timeout

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

        if self.intent_trigger is not None:
            result['IntentTrigger'] = self.intent_trigger

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.timeout is not None:
            result['Timeout'] = self.timeout

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

        if m.get('IntentTrigger') is not None:
            self.intent_trigger = m.get('IntentTrigger')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

