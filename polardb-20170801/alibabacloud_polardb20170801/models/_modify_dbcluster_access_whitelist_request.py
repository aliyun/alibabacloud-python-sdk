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
        pfs_instance_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_ids: str = None,
        security_ips: str = None,
        white_list_type: str = None,
    ):
        # The attribute of the IP whitelist group. If you set this parameter to **hidden**, the group is not displayed in the console.
        # 
        # > - IP whitelist groups that are already displayed in the console cannot be hidden.
        # > - This parameter takes effect only when **WhiteListType** is set to **IP**.
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute
        # The name of the IP whitelist group. The name must be 2 to 120 characters in length and can contain lowercase letters and digits. The name must start with a letter and end with a letter or digit.
        # 
        # - If the specified whitelist group name does not exist, a new whitelist group is created.
        # - If the specified whitelist group name already exists, the whitelist group is modified.
        # - If this parameter is not specified, the default group is modified. 
        # 
        # > - A cluster supports up to 50 IP whitelist groups.
        # > - This parameter takes effect only when **WhiteListType** is set to **IP**.
        self.dbcluster_iparray_name = dbcluster_iparray_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The method used to modify the IP whitelist. Valid values:
        # - **Cover**: overwrites the original IP whitelist. This is the default value.
        # - **Append**: appends IP addresses to the IP whitelist.
        # - **Delete**: removes IP addresses from the IP whitelist.
        # 
        # > This parameter takes effect only when **WhiteListType** is set to **IP**.
        self.modify_mode = modify_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The file system instance ID.
        self.pfs_instance_id = pfs_instance_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security group IDs. Separate multiple security group IDs with commas (,).
        # 
        # > - A cluster supports up to 3 security groups.
        # > - This parameter takes effect only when **WhiteListType** is set to **SecurityGroup**.
        self.security_group_ids = security_group_ids
        # The IP addresses or CIDR blocks in the IP whitelist group. You can add up to 1,000 IP addresses or CIDR blocks across all IP whitelist groups. Separate multiple IP addresses with commas (,). The following two formats are supported: 
        # 
        # - IP address format, such as 10.23.12.24.
        # - CIDR format, such as 10.23.12.24/24, where 24 indicates the length of the prefix in the IP address. The prefix length ranges from 1 to 32.
        # 
        # > This parameter takes effect only when **WhiteListType** is set to **IP**.
        self.security_ips = security_ips
        # The type of the whitelist. Valid values:
        # 
        # - **IP**: IP whitelist group.
        # - **SecurityGroup**: security group.
        # 
        # Default value: **IP**.
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

        if self.pfs_instance_id is not None:
            result['PfsInstanceId'] = self.pfs_instance_id

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

        if m.get('PfsInstanceId') is not None:
            self.pfs_instance_id = m.get('PfsInstanceId')

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

