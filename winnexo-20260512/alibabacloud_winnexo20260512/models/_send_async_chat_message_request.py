# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SendAsyncChatMessageRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        digital_employee_name: List[str] = None,
        direct_chat: bool = None,
        files: List[main_models.SendAsyncChatMessageRequestFiles] = None,
        model: str = None,
        reuse_last_session: bool = None,
        session_id: str = None,
        stream: bool = None,
        task_execution: main_models.SendAsyncChatMessageRequestTaskExecution = None,
        tenant_id: str = None,
    ):
        # 用户消息正文
        # 
        # This parameter is required.
        self.content = content
        # 消息类型：Text / Markdown
        self.content_type = content_type
        # 数字员工名称列表（兼容旧格式可传单个字符串）
        self.digital_employee_name = digital_employee_name
        # 是否启用直连模式；true 时跳过常规场景路由，直接进入直连对话场景
        self.direct_chat = direct_chat
        # 文件引用列表；每项为对象，fileId 必传（由 uploadChatFile 返回）
        self.files = files
        # 抽象模型档位（quick / standard / flagship）；缺省时新会话用 standard，已有会话沿用会话当前档位
        self.model = model
        # 不传 sessionId 时是否复用该数字员工下最近一个会话（CLI 场景），缺省 false 即新建会话
        self.reuse_last_session = reuse_last_session
        # 会话ID，不传则新建会话
        self.session_id = session_id
        # 是否流式生成；本接口固定按流式生成后台内容并写入消息流，取值不改变返回结构
        self.stream = stream
        # executeScheduledTask 返回的任务执行元数据；传入后按任务执行链路处理
        self.task_execution = task_execution
        # 租户ID，公共参数，缺省时使用调用方默认租户
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
                temp_model = main_models.SendAsyncChatMessageRequestFiles()
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
            temp_model = main_models.SendAsyncChatMessageRequestTaskExecution()
            self.task_execution = temp_model.from_map(m.get('taskExecution'))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class SendAsyncChatMessageRequestTaskExecution(DaraModel):
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
        # 计费 ID
        self.billing_id = billing_id
        # 是否启用联网搜索
        self.enable_web_search = enable_web_search
        # 执行记录 ID
        # 
        # This parameter is required.
        self.execution_id = execution_id
        # 数字员工名称
        self.operating_object_name = operating_object_name
        # 关联技能编码列表
        self.skill_codes = skill_codes
        # 任务 ID
        # 
        # This parameter is required.
        self.task_id = task_id
        # 任务名称
        self.task_name = task_name
        # 任务理解内容
        self.task_understand = task_understand
        # 任务所属租户 ID
        self.tenant_id = tenant_id
        # 任务所属用户 ID
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

class SendAsyncChatMessageRequestFiles(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        type: str = None,
    ):
        # 文件 ID，由 uploadChatFile 返回
        # 
        # This parameter is required.
        self.file_id = file_id
        # 文件类型
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

