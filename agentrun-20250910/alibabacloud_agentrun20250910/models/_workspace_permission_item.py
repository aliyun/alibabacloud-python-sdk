# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class WorkspacePermissionItem(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.AccessDeniedDetail = None,
        action: str = None,
        allowed: bool = None,
        message: str = None,
    ):
        # RAM 明确拒绝且可构造 detail 时返回；通过或非 RAM 拒绝场景省略
        self.access_denied_detail = access_denied_detail
        # 归一化后的 RAM action，始终含 agentrun: 前缀，如 agentrun:ListTemplates
        self.action = action
        # RAM 判定通过为 true；workspace 不存在、非法/不支持 action、RAM SDK 报错等均为 false
        self.allowed = allowed
        # 人类可读原因；通过时通常为空字符串
        self.message = message

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.action is not None:
            result['action'] = self.action

        if self.allowed is not None:
            result['allowed'] = self.allowed

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            temp_model = main_models.AccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('accessDeniedDetail'))

        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('allowed') is not None:
            self.allowed = m.get('allowed')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

