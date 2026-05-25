# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LlmFullDuplexCallOperateRequest(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        command: str = None,
        param: str = None,
    ):
        # 通话的唯一回执 ID。可通过 llmSmartCallFullDuplex 接口获取。
        # 
        # This parameter is required.
        self.call_id = call_id
        # 动作指令：play / flush / hangup / sendDtmf
        # 
        # This parameter is required.
        self.command = command
        # 扩展参数，JSON 字符串。各 command 参数说明：
        self.param = param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.command is not None:
            result['Command'] = self.command

        if self.param is not None:
            result['Param'] = self.param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        return self

