# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220302 import multi_modal_guard_ws_models as main_models
from darabonba.model import DaraModel

class AckMessageEvent(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: main_models.AckMessageEventData = None,
    ):
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.data is not None:
            result['Data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Data') is not None:
            temp_model = main_models.AckMessageEventData()
            self.data = temp_model.from_map(m.get('Data'))

        return self

class AckMessageEventData(DaraModel):
    def __init__(
        self,
        triggered: bool = None,
        msg_id: str = None,
    ):
        self.triggered = triggered
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.triggered is not None:
            result['Triggered'] = self.triggered

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Triggered') is not None:
            self.triggered = m.get('Triggered')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        return self

