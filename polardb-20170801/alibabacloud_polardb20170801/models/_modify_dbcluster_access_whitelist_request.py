# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterAccessWhitelistRequest(DaraModel):
    def __init__(
        self,
        dbcluster_iparray_attribute: str = None,
        dbcluster_iparray_name: str = None,
        dbcluster_id: str = None,
        modify_mode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_ids: str = None,
        security_ips: str = None,
        white_list_type: str = None,
    ):
        # The attribute of the IP address whitelist group. If you set this parameter to \\`hidden\\`, the whitelist group is not visible in the console.
        # 
        # > - You cannot hide an IP address whitelist group that is already visible in the console.
        # >
        # > - This parameter is available only when **WhiteListType** is set to **IP**.
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute
        # The name of the IP address whitelist group. The name must be 2 to 120 characters in length. It must consist of lowercase letters and digits. The name must start with a letter and end with a letter or a digit.
        # 
        # - If the specified whitelist group name does not exist, a new whitelist group is created.
        # 
        # - If the specified whitelist group name already exists, the whitelist group is modified.
        # 
        # - If you do not specify this parameter, the \\`default\\` group is modified.
        # 
        # > * A cluster can have up to 50 IP address whitelist groups.
        # >
        # > * This parameter is available only when **WhiteListType** is set to **IP**.
        self.dbcluster_iparray_name = dbcluster_iparray_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The method used to modify the IP address whitelist. Valid values:
        # 
        # - **Cover**: Overwrites the original IP address whitelist. This is the default value.
        # 
        # - **Append**: Appends IP addresses to the whitelist.
        # 
        # - **Delete**: Deletes IP addresses from the whitelist.
        # 
        # > This parameter is available only when **WhiteListType** is set to **IP**.
        self.modify_mode = modify_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security group ID. Separate multiple security group IDs with commas (,).
        # 
        # > - A cluster can be associated with up to three security groups.
        # >
        # > - This parameter is available only when **WhiteListType** is set to **SecurityGroup**.
        self.security_group_ids = security_group_ids
        # The IP addresses or CIDR blocks in the IP address whitelist group. All IP address whitelist groups can contain a total of 1,000 IP addresses or CIDR blocks. Separate multiple IP addresses with commas (,). The following formats are supported:
        # 
        # - IP address format. For example: 10.23.12.24.
        # 
        # - CIDR format. For example: 10.23.12.24/24. The number 24 indicates the prefix length of the IP address. The prefix length can range from 1 to 32.
        # 
        # > This parameter is available only when **WhiteListType** is set to **IP**.
        self.security_ips = security_ips
        # The type of the whitelist. Valid values:
        # 
        # - **IP**: IP address whitelist group.
        # 
        # - **SecurityGroup**: Security group.
        # 
        # The default value is **IP**.
        self.white_list_type = white_list_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute

        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

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

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips

        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')

        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

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

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')

        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')

        return self

