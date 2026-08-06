# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePromptRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        framework_content: str = None,
        framework_type: str = None,
        workspace_id: str = None,
    ):
        # The description of the prompt.
        self.description = description
        # The prompt content.
        self.framework_content = framework_content
        # The framework type of the prompt template.
        self.framework_type = framework_type
        # The workspace ID. You can obtain the ID by calling the [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) operation.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.framework_content is not None:
            result['FrameworkContent'] = self.framework_content

        if self.framework_type is not None:
            result['FrameworkType'] = self.framework_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FrameworkContent') is not None:
            self.framework_content = m.get('FrameworkContent')

        if m.get('FrameworkType') is not None:
            self.framework_type = m.get('FrameworkType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

