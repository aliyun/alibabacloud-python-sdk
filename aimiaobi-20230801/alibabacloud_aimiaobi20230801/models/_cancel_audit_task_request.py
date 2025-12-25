# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelAuditTaskRequest(DaraModel):
    def __init__(
        self,
        article_id: str = None,
        content_audit_task_id: str = None,
        workspace_id: str = None,
    ):
        self.article_id = article_id
        self.content_audit_task_id = content_audit_task_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article_id is not None:
            result['ArticleId'] = self.article_id

        if self.content_audit_task_id is not None:
            result['ContentAuditTaskId'] = self.content_audit_task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArticleId') is not None:
            self.article_id = m.get('ArticleId')

        if m.get('ContentAuditTaskId') is not None:
            self.content_audit_task_id = m.get('ContentAuditTaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

