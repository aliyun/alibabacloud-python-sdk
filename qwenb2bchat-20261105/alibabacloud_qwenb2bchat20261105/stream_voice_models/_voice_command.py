# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qwenb2bchat20261105 import stream_voice_models as main_models
from darabonba.model import DaraModel

class VoiceCommand(DaraModel):
    def __init__(
        self,
        communication: main_models.VoiceCommandCommunication = None,
        data: main_models.VoiceCommandData = None,
        params: main_models.VoiceCommandParams = None,
        header: main_models.VoiceCommandHeader = None,
        payload: main_models.VoiceCommandPayload = None,
    ):
        # 本轮语音交互的请求关联号、会话及应用和用户身份信息。
        self.communication = communication
        # run-task 可选对象，无默认值；传入时只支持 messages，不能为 null。供 Agent 使用的业务输入，语音音频另通过二进制帧上传。
        self.data = data
        # run-task 可选对象，省略为无客户扩展；显式传入不能为 null。支持 directAgent、deepthink 及已接入 Agent 的扩展，字段和值类型依 Agent 契约；语音参数放在 payload.parameters。本接口不支持通过 enableTextImageMixed 启用图文混排，传 true 不生效；历史托管方放在 communication.historyOwner。
        self.params = params
        # 控制帧头，包含客户端要执行的语音交互动作。
        # 
        # This parameter is required.
        self.header = header
        # run-task 必须提供 taskGroup=audio、task=voice 和 parameters.asr（除兼容保留的 retryOf 分支，该分支当前不可用）。finish-audio/cancel-task 的 payload 可省略、为 null 或空对象。
        self.payload = payload

    def validate(self):
        if self.communication:
            self.communication.validate()
        if self.data:
            self.data.validate()
        if self.params:
            self.params.validate()
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.communication is not None:
            result['communication'] = self.communication.to_map()

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.params is not None:
            result['params'] = self.params.to_map()

        if self.header is not None:
            result['header'] = self.header.to_map()

        if self.payload is not None:
            result['payload'] = self.payload.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('communication') is not None:
            temp_model = main_models.VoiceCommandCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('data') is not None:
            temp_model = main_models.VoiceCommandData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('params') is not None:
            temp_model = main_models.VoiceCommandParams()
            self.params = temp_model.from_map(m.get('params'))

        if m.get('header') is not None:
            temp_model = main_models.VoiceCommandHeader()
            self.header = temp_model.from_map(m.get('header'))

        if m.get('payload') is not None:
            temp_model = main_models.VoiceCommandPayload()
            self.payload = temp_model.from_map(m.get('payload'))

        return self

class VoiceCommandPayload(DaraModel):
    def __init__(
        self,
        task_group: str = None,
        task: str = None,
        retry_of: str = None,
        parameters: main_models.VoiceCommandPayloadParameters = None,
        input: main_models.VoiceCommandPayloadInput = None,
    ):
        # run-task 必填字符串，固定为 audio，区分大小写，无默认值。
        self.task_group = task_group
        # run-task 必填字符串，固定为 voice，区分大小写，无默认值。
        self.task = task
        # 可选的保留字段，字符串格式为 [A-Za-z0-9._:-]{1,128}。当前不支持引用先前请求重试；即使值符合格式，也返回 RETRY_EXPIRED，不会重试音频或继续之前的任务。正常调用请省略，不要用于自动续传。
        self.retry_of = retry_of
        # 普通 run-task 必填对象，只包含 asr 和可选 tts。asr 无默认值；tts 可省略或 null，使用默认合成设置。
        self.parameters = parameters
        # 可选对象，可省略或 null；只包含 context 和 history。context 辅助 ASR，history 是 Agent 业务历史，两者用途不同。
        self.input = input

    def validate(self):
        if self.parameters:
            self.parameters.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_group is not None:
            result['taskGroup'] = self.task_group

        if self.task is not None:
            result['task'] = self.task

        if self.retry_of is not None:
            result['retryOf'] = self.retry_of

        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()

        if self.input is not None:
            result['input'] = self.input.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskGroup') is not None:
            self.task_group = m.get('taskGroup')

        if m.get('task') is not None:
            self.task = m.get('task')

        if m.get('retryOf') is not None:
            self.retry_of = m.get('retryOf')

        if m.get('parameters') is not None:
            temp_model = main_models.VoiceCommandPayloadParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('input') is not None:
            temp_model = main_models.VoiceCommandPayloadInput()
            self.input = temp_model.from_map(m.get('input'))

        return self

