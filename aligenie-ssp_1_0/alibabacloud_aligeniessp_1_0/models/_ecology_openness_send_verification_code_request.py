# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EcologyOpennessSendVerificationCodeRequest(DaraModel):
    def __init__(
        self,
        phone_number: str = None,
        region: str = None,
        session_id: str = None,
    ):
        # Phone number
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # Region encoding
        # 
        # This parameter is required.
        self.region = region
        # Session ID
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.region is not None:
            result['Region'] = self.region

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

