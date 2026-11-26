# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScheduledTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        auto_preference: str = None,
        collaboration_group_id: str = None,
        description_shrink: str = None,
        digital_employee_name_shrink: str = None,
        is_open: bool = None,
        model: str = None,
        name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        output_mode: str = None,
        segments_shrink: str = None,
        task_detail_shrink: str = None,
        tenant_id: str = None,
        trigger_config_shrink: str = None,
        visibility: str = None,
        visible_member_user_ids_shrink: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # AUTO 偏好：none=默认、performance=效果优先、credit=成本优先；创建缺省为 none，固定模型可保存但不生效
        self.auto_preference = auto_preference
        # The ID of the associated collaboration group (such as cg_101). If this parameter is passed, a group space task is created, and the caller must be a valid group member. If this parameter is empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The description of the to-do card type.
        self.description_shrink = description_shrink
        # The name of the currently effective digital employee. This parameter is empty if it is not configured.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # Specifies whether public access is allowed.
        self.is_open = is_open
        # The large model used by the assistant. The default value is empty, which indicates that DingTalk automatically selects the model.
        self.model = model
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The output conversation mode. Default value: NEW_CONVERSATION.
        self.output_mode = output_mode
        # The site ID.
        self.segments_shrink = segments_shrink
        # The task details.
        self.task_detail_shrink = task_detail_shrink
        # The ID of the effective tenant.
        self.tenant_id = tenant_id
        # The trigger configuration of the scheduled task. triggerMode supports manual (manual trigger) and scheduled (scheduled trigger). If scheduled is used, cron must be specified. timezone and language are injected by the server, and the client does not need to pass them. pushConfig is the list of task push channels. If it is empty or no channel is enabled, no push is performed.
        self.trigger_config_shrink = trigger_config_shrink
        # The visibility scope of the group task. Valid values: PRIVATE (visible only to the creator and group owner), COLLABORATIVE (visible to specified collaboration members), and PUBLIC (visible to all group members). If this parameter is not passed for a group task, the default value is PRIVATE. This field is ignored for personal tasks.
        self.visibility = visibility
        # The list of user IDs of collaboration members. This parameter takes effect only when visibility is set to COLLABORATIVE and is ignored for other values. A maximum of 1,000 user IDs can be specified. You do not need to pass the IDs of the task creator and group creator because they are covered by the authentication layer. This field is ignored for personal tasks.
        self.visible_member_user_ids_shrink = visible_member_user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.auto_preference is not None:
            result['autoPreference'] = self.auto_preference

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

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.output_mode is not None:
            result['outputMode'] = self.output_mode

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
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('autoPreference') is not None:
            self.auto_preference = m.get('autoPreference')

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

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('outputMode') is not None:
            self.output_mode = m.get('outputMode')

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

