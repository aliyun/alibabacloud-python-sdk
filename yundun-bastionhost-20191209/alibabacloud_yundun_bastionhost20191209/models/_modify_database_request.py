# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDatabaseRequest(DaraModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_id: str = None,
        database_name: str = None,
        database_port: str = None,
        database_private_address: str = None,
        database_public_address: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        region_id: str = None,
        source_instance_id: str = None,
    ):
        # The new address type of the database. Valid values:
        # 
        # *   **Public**
        # *   **Private**
        self.active_address_type = active_address_type
        # The new remarks of the database.
        self.comment = comment
        # The ID of the database to modify.
        # 
        # This parameter is required.
        self.database_id = database_id
        # The new name of the database.
        self.database_name = database_name
        # The new port of the database.
        self.database_port = database_port
        # The new internal address of the database. Specify an IPv4 address or a domain name.
        self.database_private_address = database_private_address
        # The new public address of the database. Specify an IPv4 address or a domain name.
        self.database_public_address = database_public_address
        # The ID of the bastion host that manages the database to modify.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the new network domain for the database.
        # 
        # >  You can call the [ListNetworkDomains](https://help.aliyun.com/document_detail/2758827.html) operation to query the network domain ID.
        self.network_domain_id = network_domain_id
        # The region ID of the bastion host that manages the database to modify.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the ApsaraDB for RDS instance or PolarDB cluster to modify.
        # 
        # > This parameter is required if **Source** is set to **Rds** or **PolarDB**.
        self.source_instance_id = source_instance_id

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

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.database_port is not None:
            result['DatabasePort'] = self.database_port

        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address

        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')

        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')

        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        return self

