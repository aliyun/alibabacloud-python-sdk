# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCommandShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        domain_code: str = None,
        domain_name: str = None,
        tool_description: str = None,
        tool_examples_shrink: str = None,
        tool_name: str = None,
        tool_params_shrink: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.domain_code = domain_code
        self.domain_name = domain_name
        # This parameter is required.
        self.tool_description = tool_description
        self.tool_examples_shrink = tool_examples_shrink
        # This parameter is required.
        self.tool_name = tool_name
        self.tool_params_shrink = tool_params_shrink
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

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.tool_description is not None:
            result['ToolDescription'] = self.tool_description

        if self.tool_examples_shrink is not None:
            result['ToolExamples'] = self.tool_examples_shrink

        if self.tool_name is not None:
            result['ToolName'] = self.tool_name

        if self.tool_params_shrink is not None:
            result['ToolParams'] = self.tool_params_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ToolDescription') is not None:
            self.tool_description = m.get('ToolDescription')

        if m.get('ToolExamples') is not None:
            self.tool_examples_shrink = m.get('ToolExamples')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        if m.get('ToolParams') is not None:
            self.tool_params_shrink = m.get('ToolParams')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

