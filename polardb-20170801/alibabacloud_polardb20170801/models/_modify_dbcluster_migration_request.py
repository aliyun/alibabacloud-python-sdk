# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterMigrationRequest(DaraModel):
    def __init__(
        self,
        connection_strings: str = None,
        dbcluster_id: str = None,
        new_master_instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        source_rdsdbinstance_id: str = None,
        swap_connection_string: str = None,
    ):
        # The endpoints to be switched. The endpoints are in the JSON format.
        # 
        # > This parameter is valid when the SwapConnectionString parameter is set to true.
        self.connection_strings = connection_strings
        # The ID of cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the new instance or new cluster. Valid values:
        # 
        # *   To perform a data migration, enter the ID of the PolarDB cluster.
        # *   To perform a migration rollback, enter the ID of the ApsaraDB for RDS instance.
        # 
        # This parameter is required.
        self.new_master_instance_id = new_master_instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The ID of the source ApsaraDB RDS instance.
        # 
        # This parameter is required.
        self.source_rdsdbinstance_id = source_rdsdbinstance_id
        # Specifies whether to switch the endpoints. Valid values:
        # 
        # *   **true**: switches the endpoints. If you select this option, you do not need the change the endpoint in your applications.
        # *   **false**: does not switch the endpoints. If you select this option, you must specify the endpoint of the PolarDB cluster in your applications.
        # 
        # Default value: **false**.
        self.swap_connection_string = swap_connection_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_strings is not None:
            result['ConnectionStrings'] = self.connection_strings

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.new_master_instance_id is not None:
            result['NewMasterInstanceId'] = self.new_master_instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.source_rdsdbinstance_id is not None:
            result['SourceRDSDBInstanceId'] = self.source_rdsdbinstance_id

        if self.swap_connection_string is not None:
            result['SwapConnectionString'] = self.swap_connection_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStrings') is not None:
            self.connection_strings = m.get('ConnectionStrings')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('NewMasterInstanceId') is not None:
            self.new_master_instance_id = m.get('NewMasterInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SourceRDSDBInstanceId') is not None:
            self.source_rdsdbinstance_id = m.get('SourceRDSDBInstanceId')

        if m.get('SwapConnectionString') is not None:
            self.swap_connection_string = m.get('SwapConnectionString')

        return self

