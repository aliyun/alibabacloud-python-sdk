# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBEndpointAddressRequest(DaraModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbcluster_id: str = None,
        dbendpoint_id: str = None,
        net_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port: str = None,
        private_zone_address_prefix: str = None,
        private_zone_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The prefix of the new endpoint. The prefix must meet the following requirements:
        # 
        # *   It can contain lowercase letters, digits, and hyphens (-).
        # *   It must start with a letter and end with a digit or a letter.
        # *   It must be 6 to 30 characters in length.
        self.connection_string_prefix = connection_string_prefix
        # The ID of cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of the clusters that belong to your Alibaba Cloud account, such as cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the endpoint.
        # 
        # > You can call the [DescribeDBClusterEndpoints](https://help.aliyun.com/document_detail/98205.html) operation to query endpoint IDs.
        # 
        # This parameter is required.
        self.dbendpoint_id = dbendpoint_id
        # The network type of the endpoint. Valid values:
        # 
        # *   **Public**
        # *   **Private**
        # 
        # This parameter is required.
        self.net_type = net_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The port number. Valid values: 3000 to 5999.
        # 
        # > This parameter is valid only for PolarDB for MySQL clusters. If you leave this parameter empty, the default port 3306 is used.
        self.port = port
        # The prefix of the private domain name. The prefix must meet the following requirements:
        # 
        # *   The prefix can contain lowercase letters, digits, and hyphens (-).
        # *   The prefix must start with a letter and end with a digit or a letter.
        # *   The prefix must be 6 to 30 characters in length.
        # 
        # >- You can bind each internal endpoint of PolarDB to a private domain name. The private domain name takes effect only in the specified virtual private clouds (VPCs) in the current region. Private domain names are managed by using PrivateZone. You can use the CNAME record of PrivateZone to map domain names to PolarDB. You are charged a small fee for this feature. For more information, see [Pricing](https://help.aliyun.com/document_detail/71338.html).
        # >- This parameter takes effect only if you set **NetType** to Private.
        self.private_zone_address_prefix = private_zone_address_prefix
        # The name of the private zone.
        # 
        # > This parameter takes effect only when **NetType** is set to Private.
        self.private_zone_name = private_zone_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port is not None:
            result['Port'] = self.port

        if self.private_zone_address_prefix is not None:
            result['PrivateZoneAddressPrefix'] = self.private_zone_address_prefix

        if self.private_zone_name is not None:
            result['PrivateZoneName'] = self.private_zone_name

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateZoneAddressPrefix') is not None:
            self.private_zone_address_prefix = m.get('PrivateZoneAddressPrefix')

        if m.get('PrivateZoneName') is not None:
            self.private_zone_name = m.get('PrivateZoneName')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

