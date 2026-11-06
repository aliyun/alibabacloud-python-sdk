# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentSessionEventsRequest(DaraModel):
    def __init__(
        self,
        event_epoch: str = None,
        session_code: str = None,
    ):
        # The epoch identifier of the event stream, obtained from data.eventEpoch in the stream_open control frame of the server. Pass the original value only when Last-Event-Id of the same native session and the same epoch is provided. Omit this parameter when subscribing for the first time or when the epoch is not obtained. Do not construct it yourself or reuse it across native sessions.
        self.event_epoch = event_epoch
        # The ID of the target agent session. Set the value to the SessionId returned by CreateAgentSession. The parameter name for this API operation is SessionCode.
        # 
        # This parameter is required.
        self.session_code = session_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_epoch is not None:
            result['EventEpoch'] = self.event_epoch

        if self.session_code is not None:
            result['SessionCode'] = self.session_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventEpoch') is not None:
            self.event_epoch = m.get('EventEpoch')

        if m.get('SessionCode') is not None:
            self.session_code = m.get('SessionCode')

        return self

