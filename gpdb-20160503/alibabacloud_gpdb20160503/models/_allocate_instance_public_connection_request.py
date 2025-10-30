# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateInstancePublicConnectionRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        owner_id: int = None,
        port: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The network type of the endpoint. Valid values:
        # 
        # *   **primary**: primary endpoint
        # *   **cluster**: instance endpoint. This value is supported only for an instance that contains multiple coordinator nodes.
        # 
        # >  The default value is primary.
        self.address_type = address_type
        # The prefix of the endpoint.
        # 
        # Specify a prefix for the endpoint. Example: `gp-bp12ga6v69h86****`. In this example, the endpoint is `gp-bp12ga6v69h86****.gpdb.rds.aliyuncs.com`.
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The port number. Example: 5432.
        # 
        # This parameter is required.
        self.port = port
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port is not None:
            result['Port'] = self.port

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

