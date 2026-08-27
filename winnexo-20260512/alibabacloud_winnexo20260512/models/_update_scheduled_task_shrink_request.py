# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateScheduledTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        description_shrink: str = None,
        digital_employee_name_shrink: str = None,
        is_open: bool = None,
        model: str = None,
        name: str = None,
        segments_shrink: str = None,
        task_detail_shrink: str = None,
        task_id: str = None,
        tenant_id: str = None,
        trigger_config_shrink: str = None,
        visibility: str = None,
        visible_member_user_ids_shrink: str = None,
    ):
        # The description information.
        self.description_shrink = description_shrink
        # The list of digital human names.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # Specifies whether the task is publicly accessible.
        self.is_open = is_open
        # The execution model tier. If not specified, the model tier is not updated.
        self.model = model
        # The file name.
        self.name = name
        # The segments.
        self.segments_shrink = segments_shrink
        # The task details.
        self.task_detail_shrink = task_detail_shrink
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The trigger configuration. The configuration varies depending on the trigger type.
        self.trigger_config_shrink = trigger_config_shrink
        # The visibility scope for group tasks. Valid values: PRIVATE (visible only to the creator and group owner), COLLABORATIVE (visible to specified collaborators), and PUBLIC (visible to all group members). If not specified, the visibility is not updated. This parameter is ignored for personal tasks.
        self.visibility = visibility
        # The full replacement list of collaborator member user IDs. This parameter takes effect only when visibility is set to COLLABORATIVE. The list is cleared when switching away from the COLLABORATIVE tier. A maximum of 1000 members are supported. If not specified, the member list is not updated. The task creator and group creator do not need to be included because they are covered by the authentication layer. This parameter is ignored for personal tasks.
        self.visible_member_user_ids_shrink = visible_member_user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description_shrink is not None:
            result['description'] = self.description_shrink

        if self.digital_employee_name_shrink is not None:
            result['digitalEmployeeName'] = self.digital_employee_name_shrink

        if self.is_open is not None:
            result['isOpen'] = self.is_open

        if self.model is not None:
            result['model'] = self.model

        if self.name is not None:
            result['name'] = self.name

        if self.segments_shrink is not None:
            result['segments'] = self.segments_shrink

        if self.task_detail_shrink is not None:
            result['taskDetail'] = self.task_detail_shrink

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.trigger_config_shrink is not None:
            result['triggerConfig'] = self.trigger_config_shrink

        if self.visibility is not None:
            result['visibility'] = self.visibility

        if self.visible_member_user_ids_shrink is not None:
            result['visibleMemberUserIds'] = self.visible_member_user_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description_shrink = m.get('description')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name_shrink = m.get('digitalEmployeeName')

        if m.get('isOpen') is not None:
            self.is_open = m.get('isOpen')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('segments') is not None:
            self.segments_shrink = m.get('segments')

        if m.get('taskDetail') is not None:
            self.task_detail_shrink = m.get('taskDetail')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('triggerConfig') is not None:
            self.trigger_config_shrink = m.get('triggerConfig')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        if m.get('visibleMemberUserIds') is not None:
            self.visible_member_user_ids_shrink = m.get('visibleMemberUserIds')

        return self

