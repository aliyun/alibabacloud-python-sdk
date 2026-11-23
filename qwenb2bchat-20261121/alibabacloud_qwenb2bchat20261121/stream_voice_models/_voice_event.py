# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_qwenb2bchat20261121 import stream_voice_models as main_models
from darabonba.model import DaraModel

class VoiceEvent(DaraModel):
    def __init__(
        self,
        header: main_models.VoiceEventHeader = None,
        communication: main_models.VoiceEventCommunication = None,
        payload: main_models.VoiceEventPayload = None,
        error: main_models.VoiceEventError = None,
    ):
        # 服务端事件头，包含事件类型及适用时的错误信息。
        self.header = header
        # 服务端事件与当前语音交互的关联信息。
        self.communication = communication
        # 事件数据，按 header.event 区分。task-started 有 stage；result-generated 有 output；task-failed 有 stage/retryable；heartbeat 和 task-finished 的 payload 为 {}。字段未出现不等于其值为 0 或 false。
        self.payload = payload
        # 可选的业务错误详情。发生业务失败时可返回，与 header 中的语音阶段错误信息配合处理；成功事件省略。
        self.error = error

    def validate(self):
        if self.header:
            self.header.validate()
        if self.communication:
            self.communication.validate()
        if self.payload:
            self.payload.validate()
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header is not None:
            result['header'] = self.header.to_map()

        if self.communication is not None:
            result['communication'] = self.communication.to_map()

        if self.payload is not None:
            result['payload'] = self.payload.to_map()

        if self.error is not None:
            result['error'] = self.error.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = main_models.VoiceEventHeader()
            self.header = temp_model.from_map(m.get('header'))

        if m.get('communication') is not None:
            temp_model = main_models.VoiceEventCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('payload') is not None:
            temp_model = main_models.VoiceEventPayload()
            self.payload = temp_model.from_map(m.get('payload'))

        if m.get('error') is not None:
            temp_model = main_models.VoiceEventError()
            self.error = temp_model.from_map(m.get('error'))

        return self

