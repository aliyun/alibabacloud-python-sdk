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
        # The ID of the collaboration group to which the task belongs (such as cg_101). If this parameter is specified, a group space task is created (the caller must be a valid group member). If this parameter is left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The name of the current effective digital employee. This parameter is empty if not configured.
        # 
        # This parameter is required.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # The segments.
        self.segments_shrink = segments_shrink
        # The ID of the effective tenant.
        self.tenant_id = tenant_id
        # The natural language task description.
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

