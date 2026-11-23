# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qwenb2bmed20261121 import models as main_models
from darabonba.model import DaraModel

class MedicalModelInferenceResponseBody(DaraModel):
    def __init__(
        self,
        audio_frames: List[main_models.MedicalModelInferenceResponseBodyAudioFrames] = None,
        communication: main_models.MedicalModelInferenceResponseBodyCommunication = None,
        data: main_models.MedicalModelInferenceResponseBodyData = None,
        error: main_models.MedicalModelInferenceResponseBodyError = None,
        error_code: Any = None,
        error_msg: str = None,
        request_id: str = None,
    ):
        # 可选的聚合音频帧列表。若返回音频，正常帧可含 type=audio、Base64 字符串 data 和布尔值 last，正常末帧的 data 可为空字符串。失败帧可含 type=error、code、requestId、last 和可选 message。各帧字段依类型而定。
        self.audio_frames = audio_frames
        # 关联原请求及会话的标识。
        self.communication = communication
        # 本次应答的业务数据，正文位于 messages。
        self.data = data
        # 可选的结构化错误信息。返回时读取 code、message 和 requestId。
        self.error = error
        # 业务状态码。0 表示业务成功，非 0 时结合 errorMsg 或 error 查看原因。流式还应处理 event:error。
        self.error_code = error_code
        # 业务状态的文字说明。失败时用于辅助排查，程序分支应依据状态码。
        self.error_msg = error_msg
        # 可选的业务请求 ID。联系支持时可同时提供响应头 x-acs-request-id 中的阿里云请求 ID。
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
                temp_model = main_models.MedicalModelInferenceResponseBodyAudioFrames()
                self.audio_frames.append(temp_model.from_map(k1))

        if m.get('communication') is not None:
            temp_model = main_models.MedicalModelInferenceResponseBodyCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('data') is not None:
            temp_model = main_models.MedicalModelInferenceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error') is not None:
            temp_model = main_models.MedicalModelInferenceResponseBodyError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class MedicalModelInferenceResponseBodyError(DaraModel):
    def __init__(
        self,
        code: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # 业务错误码，客户端可根据此字段判断错误类型。
        self.code = code
        # 错误原因的文字说明，便于排查后调整请求。
        self.message = message
        # 失败请求的业务请求 ID，联系支持时可一并提供。
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

class MedicalModelInferenceResponseBodyData(DaraModel):
    def __init__(
        self,
        debug: Any = None,
        extra_info: main_models.MedicalModelInferenceResponseBodyDataExtraInfo = None,
        messages: List[main_models.MedicalModelInferenceResponseBodyDataMessages] = None,
    ):
        # 可选业务调试信息，可为任意 JSON 值（含 null）。是否返回、返回时机和内容按实际执行结果，不保证每轮或结束事件必有；不用于判断业务完成。
        self.debug = debug
        # 响应的可选补充信息。使用图片等资源时可读取 inputResources 中返回的对应资源信息。
        self.extra_info = extra_info
        # 当前响应中的消息列表。读取消息的 mimeType、status 和 content。完整正文可通过 mimeType=multi_load/iframe 且 status=complete 的消息取得。
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
            temp_model = main_models.MedicalModelInferenceResponseBodyDataExtraInfo()
            self.extra_info = temp_model.from_map(m.get('extraInfo'))

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.MedicalModelInferenceResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class MedicalModelInferenceResponseBodyDataMessages(DaraModel):
    def __init__(
        self,
        content: Any = None,
        meta_data: main_models.MedicalModelInferenceResponseBodyDataMessagesMetaData = None,
        mime_type: str = None,
        status: str = None,
    ):
        # 消息正文，具体结构随 mimeType 变化。流式快照可能包含到当前为止的完整正文，收到新快照时更新原内容，避免重复拼接。
        self.content = content
        # 可选消息附加信息，按实际返回处理。当前医疗模型不承诺返回医疗 Agent 的检索进度、资料来源或业务卡片。
        self.meta_data = meta_data
        # 该消息的内容类型，用于选择解析和展示方式。multi_load/iframe 表示正文；遇到应用不支持的类型，可跳过该消息。
        self.mime_type = mime_type
        # 当前消息的处理状态。complete 表示这条消息已完成；流式请求是否结束以 SSE 结束事件为准。
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
            temp_model = main_models.MedicalModelInferenceResponseBodyDataMessagesMetaData()
            self.meta_data = temp_model.from_map(m.get('metaData'))

        if m.get('mimeType') is not None:
            self.mime_type = m.get('mimeType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class MedicalModelInferenceResponseBodyDataMessagesMetaData(DaraModel):
    def __init__(
        self,
        bar_title: str = None,
        content: Any = None,
        multi_load: List[main_models.MedicalModelInferenceResponseBodyDataMessagesMetaDataMultiLoad] = None,
        source_seq: str = None,
        type: str = None,
    ):
        # 可选的消息附加标题，存在时按实际值使用。
        self.bar_title = bar_title
        # 可选元数据内容，按实际返回类型解释。当前医疗模型不保证返回进度模块。
        self.content = content
        # 为兼容已有响应形状保留的可选列表，可为空或省略；当前医疗模型不保证生成 Agent 业务卡片。
        self.multi_load = multi_load
        # 可选的消息关联标识，存在时按实际值使用；本模型接口不保证返回。
        self.source_seq = source_seq
        # 可选元数据类型，存在时按实际类型解释；不据此推断模型提供 Agent 过程能力。
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
                temp_model = main_models.MedicalModelInferenceResponseBodyDataMessagesMetaDataMultiLoad()
                self.multi_load.append(temp_model.from_map(k1))

        if m.get('sourceSeq') is not None:
            self.source_seq = m.get('sourceSeq')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class MedicalModelInferenceResponseBodyDataMessagesMetaDataMultiLoad(DaraModel):
    def __init__(
        self,
        content: Any = None,
        source_seq: str = None,
        type: str = None,
    ):
        # 可选 JSON 内容，结构随实际附加项类型变化，不保证存在固定业务卡片。
        self.content = content
        # 可选的附加项关联标识，存在时按实际值解释。
        self.source_seq = source_seq
        # 可选的附加项类型，遇到未识别类型可忽略该附加项。
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

class MedicalModelInferenceResponseBodyDataExtraInfo(DaraModel):
    def __init__(
        self,
        input_resources: List[main_models.MedicalModelInferenceResponseBodyDataExtraInfoInputResources] = None,
    ):
        # 可选的资源信息数组，通过 contentIndex 与请求中的内容块对应。未返回资源信息时可省略。
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
                temp_model = main_models.MedicalModelInferenceResponseBodyDataExtraInfoInputResources()
                self.input_resources.append(temp_model.from_map(k1))

        return self

class MedicalModelInferenceResponseBodyDataExtraInfoInputResources(DaraModel):
    def __init__(
        self,
        content_index: int = None,
        file_name: str = None,
        resource_id: str = None,
        type: str = None,
        url: str = None,
    ):
        # 原请求本轮 content 数组的索引，从 0 开始。文本块也占用索引。
        self.content_index = content_index
        # 上游提供时返回资源文件名。
        self.file_name = file_name
        # 返回的输入资源标识，存在时可用于在业务记录中引用该资源。
        self.resource_id = resource_id
        # 资源类型，例如图片引用。
        self.type = type
        # 返回的资源访问地址。客户端按实际返回值使用。
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

class MedicalModelInferenceResponseBodyCommunication(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        response_id: int = None,
        session_id: str = None,
    ):
        # 对应请求中的 communication.requestId，便于匹配并发请求。
        self.request_id = request_id
        # 业务响应帧标识。一次完整 JSON 聚合时可为 0。SSE 按事件到达顺序处理，responseId 无需连续。
        self.response_id = response_id
        # 对应请求中的 communication.sessionId。
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

class MedicalModelInferenceResponseBodyAudioFrames(DaraModel):
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