class VoiceEventError(DaraModel):
    def __init__(
        self,
        code: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        # 业务错误码，可为字符串或数值，具体类型由所用 Agent 的公开接口约定确定。它与 header.errorCode 的语音阶段错误码含义不同，应分别处理。
        self.code = code
        # 公开业务错误说明，可读文本；不要依赖固定全文做程序判断。
        self.message = message
        # 失败调用的业务请求关联号，用于排查；不是握手平台 RequestId、订单号或实例 ID。
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

class VoiceEventPayload(DaraModel):
    def __init__(
        self,
        stage: str = None,
        retryable: bool = None,
        output: main_models.VoiceEventPayloadOutput = None,
    ):
        # 条件返回；task-started 时为 asr，task-failed 时为 request/asr/agent/tts。result-generated 的阶段在 payload.output.stage 中。
        self.stage = stage
        # 仅 task-failed 返回。以本次事件的值为准，同一错误码可因失败阶段而不同。值为 true 时可考虑用新连接和新签名发起一轮交互。
        self.retryable = retryable
        # 仅 result-generated 返回；读取 payload.output.stage 选择 asr、agent 或 tts，再按 type 选择该阶段的结构。Agent 完整响应和兼容进度可能同时出现；使用 response 作为回答主数据，避免与 text/delta/messages 重复拼接。
        self.output = output

    def validate(self):
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stage is not None:
            result['stage'] = self.stage

        if self.retryable is not None:
            result['retryable'] = self.retryable

        if self.output is not None:
            result['output'] = self.output.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stage') is not None:
            self.stage = m.get('stage')

        if m.get('retryable') is not None:
            self.retryable = m.get('retryable')

        if m.get('output') is not None:
            temp_model = main_models.VoiceEventPayloadOutput()
            self.output = temp_model.from_map(m.get('output'))

        return self

class VoiceEventPayloadOutput(DaraModel):
    def __init__(
        self,
        stage: str = None,
        type: str = None,
        event: str = None,
        text: str = None,
        delta: str = None,
        final: bool = None,
        messages: List[Any] = None,
        response: main_models.VoiceEventPayloadOutputResponse = None,
        sentence: main_models.VoiceEventPayloadOutputSentence = None,
    ):
        # result-generated 的输出阶段，asr=语音识别、agent=Agent 回答、tts=语音合成。字段可用性取决于该阶段及 type。
        self.stage = stage
        # 按阶段解释：Agent 完整帧=response、兼容状态进度=progress；TTS 为 sentence-begin/sentence-synthesis/sentence-end。ASR/兼容文字按 text/final 等字段解析；不要假设所有事件都返回全部 output 字段。
        self.type = type
        # 仅 Agent type=response 返回，message 或 complete。complete 仅表示 Agent 流结束，可能仍需等待 TTS 音频；整轮结束以 task-finished 为准。
        self.event = event
        # asr 阶段为最终转写。Agent 兼容终稿使用累计完整回答。
        self.text = text
        # 仅兼容增量事件返回，使用完整 response 的客户端可以忽略本字段。
        self.delta = delta
        # ASR 最终转写及兼容 Agent 终稿为 true，兼容 Agent 文字增量为 false。
        self.final = final
        # type=progress 时返回状态栏消息批次，不拼接到正式回答。结构与 response.data.messages 中的状态栏消息一致。
        self.messages = messages
        # 仅 Agent type=response 时返回，与 Chat 流式帧一致的响应对象。complete 可携带最终正文，也可以为 {}；还可包含所用 Agent 的公开业务扩展。按字段说明读取正文、消息和错误信息。
        self.response = response
        # 仅 TTS 句子事件返回的关联对象；同一句 index 一致。sentence-synthesis 后紧跟该句的一帧二进制音频，按本轮 TTS format/sampleRate 解码；句子 text 仅在 sentence-begin 返回。
        self.sentence = sentence

    def validate(self):
        if self.response:
            self.response.validate()
        if self.sentence:
            self.sentence.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stage is not None:
            result['stage'] = self.stage

        if self.type is not None:
            result['type'] = self.type

        if self.event is not None:
            result['event'] = self.event

        if self.text is not None:
            result['text'] = self.text

        if self.delta is not None:
            result['delta'] = self.delta

        if self.final is not None:
            result['final'] = self.final

        if self.messages is not None:
            result['messages'] = self.messages

        if self.response is not None:
            result['response'] = self.response.to_map()

        if self.sentence is not None:
            result['sentence'] = self.sentence.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stage') is not None:
            self.stage = m.get('stage')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('delta') is not None:
            self.delta = m.get('delta')

        if m.get('final') is not None:
            self.final = m.get('final')

        if m.get('messages') is not None:
            self.messages = m.get('messages')

        if m.get('response') is not None:
            temp_model = main_models.VoiceEventPayloadOutputResponse()
            self.response = temp_model.from_map(m.get('response'))

        if m.get('sentence') is not None:
            temp_model = main_models.VoiceEventPayloadOutputSentence()
            self.sentence = temp_model.from_map(m.get('sentence'))

        return self

class VoiceEventPayloadOutputSentence(DaraModel):
    def __init__(
        self,
        index: int = None,
        text: str = None,
    ):
        # TTS 句子事件返回的整数索引，同一句的多个事件共用该值，用于关联随后音频；不能作为整轮完成标记。
        self.index = index
        # 仅 TTS sentence-begin 返回的待合成文本；sentence-synthesis/sentence-end 不保证存在。
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['index'] = self.index

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class VoiceEventPayloadOutputResponse(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        communication: main_models.VoiceEventPayloadOutputResponseCommunication = None,
        data: main_models.VoiceEventPayloadOutputResponseData = None,
        error_code: Any = None,
        error_msg: str = None,
    ):
        # 用于关联此 Agent 响应的业务请求。
        self.request_id = request_id
        # 与外层语音帧的 communication 独立，来自对应 Chat 响应。
        self.communication = communication
        # 可携带正文快照、图文卡片、过程消息和业务扩展。
        self.data = data
        # 该 Agent 响应中的业务状态。
        self.error_code = error_code
        # 与 errorCode 对应的说明。
        self.error_msg = error_msg

    def validate(self):
        if self.communication:
            self.communication.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.communication is not None:
            result['communication'] = self.communication.to_map()

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('communication') is not None:
            temp_model = main_models.VoiceEventPayloadOutputResponseCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('data') is not None:
            temp_model = main_models.VoiceEventPayloadOutputResponseData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        return self

class VoiceEventPayloadOutputResponseData(DaraModel):
    def __init__(
        self,
        debug: Any = None,
        messages: List[main_models.VoiceEventPayloadOutputResponseDataMessages] = None,
        extra_info: main_models.VoiceEventPayloadOutputResponseDataExtraInfo = None,
    ):
        # 仅在 result-generated 事件的 payload.output.stage=agent 且 type=response 时，完整 Agent 业务包可能提供此字段。按本帧的实际 JSON 值处理，可为 null。语音接口未约定调试开关、固定子字段或返回时机。内部计量字段不会随业务回包返回。
        self.debug = debug
        # 按 mimeType 区分文字、卡片和状态栏消息。累计文字快照使用新内容替换。同一状态栏模块按 metaData.sourceSeq 更新。
        self.messages = messages
        # 可含 inputResources 等资源处理结果。
        self.extra_info = extra_info

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.extra_info:
            self.extra_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug is not None:
            result['debug'] = self.debug

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('debug') is not None:
            self.debug = m.get('debug')

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.VoiceEventPayloadOutputResponseDataMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('extraInfo') is not None:
            temp_model = main_models.VoiceEventPayloadOutputResponseDataExtraInfo()
            self.extra_info = temp_model.from_map(m.get('extraInfo'))

        return self

class VoiceEventPayloadOutputResponseDataExtraInfo(DaraModel):
    def __init__(
        self,
        input_resources: List[main_models.VoiceEventPayloadOutputResponseDataExtraInfoInputResources] = None,
    ):
        # 仅在 Agent 返回资源处理结果时出现。
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
                temp_model = main_models.VoiceEventPayloadOutputResponseDataExtraInfoInputResources()
                self.input_resources.append(temp_model.from_map(k1))

        return self

class VoiceEventPayloadOutputResponseDataExtraInfoInputResources(DaraModel):
    def __init__(
        self,
        content_index: int = None,
        type: str = None,
        resource_id: str = None,
        url: str = None,
        file_name: str = None,
    ):
        # 以本轮原始 content 数组的顺序计数，从零开始，文本项也计数。
        self.content_index = content_index
        # 用于区分本轮输入资源的类型。
        self.type = type
        # 资源服务返回的标识。
        self.resource_id = resource_id
        # 资源处理成功时返回的文件 URL。
        self.url = url
        # 可选的资源文件名。
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_index is not None:
            result['contentIndex'] = self.content_index

        if self.type is not None:
            result['type'] = self.type

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.url is not None:
            result['url'] = self.url

        if self.file_name is not None:
            result['fileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentIndex') is not None:
            self.content_index = m.get('contentIndex')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        return self

class VoiceEventPayloadOutputResponseDataMessages(DaraModel):
    def __init__(
        self,
        mime_type: str = None,
        status: str = None,
        content: Any = None,
        meta_data: main_models.VoiceEventPayloadOutputResponseDataMessagesMetaData = None,
    ):
        # 例如 multi_load/iframe、bar/progress。
        self.mime_type = mime_type
        # 例如 processing、complete，不代表整轮完成。
        self.status = status
        # 文本或结构化内容，格式由 mimeType 决定。
        self.content = content
        # 结构随消息类型变化，可含卡片、状态栏过程信息及关联标识。
        self.meta_data = meta_data

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mime_type is not None:
            result['mimeType'] = self.mime_type

        if self.status is not None:
            result['status'] = self.status

        if self.content is not None:
            result['content'] = self.content

        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mimeType') is not None:
            self.mime_type = m.get('mimeType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('metaData') is not None:
            temp_model = main_models.VoiceEventPayloadOutputResponseDataMessagesMetaData()
            self.meta_data = temp_model.from_map(m.get('metaData'))

        return self

class VoiceEventPayloadOutputResponseDataMessagesMetaData(DaraModel):
    def __init__(
        self,
        source_seq: str = None,
        type: str = None,
        bar_title: str = None,
        content: Any = None,
        multi_load: List[main_models.VoiceEventPayloadOutputResponseDataMessagesMetaDataMultiLoad] = None,
    ):
        # 用于匹配正文中的卡片挂载标记，或关联同一轮的状态栏模块。收到该模块的新快照时替换旧内容。
        self.source_seq = source_seq
        # 按所用 Agent 的业务输出提供。常见有 bar_thinking、bar_tool、bar_think_finish、bar_ref_source_inline 和 bar_image_inline。各类型的显示方式见接口说明第 8.2 节。
        self.type = type
        # Agent 返回时可用于展示。
        self.bar_title = bar_title
        # 当前模块的完整业务快照，格式由 metaData.type 决定。过程资料条目由 bar_ref_source_inline 的 docs 提供。
        self.content = content
        # 卡片结构随类型变化，按关联标识挂载。
        self.multi_load = multi_load

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
        if self.source_seq is not None:
            result['sourceSeq'] = self.source_seq

        if self.type is not None:
            result['type'] = self.type

        if self.bar_title is not None:
            result['barTitle'] = self.bar_title

        if self.content is not None:
            result['content'] = self.content

        result['multiLoad'] = []
        if self.multi_load is not None:
            for k1 in self.multi_load:
                result['multiLoad'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceSeq') is not None:
            self.source_seq = m.get('sourceSeq')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('barTitle') is not None:
            self.bar_title = m.get('barTitle')

        if m.get('content') is not None:
            self.content = m.get('content')

        self.multi_load = []
        if m.get('multiLoad') is not None:
            for k1 in m.get('multiLoad'):
                temp_model = main_models.VoiceEventPayloadOutputResponseDataMessagesMetaDataMultiLoad()
                self.multi_load.append(temp_model.from_map(k1))

        return self

class VoiceEventPayloadOutputResponseDataMessagesMetaDataMultiLoad(DaraModel):
    def __init__(
        self,
        type: str = None,
        source_seq: str = None,
        content: Any = None,
    ):
        # 按类型选择卡片展示组件。
        self.type = type
        # 与正文中的卡片占位符关联。sourceSeq 为 image_waterfall_1 时，正文占位符为 [(image_waterfall_1)]。
        self.source_seq = source_seq
        # 可选，结构随卡片类型变化。图文卡片可含资源列表。
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.source_seq is not None:
            result['sourceSeq'] = self.source_seq

        if self.content is not None:
            result['content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('sourceSeq') is not None:
            self.source_seq = m.get('sourceSeq')

        if m.get('content') is not None:
            self.content = m.get('content')

        return self

class VoiceEventPayloadOutputResponseCommunication(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        session_id: str = None,
        app_id: str = None,
        response_id: int = None,
    ):
        # Agent 业务响应关联号。
        self.request_id = request_id
        # 当前 Agent 响应所属的客户会话。
        self.session_id = session_id
        # 当前响应所属的业务应用。
        self.app_id = app_id
        # 该值不代表网关发送帧的顺序。
        self.response_id = response_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.response_id is not None:
            result['responseId'] = self.response_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('responseId') is not None:
            self.response_id = m.get('responseId')

        return self

class VoiceEventCommunication(DaraModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 对应当前 run-task 的 communication.requestId，用于轮次关联；无法解析出合法请求号时，整个 communication 可省略。不能用音频帧或事件数量替代关联号。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class VoiceEventHeader(DaraModel):
    def __init__(
        self,
        event: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # 必填事件类型，只可能为 task-started、result-generated、heartbeat、task-finished、task-failed。整轮完成以 task-finished 为准，不以 Agent complete 或单个 TTS 事件代替。
        self.event = event
        # task-failed 时返回的语音阶段错误码，字符串；例如 INVALID_REQUEST、ASR_FAILED、AGENT_FAILED、TTS_FAILED，其他准入/协议错误见接口说明。若同时存在 Agent 业务错误，另看顶层 error.code，分别处理两层错误。
        self.error_code = error_code
        # task-failed 时返回的可读失败说明；非失败事件省略，不依赖固定文案做程序判断。
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['event'] = self.event

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        return self

