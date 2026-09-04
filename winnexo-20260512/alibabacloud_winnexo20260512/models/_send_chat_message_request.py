# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SendChatMessageRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        digital_employee_name: List[str] = None,
        direct_chat: bool = None,
        files: List[main_models.SendChatMessageRequestFiles] = None,
        model: str = None,
        reuse_last_session: bool = None,
        session_id: str = None,
        stream: bool = None,
        task_execution: main_models.SendChatMessageRequestTaskExecution = None,
        tenant_id: str = None,
    ):
        # The message body from the user.
        # 
        # This parameter is required.
        self.content = content
        # The message type. Valid values: Text and Markdown.
        self.content_type = content_type
        # The list of digital employee names. A single string can be passed for backward compatibility with the legacy format.
        self.digital_employee_name = digital_employee_name
        # Specifies whether to enable direct connection mode. If set to true, the regular scenario routing is skipped and the direct conversation scenario is entered.
        self.direct_chat = direct_chat
        # The list of file references. Each item is an object in which fileId is required and is returned by uploadChatFile.
        self.files = files
        # The abstract model tier. Valid values: quick, standard, and flagship. If not specified, new sessions use standard, and existing sessions retain the current session tier.
        self.model = model
        # Specifies whether to reuse the most recent session of the digital employee when sessionId is not provided (CLI scenario). Default value: false, which creates a new session.
        self.reuse_last_session = reuse_last_session
        # The session ID.
        self.session_id = session_id
        # Specifies whether to use streaming output.
        self.stream = stream
        # The task execution metadata returned by executeScheduledTask. When provided, the request is processed through the task execution pipeline.
        self.task_execution = task_execution
        # The effective tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()
        if self.task_execution:
            self.task_execution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.direct_chat is not None:
            result['directChat'] = self.direct_chat

        result['files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['files'].append(k1.to_map() if k1 else None)

        if self.model is not None:
            result['model'] = self.model

        if self.reuse_last_session is not None:
            result['reuseLastSession'] = self.reuse_last_session

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.stream is not None:
            result['stream'] = self.stream

        if self.task_execution is not None:
            result['taskExecution'] = self.task_execution.to_map()

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('directChat') is not None:
            self.direct_chat = m.get('directChat')

        self.files = []
        if m.get('files') is not None:
            for k1 in m.get('files'):
                temp_model = main_models.SendChatMessageRequestFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('reuseLastSession') is not None:
            self.reuse_last_session = m.get('reuseLastSession')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('taskExecution') is not None:
            temp_model = main_models.SendChatMessageRequestTaskExecution()
            self.task_execution = temp_model.from_map(m.get('taskExecution'))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class SendChatMessageRequestTaskExecution(DaraModel):
    def __init__(
        self,
        billing_id: str = None,
        enable_web_search: bool = None,
        execution_id: str = None,
        operating_object_name: str = None,
        skill_codes: List[str] = None,
        task_id: str = None,
        task_name: str = None,
        task_understand: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        # The billing ID.
        self.billing_id = billing_id
        # Specifies whether to enable web search.
        self.enable_web_search = enable_web_search
        # The execution record ID.
        # 
        # This parameter is required.
        self.execution_id = execution_id
        # The digital employee name.
        self.operating_object_name = operating_object_name
        # The list of associated skill codes.
        self.skill_codes = skill_codes
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name
        # The task understanding content.
        self.task_understand = task_understand
        # The tenant ID to which the task belongs.
        self.tenant_id = tenant_id
        # The user ID to which the task belongs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_id is not None:
            result['billingId'] = self.billing_id

        if self.enable_web_search is not None:
            result['enableWebSearch'] = self.enable_web_search

        if self.execution_id is not None:
            result['executionId'] = self.execution_id

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.skill_codes is not None:
            result['skillCodes'] = self.skill_codes

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.task_understand is not None:
            result['taskUnderstand'] = self.task_understand

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingId') is not None:
            self.billing_id = m.get('billingId')

        if m.get('enableWebSearch') is not None:
            self.enable_web_search = m.get('enableWebSearch')

        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('skillCodes') is not None:
            self.skill_codes = m.get('skillCodes')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('taskUnderstand') is not None:
            self.task_understand = m.get('taskUnderstand')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class SendChatMessageRequestFiles(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        type: str = None,
    ):
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The element type. Valid values: text, web_search, mention, and skill.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['fileId'] = self.file_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

