# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InterruptForArbitrationShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        chat_id: str = None,
        hub_request_id: str = None,
        interrupt_shrink: str = None,
        session_id: str = None,
    ):
        self.app_id = app_id
        self.chat_id = chat_id
        # This parameter is required.
        self.hub_request_id = hub_request_id
        # This parameter is required.
        self.interrupt_shrink = interrupt_shrink
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.hub_request_id is not None:
            result['HubRequestId'] = self.hub_request_id

        if self.interrupt_shrink is not None:
            result['Interrupt'] = self.interrupt_shrink

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('HubRequestId') is not None:
            self.hub_request_id = m.get('HubRequestId')

        if m.get('Interrupt') is not None:
            self.interrupt_shrink = m.get('Interrupt')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

