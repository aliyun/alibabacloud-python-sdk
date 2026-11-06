# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendChatMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        digital_employee_name_shrink: str = None,
        direct_chat: bool = None,
        enable_web_search: bool = None,
        files_shrink: str = None,
        model: str = None,
        reuse_last_session: bool = None,
        session_id: str = None,
        stream: bool = None,
        task_execution_shrink: str = None,
        tenant_id: str = None,
        work_mode: str = None,
    ):
        # The body of the user message.
        # 
        # This parameter is required.
        self.content = content
        # The message type. Valid values: Text and Markdown.
        self.content_type = content_type
        # The list of digital employee names. For compatibility with the legacy format, a single string can be passed.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # Specifies whether to enable the direct connection mode. If this parameter is set to true, the regular scenario routing is skipped and the direct connection conversation scenario is directly entered.
        self.direct_chat = direct_chat
        # Specifies whether to enable web search. Default value: false. In the task execution scenario where taskExecution is passed, the task configuration prevails.
        self.enable_web_search = enable_web_search
        # The list of file references. Each item is an object, and the fileId parameter is required, which is returned by uploadChatFile.
        self.files_shrink = files_shrink
        # The abstract model tier. Valid values: quick, standard, and flagship. If this parameter is not specified, standard is used for new sessions, and the current tier is used for existing sessions.
        self.model = model
        # Specifies whether to reuse the most recent session under the digital employee when sessionId is not passed, which applies to CLI scenarios. Default value: false, which indicates that a new session is created.
        self.reuse_last_session = reuse_last_session
        # The session ID.
        self.session_id = session_id
        # Specifies whether to enable streaming output.
        self.stream = stream
        # The task execution metadata returned by executeScheduledTask. If this parameter is passed, the request is processed according to the task execution link.
        self.task_execution_shrink = task_execution_shrink
        # The effective tenant ID.
        self.tenant_id = tenant_id
        # The session work mode. Valid values: ask (quick Q&A, which trims tools, skills, and connectors for single-turn direct answers), work (deep work, which is the default value), and direct (direct connection mode at the request level, which does not start the sandbox and prevents context pollution, equivalent to directChat=true). The ask and work modes are at the session level. The mode is fixed when a new session is created. Subsequent chats inherit the session mode by default. If the explicitly passed value is inconsistent with the session mode, a parameter error is returned. To switch the mode, create a new session or fork the session. If ask is passed in the multi-digital employee or task execution scenario, it takes effect as work. If directChat is set to true, this parameter is ignored.
        self.work_mode = work_mode

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

        if self.enable_web_search is not None:
            result['enableWebSearch'] = self.enable_web_search

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

        if self.work_mode is not None:
            result['workMode'] = self.work_mode

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

        if m.get('enableWebSearch') is not None:
            self.enable_web_search = m.get('enableWebSearch')

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

        if m.get('workMode') is not None:
            self.work_mode = m.get('workMode')

        return self

