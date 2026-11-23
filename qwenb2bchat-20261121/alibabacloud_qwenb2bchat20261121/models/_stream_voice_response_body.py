# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StreamVoiceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 仅描述 WebSocket 接入/握手的请求标识，不代表后续语音轮次或音频结果。成功连接后使用下文 VoiceEvent 文本事件和 VoiceOutputAudio 二进制帧，不能把整条 WSS 连接按单次 JSON 响应处理。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

