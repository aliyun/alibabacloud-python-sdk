# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportWorkflowTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        template_shrink: str = None,
        tenant_id: str = None,
    ):
        # 协作空间 ID
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 可移植模板 JSON（stepId/sortOrder 可省略）
        # 
        # This parameter is required.
        self.template_shrink = template_shrink
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.template_shrink is not None:
            result['template'] = self.template_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('template') is not None:
            self.template_shrink = m.get('template')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

