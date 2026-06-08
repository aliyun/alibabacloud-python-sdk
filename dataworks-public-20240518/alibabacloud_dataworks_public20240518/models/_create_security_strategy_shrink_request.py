# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSecurityStrategyShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content_shrink: str = None,
        control_dw_scope: str = None,
        control_module: str = None,
        control_sub_module: str = None,
        description: str = None,
        name: str = None,
        schema_name: str = None,
        workspaces_shrink: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.content_shrink = content_shrink
        # This parameter is required.
        self.control_dw_scope = control_dw_scope
        # This parameter is required.
        self.control_module = control_module
        self.control_sub_module = control_sub_module
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.schema_name = schema_name
        self.workspaces_shrink = workspaces_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.control_dw_scope is not None:
            result['ControlDwScope'] = self.control_dw_scope

        if self.control_module is not None:
            result['ControlModule'] = self.control_module

        if self.control_sub_module is not None:
            result['ControlSubModule'] = self.control_sub_module

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.workspaces_shrink is not None:
            result['Workspaces'] = self.workspaces_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('ControlDwScope') is not None:
            self.control_dw_scope = m.get('ControlDwScope')

        if m.get('ControlModule') is not None:
            self.control_module = m.get('ControlModule')

        if m.get('ControlSubModule') is not None:
            self.control_sub_module = m.get('ControlSubModule')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Workspaces') is not None:
            self.workspaces_shrink = m.get('Workspaces')

        return self

