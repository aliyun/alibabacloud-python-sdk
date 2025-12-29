# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityIpsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        modify_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_ip_group_attribute: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The method that is used to modify the IP address whitelist. Valid values:
        # 
        # *   **Cover**: overwrites the original IP address whitelist.
        # *   **Append**: appends data to the IP address whitelist.
        # *   **Delete**: deletes the IP address whitelist.
        # 
        # Default value: **Cover**.
        self.modify_mode = modify_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The attribute of the IP address whitelist. It can contain a maximum of 120 characters in length and can contain uppercase letters, lowercase letters, and digits.
        # 
        # This parameter is empty by default.
        self.security_ip_group_attribute = security_ip_group_attribute
        # The name of the IP address whitelist that you want to modify. Default value: **default**.
        self.security_ip_group_name = security_ip_group_name
        # The IP addresses in the IP address whitelist. Separate multiple IP addresses with commas (,). You can add a maximum of 1,000 different IP addresses to the IP address whitelist. The entries in the IP address whitelist must be in one of the following formats:
        # 
        # *   IP addresses, such as 127.0.0.1.
        # *   CIDR blocks, such as 127.0.0.1/24. In this example, 24 indicates that the prefix of each IP address in the IP address whitelist is 24 bits in length. You can replace 24 with a value within the range of 1 to 32.
        # 
        # This parameter is required.
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_ip_group_attribute is not None:
            result['SecurityIpGroupAttribute'] = self.security_ip_group_attribute

        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name

        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityIpGroupAttribute') is not None:
            self.security_ip_group_attribute = m.get('SecurityIpGroupAttribute')

        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')

        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')

        return self

