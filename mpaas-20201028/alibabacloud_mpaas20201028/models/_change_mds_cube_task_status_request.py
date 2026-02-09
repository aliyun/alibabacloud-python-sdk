# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeMdsCubeTaskStatusRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        task_status: int = None,
        template_resource_id: int = None,
        template_task_id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.task_status = task_status
        self.template_resource_id = template_resource_id
        self.template_task_id = template_task_id
        self.tenant_id = tenant_id
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

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.template_resource_id is not None:
            result['TemplateResourceId'] = self.template_resource_id

        if self.template_task_id is not None:
            result['TemplateTaskId'] = self.template_task_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TemplateResourceId') is not None:
            self.template_resource_id = m.get('TemplateResourceId')

        if m.get('TemplateTaskId') is not None:
            self.template_task_id = m.get('TemplateTaskId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

