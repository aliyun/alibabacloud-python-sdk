# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatabaseRequest(DaraModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_name: str = None,
        database_port: int = None,
        database_private_address: str = None,
        database_public_address: str = None,
        database_type: str = None,
        instance_id: str = None,
        instance_member_id: int = None,
        network_domain_id: str = None,
        polar_dbendpoint_type: str = None,
        region_id: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_region_id: str = None,
    ):
        # The address type of the database to add. Valid values:
        # 
        # *   Public
        # *   Private
        # 
        # This parameter is required.
        self.active_address_type = active_address_type
        # The remarks of the database to add. The remarks can be up to 500 characters in length.
        self.comment = comment
        # The name of the database to add. This parameter is required if Source is set to **Local**.
        self.database_name = database_name
        # The port of the database. This parameter is required if Source is set to **Local**.
        self.database_port = database_port
        # The internal IP address of the database. Specify an IPv4 address or a domain name.
        # 
        # >  This parameter is required if ActiveAddressType is set to Private.
        self.database_private_address = database_private_address
        # The public IP address of the database. Specify an IPv4 address or a domain name.
        # 
        # >  This parameter is required if ActiveAddressType is set to Public.
        self.database_public_address = database_public_address
        # The type of the database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **Oracle**
        # *   **PostgreSQL**
        # *   **SQLServer**
        # 
        # This parameter is required.
        self.database_type = database_type
        # The bastion host ID.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_member_id = instance_member_id
        # The ID of the network domain to which the database to add belongs.
        # 
        # >  You can call the [ListNetworkDomains](https://help.aliyun.com/document_detail/2758827.html) operation to query the network domain ID.
        self.network_domain_id = network_domain_id
        # The endpoint type of the PolarDB database. This parameter is required if Source is set to PolarDB. Valid values:
        # 
        # *   Cluster
        # *   Primary
        self.polar_dbendpoint_type = polar_dbendpoint_type
        # The region ID of the bastion host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The type of the database to add. Valid values:
        # 
        # *   Local: on-premises database.
        # *   Rds: ApsaraDB RDS instance.
        # *   PolarDB: PolarDB cluster.
        # 
        # This parameter is required.
        self.source = source
        # The instance ID of the database to add.
        # 
        # > This parameter is required if **Source** is set to **Rds** or **PolarDB**.
        self.source_instance_id = source_instance_id
        # The region ID of the database to add.
        # 
        # >  This parameter is required if **Source** is set to **Rds** or **PolarDB**.
        self.source_instance_region_id = source_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.database_port is not None:
            result['DatabasePort'] = self.database_port

        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address

        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_member_id is not None:
            result['InstanceMemberId'] = self.instance_member_id

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.polar_dbendpoint_type is not None:
            result['PolarDBEndpointType'] = self.polar_dbendpoint_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_instance_region_id is not None:
            result['SourceInstanceRegionId'] = self.source_instance_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')

        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')

        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceMemberId') is not None:
            self.instance_member_id = m.get('InstanceMemberId')

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('PolarDBEndpointType') is not None:
            self.polar_dbendpoint_type = m.get('PolarDBEndpointType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourceInstanceRegionId') is not None:
            self.source_instance_region_id = m.get('SourceInstanceRegionId')

        return self

