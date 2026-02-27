# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SendOpsMessageToTerminalsRequest(DaraModel):
    def __init__(
        self,
        delay: bool = None,
        msg: str = None,
        ops_action: str = None,
        uuids: List[str] = None,
        wait_for_ack: bool = None,
    ):
        self.delay = delay
        self.msg = msg
        self.ops_action = ops_action
        self.uuids = uuids
        self.wait_for_ack = wait_for_ack

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay is not None:
            result['Delay'] = self.delay

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.ops_action is not None:
            result['OpsAction'] = self.ops_action

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        if self.wait_for_ack is not None:
            result['WaitForAck'] = self.wait_for_ack

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('OpsAction') is not None:
            self.ops_action = m.get('OpsAction')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        if m.get('WaitForAck') is not None:
            self.wait_for_ack = m.get('WaitForAck')

        return self

