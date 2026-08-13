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
        files_shrink: str = None,
        model: str = None,
        reuse_last_session: bool = None,
        session_id: str = None,
        stream: bool = None,
        task_execution_shrink: str = None,
        tenant_id: str = None,
    ):
        # 用户消息正文
        # 
        # This parameter is required.
        self.content = content
        # 消息类型: Text / Markdown
        self.content_type = content_type
        # 数字员工名称列表（兼容旧格式可传单个字符串）
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # 是否启用直连模式；true 时跳过常规场景路由，直接进入直连对话场景
        self.direct_chat = direct_chat
        # 文件引用列表；每项为对象，fileId 必传（由 uploadChatFile 返回）
        self.files_shrink = files_shrink
        # 抽象模型档位（quick / standard / flagship）；缺省时新会话用 standard，已有会话沿用会话当前档位
        self.model = model
        # 不传 sessionId 时是否复用该数字员工下最近一个会话（CLI 场景），缺省 false 即新建会话
        self.reuse_last_session = reuse_last_session
        # 会话 ID
        self.session_id = session_id
        # 是否流式返回，默认True
        self.stream = stream
        # executeScheduledTask 返回的任务执行元数据；传入后按任务执行链路处理
        self.task_execution_shrink = task_execution_shrink
        # 租户ID，公共参数，缺省时使用调用方默认租户
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

