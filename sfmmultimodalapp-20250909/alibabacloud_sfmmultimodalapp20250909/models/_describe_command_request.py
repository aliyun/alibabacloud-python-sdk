# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCommandRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        tool_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.domain_code = domain_code
        # This parameter is required.
        self.tool_id = tool_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code

        if self.tool_id is not None:
            result['ToolId'] = self.tool_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

