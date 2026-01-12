# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterAccessWhiteListRequest(DaraModel):
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
        security_ips: str = None,
    ):
        # The attribute of the IP address whitelist. By default, this parameter is **empty**.
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute
        # The name of the IP address whitelist that you want to modify.
        # 
        # >  If you do not specify this parameter, the default IP address whitelist is modified.
        self.dbcluster_iparray_name = dbcluster_iparray_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The method that is used to modify the IP address whitelist. Valid values:
        # 
        # *   **Cover**: overwrites the original IP address whitelist.
        # *   **Append**: appends the specified IP addresses to the original IP address whitelist.
        # *   **Delete**: deletes the original IP address whitelist.
        # 
        # >  If you do not specify this parameter, the default value of Cover is used.
        self.modify_mode = modify_mode
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IP addresses in the IP address whitelist. You can specify IP addresses in the following formats:
        # 
        # *   IP address. For example, you can set SecurityIps to 192.168.0.1. This allows you to use this IP address to access your ApsaraDB for ClickHouse cluster.
        # *   CIDR block. For example, you can set SecurityIps to 192.168.0.0/24. This allows you to use the IP addresses from 192.168.0.1 to 192.168.0.255 to access your ApsaraDB for ClickHouse cluster.
        # 
        # > 
        # 
        # *   Do not set SecurityIps to 0.0.0.0.
        # 
        # *   If you set SecurityIps to 127.0.0.1, all IP addresses are blocked from accessing your ApsaraDB for ClickHouse cluster.
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

        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips

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

        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')

        return self