class VoiceCommandPayloadInput(DaraModel):
    def __init__(
        self,
        context: List[main_models.VoiceCommandPayloadInputContext] = None,
        history: List[main_models.VoiceCommandPayloadInputHistory] = None,
    ):
        # 可选数组，省略为无 ASR 上下文。最多 10 条，user/assistant 各最多 5 条，assistant 必须紧跟 user。每条 content 文本块顺序合并后最多 400 个 UTF-16 代码单元。
        self.context = context
        # CLIENT 模式可选历史数组，省略或空数组为无历史；仅含此前完整 user/assistant 对，交替并以 assistant 结束，不含本轮问题。GATEWAY 模式不能提交非空历史。本轮附加图文放 data.messages，音频走二进制帧。
        self.history = history

    def validate(self):
        if self.context:
            for v1 in self.context:
                 if v1:
                    v1.validate()
        if self.history:
            for v1 in self.history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['context'] = []
        if self.context is not None:
            for k1 in self.context:
                result['context'].append(k1.to_map() if k1 else None)

        result['history'] = []
        if self.history is not None:
            for k1 in self.history:
                result['history'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.context = []
        if m.get('context') is not None:
            for k1 in m.get('context'):
                temp_model = main_models.VoiceCommandPayloadInputContext()
                self.context.append(temp_model.from_map(k1))

        self.history = []
        if m.get('history') is not None:
            for k1 in m.get('history'):
                temp_model = main_models.VoiceCommandPayloadInputHistory()
                self.history.append(temp_model.from_map(k1))

        return self

class VoiceCommandPayloadInputHistory(DaraModel):
    def __init__(
        self,
        role: str = None,
        content: Any = None,
    ):
        # 历史条目必填字符串，只接受 user 或 assistant，按 user、assistant 成对交替并以 assistant 结束。
        # 
        # This parameter is required.
        self.role = role
        # 历史条目必填，为非空字符串或非空内容块数组。user 历史支持文本/图片，assistant 历史只接受文本；内容块格式沿用 Chat。
        # 
        # This parameter is required.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role is not None:
            result['role'] = self.role

        if self.content is not None:
            result['content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('content') is not None:
            self.content = m.get('content')

        return self

class VoiceCommandPayloadInputContext(DaraModel):
    def __init__(
        self,
        role: str = None,
        content: List[main_models.VoiceCommandPayloadInputContextContent] = None,
    ):
        # 上下文条目必填字符串，只接受 user 或 assistant，区分大小写；assistant 必须紧跟同一轮 user。
        # 
        # This parameter is required.
        self.role = role
        # 上下文条目必填的非空数组，同一条消息的各文本块按顺序合并后用于识别。
        # 
        # This parameter is required.
        self.content = content

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role is not None:
            result['role'] = self.role

        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')

        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.VoiceCommandPayloadInputContextContent()
                self.content.append(temp_model.from_map(k1))

        return self

class VoiceCommandPayloadInputContextContent(DaraModel):
    def __init__(
        self,
        type: str = None,
        text: str = None,
    ):
        # 上下文内容块必填字符串；user 消息固定 input_text，assistant 消息固定 text。
        # 
        # This parameter is required.
        self.type = type
        # 上下文内容块必填的非空文本，用于辅助识别；计入该条消息合计 400 个 UTF-16 代码单元限制。
        # 
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class VoiceCommandPayloadParameters(DaraModel):
    def __init__(
        self,
        asr: main_models.VoiceCommandPayloadParametersAsr = None,
        tts: main_models.VoiceCommandPayloadParametersTts = None,
    ):
        # 普通 run-task 必填对象；format 和 sampleRate 必填且无默认值，languageHints 可选。上传与这些参数匹配的音频二进制帧，不使用 Base64 JSON 音频字段。
        self.asr = asr
        # 可选对象，可省略或传 null，使用默认合成设置。默认 format=mp3、sampleRate=22050、volume=50、rate=1.0，voice 使用租户默认音色；显式字段仍须符合租户许可。
        self.tts = tts

    def validate(self):
        if self.asr:
            self.asr.validate()
        if self.tts:
            self.tts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr is not None:
            result['asr'] = self.asr.to_map()

        if self.tts is not None:
            result['tts'] = self.tts.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asr') is not None:
            temp_model = main_models.VoiceCommandPayloadParametersAsr()
            self.asr = temp_model.from_map(m.get('asr'))

        if m.get('tts') is not None:
            temp_model = main_models.VoiceCommandPayloadParametersTts()
            self.tts = temp_model.from_map(m.get('tts'))

        return self

class VoiceCommandPayloadParametersTts(DaraModel):
    def __init__(
        self,
        format: str = None,
        sample_rate: int = None,
        voice: str = None,
        volume: int = None,
        rate: float = None,
    ):
        # 可选字符串，只支持 mp3 或 pcm；省略或 null 时为 mp3。客户端按该格式解码随后返回的二进制音频。
        self.format = format
        # 可选整数，单位 Hz；默认 22050，可选 8000、16000、22050、24000、44100、48000。客户端按本轮格式及采样率解码音频。
        self.sample_rate = sample_rate
        # 可选字符串，须为租户许可的音色；省略或 null 时使用租户默认音色。没有跨租户固定的默认音色名称。
        self.voice = voice
        # 可选整数，范围 [0,100]，默认 50；不是小数比例。
        self.volume = volume
        # 可选数值，范围 [0.5,2.0]，默认 1.0，表示语速倍率。
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['format'] = self.format

        if self.sample_rate is not None:
            result['sampleRate'] = self.sample_rate

        if self.voice is not None:
            result['voice'] = self.voice

        if self.volume is not None:
            result['volume'] = self.volume

        if self.rate is not None:
            result['rate'] = self.rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('sampleRate') is not None:
            self.sample_rate = m.get('sampleRate')

        if m.get('voice') is not None:
            self.voice = m.get('voice')

        if m.get('volume') is not None:
            self.volume = m.get('volume')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        return self

class VoiceCommandPayloadParametersAsr(DaraModel):
    def __init__(
        self,
        format: str = None,
        sample_rate: int = None,
        language_hints: List[str] = None,
    ):
        # ASR 必填字符串，无默认值；支持 pcm、wav 或 opus，具体值须符合租户许可。音频实际编码须与声明一致，不能用文件后缀代替编码。
        self.format = format
        # ASR 必填整数，单位 Hz，无默认值；须为租户许可的采样率并与实际音频一致，例如 16000。
        self.sample_rate = sample_rate
        # 可选字符串数组，无默认提示；最多 4 项，每项非空白、最多 16 个 UTF-16 代码单元。用于辅助识别，非业务用户身份。
        self.language_hints = language_hints

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['format'] = self.format

        if self.sample_rate is not None:
            result['sampleRate'] = self.sample_rate

        if self.language_hints is not None:
            result['languageHints'] = self.language_hints

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('sampleRate') is not None:
            self.sample_rate = m.get('sampleRate')

        if m.get('languageHints') is not None:
            self.language_hints = m.get('languageHints')

        return self

class VoiceCommandHeader(DaraModel):
    def __init__(
        self,
        action: str = None,
    ):
        # 所有控制帧必填，无默认值；区分大小写，只接受 run-task、finish-audio、cancel-task。run-task 启动一轮交互；finish-audio 表示上行音频发送结束；cancel-task 取消当前轮次。没有 continue-task 或 finish-task；Ping/Pong 使用 WebSocket 原生控制帧。
        # 
        # This parameter is required.
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        return self

class VoiceCommandParams(DaraModel):
    def __init__(
        self,
        direct_agent: str = None,
        deepthink: str = None,
    ):
        # 可选的本轮 Agent 选择器；省略使用租户默认路由，显式值须在已授权 Agent 范围内。无统一公开枚举，请使用接入方提供的 Agent 名称。
        self.direct_agent = direct_agent
        # 可选的 Agent 参数，无统一网关默认值。支持本参数的 Agent 使用字符串 true 开启，具体值和默认行为依所接入 Agent 契约；不要误写为控制帧顶层字段。
        self.deepthink = deepthink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direct_agent is not None:
            result['directAgent'] = self.direct_agent

        if self.deepthink is not None:
            result['deepthink'] = self.deepthink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directAgent') is not None:
            self.direct_agent = m.get('directAgent')

        if m.get('deepthink') is not None:
            self.deepthink = m.get('deepthink')

        return self

class VoiceCommandData(DaraModel):
    def __init__(
        self,
        messages: List[main_models.VoiceCommandDataMessages] = None,
    ):
        # run-task 可选，省略或空数组表示没有附加图文消息。传入时只包含本轮一条 user 消息，历史放入 payload.input.history；不要重复提交音频转写。
        self.messages = messages

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.VoiceCommandDataMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class VoiceCommandDataMessages(DaraModel):
    def __init__(
        self,
        role: str = None,
        content: Any = None,
    ):
        # 本轮消息的角色，传 user。CLIENT 托管的历史消息放在 payload.input.history。
        self.role = role
        # 本轮 user 消息的内容，为非空文本或所接入 Agent 支持的内容块数组；文本/图片块格式沿用 Chat。音频不放入此字段，另发 WSS 二进制帧。
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role is not None:
            result['role'] = self.role

        if self.content is not None:
            result['content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('content') is not None:
            self.content = m.get('content')

        return self

class VoiceCommandCommunication(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        session_id: str = None,
        app_id: str = None,
        history_owner: str = None,
        user_id: str = None,
    ):
        # run-task 必填，本轮客户业务请求 ID，匹配 [A-Za-z0-9._:-]{1,128}。不能使用 gw-ingress- 保留前缀。下一轮需新建连接并使用独立 ID；finish-audio/cancel-task 沿用当前轮次且不另传 communication。与可选握手 X-Request-Id 不同。
        self.request_id = request_id
        # 每个 run-task 必填。客户会话 ID，匹配 [A-Za-z0-9._-]{1,128}，同一会话续聊时复用；用于会话历史关联，不是订单号或业务请求 ID。
        self.session_id = session_id
        # 每个 run-task 必填的业务应用 ID，不从握手 query 读取。须符合业务网关凭据的应用绑定或委托配置；每条连接只接受一个 run-task；下一轮需新建连接，即使复用 sessionId 也要提供本字段。非空，最多 256 个 UTF-16 代码单元，无首尾空白、控制字符或非法 Unicode。
        self.app_id = app_id
        # 每个 run-task 必填，区分大小写，只能是 CLIENT 或 GATEWAY，无默认值。须与该会话首次调用一致。CLIENT 历史放在 payload.input.history；GATEWAY 由服务端托管，不接受客户提交非空历史。
        self.history_owner = history_owner
        # 可选，无默认用户。省略时匿名，不启用用户记忆；即使凭据绑定固定用户也不要求必须传入。若显式传入，须符合固定绑定；必须为非空字符串，最多 256 个 UTF-16 代码单元，无首尾空白、控制字符或非法 Unicode。不能为 null。
        self.user_id = user_id

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

        if self.history_owner is not None:
            result['historyOwner'] = self.history_owner

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('historyOwner') is not None:
            self.history_owner = m.get('historyOwner')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

