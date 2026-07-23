# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class InterruptForArbitrationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        chat_id: str = None,
        hub_request_id: str = None,
        interrupt: main_models.InterruptForArbitrationRequestInterrupt = None,
        session_id: str = None,
    ):
        self.app_id = app_id
        self.chat_id = chat_id
        # This parameter is required.
        self.hub_request_id = hub_request_id
        # This parameter is required.
        self.interrupt = interrupt
        self.session_id = session_id

    def validate(self):
        if self.interrupt:
            self.interrupt.validate()

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

        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt.to_map()

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
            temp_model = main_models.InterruptForArbitrationRequestInterrupt()
            self.interrupt = temp_model.from_map(m.get('Interrupt'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

class InterruptForArbitrationRequestInterrupt(DaraModel):
    def __init__(
        self,
        submit: bool = None,
    ):
        # This parameter is required.
        self.submit = submit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.submit is not None:
            result['Submit'] = self.submit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Submit') is not None:
            self.submit = m.get('Submit')

        return self

