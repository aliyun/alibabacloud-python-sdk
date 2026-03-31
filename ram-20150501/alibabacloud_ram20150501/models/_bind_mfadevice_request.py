# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindMFADeviceRequest(DaraModel):
    def __init__(
        self,
        authentication_code_1: str = None,
        authentication_code_2: str = None,
        serial_number: str = None,
        user_name: str = None,
    ):
        # The first authentication code.
        self.authentication_code_1 = authentication_code_1
        # The second authentication code.
        self.authentication_code_2 = authentication_code_2
        # The serial number of the MFA device.
        self.serial_number = serial_number
        # The name of the RAM user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_code_1 is not None:
            result['AuthenticationCode1'] = self.authentication_code_1

        if self.authentication_code_2 is not None:
            result['AuthenticationCode2'] = self.authentication_code_2

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationCode1') is not None:
            self.authentication_code_1 = m.get('AuthenticationCode1')

        if m.get('AuthenticationCode2') is not None:
            self.authentication_code_2 = m.get('AuthenticationCode2')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

