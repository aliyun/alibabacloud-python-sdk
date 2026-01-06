# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatasetJobRequest(DaraModel):
    def __init__(
        self,
        dataset_version: str = None,
        description: str = None,
        job_action: str = None,
        job_mode: str = None,
        job_spec: str = None,
        workspace_id: str = None,
    ):
        # The dataset version.
        self.dataset_version = dataset_version
        # The job description.
        self.description = description
        # The job action.
        # 
        # Valid values:
        # 
        # *   SemanticIndex
        # *   IntelligentTag
        # *   FileMetaExport
        # 
        # This parameter is required.
        self.job_action = job_action
        # The job mode.
        # 
        # Valid values:
        # 
        # *   Full: full mode.
        self.job_mode = job_mode
        # The job configuration.
        # 
        # This parameter is required.
        self.job_spec = job_spec
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
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
        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.description is not None:
            result['Description'] = self.description

        if self.job_action is not None:
            result['JobAction'] = self.job_action

        if self.job_mode is not None:
            result['JobMode'] = self.job_mode

        if self.job_spec is not None:
            result['JobSpec'] = self.job_spec

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('JobAction') is not None:
            self.job_action = m.get('JobAction')

        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')

        if m.get('JobSpec') is not None:
            self.job_spec = m.get('JobSpec')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

