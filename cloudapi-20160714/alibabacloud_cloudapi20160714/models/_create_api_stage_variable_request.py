# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiStageVariableRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
        stage_id: str = None,
        stage_route_model: str = None,
        support_route: bool = None,
        variable_name: str = None,
        variable_value: str = None,
    ):
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        self.security_token = security_token
        # The ID of the runtime environment.
        # 
        # This parameter is required.
        self.stage_id = stage_id
        # The routing model of the environment.
        self.stage_route_model = stage_route_model
        # Specifies whether routing is supported.
        self.support_route = support_route
        # The name of the variable to be added. This parameter is case-sensitive.
        # 
        # This parameter is required.
        self.variable_name = variable_name
        # The value of the variable.
        self.variable_value = variable_value

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

        if self.stage_route_model is not None:
            result['StageRouteModel'] = self.stage_route_model

        if self.support_route is not None:
            result['SupportRoute'] = self.support_route

        if self.variable_name is not None:
            result['VariableName'] = self.variable_name

        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageRouteModel') is not None:
            self.stage_route_model = m.get('StageRouteModel')

        if m.get('SupportRoute') is not None:
            self.support_route = m.get('SupportRoute')

        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')

        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')

        return self

