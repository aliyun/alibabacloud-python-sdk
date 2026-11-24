# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InputAudioBufferAppend(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        audio: bytes = None,
        sequence: int = None,
    ):
        # This parameter is required.
        self.type = type
        # 可省略；提供时必须为非空、非纯空白字符串。
        self.event_id = event_id
        # 等待 SessionUpdated 后发送；必须为 JSON 文本消息中的 Base64 字符串，不能发送 binary 帧。解码后每块最多10240字节；双向必须为非空 PCM16 完整采样，字节数为偶数。解码与大小检查由后端执行。
        # 
        # This parameter is required.
        self.audio = audio
        # 仅双向使用；可省略，提供时从0开始递增。只有携带 sequence 且成功接受的块推进计数；clear 不重置。网关不补默认值，连续性由后端校验。
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.event_id is not None:
            result['event_id'] = self.event_id

        if self.audio is not None:
            result['audio'] = self.audio

        if self.sequence is not None:
            result['sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('audio') is not None:
            self.audio = m.get('audio')

        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')

        return self

