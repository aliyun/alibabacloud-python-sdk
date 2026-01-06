# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDatasetJobRequest(DaraModel):
    def __init__(
        self,
        dataset_version: str = None,
        description: str = None,
        workspace_id: str = None,
    ):
        # The dataset version name.
        self.dataset_version = dataset_version
        # The dataset job description.
        self.description = description
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.description is not None:
            result['Description'] = self.description

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

