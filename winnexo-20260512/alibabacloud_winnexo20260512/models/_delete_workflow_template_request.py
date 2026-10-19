# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWorkflowTemplateRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        template_id: str = None,
        tenant_id: str = None,
    ):
        # 协作空间 ID
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 模板 ID
        # 
        # This parameter is required.
        self.template_id = template_id
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

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

