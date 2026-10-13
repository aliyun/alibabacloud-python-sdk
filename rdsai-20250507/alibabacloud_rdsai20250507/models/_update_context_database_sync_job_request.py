# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateContextDatabaseSyncJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enabled: bool = None,
        filters: Dict[str, Any] = None,
        job_id: str = None,
        name: str = None,
        target_knowledge_base_id: str = None,
        target_knowledge_base_name: str = None,
        workspace_id: str = None,
    ):
        self.client_token = client_token
        self.enabled = enabled
        self.filters = filters
        # This parameter is required.
        self.job_id = job_id
        self.name = name
        self.target_knowledge_base_id = target_knowledge_base_id
        self.target_knowledge_base_name = target_knowledge_base_name
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.filters is not None:
            result['Filters'] = self.filters

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.target_knowledge_base_id is not None:
            result['TargetKnowledgeBaseId'] = self.target_knowledge_base_id

        if self.target_knowledge_base_name is not None:
            result['TargetKnowledgeBaseName'] = self.target_knowledge_base_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TargetKnowledgeBaseId') is not None:
            self.target_knowledge_base_id = m.get('TargetKnowledgeBaseId')

        if m.get('TargetKnowledgeBaseName') is not None:
            self.target_knowledge_base_name = m.get('TargetKnowledgeBaseName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

