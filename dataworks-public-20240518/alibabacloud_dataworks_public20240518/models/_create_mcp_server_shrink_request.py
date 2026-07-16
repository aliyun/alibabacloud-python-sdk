# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMcpServerShrinkRequest(DaraModel):
    def __init__(
        self,
        config_shrink: str = None,
        name: str = None,
        visibility: str = None,
        visibility_scope_shrink: str = None,
    ):
        # The connection configuration for the MCP Server.
        self.config_shrink = config_shrink
        # The name of the MCP Server. The name must be unique at the tenant level. It must start with a lowercase letter and contain only characters from `a-z`, `0-9`, `_`, and `-`.
        # 
        # This parameter is required.
        self.name = name
        # The visibility level.
        self.visibility = visibility
        # The visibility scope. The required fields depend on the value of the `Visibility` parameter.
        self.visibility_scope_shrink = visibility_scope_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope_shrink is not None:
            result['VisibilityScope'] = self.visibility_scope_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            self.visibility_scope_shrink = m.get('VisibilityScope')

        return self

