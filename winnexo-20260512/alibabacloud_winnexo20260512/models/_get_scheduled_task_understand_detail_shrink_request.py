# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledTaskUnderstandDetailShrinkRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        digital_employee_name_shrink: str = None,
        segments_shrink: str = None,
        tenant_id: str = None,
        user_input: str = None,
    ):
        # 所属协作群组 ID（如 cg_101）；群任务理解时传入（调用者需为有效群成员），候选技能额外并入群绑定技能
        self.collaboration_group_id = collaboration_group_id
        # 数字员工名称列表，用于过滤可用技能；必传（传空列表表示仅用租户 global 技能）
        # 
        # This parameter is required.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        self.segments_shrink = segments_shrink
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 自然语言任务描述
        # 
        # This parameter is required.
        self.user_input = user_input

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.digital_employee_name_shrink is not None:
            result['digitalEmployeeName'] = self.digital_employee_name_shrink

        if self.segments_shrink is not None:
            result['segments'] = self.segments_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_input is not None:
            result['userInput'] = self.user_input

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name_shrink = m.get('digitalEmployeeName')

        if m.get('segments') is not None:
            self.segments_shrink = m.get('segments')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userInput') is not None:
            self.user_input = m.get('userInput')

        return self

