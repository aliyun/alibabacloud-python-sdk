# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SendAsyncChatMessageRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        auto_preference: str = None,
        content: str = None,
        content_type: str = None,
        context_items: List[main_models.SendAsyncChatMessageRequestContextItems] = None,
        digital_employee_name: List[str] = None,
        direct_chat: bool = None,
        direct_max_history_rounds: Any = None,
        enable_web_search: bool = None,
        files: List[main_models.SendAsyncChatMessageRequestFiles] = None,
        locale: str = None,
        model: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        reuse_last_session: bool = None,
        segments: List[main_models.SendAsyncChatMessageRequestSegments] = None,
        session_id: str = None,
        stream: bool = None,
        task_execution: main_models.SendAsyncChatMessageRequestTaskExecution = None,
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
        self.context_items = context_items
        # The list of digital employee names. For compatibility with the old format, a single string can also be passed.
        self.digital_employee_name = digital_employee_name
        # **[Deprecated]** Use workMode=direct instead. If set to true, winnexo_chat is retained and processed in request-level direct mode.
        self.direct_chat = direct_chat
        # The maximum number of history rounds referenced in the current turn for the direct mode. Valid values: integers from 0 to 100. Default value: 0. Invalid values fall back to the original single-turn path. This parameter is ignored in non-direct modes.
        self.direct_max_history_rounds = direct_max_history_rounds
        # Specifies whether to enable web search. Default value: false. In the task execution scenario (when taskExecution is passed), the task configuration prevails.
        self.enable_web_search = enable_web_search
        # The list of file references. Each item is an object, and fileId is required (returned by uploadChatFile).
        self.files = files
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
        self.segments = segments
        # The session ID. If not specified, a new session is created.
        self.session_id = session_id
        # Specifies whether to use streaming generation. This API always generates background content in streaming mode and writes it to the message stream. The value of this parameter does not change the response structure.
        self.stream = stream
        # The task execution metadata returned by executeScheduledTask. If passed, the request is processed through the task execution pipeline.
        self.task_execution = task_execution
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # 本轮显式覆盖是否思考；AUTO 未传时由决策模型判断，固定档未传时沿用个人设置，最终遵守模型能力与租户开关
        self.thinking_enabled = thinking_enabled
        # 本轮显式覆盖思考强度；AUTO 未传时由决策模型判断，固定档未传时沿用个人设置，最终遵守模型能力与租户开关
        self.thinking_level = thinking_level
        # The session work mode. Valid values: ask (quick Q&A), work (deep work, default), and direct (direct connection mode, which does not start the sandbox, uses independent direct history controlled by directMaxHistoryRounds, and is equivalent to directChat=true). The ask and work modes are session-level. For continued chats, the session mode is inherited by default. To switch modes, create a new session or fork. In multi-digital employee or task execution scenarios, if ask is passed, it takes effect as work. If directChat is set to true, this parameter is ignored.
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
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.auto_preference is not None:
            result['autoPreference'] = self.auto_preference

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

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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

        self.context_items = []
        if m.get('contextItems') is not None:
            for k1 in m.get('contextItems'):
                temp_model = main_models.SendAsyncChatMessageRequestContextItems()
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
                temp_model = main_models.SendAsyncChatMessageRequestFiles()
                self.files.append(temp_model.from_map(k1))

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

        self.segments = []
        if m.get('segments') is not None:
            for k1 in m.get('segments'):
                temp_model = main_models.SendAsyncChatMessageRequestSegments()
                self.segments.append(temp_model.from_map(k1))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('taskExecution') is not None:
            temp_model = main_models.SendAsyncChatMessageRequestTaskExecution()
            self.task_execution = temp_model.from_map(m.get('taskExecution'))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('thinkingEnabled') is not None:
            self.thinking_enabled = m.get('thinkingEnabled')

        if m.get('thinkingLevel') is not None:
            self.thinking_level = m.get('thinkingLevel')

        if m.get('workMode') is not None:
            self.work_mode = m.get('workMode')

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

class SendAsyncChatMessageRequestSegments(DaraModel):
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
        # The display content of the segment.
        self.content = content
        # The category of the mentioned object.
        self.mention_type = mention_type
        # The name of the referenced object.
        self.name = name
        # The ID of the referenced object.
        self.object_id = object_id
        # The object type of the referenced object.
        self.object_type = object_type
        # The session type.
        self.session_type = session_type
        # The segment type.
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

class SendAsyncChatMessageRequestFiles(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        type: str = None,
    ):
        # The file ID, returned by uploadChatFile.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The file type.
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

class SendAsyncChatMessageRequestContextItems(DaraModel):
    def __init__(
        self,
        annotation: str = None,
        annotation_files: List[main_models.SendAsyncChatMessageRequestContextItemsAnnotationFiles] = None,
        content: str = None,
        file_id: str = None,
        file_name: str = None,
        file_type: str = None,
        message_id: str = None,
        sender_name: str = None,
        type: str = None,
    ):
        # The annotation content entered by the user.
        self.annotation = annotation
        # The list of attachments associated with the output annotation. This parameter is only applicable when type is set to output_annotation.
        self.annotation_files = annotation_files
        # The content corresponding to the reference or annotation. For output_annotation, this parameter is optional, but annotationFiles must be provided.
        self.content = content
        # The ID of the referenced or annotated output file.
        self.file_id = file_id
        # The name of the referenced or annotated output file.
        self.file_name = file_name
        # The type of the referenced or annotated output file.
        self.file_type = file_type
        # The ID of the referenced or annotated message.
        self.message_id = message_id
        # The name of the sender of the referenced or annotated message.
        self.sender_name = sender_name
        # The context type. Valid values: message_reference, message_selection, message_annotation, output_selection, and output_annotation.
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
                temp_model = main_models.SendAsyncChatMessageRequestContextItemsAnnotationFiles()
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

class SendAsyncChatMessageRequestContextItemsAnnotationFiles(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_public_url: str = None,
        file_record_id: str = None,
        file_url: str = None,
    ):
        # The file name of the attachment.
        self.file_name = file_name
        # The public access URL of the attachment. This parameter is optional.
        self.file_public_url = file_public_url
        # The file record ID of the attachment. This parameter is required. It is used to verify the ownership of the attachment and provide it for session processing.
        self.file_record_id = file_record_id
        # The internal access URL of the attachment. This parameter is optional.
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

