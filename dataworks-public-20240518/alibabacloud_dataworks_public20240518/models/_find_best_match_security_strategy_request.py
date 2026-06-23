# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindBestMatchSecurityStrategyRequest(DaraModel):
    def __init__(
        self,
        control_module: str = None,
        control_sub_module: str = None,
        workspace_id: int = None,
    ):
        # Control module, used to match the security policy type.
        self.control_module = control_module
        # Control sub-module, used to match the security policy type.
        self.control_sub_module = control_sub_module
        # **Workspace ID**, used to precisely match workspace-level policies.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_module is not None:
            result['ControlModule'] = self.control_module

        if self.control_sub_module is not None:
            result['ControlSubModule'] = self.control_sub_module

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlModule') is not None:
            self.control_module = m.get('ControlModule')

        if m.get('ControlSubModule') is not None:
            self.control_sub_module = m.get('ControlSubModule')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

