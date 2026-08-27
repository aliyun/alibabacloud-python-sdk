# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScheduledTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        description_shrink: str = None,
        digital_employee_name_shrink: str = None,
        is_open: bool = None,
        model: str = None,
        name: str = None,
        segments_shrink: str = None,
        task_detail_shrink: str = None,
        tenant_id: str = None,
        trigger_config_shrink: str = None,
        visibility: str = None,
        visible_member_user_ids_shrink: str = None,
    ):
        # The ID of the collaboration group (such as cg_101). If specified, a group space task is created (the caller must be a valid group member). If empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The description of the to-do card type.
        self.description_shrink = description_shrink
        # The name of the current effective digital employee. This parameter is empty if not configured.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # Specifies whether public access is enabled.
        self.is_open = is_open
        # The large model used by the assistant. An empty value indicates that DingTalk automatically selects the model.
        self.model = model
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The site ID.
        self.segments_shrink = segments_shrink
        # The task details.
        self.task_detail_shrink = task_detail_shrink
        # The ID of the effective tenant.
        self.tenant_id = tenant_id
        # The trigger configuration. The configuration varies depending on the trigger type. For the specific format, refer to the following data structures:
        # 
        #   - OSS trigger: See [OSSTriggerConfig](https://help.aliyun.com/document_detail/415697.html).
        #   - Simple Log Service trigger: See [LogTriggerConfig](https://help.aliyun.com/document_detail/415694.html).
        #   - Time trigger: See [TimeTriggerConfig](https://help.aliyun.com/document_detail/415712.html).
        #   - HTTP trigger: See [HTTPTriggerConfig](https://help.aliyun.com/document_detail/415685.html).
        #   - Tablestore trigger: You only need to specify the complete **SourceArn** parameter. No additional configuration is required. Set the value to an empty object {}.
        #   - CDN event trigger: See [CDNEventsTriggerConfig](https://help.aliyun.com/document_detail/415674.html).
        #   - MNS topic trigger: See [MnsTopicTriggerConfig](https://help.aliyun.com/document_detail/415695.html).
        #   - EventBridge trigger: See [EventBridgeTriggerConfig](https://help.aliyun.com/document_detail/2508622.html).
        self.trigger_config_shrink = trigger_config_shrink
        # The visibility scope of the group task. Valid values: PRIVATE (visible only to the creator and group owner), COLLABORATIVE (visible to specified collaborators), and PUBLIC (visible to all group members). Default value for group tasks: PRIVATE. This parameter is ignored for personal tasks.
        self.visibility = visibility
        # The list of collaborator user IDs. This parameter takes effect only when visibility is set to COLLABORATIVE. It is ignored for other visibility levels. A maximum of 1000 IDs are supported. The task creator and group creator do not need to be included (covered by the authentication layer). This parameter is ignored for personal tasks.
        self.visible_member_user_ids_shrink = visible_member_user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

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
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

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

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('triggerConfig') is not None:
            self.trigger_config_shrink = m.get('triggerConfig')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        if m.get('visibleMemberUserIds') is not None:
            self.visible_member_user_ids_shrink = m.get('visibleMemberUserIds')

        return self

