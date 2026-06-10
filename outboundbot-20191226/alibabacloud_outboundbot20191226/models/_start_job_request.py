# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartJobRequest(DaraModel):
    def __init__(
        self,
        calling_number: List[str] = None,
        instance_id: str = None,
        job_group_id: str = None,
        job_json: str = None,
        scenario_id: str = None,
        script_id: str = None,
    ):
        # List of caller numbers
        self.calling_number = calling_number
        # Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Task group ID
        self.job_group_id = job_group_id
        # Job data, which includes the following fields:
        # 
        # extras // Optional extra information
        # 
        # - key // Key for a custom variable
        # 
        # - value // Value for a custom variable
        # 
        # contacts // Required contact information for the callee
        # 
        # - phoneNumber // Required phone number of the callee
        # 
        # - referenceId // Required contact ID (user-defined) to avoid duplicate names
        # 
        # - role // Optional role of this contact in the outbound call scenario. If omitted, no role distinction is made
        # 
        # - honorific // Optional honorific for the contact
        # 
        # - name // Optional name of the contact
        # 
        # This parameter is required.
        self.job_json = job_json
        # Scenario ID. This field supports backward compatibility with legacy outbound calling features. You can omit it.
        self.scenario_id = scenario_id
        # Scenario ID (required)
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_json is not None:
            result['JobJson'] = self.job_json

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobJson') is not None:
            self.job_json = m.get('JobJson')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

