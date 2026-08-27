# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendAsyncChatMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        digital_employee_name_shrink: str = None,
        direct_chat: bool = None,
        files_shrink: str = None,
        model: str = None,
        reuse_last_session: bool = None,
        session_id: str = None,
        stream: bool = None,
        task_execution_shrink: str = None,
        tenant_id: str = None,
    ):
        # The message body from the user.
        # 
        # This parameter is required.
        self.content = content
        # The message type. Valid values: Text and Markdown.
        self.content_type = content_type
        # The list of digital employee names. A single string can be passed for backward compatibility with the legacy format.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # Specifies whether to enable direct chat mode. If set to true, the regular scenario routing is skipped and the direct chat scenario is entered.
        self.direct_chat = direct_chat
        # The list of file references. Each item is an object in which fileId is required and is returned by uploadChatFile.
        self.files_shrink = files_shrink
        # The abstract model tier. Valid values: quick, standard, and flagship. If not specified, new sessions use standard, and existing sessions retain their current tier.
        self.model = model
        # Specifies whether to reuse the most recent session of the digital employee when sessionId is not specified. This is designed for CLI scenarios. Default value: false, which creates a new session.
        self.reuse_last_session = reuse_last_session
        # The session ID. If not specified, a new session is created.
        self.session_id = session_id
        # Specifies whether to use streaming generation. This operation always generates backend content in streaming mode and writes it to the message stream. The value does not change the response structure.
        self.stream = stream
        # The task execution metadata returned by executeScheduledTask. When provided, the request is processed through the task execution pipeline.
        self.task_execution_shrink = task_execution_shrink
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.digital_employee_name_shrink is not None:
            result['digitalEmployeeName'] = self.digital_employee_name_shrink

        if self.direct_chat is not None:
            result['directChat'] = self.direct_chat

        if self.files_shrink is not None:
            result['files'] = self.files_shrink

        if self.model is not None:
            result['model'] = self.model

        if self.reuse_last_session is not None:
            result['reuseLastSession'] = self.reuse_last_session

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.stream is not None:
            result['stream'] = self.stream

        if self.task_execution_shrink is not None:
            result['taskExecution'] = self.task_execution_shrink

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
            self.digital_employee_name_shrink = m.get('digitalEmployeeName')

        if m.get('directChat') is not None:
            self.direct_chat = m.get('directChat')

        if m.get('files') is not None:
            self.files_shrink = m.get('files')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('reuseLastSession') is not None:
            self.reuse_last_session = m.get('reuseLastSession')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('taskExecution') is not None:
            self.task_execution_shrink = m.get('taskExecution')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

