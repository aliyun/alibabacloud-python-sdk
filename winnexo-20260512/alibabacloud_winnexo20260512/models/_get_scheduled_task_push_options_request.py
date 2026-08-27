# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledTaskPushOptionsRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        digital_employee_name: str = None,
        tenant_id: str = None,
    ):
        # The ID of the collaboration group (such as cg_101). If specified, a group workspace task is created (the caller must be a valid group member). If left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The name of the currently active digital employee. This value is empty if not configured.
        self.digital_employee_name = digital_employee_name
        # The tenant ID. This is a common parameter. In winnexo-cli, pass it explicitly with --tenant-id.
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

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

