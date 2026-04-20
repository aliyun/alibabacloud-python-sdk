# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class MmAppBindingMcpRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        mcps: List[main_models.MmAppBindingMcpRequestMcps] = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.mcps = mcps
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.mcps:
            for v1 in self.mcps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['Mcps'] = []
        if self.mcps is not None:
            for k1 in self.mcps:
                result['Mcps'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.mcps = []
        if m.get('Mcps') is not None:
            for k1 in m.get('Mcps'):
                temp_model = main_models.MmAppBindingMcpRequestMcps()
                self.mcps.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class MmAppBindingMcpRequestMcps(DaraModel):
    def __init__(
        self,
        code: str = None,
        tool_list: List[str] = None,
        type: str = None,
    ):
        self.code = code
        self.tool_list = tool_list
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.tool_list is not None:
            result['ToolList'] = self.tool_list

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ToolList') is not None:
            self.tool_list = m.get('ToolList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

