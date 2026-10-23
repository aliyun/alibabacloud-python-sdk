# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetTodoDetailResponseBody(DaraModel):
    def __init__(
        self,
        assignee_count: int = None,
        assignees: List[main_models.GetTodoDetailResponseBodyAssignees] = None,
        attachment_policy: Dict[str, Any] = None,
        code: str = None,
        completed_at: str = None,
        completed_by_user_id: str = None,
        completed_by_user_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_read: bool = None,
        message: str = None,
        message_id: str = None,
        my_assignee_status: str = None,
        my_display_state: str = None,
        my_permissions: Dict[str, Any] = None,
        priority: str = None,
        questions: List[main_models.GetTodoDetailResponseBodyQuestions] = None,
        request_id: str = None,
        result_payload: Dict[str, Any] = None,
        source_context: Dict[str, Any] = None,
        source_type: str = None,
        source_workflow_id: str = None,
        status: str = None,
        summary: str = None,
        title: str = None,
        todo_id: str = None,
    ):
        # The number of assignees.
        self.assignee_count = assignee_count
        # All assignees.
        self.assignees = assignees
        # The attachment policy. Attachments are not stored in the database in the current version.
        self.attachment_policy = attachment_policy
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The completion time in UTC+8 (YYYY-MM-DD HH:mm:ss).
        self.completed_at = completed_at
        # The user ID of the user who completed the item. This field is empty if the item is not completed.
        self.completed_by_user_id = completed_by_user_id
        # The name of the user who completed the item. This field is empty if the item is not completed.
        self.completed_by_user_name = completed_by_user_name
        # The creation time in UTC+8 (YYYY-MM-DD HH:mm:ss).
        self.gmt_create = gmt_create
        # The last modification time in UTC+8 (YYYY-MM-DD HH:mm:ss).
        self.gmt_modified = gmt_modified
        # Indicates whether the caller has read the item.
        self.is_read = is_read
        # The error description.
        self.message = message
        # The ID of the assistant message that generated the to-do item. This field is empty if there is no conversation source.
        self.message_id = message_id
        # The action status of the caller as the assignee.
        self.my_assignee_status = my_assignee_status
        # The list display status for the caller.
        self.my_display_state = my_display_state
        # The permissions of the caller, such as canSubmit and canTransfer.
        self.my_permissions = my_permissions
        # The priority.
        self.priority = priority
        # The list of questions (structured projection).
        self.questions = questions
        # The request tracking ID.
        self.request_id = request_id
        # The response content in JSONB format as-is. Defaults to an empty object if not submitted.
        self.result_payload = result_payload
        # The source context. This context is passed through as-is during creation.
        self.source_context = source_context
        # The source type of the to-do item.
        self.source_type = source_type
        # The workflow ID. This field is required when sourceType is set to WORKFLOW.
        self.source_workflow_id = source_workflow_id
        # The primary status of the to-do item.
        self.status = status
        # The summary of the to-do item.
        self.summary = summary
        # The title of the to-do item.
        self.title = title
        # The ID of the to-do item.
        self.todo_id = todo_id

    def validate(self):
        if self.assignees:
            for v1 in self.assignees:
                 if v1:
                    v1.validate()
        if self.questions:
            for v1 in self.questions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assignee_count is not None:
            result['assigneeCount'] = self.assignee_count

        result['assignees'] = []
        if self.assignees is not None:
            for k1 in self.assignees:
                result['assignees'].append(k1.to_map() if k1 else None)

        if self.attachment_policy is not None:
            result['attachmentPolicy'] = self.attachment_policy

        if self.code is not None:
            result['code'] = self.code

        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.completed_by_user_id is not None:
            result['completedByUserId'] = self.completed_by_user_id

        if self.completed_by_user_name is not None:
            result['completedByUserName'] = self.completed_by_user_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.is_read is not None:
            result['isRead'] = self.is_read

        if self.message is not None:
            result['message'] = self.message

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.my_assignee_status is not None:
            result['myAssigneeStatus'] = self.my_assignee_status

        if self.my_display_state is not None:
            result['myDisplayState'] = self.my_display_state

        if self.my_permissions is not None:
            result['myPermissions'] = self.my_permissions

        if self.priority is not None:
            result['priority'] = self.priority

        result['questions'] = []
        if self.questions is not None:
            for k1 in self.questions:
                result['questions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_payload is not None:
            result['resultPayload'] = self.result_payload

        if self.source_context is not None:
            result['sourceContext'] = self.source_context

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.source_workflow_id is not None:
            result['sourceWorkflowId'] = self.source_workflow_id

        if self.status is not None:
            result['status'] = self.status

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assigneeCount') is not None:
            self.assignee_count = m.get('assigneeCount')

        self.assignees = []
        if m.get('assignees') is not None:
            for k1 in m.get('assignees'):
                temp_model = main_models.GetTodoDetailResponseBodyAssignees()
                self.assignees.append(temp_model.from_map(k1))

        if m.get('attachmentPolicy') is not None:
            self.attachment_policy = m.get('attachmentPolicy')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('completedByUserId') is not None:
            self.completed_by_user_id = m.get('completedByUserId')

        if m.get('completedByUserName') is not None:
            self.completed_by_user_name = m.get('completedByUserName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('isRead') is not None:
            self.is_read = m.get('isRead')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('myAssigneeStatus') is not None:
            self.my_assignee_status = m.get('myAssigneeStatus')

        if m.get('myDisplayState') is not None:
            self.my_display_state = m.get('myDisplayState')

        if m.get('myPermissions') is not None:
            self.my_permissions = m.get('myPermissions')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        self.questions = []
        if m.get('questions') is not None:
            for k1 in m.get('questions'):
                temp_model = main_models.GetTodoDetailResponseBodyQuestions()
                self.questions.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultPayload') is not None:
            self.result_payload = m.get('resultPayload')

        if m.get('sourceContext') is not None:
            self.source_context = m.get('sourceContext')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('sourceWorkflowId') is not None:
            self.source_workflow_id = m.get('sourceWorkflowId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

class GetTodoDetailResponseBodyQuestions(DaraModel):
    def __init__(
        self,
        allow_custom: bool = None,
        custom_label: str = None,
        custom_max_length: int = None,
        custom_placeholder: str = None,
        max_length: int = None,
        mode: str = None,
        options: List[main_models.GetTodoDetailResponseBodyQuestionsOptions] = None,
        placeholder: str = None,
        question: str = None,
        required: bool = None,
    ):
        # Indicates whether custom input is allowed.
        self.allow_custom = allow_custom
        # The text for the custom input field.
        self.custom_label = custom_label
        # The maximum length for custom input.
        self.custom_max_length = custom_max_length
        # The placeholder for custom input.
        self.custom_placeholder = custom_placeholder
        # The maximum length for text questions.
        self.max_length = max_length
        # The response mode. Valid values: SINGLE_CHOICE, MULTI_CHOICE, and TEXT.
        self.mode = mode
        # The options. This field is required for choice questions.
        self.options = options
        # The placeholder for text questions.
        self.placeholder = placeholder
        # The question text (reference key).
        self.question = question
        # Indicates whether the question is required.
        self.required = required

    def validate(self):
        if self.options:
            for v1 in self.options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_custom is not None:
            result['allowCustom'] = self.allow_custom

        if self.custom_label is not None:
            result['customLabel'] = self.custom_label

        if self.custom_max_length is not None:
            result['customMaxLength'] = self.custom_max_length

        if self.custom_placeholder is not None:
            result['customPlaceholder'] = self.custom_placeholder

        if self.max_length is not None:
            result['maxLength'] = self.max_length

        if self.mode is not None:
            result['mode'] = self.mode

        result['options'] = []
        if self.options is not None:
            for k1 in self.options:
                result['options'].append(k1.to_map() if k1 else None)

        if self.placeholder is not None:
            result['placeholder'] = self.placeholder

        if self.question is not None:
            result['question'] = self.question

        if self.required is not None:
            result['required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowCustom') is not None:
            self.allow_custom = m.get('allowCustom')

        if m.get('customLabel') is not None:
            self.custom_label = m.get('customLabel')

        if m.get('customMaxLength') is not None:
            self.custom_max_length = m.get('customMaxLength')

        if m.get('customPlaceholder') is not None:
            self.custom_placeholder = m.get('customPlaceholder')

        if m.get('maxLength') is not None:
            self.max_length = m.get('maxLength')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        self.options = []
        if m.get('options') is not None:
            for k1 in m.get('options'):
                temp_model = main_models.GetTodoDetailResponseBodyQuestionsOptions()
                self.options.append(temp_model.from_map(k1))

        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')

        if m.get('question') is not None:
            self.question = m.get('question')

        if m.get('required') is not None:
            self.required = m.get('required')

        return self

class GetTodoDetailResponseBodyQuestionsOptions(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        recommended: bool = None,
    ):
        # The supplementary description of the option.
        self.description = description
        # The option text (reference key).
        self.label = label
        # Indicates whether the option is recommended.
        self.recommended = recommended

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.label is not None:
            result['label'] = self.label

        if self.recommended is not None:
            result['recommended'] = self.recommended

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('recommended') is not None:
            self.recommended = m.get('recommended')

        return self

class GetTodoDetailResponseBodyAssignees(DaraModel):
    def __init__(
        self,
        acted_at: str = None,
        assignee_source: str = None,
        assignee_user_id: str = None,
        read_at: str = None,
        status: str = None,
        transferred_from_user_id: str = None,
    ):
        # The action time in UTC+8. This field is empty if the item is not processed.
        self.acted_at = acted_at
        # The source of the assignee. Valid values: ORIGINAL and TRANSFERRED.
        self.assignee_source = assignee_source
        # The user ID of the assignee.
        self.assignee_user_id = assignee_user_id
        # The read time in UTC+8. This field is empty if the item is unread.
        self.read_at = read_at
        # The action status of the assignee.
        self.status = status
        # The user ID of the user who transferred the task. This field is populated only when the task is transferred.
        self.transferred_from_user_id = transferred_from_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acted_at is not None:
            result['actedAt'] = self.acted_at

        if self.assignee_source is not None:
            result['assigneeSource'] = self.assignee_source

        if self.assignee_user_id is not None:
            result['assigneeUserId'] = self.assignee_user_id

        if self.read_at is not None:
            result['readAt'] = self.read_at

        if self.status is not None:
            result['status'] = self.status

        if self.transferred_from_user_id is not None:
            result['transferredFromUserId'] = self.transferred_from_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actedAt') is not None:
            self.acted_at = m.get('actedAt')

        if m.get('assigneeSource') is not None:
            self.assignee_source = m.get('assigneeSource')

        if m.get('assigneeUserId') is not None:
            self.assignee_user_id = m.get('assigneeUserId')

        if m.get('readAt') is not None:
            self.read_at = m.get('readAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('transferredFromUserId') is not None:
            self.transferred_from_user_id = m.get('transferredFromUserId')

        return self

