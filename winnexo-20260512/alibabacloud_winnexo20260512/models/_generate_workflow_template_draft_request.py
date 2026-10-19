# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GenerateWorkflowTemplateDraftRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        previous_draft: Dict[str, Any] = None,
        requirement: str = None,
        tenant_id: str = None,
    ):
        # 协作空间 ID
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 上一轮草稿；提供时基于它迭代修改
        self.previous_draft = previous_draft
        # 模板需求描述
        # 
        # This parameter is required.
        self.requirement = requirement
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

        if self.previous_draft is not None:
            result['previousDraft'] = self.previous_draft

        if self.requirement is not None:
            result['requirement'] = self.requirement

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('previousDraft') is not None:
            self.previous_draft = m.get('previousDraft')

        if m.get('requirement') is not None:
            self.requirement = m.get('requirement')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

