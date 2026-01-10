# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Sandbox(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        ended_at: str = None,
        last_updated_at: str = None,
        metadata: Dict[str, Any] = None,
        sandbox_arn: str = None,
        sandbox_id: str = None,
        sandbox_idle_ttlin_seconds: int = None,
        sandbox_idle_timeout_seconds: int = None,
        status: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # 沙箱创建时间
        # 
        # This parameter is required.
        self.created_at = created_at
        self.ended_at = ended_at
        # 最后更新时间
        self.last_updated_at = last_updated_at
        self.metadata = metadata
        self.sandbox_arn = sandbox_arn
        # This parameter is required.
        self.sandbox_id = sandbox_id
        self.sandbox_idle_ttlin_seconds = sandbox_idle_ttlin_seconds
        # 沙箱空闲超时时间（秒）
        self.sandbox_idle_timeout_seconds = sandbox_idle_timeout_seconds
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.ended_at is not None:
            result['endedAt'] = self.ended_at

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.sandbox_arn is not None:
            result['sandboxArn'] = self.sandbox_arn

        if self.sandbox_id is not None:
            result['sandboxId'] = self.sandbox_id

        if self.sandbox_idle_ttlin_seconds is not None:
            result['sandboxIdleTTLInSeconds'] = self.sandbox_idle_ttlin_seconds

        if self.sandbox_idle_timeout_seconds is not None:
            result['sandboxIdleTimeoutSeconds'] = self.sandbox_idle_timeout_seconds

        if self.status is not None:
            result['status'] = self.status

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('endedAt') is not None:
            self.ended_at = m.get('endedAt')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('sandboxArn') is not None:
            self.sandbox_arn = m.get('sandboxArn')

        if m.get('sandboxId') is not None:
            self.sandbox_id = m.get('sandboxId')

        if m.get('sandboxIdleTTLInSeconds') is not None:
            self.sandbox_idle_ttlin_seconds = m.get('sandboxIdleTTLInSeconds')

        if m.get('sandboxIdleTimeoutSeconds') is not None:
            self.sandbox_idle_timeout_seconds = m.get('sandboxIdleTimeoutSeconds')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        return self

