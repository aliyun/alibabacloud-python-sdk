# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetScheduledTaskExecutionDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        completed_at: str = None,
        content: str = None,
        creator: str = None,
        digital_employee_name: List[str] = None,
        error_message: str = None,
        execution_id: str = None,
        files: List[main_models.GetScheduledTaskExecutionDetailResponseBodyFiles] = None,
        gmt_create: str = None,
        message: str = None,
        metadata: main_models.GetScheduledTaskExecutionDetailResponseBodyMetadata = None,
        output_content: str = None,
        push_result: str = None,
        request_id: str = None,
        skill_codes: List[str] = None,
        started_at: str = None,
        status: str = None,
        task_id: str = None,
        title: str = None,
        trigger_info: main_models.GetScheduledTaskExecutionDetailResponseBodyTriggerInfo = None,
        trigger_type: str = None,
        visibility: str = None,
    ):
        # The status code.
        self.code = code
        # The completion time in ISO 8601 format.
        self.completed_at = completed_at
        # The full execution content.
        self.content = content
        # The creator.
        self.creator = creator
        # The list of digital employee names.
        self.digital_employee_name = digital_employee_name
        # The error message.
        self.error_message = error_message
        # The execution ID.
        self.execution_id = execution_id
        # The list of output files.
        self.files = files
        # The creation time in ISO 8601 format.
        self.gmt_create = gmt_create
        # The status code description.
        self.message = message
        # The extended metadata.
        self.metadata = metadata
        # The structured output content.
        self.output_content = output_content
        # The push status of the execution result.
        self.push_result = push_result
        # The request ID.
        self.request_id = request_id
        # The list of associated skill codes.
        self.skill_codes = skill_codes
        # The start time in ISO 8601 format.
        self.started_at = started_at
        # The execution status.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The execution result title.
        self.title = title
        # The trigger information.
        self.trigger_info = trigger_info
        # The trigger type.
        self.trigger_type = trigger_type
        # The visibility scope of the execution record, which is always equal to the visibility scope of the associated task. Valid values: PRIVATE, COLLABORATIVE, and PUBLIC. This field is empty for personal task executions.
        self.visibility = visibility

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()
        if self.metadata:
            self.metadata.validate()
        if self.trigger_info:
            self.trigger_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.content is not None:
            result['content'] = self.content

        if self.creator is not None:
            result['creator'] = self.creator

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.execution_id is not None:
            result['executionId'] = self.execution_id

        result['files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['files'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.message is not None:
            result['message'] = self.message

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.output_content is not None:
            result['outputContent'] = self.output_content

        if self.push_result is not None:
            result['pushResult'] = self.push_result

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.skill_codes is not None:
            result['skillCodes'] = self.skill_codes

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.title is not None:
            result['title'] = self.title

        if self.trigger_info is not None:
            result['triggerInfo'] = self.trigger_info.to_map()

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        if self.visibility is not None:
            result['visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')

        self.files = []
        if m.get('files') is not None:
            for k1 in m.get('files'):
                temp_model = main_models.GetScheduledTaskExecutionDetailResponseBodyFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('metadata') is not None:
            temp_model = main_models.GetScheduledTaskExecutionDetailResponseBodyMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('outputContent') is not None:
            self.output_content = m.get('outputContent')

        if m.get('pushResult') is not None:
            self.push_result = m.get('pushResult')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('skillCodes') is not None:
            self.skill_codes = m.get('skillCodes')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('triggerInfo') is not None:
            temp_model = main_models.GetScheduledTaskExecutionDetailResponseBodyTriggerInfo()
            self.trigger_info = temp_model.from_map(m.get('triggerInfo'))

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        return self

class GetScheduledTaskExecutionDetailResponseBodyTriggerInfo(DaraModel):
    def __init__(
        self,
        triggered_by: str = None,
    ):
        # The user identifier that triggered the execution.
        self.triggered_by = triggered_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.triggered_by is not None:
            result['triggeredBy'] = self.triggered_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('triggeredBy') is not None:
            self.triggered_by = m.get('triggeredBy')

        return self

class GetScheduledTaskExecutionDetailResponseBodyMetadata(DaraModel):
    def __init__(
        self,
        session_id: str = None,
        usage: Dict[str, Any] = None,
    ):
        # The session ID.
        self.session_id = session_id
        # The token usage information.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

class GetScheduledTaskExecutionDetailResponseBodyFiles(DaraModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
    ):
        # The file name.
        self.name = name
        # The OSS URL of the file.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

