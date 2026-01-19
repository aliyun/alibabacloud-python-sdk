# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteApiStageVariableRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
        stage_id: str = None,
        variable_name: str = None,
    ):
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        self.security_token = security_token
        # The ID of the environment.
        # 
        # This parameter is required.
        self.stage_id = stage_id
        # The name of the variable to be deleted. This parameter is case-sensitive.
        # 
        # This parameter is required.
        self.variable_name = variable_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.variable_name is not None:
            result['VariableName'] = self.variable_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')

        return self

