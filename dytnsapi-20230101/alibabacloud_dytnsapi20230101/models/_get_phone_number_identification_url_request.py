# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPhoneNumberIdentificationUrlRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        ip: str = None,
        out_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        remember_phone_number: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The authorization code.
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The IP address of the subscriber\\"s phone.
        self.ip = ip
        # The external ID.
        # 
        # This parameter is required.
        self.out_id = out_id
        self.owner_id = owner_id
        # The phone number of the subscriber. The phone number is in the Mobile Station International Subscriber Directory Number (MSISDN) format.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # Specifies whether to remember the phone number.
        self.remember_phone_number = remember_phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.remember_phone_number is not None:
            result['RememberPhoneNumber'] = self.remember_phone_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('RememberPhoneNumber') is not None:
            self.remember_phone_number = m.get('RememberPhoneNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

