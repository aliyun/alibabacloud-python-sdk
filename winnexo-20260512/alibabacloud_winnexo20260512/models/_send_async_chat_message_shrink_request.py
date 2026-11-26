# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class SendAsyncChatMessageShrinkRequest(DaraModel):
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
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # AUTO 偏好：none=默认、performance=效果优先、credit=成本优先；缺省或 null 继承会话，空白重置为 none
        self.auto_preference = auto_preference
        # The body of the user message.
        # 
        # This parameter is required.
        self.content = content
        # The message type. Valid values: Text and Markdown.
        self.content_type = content_type
        # The references and annotations for the current turn.
        self.context_items_shrink = context_items_shrink
        # The list of digital employee names. For compatibility with the old format, a single string can also be passed.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # **[Deprecated]** Use workMode=direct instead. If set to true, winnexo_chat is retained and processed in request-level direct mode.
        self.direct_chat = direct_chat
        # The maximum number of history rounds referenced in the current turn for the direct mode. Valid values: integers from 0 to 100. Default value: 0. Invalid values fall back to the original single-turn path. This parameter is ignored in non-direct modes.
        self.direct_max_history_rounds = direct_max_history_rounds
        # Specifies whether to enable web search. Default value: false. In the task execution scenario (when taskExecution is passed), the task configuration prevails.
        self.enable_web_search = enable_web_search
        # The list of file references. Each item is an object, and fileId is required (returned by uploadChatFile).
        self.files_shrink = files_shrink
        # The language for the current turn. Valid values: zh-CN and en-US. This parameter is used for API error messages and passed through to CodeAgent. If omitted, the current language behavior is retained and user settings are not modified.
        self.locale = locale
        # The model tier. Valid values: quick, standard, flagship, auto, or other currently available model names (case-insensitive). If not specified, the model tier of the session is inherited. For a new session, the default value is standard.
        self.model = model
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # Specifies whether to reuse the most recent session under the digital employee when sessionId is not provided (CLI scenario). Default value: false, which means a new session is created.
        self.reuse_last_session = reuse_last_session
        # The structured segments in the message, such as session or object mentions.
        self.segments_shrink = segments_shrink
        # The session ID. If not specified, a new session is created.
        self.session_id = session_id
        # Specifies whether to use streaming generation. This API always generates background content in streaming mode and writes it to the message stream. The value of this parameter does not change the response structure.
        self.stream = stream
        # The task execution metadata returned by executeScheduledTask. If passed, the request is processed through the task execution pipeline.
        self.task_execution_shrink = task_execution_shrink
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # 本轮显式覆盖是否思考；AUTO 未传时由决策模型判断，固定档未传时沿用个人设置，最终遵守模型能力与租户开关
        self.thinking_enabled = thinking_enabled
        # 本轮显式覆盖思考强度；AUTO 未传时由决策模型判断，固定档未传时沿用个人设置，最终遵守模型能力与租户开关
        self.thinking_level = thinking_level
        # The session work mode. Valid values: ask (quick Q&A), work (deep work, default), and direct (direct connection mode, which does not start the sandbox, uses independent direct history controlled by directMaxHistoryRounds, and is equivalent to directChat=true). The ask and work modes are session-level. For continued chats, the session mode is inherited by default. To switch modes, create a new session or fork. In multi-digital employee or task execution scenarios, if ask is passed, it takes effect as work. If directChat is set to true, this parameter is ignored.
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

