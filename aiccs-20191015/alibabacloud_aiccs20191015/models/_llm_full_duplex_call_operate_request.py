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
        # The unique receipt ID of the call. You can obtain this ID by calling the LlmSmartCallFullDuplex operation.
        # 
        # This parameter is required.
        self.call_id = call_id
        # The action command: play / flush / hangup / sendDtmf.
        # 
        # This parameter is required.
        self.command = command
        # The extension parameter, a JSON character string. The metric description for each command:
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

