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
        user_principal_name: str = None,
    ):
        # The first verification code.
        # 
        # >  You can call the [CreateVirtualMFADevice](https://help.aliyun.com/document_detail/186179.html) operation to create an MFA device and generate a key (value of `Base32StringSeed`). Then, use the key on the Alibaba Cloud app to manually add an MFA device, and obtain the two consecutive verification codes.
        self.authentication_code_1 = authentication_code_1
        # The second verification code.
        # 
        # >  You can call the [CreateVirtualMFADevice](https://help.aliyun.com/document_detail/186179.html) operation to create an MFA device and generate a key (value of `Base32StringSeed`). Then, use the key on the Alibaba Cloud app to manually add an MFA device, and obtain the two consecutive verification codes.
        self.authentication_code_2 = authentication_code_2
        # The serial number of the MFA device.
        # 
        # >  You can call the [CreateVirtualMFADevice](https://help.aliyun.com/document_detail/186179.html) operation to obtain the serial number of the MFA device.
        self.serial_number = serial_number
        # The logon name of the RAM user.
        # 
        # This parameter is required.
        self.user_principal_name = user_principal_name

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

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationCode1') is not None:
            self.authentication_code_1 = m.get('AuthenticationCode1')

        if m.get('AuthenticationCode2') is not None:
            self.authentication_code_2 = m.get('AuthenticationCode2')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

