# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmartAccessGatewayClientUserRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_ip: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        user_mail: str = None,
        user_name: str = None,
    ):
        # The maximum bandwidth value. Unit: Kbit/s. Valid values: **1 to 20000**. Default value: **2000**.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # *   If you enable the client app service, you must set the IP address of the client app. The current client account uses the specified IP address to connect to Alibaba Cloud.
        # 
        # >  The IP address must fall within a private CIDR block.
        # 
        # *   If you disable the client app service, an IP address within a private CIDR block is assigned to the client account. Each connection to Alibaba Cloud uses a different IP address.
        self.client_ip = client_ip
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password that is used to log on to the SAG app.
        # 
        # The password must be 8 to 32 characters in length. It can contain letters, digits, underscores (_), at signs (@), and hyphens (-). It must start with a letter or a digit.
        self.password = password
        # The region ID of the Smart Access Gateway (SAG) app instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SAG app instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The email address of the client account. The username and password are sent to the specified email address by the administrator.
        # 
        # This parameter is required.
        self.user_mail = user_mail
        # The username of the client account. The usernames of client accounts added to the same SAG app instance must be unique.
        # 
        # The username must be 7 to 33 characters in length, and can contain letters, digits, underscores (_), at signs (@), periods (.), and hyphens (-). It must start with a letter or a digit.
        # 
        # >  For a client account, if you specify the username, you must also specify the password. If you specify the password, you must specify the username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.user_mail is not None:
            result['UserMail'] = self.user_mail

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

