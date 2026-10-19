# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityIpsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        modify_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_ip_group_attribute: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
        security_token: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The modification method. Valid values:
        # 
        # * **Cover** (default): overwrites the original whitelist.
        # * **Append**: appends IP addresses to the whitelist.
        # * **Delete**: deletes the whitelist.
        self.modify_mode = modify_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The attribute of the IP whitelist group. This parameter is empty by default. The console does not display the whitelist group if the value is set to **hidden**.
        self.security_ip_group_attribute = security_ip_group_attribute
        # The name of the IP whitelist group.
        # <warning>You cannot modify a system-generated whitelist group. If you do not specify this parameter, the whitelist of the default group is modified.</warning>
        self.security_ip_group_name = security_ip_group_name
        # The IP addresses in the IP whitelist group. You can add up to 1,000 IP addresses. Separate multiple IP addresses with commas (,). The following formats are supported: 0.0.0.0/0,10.23.12.24 or 10.23.12.24/24 (CIDR notation, where /24 specifies the prefix length, which ranges from 1 to 32).
        # 
        # This parameter is required.
        self.security_ips = security_ips
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

