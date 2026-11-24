# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class SessionCreate(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        mode: str = None,
        language_pair: List[str] = None,
        session: main_models.SessionCreateSession = None,
    ):
        # This parameter is required.
        self.type = type
        # 可省略；提供时必须为非空、非纯空白字符串，用于关联响应。
        self.event_id = event_id
        # 与 session.mode 二选一；同时提供必须一致。均省略时后端选择 single，网关不补默认值。
        self.mode = mode
        # 双向条件必填，与 session.language_pair 二选一；同时提供时内容及顺序必须一致。仅支持 zh 与 en/ja/ko 组合，顺序可反转，由后端校验。
        self.language_pair = language_pair
        # 单向可省略或指定 mode=single；双向须指定 bidirectional 模式及语言对。创建后模式与语言对不可变，音频和输出配置通过 SessionUpdate 下发。
        self.session = session

    def validate(self):
        if self.session:
            self.session.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.event_id is not None:
            result['event_id'] = self.event_id

        if self.mode is not None:
            result['mode'] = self.mode

        if self.language_pair is not None:
            result['language_pair'] = self.language_pair

        if self.session is not None:
            result['session'] = self.session.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('language_pair') is not None:
            self.language_pair = m.get('language_pair')

        if m.get('session') is not None:
            temp_model = main_models.SessionCreateSession()
            self.session = temp_model.from_map(m.get('session'))

        return self

class SessionCreateSession(DaraModel):
    def __init__(
        self,
        mode: str = None,
        language_pair: List[str] = None,
    ):
        self.mode = mode
        # 双向须提供本字段或根节点 language_pair；须包含 zh 和 en/ja/ko 之一。
        self.language_pair = language_pair

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.language_pair is not None:
            result['language_pair'] = self.language_pair

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('language_pair') is not None:
            self.language_pair = m.get('language_pair')

        return self

