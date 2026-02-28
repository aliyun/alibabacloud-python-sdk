# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartPredictiveCallRequest(DaraModel):
    def __init__(
        self,
        callee: str = None,
        caller: str = None,
        contact_flow_id: str = None,
        contact_flow_variables: str = None,
        instance_id: str = None,
        masked_callee: str = None,
        skill_group_id: str = None,
        tags: str = None,
        timeout_seconds: int = None,
    ):
        # This parameter is required.
        self.callee = callee
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.contact_flow_id = contact_flow_id
        self.contact_flow_variables = contact_flow_variables
        # This parameter is required.
        self.instance_id = instance_id
        self.masked_callee = masked_callee
        self.skill_group_id = skill_group_id
        self.tags = tags
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.contact_flow_id is not None:
            result['ContactFlowId'] = self.contact_flow_id

        if self.contact_flow_variables is not None:
            result['ContactFlowVariables'] = self.contact_flow_variables

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.masked_callee is not None:
            result['MaskedCallee'] = self.masked_callee

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')

        if m.get('ContactFlowVariables') is not None:
            self.contact_flow_variables = m.get('ContactFlowVariables')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaskedCallee') is not None:
            self.masked_callee = m.get('MaskedCallee')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

