# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateServiceRequest(DaraModel):
    def __init__(
        self,
        develop: str = None,
        labels: Dict[str, str] = None,
        workspace_id: str = None,
        body: str = None,
    ):
        # Specifies whether to enter development mode.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.develop = develop
        # The custom label.
        self.labels = labels
        # The workspace ID.
        self.workspace_id = workspace_id
        # The request body. For more information about the key request parameters, see **Table 1. Request body parameters** and **Table 2. Metadata parameters**. For more information about all related parameters, see [Parameters of model services](https://help.aliyun.com/document_detail/450525.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.develop is not None:
            result['Develop'] = self.develop

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.body is not None:
            result['body'] = self.body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Develop') is not None:
            self.develop = m.get('Develop')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('body') is not None:
            self.body = m.get('body')

        return self

