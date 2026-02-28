# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class RemoveTerminalsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        terminals: main_models.RemoveTerminalsResponseBodyTerminals = None,
    ):
        self.request_id = request_id
        self.terminals = terminals

    def validate(self):
        if self.terminals:
            self.terminals.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.terminals is not None:
            result['Terminals'] = self.terminals.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Terminals') is not None:
            temp_model = main_models.RemoveTerminalsResponseBodyTerminals()
            self.terminals = temp_model.from_map(m.get('Terminals'))

        return self

class RemoveTerminalsResponseBodyTerminals(DaraModel):
    def __init__(
        self,
        terminal: List[main_models.RemoveTerminalsResponseBodyTerminalsTerminal] = None,
    ):
        self.terminal = terminal

    def validate(self):
        if self.terminal:
            for v1 in self.terminal:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Terminal'] = []
        if self.terminal is not None:
            for k1 in self.terminal:
                result['Terminal'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.terminal = []
        if m.get('Terminal') is not None:
            for k1 in m.get('Terminal'):
                temp_model = main_models.RemoveTerminalsResponseBodyTerminalsTerminal()
                self.terminal.append(temp_model.from_map(k1))

        return self

class RemoveTerminalsResponseBodyTerminalsTerminal(DaraModel):
    def __init__(
        self,
        code: int = None,
        id: str = None,
        message: str = None,
    ):
        self.code = code
        self.id = id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

