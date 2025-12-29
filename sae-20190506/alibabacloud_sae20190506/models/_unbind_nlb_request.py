# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindNlbRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        nlb_id: str = None,
        port: int = None,
        protocol: str = None,
    ):
        # A short description of struct
        self.app_id = app_id
        # The ID of NLB instance.
        self.nlb_id = nlb_id
        # The listener port of the instance. Valid values: 0 to 65535.
        self.port = port
        # The type of the protocol. Valid values:
        # 
        # *   **TCP**.
        # *   **UDP**.
        # *   **TCPSSL**.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.nlb_id is not None:
            result['NlbId'] = self.nlb_id

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('NlbId') is not None:
            self.nlb_id = m.get('NlbId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

