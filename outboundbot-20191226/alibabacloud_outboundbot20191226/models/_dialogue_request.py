# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DialogueRequest(DaraModel):
    def __init__(
        self,
        action_key: str = None,
        action_params: str = None,
        call_id: str = None,
        call_type: str = None,
        called_number: str = None,
        calling_number: str = None,
        instance_id: str = None,
        scenario_id: str = None,
        script_id: str = None,
        task_id: str = None,
        utterance: str = None,
    ):
        self.action_key = action_key
        self.action_params = action_params
        # This parameter is required.
        self.call_id = call_id
        # This parameter is required.
        self.call_type = call_type
        # This parameter is required.
        self.called_number = called_number
        # This parameter is required.
        self.calling_number = calling_number
        # This parameter is required.
        self.instance_id = instance_id
        self.scenario_id = scenario_id
        # 场景id
        self.script_id = script_id
        self.task_id = task_id
        # This parameter is required.
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_key is not None:
            result['ActionKey'] = self.action_key

        if self.action_params is not None:
            result['ActionParams'] = self.action_params

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.utterance is not None:
            result['Utterance'] = self.utterance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionKey') is not None:
            self.action_key = m.get('ActionKey')

        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        return self

