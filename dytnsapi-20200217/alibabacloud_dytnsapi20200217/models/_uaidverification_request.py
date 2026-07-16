# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UAIDVerificationRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        carrier: str = None,
        ip: str = None,
        out_id: str = None,
        owner_id: int = None,
        province: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        token: str = None,
        user_grant_id: str = None,
    ):
        # The authorization code.
        # 
        # > In **Cell Phone Number Service** -> [**Tag Marketplace**](https://dytns.console.aliyun.com/analysis/square), select a tag and submit a usage application. After the application is approved, you will obtain this authorization code.
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The carrier of the user. Valid values:
        # - **CM**: China Mobile.
        # - **CU**: China Unicom.
        # - **CT**: China Telecom.
        # 
        # This parameter is required.
        self.carrier = carrier
        # The public IP address. This parameter is required when the carrier is China Unicom (CU). Both IPv4 and IPv6 addresses are supported.
        self.ip = ip
        # The external serial number.
        self.out_id = out_id
        self.owner_id = owner_id
        # The province ID. This parameter is optional when the carrier is China Unicom (CU). The value must be the same as the value of the province field in the response returned when the token is obtained.
        self.province = province
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The carrier authorization token.  
        # > For information about how to obtain the authorization token and its signature, see the GetUAIDApplyTokenSign API documentation.
        # 
        # This parameter is required.
        self.token = token
        # The user authorization code, which indicates that the user has granted authorization. The value must be a unique random number that does not exceed 128 characters in length.  
        # 
        # <warning>When you integrate the service, we recommend that you include UAID-related content in the privacy policy of your product.</warning>
        self.user_grant_id = user_grant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.carrier is not None:
            result['Carrier'] = self.carrier

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.province is not None:
            result['Province'] = self.province

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.token is not None:
            result['Token'] = self.token

        if self.user_grant_id is not None:
            result['UserGrantId'] = self.user_grant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserGrantId') is not None:
            self.user_grant_id = m.get('UserGrantId')

        return self

