# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qwenb2bchat20261121 import models as main_models
from darabonba.model import DaraModel

class ChatResponseBody(DaraModel):
    def __init__(
        self,
        audio_frames: List[main_models.ChatResponseBodyAudioFrames] = None,
        communication: main_models.ChatResponseBodyCommunication = None,
        data: main_models.ChatResponseBodyData = None,
        error: main_models.ChatResponseBodyError = None,
        error_code: Any = None,
        error_msg: str = None,
        request_id: str = None,
    ):
        # 开通 HTTP 音频输出后，完整 JSON 可在 audioFrames 中返回音频帧。type 为 audio 时，data 为 Base64 音频数据，last 为布尔末帧标识。type 为 error 时可含 code、requestId 和 message。无音频时可为空或省略。
        self.audio_frames = audio_frames
        # 用于关联响应帧与原业务请求和会话的信息。
        self.communication = communication
        # 可选业务对象，字段按实际响应出现。单帧 HTTP 音频响应的 data 也可能直接为 Base64 字符串；多态音频完整形状见接口说明。客户端不得假定固定字段全部存在。
        self.data = data
        # 可选错误对象，出现时按失败处理。准备阶段可用错误HTTP状态+JSON返回；已识别业务错误可保留HTTP200，SSE首帧提交后用错误终帧表达。优先结合HTTP X-Request-Id关联。
        self.error = error
        # 可选字符串或数值，成功业务响应可为数字0；非零或失败码按错误处理。未返回本字段不自动判失败，须综合 error、HTTP 和流终帧。
        self.error_code = error_code
        # 与响应顶层业务状态码对应的说明。
        self.error_msg = error_msg
        # 响应顶层可选的业务请求关联号。POP 请求号由响应头 x-acs-request-id 提供。
        self.request_id = request_id

    def validate(self):
        if self.audio_frames:
            for v1 in self.audio_frames:
                 if v1:
                    v1.validate()
        if self.communication:
            self.communication.validate()
        if self.data:
            self.data.validate()
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['audioFrames'] = []
        if self.audio_frames is not None:
            for k1 in self.audio_frames:
                result['audioFrames'].append(k1.to_map() if k1 else None)

        if self.communication is not None:
            result['communication'] = self.communication.to_map()

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_frames = []
        if m.get('audioFrames') is not None:
            for k1 in m.get('audioFrames'):
                temp_model = main_models.ChatResponseBodyAudioFrames()
                self.audio_frames.append(temp_model.from_map(k1))

        if m.get('communication') is not None:
            temp_model = main_models.ChatResponseBodyCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('data') is not None:
            temp_model = main_models.ChatResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error') is not None:
            temp_model = main_models.ChatResponseBodyError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ChatResponseBodyError(DaraModel):
    def __init__(
        self,
        code: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # 可选的错误码，可为字符串或数值，表示服务或 Agent 的具体错误类型。程序应按 code 判断，不依赖 message 全文；数值业务码 500 不代表 HTTP 状态一定为 500。
        self.code = code
        # 业务错误的说明文本。
        self.message = message
        # 失败调用的业务请求关联号，用于定位问题。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ChatResponseBodyData(DaraModel):
    def __init__(
        self,
        debug: Any = None,
        extra_info: main_models.ChatResponseBodyDataExtraInfo = None,
        messages: List[main_models.ChatResponseBodyDataMessages] = None,
    ):
        # 可选业务调试信息，可省略或为 null。在支持的联调场景中可能包含 intentLabel；具体结构和返回时机按实际响应读取。
        self.debug = debug
        # 业务响应附带的可选扩展信息。inputResources 是本轮输入资源的处理结果数组，元素可含 contentIndex、type、resourceId、url 和 fileName。contentIndex 是原始消息 content 数组的零起始下标，文本块也计数。
        self.extra_info = extra_info
        # 可选数组，可能含多条正文、过程或卡片消息。multi_load/iframe 文本为累计快照，不将每帧全文重复拼接；不要固定只取 messages[0]。
        self.messages = messages

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug is not None:
            result['debug'] = self.debug

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info.to_map()

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('debug') is not None:
            self.debug = m.get('debug')

        if m.get('extraInfo') is not None:
            temp_model = main_models.ChatResponseBodyDataExtraInfo()
            self.extra_info = temp_model.from_map(m.get('extraInfo'))

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.ChatResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class ChatResponseBodyDataMessages(DaraModel):
    def __init__(
        self,
        content: Any = None,
        meta_data: main_models.ChatResponseBodyDataMessagesMetaData = None,
        mime_type: str = None,
        status: str = None,
    ):
        # 可选多态内容，按 mimeType 解析。multi_load/iframe 常为累计文本快照；后帧更新当前内容。过程、卡片按各自类型处理，不把任意 content 强转字符串。
        self.content = content
        # 可选、可扩展的消息元数据。正文消息可通过 multiLoad 提供卡片；过程消息可按类型包含 sourceSeq、type、barTitle、content，用于关联和展示相应内容。
        self.meta_data = meta_data
        # 消息类型，按此值解析正文、进度及可选信号和追问。常见类型见接入说明。
        self.mime_type = mime_type
        # 可选消息状态，如 processing、complete；complete 只结束该消息，不替代 SSE event:complete。HTTP200 或单条消息complete都不足以判定整次流成功。
        self.status = status

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()

        if self.mime_type is not None:
            result['mimeType'] = self.mime_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('metaData') is not None:
            temp_model = main_models.ChatResponseBodyDataMessagesMetaData()
            self.meta_data = temp_model.from_map(m.get('metaData'))

        if m.get('mimeType') is not None:
            self.mime_type = m.get('mimeType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ChatResponseBodyDataMessagesMetaData(DaraModel):
    def __init__(
        self,
        bar_title: str = None,
        content: Any = None,
        multi_load: List[main_models.ChatResponseBodyDataMessagesMetaDataMultiLoad] = None,
        source_seq: str = None,
        type: str = None,
    ):
        # 用于展示当前过程的上下文标题。处理状态见对应消息的 status。
        self.bar_title = bar_title
        # 数据结构随模块类型变化。bar/progress 中，思考过程使用 body，工具和结束提示使用 title，过程中检索资料或图片分别使用 docs、images。完整键和示例见接入说明。
        self.content = content
        # 与正文关联的结构化内容列表，例如图文卡片，按消息类型返回。
        self.multi_load = multi_load
        # 按本次请求和 sourceSeq 关联同一模块的更新。新的完整快照替换旧快照。
        self.source_seq = source_seq
        # 例如 bar_thinking、bar_tool、bar_think_finish、bar_ref_source_inline 或 bar_image_inline。按实际类型选择展示组件。
        self.type = type

    def validate(self):
        if self.multi_load:
            for v1 in self.multi_load:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bar_title is not None:
            result['barTitle'] = self.bar_title

        if self.content is not None:
            result['content'] = self.content

        result['multiLoad'] = []
        if self.multi_load is not None:
            for k1 in self.multi_load:
                result['multiLoad'].append(k1.to_map() if k1 else None)

        if self.source_seq is not None:
            result['sourceSeq'] = self.source_seq

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('barTitle') is not None:
            self.bar_title = m.get('barTitle')

        if m.get('content') is not None:
            self.content = m.get('content')

        self.multi_load = []
        if m.get('multiLoad') is not None:
            for k1 in m.get('multiLoad'):
                temp_model = main_models.ChatResponseBodyDataMessagesMetaDataMultiLoad()
                self.multi_load.append(temp_model.from_map(k1))

        if m.get('sourceSeq') is not None:
            self.source_seq = m.get('sourceSeq')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ChatResponseBodyDataMessagesMetaDataMultiLoad(DaraModel):
    def __init__(
        self,
        content: Any = None,
        source_seq: str = None,
        type: str = None,
    ):
        # 可选，结构随卡片类型变化。图文卡片可含资源列表。
        self.content = content
        # 与正文中的卡片引用关联。相同标识代表同一卡片。
        self.source_seq = source_seq
        # 按类型选择卡片展示组件。
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

        if self.source_seq is not None:
            result['sourceSeq'] = self.source_seq

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('sourceSeq') is not None:
            self.source_seq = m.get('sourceSeq')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ChatResponseBodyDataExtraInfo(DaraModel):
    def __init__(
        self,
        input_resources: List[main_models.ChatResponseBodyDataExtraInfoInputResources] = None,
    ):
        # 仅在响应提供本轮输入资源处理结果时返回。
        self.input_resources = input_resources

    def validate(self):
        if self.input_resources:
            for v1 in self.input_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['inputResources'] = []
        if self.input_resources is not None:
            for k1 in self.input_resources:
                result['inputResources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input_resources = []
        if m.get('inputResources') is not None:
            for k1 in m.get('inputResources'):
                temp_model = main_models.ChatResponseBodyDataExtraInfoInputResources()
                self.input_resources.append(temp_model.from_map(k1))

        return self

class ChatResponseBodyDataExtraInfoInputResources(DaraModel):
    def __init__(
        self,
        content_index: int = None,
        file_name: str = None,
        resource_id: str = None,
        type: str = None,
        url: str = None,
    ):
        # 从零开始，按原始 content 数组计数，包含文本块。
        self.content_index = content_index
        # 有文件名时返回。
        self.file_name = file_name
        # 本轮输入资源的标识，用于关联对应资源。
        self.resource_id = resource_id
        # 原始内容块对应的资源类型。
        self.type = type
        # 本轮输入资源的可访问地址。
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_index is not None:
            result['contentIndex'] = self.content_index

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.type is not None:
            result['type'] = self.type

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentIndex') is not None:
            self.content_index = m.get('contentIndex')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ChatResponseBodyCommunication(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        response_id: int = None,
        session_id: str = None,
    ):
        # 当前响应所属的业务请求 ID，返回时与请求中的 communication.requestId 一致。
        self.request_id = request_id
        # 可选整数，业务响应帧标识；网关多帧聚合可为0。不代表可对所有网络帧排序的序列号，也不是会话或请求ID。
        self.response_id = response_id
        # 当前响应所属的客户会话 ID。
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.response_id is not None:
            result['responseId'] = self.response_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('responseId') is not None:
            self.response_id = m.get('responseId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self



class ChatResponseBodyAudioFrames(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        last: bool = None,
        message: str = None,
        request_id: str = None,
        type: str = None,
    ):
        # 音频处理失败时可能提供。
        self.code = code
        # 音频帧的 Base64 数据。末帧的值可以为空字符串。
        self.data = data
        # true 表示本路音频的最后一帧。
        self.last = last
        # 音频处理失败时按实际错误返回。
        self.message = message
        # 用于关联音频错误与本次业务请求。
        self.request_id = request_id
        # audio 表示音频，error 表示处理失败。
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data

        if self.last is not None:
            result['last'] = self.last

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('last') is not None:
            self.last = m.get('last')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

