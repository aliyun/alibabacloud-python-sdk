# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendAsyncEmailCaptchaRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        contact_info: str = None,
        contactor_id: str = None,
    ):
        self.app_name = app_name
        self.contact_info = contact_info
        self.contactor_id = contactor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.contact_info is not None:
            result['ContactInfo'] = self.contact_info

        if self.contactor_id is not None:
            result['ContactorId'] = self.contactor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ContactInfo') is not None:
            self.contact_info = m.get('ContactInfo')

        if m.get('ContactorId') is not None:
            self.contactor_id = m.get('ContactorId')

        return self

