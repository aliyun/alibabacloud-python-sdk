# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDTCSecurityIpHostsForSQLServerRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_ip_hosts: str = None,
        security_token: str = None,
        white_list_group_name: str = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IP address of the ECS instance and the hostname of the Windows computer. Format: `IP address,Hostname`. Separate multiple entries with semicolon (;).
        # 
        # >  For more information about how to query the computer hostname, see [Configure a distributed transaction whitelist](https://help.aliyun.com/document_detail/124321.html).
        # 
        # This parameter is required.
        self.security_ip_hosts = security_ip_hosts
        self.security_token = security_token
        # The name of the IP address whitelist.
        # 
        # This parameter is required.
        self.white_list_group_name = white_list_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_ip_hosts is not None:
            result['SecurityIpHosts'] = self.security_ip_hosts

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.white_list_group_name is not None:
            result['WhiteListGroupName'] = self.white_list_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityIpHosts') is not None:
            self.security_ip_hosts = m.get('SecurityIpHosts')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('WhiteListGroupName') is not None:
            self.white_list_group_name = m.get('WhiteListGroupName')

        return self

