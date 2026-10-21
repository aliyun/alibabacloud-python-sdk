# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class CreateCopilotConversationResponseBody(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        conversation: main_models.CreateCopilotConversationResponseBodyConversation = None,
        request_id: str = None,
    ):
        # The API version number. The value is 1.0.0.
        self.api_version = api_version
        # The conversation timestamp.
        self.conversation = conversation
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.conversation:
            self.conversation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version

        if self.conversation is not None:
            result['Conversation'] = self.conversation.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')

        if m.get('Conversation') is not None:
            temp_model = main_models.CreateCopilotConversationResponseBodyConversation()
            self.conversation = temp_model.from_map(m.get('Conversation'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateCopilotConversationResponseBodyConversation(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        created_at: str = None,
        feedback: int = None,
        model: str = None,
        plan_mode: str = None,
        project_id: str = None,
        scheduled_task_id: str = None,
        status: str = None,
        thinking_mode: str = None,
        title: str = None,
        updated_at: str = None,
        visibility: str = None,
    ):
        # The security operations Agent session ID.
        self.conversation_id = conversation_id
        # The creation time. The time follows the ISO 8601 standard in UTC.
        self.created_at = created_at
        # The returned conversation information.
        self.feedback = feedback
        # The model configuration.
        self.model = model
        # Specifies whether planning is enabled. Valid values: disable, enable, force. Default value: enable.
        self.plan_mode = plan_mode
        # The security project ID.
        self.project_id = project_id
        # The ID of the scheduled task. The ID is system-generated and globally unique.
        self.scheduled_task_id = scheduled_task_id
        # The status.
        self.status = status
        # The thinking mode configuration.
        self.thinking_mode = thinking_mode
        # The session title.
        self.title = title
        # The update time.
        self.updated_at = updated_at
        # The session visibility.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.model is not None:
            result['Model'] = self.model

        if self.plan_mode is not None:
            result['PlanMode'] = self.plan_mode

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id

        if self.status is not None:
            result['Status'] = self.status

        if self.thinking_mode is not None:
            result['ThinkingMode'] = self.thinking_mode

        if self.title is not None:
            result['Title'] = self.title

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('PlanMode') is not None:
            self.plan_mode = m.get('PlanMode')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThinkingMode') is not None:
            self.thinking_mode = m.get('ThinkingMode')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

