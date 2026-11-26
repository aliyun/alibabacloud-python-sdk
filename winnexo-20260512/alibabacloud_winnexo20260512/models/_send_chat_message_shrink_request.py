# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class SendChatMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        auto_preference: str = None,
        content: str = None,
        content_type: str = None,
        context_items_shrink: str = None,
        digital_employee_name_shrink: str = None,
        direct_chat: bool = None,
        direct_max_history_rounds: Any = None,
        enable_web_search: bool = None,
        files_shrink: str = None,
        locale: str = None,
        model: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        reuse_last_session: bool = None,
        segments_shrink: str = None,
        session_id: str = None,
        stream: bool = None,
        task_execution_shrink: str = None,
        tenant_id: str = None,
        thinking_enabled: bool = None,
        thinking_level: str = None,
        work_mode: str = None,
    ):
        # The platform application token issued by the console. If this parameter is passed, the operation is executed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The AUTO preference. Valid values: none (default), performance (effect first), and credit (cost first). If this parameter is omitted or set to null, the session preference is inherited. If it is left blank, it is reset to none.
        self.auto_preference = auto_preference
        # The body of the user message.
        # 
        # This parameter is required.
        self.content = content
        # The message type. Valid values: Text and Markdown.
        self.content_type = content_type
        # The message or file entries referenced as context for the current turn.
        self.context_items_shrink = context_items_shrink
        # The list of digital employee names. For compatibility with the old format, a single string can also be passed.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # Specifies whether to enable direct connection mode. If this parameter is set to true, regular scenario routing is skipped and the direct conversation scenario is entered directly.
        self.direct_chat = direct_chat
        # The number of recent complete direct Q&A rounds carried in the current turn, excluding the input of the current turn. This parameter takes effect only when workMode is set to direct or directChat is set to true. Valid values: JSON integers from 0 to 100. If this parameter is omitted, the backend processes it as 0, carrying no history but still saving the current turn. Null, Boolean values, strings, decimals, and out-of-bounds values are processed through the original direct path, and the gateway retains the original values for backend determination. This field is ignored in work and ask modes. This parameter does not limit the history range when switching to the work mode.
        self.direct_max_history_rounds = direct_max_history_rounds
        # Specifies whether to enable web search. Default value: false. In the task execution scenario where taskExecution is passed, the task configuration prevails.
        self.enable_web_search = enable_web_search
        # The list of file references. Each item is an object, and fileId is required, which is returned by uploadChatFile.
        self.files_shrink = files_shrink
        # The language for the current turn. Valid values: zh-CN and en-US. This parameter is used for API error messages and passed through to CodeAgent. If this parameter is omitted, the current language behavior is retained and the user settings are not modified.
        self.locale = locale
        # The abstract model tier. Valid values: quick, standard, and flagship. If this parameter is omitted, standard is used for new sessions, and the current tier is retained for existing sessions.
        self.model = model
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # Specifies whether to reuse the most recent session under the digital employee when sessionId is not passed, which applies to CLI scenarios. Default value: false, which means a new session is created.
        self.reuse_last_session = reuse_last_session
        # The structured segments in the message, such as session or object mentions.
        self.segments_shrink = segments_shrink
        # The session ID.
        self.session_id = session_id
        # Specifies whether to use streaming output.
        self.stream = stream
        # The task execution metadata returned by executeScheduledTask. If this parameter is passed, the request is processed through the task execution pipeline.
        self.task_execution_shrink = task_execution_shrink
        # The effective tenant ID.
        self.tenant_id = tenant_id
        # Specifies whether to explicitly override the thinking mode for the current turn. If this parameter is not passed in AUTO mode, the decision model determines the behavior. If it is not passed in fixed tier mode, the personal settings are retained. The final behavior complies with the model capabilities and tenant switches.
        self.thinking_enabled = thinking_enabled
        # The explicit override for the thinking intensity in the current turn. If this parameter is not passed in AUTO mode, the decision model determines the behavior. If it is not passed in fixed tier mode, the personal settings are retained. The final behavior complies with the model capabilities and tenant switches.
        self.thinking_level = thinking_level
        # The session work mode. Valid values: ask (quick Q&A, which trims tools, skills, and connectors for single-turn direct answers), work (deep work, which is the default), and direct (direct connection mode at the request level, which does not start the sandbox and prevents context pollution, equivalent to directChat=true). The ask and work modes are session-level. The mode is fixed when a new session is created. Subsequent chats inherit the session mode by default. If the explicitly passed value is inconsistent with the session mode, a parameter error is returned. To switch modes, create a new session or fork the current one. If ask is passed in multi-digital employee or task execution scenarios, it takes effect as work. If directChat is set to true, this parameter is ignored.
        self.work_mode = work_mode

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

        if self.content is not None:
            result['content'] = self.content

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.context_items_shrink is not None:
            result['contextItems'] = self.context_items_shrink

        if self.digital_employee_name_shrink is not None:
            result['digitalEmployeeName'] = self.digital_employee_name_shrink

        if self.direct_chat is not None:
            result['directChat'] = self.direct_chat

        if self.direct_max_history_rounds is not None:
            result['directMaxHistoryRounds'] = self.direct_max_history_rounds

        if self.enable_web_search is not None:
            result['enableWebSearch'] = self.enable_web_search

        if self.files_shrink is not None:
            result['files'] = self.files_shrink

        if self.locale is not None:
            result['locale'] = self.locale

        if self.model is not None:
            result['model'] = self.model

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.reuse_last_session is not None:
            result['reuseLastSession'] = self.reuse_last_session

        if self.segments_shrink is not None:
            result['segments'] = self.segments_shrink

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.stream is not None:
            result['stream'] = self.stream

        if self.task_execution_shrink is not None:
            result['taskExecution'] = self.task_execution_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.thinking_enabled is not None:
            result['thinkingEnabled'] = self.thinking_enabled

        if self.thinking_level is not None:
            result['thinkingLevel'] = self.thinking_level

        if self.work_mode is not None:
            result['workMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('autoPreference') is not None:
            self.auto_preference = m.get('autoPreference')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('contextItems') is not None:
            self.context_items_shrink = m.get('contextItems')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name_shrink = m.get('digitalEmployeeName')

        if m.get('directChat') is not None:
            self.direct_chat = m.get('directChat')

        if m.get('directMaxHistoryRounds') is not None:
            self.direct_max_history_rounds = m.get('directMaxHistoryRounds')

        if m.get('enableWebSearch') is not None:
            self.enable_web_search = m.get('enableWebSearch')

        if m.get('files') is not None:
            self.files_shrink = m.get('files')

        if m.get('locale') is not None:
            self.locale = m.get('locale')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('reuseLastSession') is not None:
            self.reuse_last_session = m.get('reuseLastSession')

        if m.get('segments') is not None:
            self.segments_shrink = m.get('segments')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('taskExecution') is not None:
            self.task_execution_shrink = m.get('taskExecution')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('thinkingEnabled') is not None:
            self.thinking_enabled = m.get('thinkingEnabled')

        if m.get('thinkingLevel') is not None:
            self.thinking_level = m.get('thinkingLevel')

        if m.get('workMode') is not None:
            self.work_mode = m.get('workMode')

        return self

