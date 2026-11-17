# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SendChatMessageRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        context_items: List[main_models.SendChatMessageRequestContextItems] = None,
        digital_employee_name: List[str] = None,
        direct_chat: bool = None,
        direct_max_history_rounds: Any = None,
        enable_web_search: bool = None,
        files: List[main_models.SendChatMessageRequestFiles] = None,
        locale: str = None,
        model: str = None,
        reuse_last_session: bool = None,
        segments: List[main_models.SendChatMessageRequestSegments] = None,
        session_id: str = None,
        stream: bool = None,
        task_execution: main_models.SendChatMessageRequestTaskExecution = None,
        tenant_id: str = None,
        work_mode: str = None,
    ):
        # The body of the user message.
        # 
        # This parameter is required.
        self.content = content
        # The message type. Valid values: Text and Markdown.
        self.content_type = content_type
        # 作为本轮上下文引用的消息或文件条目
        self.context_items = context_items
        # The list of digital employee names. For compatibility with the legacy format, a single string can be passed.
        self.digital_employee_name = digital_employee_name
        # Specifies whether to enable the direct connection mode. If this parameter is set to true, the regular scenario routing is skipped and the direct connection conversation scenario is directly entered.
        self.direct_chat = direct_chat
        # 本轮携带的最近完整 direct 问答轮数，不含本轮输入。仅 workMode=direct 或 directChat=true 时生效。有效值为 0–100 的 JSON 整数，省略时由后端按 0 处理，不携带历史但仍保存当前轮。null、布尔值、字符串、小数及越界值按原 direct 路径处理，网关保留原始值供后端判定。work/ask 忽略此字段。该参数不限制转换为 work 时的历史范围
        self.direct_max_history_rounds = direct_max_history_rounds
        # Specifies whether to enable web search. Default value: false. In the task execution scenario where taskExecution is passed, the task configuration prevails.
        self.enable_web_search = enable_web_search
        # The list of file references. Each item is an object, and the fileId parameter is required, which is returned by uploadChatFile.
        self.files = files
        # 本轮语言，可选 zh-CN、en-US，用于接口错误文案并透传给 CodeAgent；省略时沿用当前语言行为，不修改用户设置
        self.locale = locale
        # The abstract model tier. Valid values: quick, standard, and flagship. If this parameter is not specified, standard is used for new sessions, and the current tier is used for existing sessions.
        self.model = model
        # Specifies whether to reuse the most recent session under the digital employee when sessionId is not passed, which applies to CLI scenarios. Default value: false, which indicates that a new session is created.
        self.reuse_last_session = reuse_last_session
        # 消息中的结构化片段，例如会话或对象提及
        self.segments = segments
        # The session ID.
        self.session_id = session_id
        # Specifies whether to enable streaming output.
        self.stream = stream
        # The task execution metadata returned by executeScheduledTask. If this parameter is passed, the request is processed according to the task execution link.
        self.task_execution = task_execution
        # The effective tenant ID.
        self.tenant_id = tenant_id
        # The session work mode. Valid values: ask (quick Q&A, which trims tools, skills, and connectors for single-turn direct answers), work (deep work, which is the default value), and direct (direct connection mode at the request level, which does not start the sandbox and prevents context pollution, equivalent to directChat=true). The ask and work modes are at the session level. The mode is fixed when a new session is created. Subsequent chats inherit the session mode by default. If the explicitly passed value is inconsistent with the session mode, a parameter error is returned. To switch the mode, create a new session or fork the session. If ask is passed in the multi-digital employee or task execution scenario, it takes effect as work. If directChat is set to true, this parameter is ignored.
        self.work_mode = work_mode

    def validate(self):
        if self.context_items:
            for v1 in self.context_items:
                 if v1:
                    v1.validate()
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()
        if self.segments:
            for v1 in self.segments:
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

        result['contextItems'] = []
        if self.context_items is not None:
            for k1 in self.context_items:
                result['contextItems'].append(k1.to_map() if k1 else None)

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.direct_chat is not None:
            result['directChat'] = self.direct_chat

        if self.direct_max_history_rounds is not None:
            result['directMaxHistoryRounds'] = self.direct_max_history_rounds

        if self.enable_web_search is not None:
            result['enableWebSearch'] = self.enable_web_search

        result['files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['files'].append(k1.to_map() if k1 else None)

        if self.locale is not None:
            result['locale'] = self.locale

        if self.model is not None:
            result['model'] = self.model

        if self.reuse_last_session is not None:
            result['reuseLastSession'] = self.reuse_last_session

        result['segments'] = []
        if self.segments is not None:
            for k1 in self.segments:
                result['segments'].append(k1.to_map() if k1 else None)

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.stream is not None:
            result['stream'] = self.stream

        if self.task_execution is not None:
            result['taskExecution'] = self.task_execution.to_map()

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

        self.context_items = []
        if m.get('contextItems') is not None:
            for k1 in m.get('contextItems'):
                temp_model = main_models.SendChatMessageRequestContextItems()
                self.context_items.append(temp_model.from_map(k1))

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('directChat') is not None:
            self.direct_chat = m.get('directChat')

        if m.get('directMaxHistoryRounds') is not None:
            self.direct_max_history_rounds = m.get('directMaxHistoryRounds')

        if m.get('enableWebSearch') is not None:
            self.enable_web_search = m.get('enableWebSearch')

        self.files = []
        if m.get('files') is not None:
            for k1 in m.get('files'):
                temp_model = main_models.SendChatMessageRequestFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('locale') is not None:
            self.locale = m.get('locale')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('reuseLastSession') is not None:
            self.reuse_last_session = m.get('reuseLastSession')

        self.segments = []
        if m.get('segments') is not None:
            for k1 in m.get('segments'):
                temp_model = main_models.SendChatMessageRequestSegments()
                self.segments.append(temp_model.from_map(k1))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('taskExecution') is not None:
            temp_model = main_models.SendChatMessageRequestTaskExecution()
            self.task_execution = temp_model.from_map(m.get('taskExecution'))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('workMode') is not None:
            self.work_mode = m.get('workMode')

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
        # The name of the digital employee.
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
        # The ID of the tenant to which the task belongs.
        self.tenant_id = tenant_id
        # The ID of the user to which the task belongs.
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

class SendChatMessageRequestSegments(DaraModel):
    def __init__(
        self,
        content: str = None,
        mention_type: str = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
        session_type: str = None,
        type: str = None,
    ):
        # 片段展示内容
        self.content = content
        # 提及对象类别
        self.mention_type = mention_type
        # 被引用对象名称
        self.name = name
        # 被引用对象 ID
        self.object_id = object_id
        # 被引用对象类型
        self.object_type = object_type
        # 会话类型
        self.session_type = session_type
        # 片段类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.mention_type is not None:
            result['mentionType'] = self.mention_type

        if self.name is not None:
            result['name'] = self.name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.session_type is not None:
            result['sessionType'] = self.session_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('mentionType') is not None:
            self.mention_type = m.get('mentionType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('sessionType') is not None:
            self.session_type = m.get('sessionType')

        if m.get('type') is not None:
            self.type = m.get('type')

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

class SendChatMessageRequestContextItems(DaraModel):
    def __init__(
        self,
        annotation: str = None,
        annotation_files: List[main_models.SendChatMessageRequestContextItemsAnnotationFiles] = None,
        content: str = None,
        file_id: str = None,
        file_name: str = None,
        file_type: str = None,
        message_id: str = None,
        sender_name: str = None,
        type: str = None,
    ):
        # 用户对引用内容的批注
        self.annotation = annotation
        # 批注关联的文件列表
        self.annotation_files = annotation_files
        # 被引用内容正文
        self.content = content
        # 被引用文件 ID
        self.file_id = file_id
        # 被引用文件名称
        self.file_name = file_name
        # 被引用文件类型
        self.file_type = file_type
        # 被引用消息 ID
        self.message_id = message_id
        # 消息发送者名称
        self.sender_name = sender_name
        # 上下文条目类型
        self.type = type

    def validate(self):
        if self.annotation_files:
            for v1 in self.annotation_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation is not None:
            result['annotation'] = self.annotation

        result['annotationFiles'] = []
        if self.annotation_files is not None:
            for k1 in self.annotation_files:
                result['annotationFiles'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['content'] = self.content

        if self.file_id is not None:
            result['fileId'] = self.file_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.sender_name is not None:
            result['senderName'] = self.sender_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotation') is not None:
            self.annotation = m.get('annotation')

        self.annotation_files = []
        if m.get('annotationFiles') is not None:
            for k1 in m.get('annotationFiles'):
                temp_model = main_models.SendChatMessageRequestContextItemsAnnotationFiles()
                self.annotation_files.append(temp_model.from_map(k1))

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('senderName') is not None:
            self.sender_name = m.get('senderName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class SendChatMessageRequestContextItemsAnnotationFiles(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_public_url: str = None,
        file_record_id: str = None,
        file_url: str = None,
    ):
        # 文件名称
        self.file_name = file_name
        # 文件公开访问地址
        self.file_public_url = file_public_url
        # 文件记录 ID
        self.file_record_id = file_record_id
        # 文件内部访问地址
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_public_url is not None:
            result['filePublicUrl'] = self.file_public_url

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('filePublicUrl') is not None:
            self.file_public_url = m.get('filePublicUrl')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        return self

