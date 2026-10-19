# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SetWorkItemPinnedResponseBody(DaraModel):
    def __init__(
        self,
        acceptance_criteria: str = None,
        applied_status_version: int = None,
        attachments: List[main_models.SetWorkItemPinnedResponseBodyAttachments] = None,
        business_status: str = None,
        can_delete: bool = None,
        can_manage: bool = None,
        can_manage_visibility: bool = None,
        can_rename: bool = None,
        code: str = None,
        collaboration_group_id: str = None,
        collaborator_user_ids: List[int] = None,
        conversation_id: str = None,
        created_at: str = None,
        created_by_user_id: int = None,
        creation_type: str = None,
        current_plan_id: str = None,
        current_revision: int = None,
        current_run_id: str = None,
        current_run_seq: int = None,
        current_step_name: str = None,
        description: str = None,
        input_version: int = None,
        item_type: str = None,
        last_processing_at: str = None,
        legacy_topic: bool = None,
        member_user_ids: List[int] = None,
        message: str = None,
        modified_at: str = None,
        owner_user_id: int = None,
        pinned: bool = None,
        priority: str = None,
        progress_completed: int = None,
        progress_total: int = None,
        request_id: str = None,
        source_execution_id: str = None,
        source_task_id: str = None,
        source_task_name: str = None,
        source_trigger_key: str = None,
        source_type: str = None,
        title: str = None,
        trigger_timezone: str = None,
        triggered_at: str = None,
        version: int = None,
        visibility: str = None,
        visibility_source: str = None,
        work_item_id: str = None,
        workflow_status: str = None,
        workflow_template_ids: List[str] = None,
    ):
        # 验收标准
        self.acceptance_criteria = acceptance_criteria
        # 已应用的状态版本
        self.applied_status_version = applied_status_version
        # 输入附件列表
        self.attachments = attachments
        # 业务状态（七态）
        self.business_status = business_status
        # 调用者是否可删除
        self.can_delete = can_delete
        # 调用者是否可管理
        self.can_manage = can_manage
        # 是否可独立调整可见范围
        self.can_manage_visibility = can_manage_visibility
        # 调用者是否可重命名
        self.can_rename = can_rename
        # 业务状态码；成功为200
        self.code = code
        # 协作空间ID
        self.collaboration_group_id = collaboration_group_id
        # 协作人用户ID列表
        self.collaborator_user_ids = collaborator_user_ids
        # 关联会话ID
        self.conversation_id = conversation_id
        # 创建时间(ISO8601)
        self.created_at = created_at
        # 创建人用户ID
        self.created_by_user_id = created_by_user_id
        # 创建来源：DEFAULT/TASK
        self.creation_type = creation_type
        # 当前物理计划ID
        self.current_plan_id = current_plan_id
        # 当前修订号
        self.current_revision = current_revision
        # 当前运行ID
        self.current_run_id = current_run_id
        # 当前运行序号
        self.current_run_seq = current_run_seq
        # 当前步骤名称
        self.current_step_name = current_step_name
        # 描述
        self.description = description
        # 输入快照版本
        self.input_version = input_version
        # 工作项类型
        self.item_type = item_type
        # 最近进入处理中的时间(ISO8601)
        self.last_processing_at = last_processing_at
        # 是否为兼容期自由探索话题
        self.legacy_topic = legacy_topic
        # 可见成员用户ID列表
        self.member_user_ids = member_user_ids
        # 错误描述
        self.message = message
        # 修改时间(ISO8601)
        self.modified_at = modified_at
        # 负责人用户ID
        self.owner_user_id = owner_user_id
        # 调用者个人置顶状态
        self.pinned = pinned
        # 优先级
        self.priority = priority
        # 已完成进度
        self.progress_completed = progress_completed
        # 总进度
        self.progress_total = progress_total
        # 请求追踪ID
        self.request_id = request_id
        # 任务执行ID
        self.source_execution_id = source_execution_id
        # 任务来源ID
        self.source_task_id = source_task_id
        # 任务来源名称
        self.source_task_name = source_task_name
        # 任务触发键
        self.source_trigger_key = source_trigger_key
        # 任务来源类型
        self.source_type = source_type
        # 标题
        self.title = title
        # 任务触发时区
        self.trigger_timezone = trigger_timezone
        # 任务触发时间(ISO8601)
        self.triggered_at = triggered_at
        # 乐观版本号
        self.version = version
        # 可见范围
        self.visibility = visibility
        # 可见范围来源：SELF/TASK/TEMPLATE
        self.visibility_source = visibility_source
        # 工作项ID
        self.work_item_id = work_item_id
        # Workflow四态投影
        self.workflow_status = workflow_status
        # 绑定的工作流模板ID列表
        self.workflow_template_ids = workflow_template_ids

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceptance_criteria is not None:
            result['acceptanceCriteria'] = self.acceptance_criteria

        if self.applied_status_version is not None:
            result['appliedStatusVersion'] = self.applied_status_version

        result['attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['attachments'].append(k1.to_map() if k1 else None)

        if self.business_status is not None:
            result['businessStatus'] = self.business_status

        if self.can_delete is not None:
            result['canDelete'] = self.can_delete

        if self.can_manage is not None:
            result['canManage'] = self.can_manage

        if self.can_manage_visibility is not None:
            result['canManageVisibility'] = self.can_manage_visibility

        if self.can_rename is not None:
            result['canRename'] = self.can_rename

        if self.code is not None:
            result['code'] = self.code

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.collaborator_user_ids is not None:
            result['collaboratorUserIds'] = self.collaborator_user_ids

        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by_user_id is not None:
            result['createdByUserId'] = self.created_by_user_id

        if self.creation_type is not None:
            result['creationType'] = self.creation_type

        if self.current_plan_id is not None:
            result['currentPlanId'] = self.current_plan_id

        if self.current_revision is not None:
            result['currentRevision'] = self.current_revision

        if self.current_run_id is not None:
            result['currentRunId'] = self.current_run_id

        if self.current_run_seq is not None:
            result['currentRunSeq'] = self.current_run_seq

        if self.current_step_name is not None:
            result['currentStepName'] = self.current_step_name

        if self.description is not None:
            result['description'] = self.description

        if self.input_version is not None:
            result['inputVersion'] = self.input_version

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.last_processing_at is not None:
            result['lastProcessingAt'] = self.last_processing_at

        if self.legacy_topic is not None:
            result['legacyTopic'] = self.legacy_topic

        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids

        if self.message is not None:
            result['message'] = self.message

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.owner_user_id is not None:
            result['ownerUserId'] = self.owner_user_id

        if self.pinned is not None:
            result['pinned'] = self.pinned

        if self.priority is not None:
            result['priority'] = self.priority

        if self.progress_completed is not None:
            result['progressCompleted'] = self.progress_completed

        if self.progress_total is not None:
            result['progressTotal'] = self.progress_total

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.source_execution_id is not None:
            result['sourceExecutionId'] = self.source_execution_id

        if self.source_task_id is not None:
            result['sourceTaskId'] = self.source_task_id

        if self.source_task_name is not None:
            result['sourceTaskName'] = self.source_task_name

        if self.source_trigger_key is not None:
            result['sourceTriggerKey'] = self.source_trigger_key

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.trigger_timezone is not None:
            result['triggerTimezone'] = self.trigger_timezone

        if self.triggered_at is not None:
            result['triggeredAt'] = self.triggered_at

        if self.version is not None:
            result['version'] = self.version

        if self.visibility is not None:
            result['visibility'] = self.visibility

        if self.visibility_source is not None:
            result['visibilitySource'] = self.visibility_source

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        if self.workflow_status is not None:
            result['workflowStatus'] = self.workflow_status

        if self.workflow_template_ids is not None:
            result['workflowTemplateIds'] = self.workflow_template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptanceCriteria') is not None:
            self.acceptance_criteria = m.get('acceptanceCriteria')

        if m.get('appliedStatusVersion') is not None:
            self.applied_status_version = m.get('appliedStatusVersion')

        self.attachments = []
        if m.get('attachments') is not None:
            for k1 in m.get('attachments'):
                temp_model = main_models.SetWorkItemPinnedResponseBodyAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('businessStatus') is not None:
            self.business_status = m.get('businessStatus')

        if m.get('canDelete') is not None:
            self.can_delete = m.get('canDelete')

        if m.get('canManage') is not None:
            self.can_manage = m.get('canManage')

        if m.get('canManageVisibility') is not None:
            self.can_manage_visibility = m.get('canManageVisibility')

        if m.get('canRename') is not None:
            self.can_rename = m.get('canRename')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('collaboratorUserIds') is not None:
            self.collaborator_user_ids = m.get('collaboratorUserIds')

        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdByUserId') is not None:
            self.created_by_user_id = m.get('createdByUserId')

        if m.get('creationType') is not None:
            self.creation_type = m.get('creationType')

        if m.get('currentPlanId') is not None:
            self.current_plan_id = m.get('currentPlanId')

        if m.get('currentRevision') is not None:
            self.current_revision = m.get('currentRevision')

        if m.get('currentRunId') is not None:
            self.current_run_id = m.get('currentRunId')

        if m.get('currentRunSeq') is not None:
            self.current_run_seq = m.get('currentRunSeq')

        if m.get('currentStepName') is not None:
            self.current_step_name = m.get('currentStepName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('inputVersion') is not None:
            self.input_version = m.get('inputVersion')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('lastProcessingAt') is not None:
            self.last_processing_at = m.get('lastProcessingAt')

        if m.get('legacyTopic') is not None:
            self.legacy_topic = m.get('legacyTopic')

        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('ownerUserId') is not None:
            self.owner_user_id = m.get('ownerUserId')

        if m.get('pinned') is not None:
            self.pinned = m.get('pinned')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('progressCompleted') is not None:
            self.progress_completed = m.get('progressCompleted')

        if m.get('progressTotal') is not None:
            self.progress_total = m.get('progressTotal')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sourceExecutionId') is not None:
            self.source_execution_id = m.get('sourceExecutionId')

        if m.get('sourceTaskId') is not None:
            self.source_task_id = m.get('sourceTaskId')

        if m.get('sourceTaskName') is not None:
            self.source_task_name = m.get('sourceTaskName')

        if m.get('sourceTriggerKey') is not None:
            self.source_trigger_key = m.get('sourceTriggerKey')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('triggerTimezone') is not None:
            self.trigger_timezone = m.get('triggerTimezone')

        if m.get('triggeredAt') is not None:
            self.triggered_at = m.get('triggeredAt')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        if m.get('visibilitySource') is not None:
            self.visibility_source = m.get('visibilitySource')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        if m.get('workflowStatus') is not None:
            self.workflow_status = m.get('workflowStatus')

        if m.get('workflowTemplateIds') is not None:
            self.workflow_template_ids = m.get('workflowTemplateIds')

        return self

class SetWorkItemPinnedResponseBodyAttachments(DaraModel):
    def __init__(
        self,
        attachment_id: str = None,
        content_type: str = None,
        ref_url: str = None,
        resource_id: str = None,
        resource_kind: str = None,
        size_bytes: int = None,
        title: str = None,
    ):
        # 附件ID
        self.attachment_id = attachment_id
        # 内容类型
        self.content_type = content_type
        # 附件访问入口（OpenAPI 302 前置）
        self.ref_url = ref_url
        # 附件资源ID
        self.resource_id = resource_id
        # 附件资源类型
        self.resource_kind = resource_kind
        # 附件大小(字节)
        self.size_bytes = size_bytes
        # 附件标题
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_id is not None:
            result['attachmentId'] = self.attachment_id

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.ref_url is not None:
            result['refUrl'] = self.ref_url

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_kind is not None:
            result['resourceKind'] = self.resource_kind

        if self.size_bytes is not None:
            result['sizeBytes'] = self.size_bytes

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachmentId') is not None:
            self.attachment_id = m.get('attachmentId')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('refUrl') is not None:
            self.ref_url = m.get('refUrl')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceKind') is not None:
            self.resource_kind = m.get('resourceKind')

        if m.get('sizeBytes') is not None:
            self.size_bytes = m.get('sizeBytes')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

