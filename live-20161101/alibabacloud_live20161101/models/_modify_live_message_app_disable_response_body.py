# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLiveMessageAppDisableResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_sign: str = None,
        disable: bool = None,
        request_id: str = None,
    ):
        # The ID of the interactive messaging application.
        self.app_id = app_id
        # The signature of the interactive messaging application. It is required by the interactive messaging SDK.
        self.app_sign = app_sign
        # Indicates whether the interactive messaging application is disabled.
        self.disable = disable
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_sign is not None:
            result['AppSign'] = self.app_sign

        if self.disable is not None:
            result['Disable'] = self.disable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSign') is not None:
            self.app_sign = m.get('AppSign')

        if m.get('Disable') is not None:
            self.disable = m.get('Disable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

