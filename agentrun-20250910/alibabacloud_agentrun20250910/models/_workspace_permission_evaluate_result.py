# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class WorkspacePermissionEvaluateResult(DaraModel):
    def __init__(
        self,
        permissions: List[main_models.WorkspacePermissionItem] = None,
        workspace_found: bool = None,
        workspace_id: str = None,
    ):
        # 各 action 的校验结果；顺序与请求 actions 一致
        self.permissions = permissions
        # 当前租户下是否解析到该 workspace；为 false 时各 permissions 一般为 allowed: false，不会调用 RAM
        self.workspace_found = workspace_found
        # 回显请求中的 workspace ID（trim 后）
        self.workspace_id = workspace_id

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['permissions'].append(k1.to_map() if k1 else None)

        if self.workspace_found is not None:
            result['workspaceFound'] = self.workspace_found

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permissions = []
        if m.get('permissions') is not None:
            for k1 in m.get('permissions'):
                temp_model = main_models.WorkspacePermissionItem()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('workspaceFound') is not None:
            self.workspace_found = m.get('workspaceFound')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

