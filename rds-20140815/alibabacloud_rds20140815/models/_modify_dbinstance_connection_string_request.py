# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceConnectionStringRequest(DaraModel):
    def __init__(
        self,
        babelfish_port: str = None,
        connection_string_prefix: str = None,
        current_connection_string: str = None,
        dbinstance_id: str = None,
        general_group_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pgbouncer_port: str = None,
        port: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retain_vip: bool = None,
        target_dbinstance_id: str = None,
    ):
        # The TDS port number for Babelfish for RDS PostgreSQL.
        # > This parameter is applicable only to ApsaraDB RDS for PostgreSQL instances. For more information about Babelfish for RDS PostgreSQL, see [Introduction to Babelfish](https://help.aliyun.com/document_detail/428613.html).
        self.babelfish_port = babelfish_port
        # The prefix of the endpoint. You can modify only the prefix of the value specified by the **CurrentConnectionString** parameter.
        # >The prefix must be 8 to 64 characters in length and cannot contain Chinese characters or special characters (~!#%^&*=+\\|{};:\\"",<>/?). The prefix can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The current endpoint of the instance. The endpoint can be a public endpoint or internal endpoint, or a classic network connectivity endpoint in hybrid access mode.
        # >Modification of read/write splitting connection endpoints is not supported.
        # 
        # This parameter is required.
        self.current_connection_string = current_connection_string
        # The instance ID. You can call DescribeDBInstances to obtain the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the group to which the dedicated cluster MySQL general-purpose instance belongs.
        self.general_group_name = general_group_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The PgBouncer port number.
        # > This parameter is applicable only to ApsaraDB RDS for PostgreSQL instances. If PgBouncer is enabled, you can modify the PgBouncer port number.
        self.pgbouncer_port = pgbouncer_port
        # The target port.
        # 
        # This parameter is required.
        self.port = port
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to retain the virtual IP address (VIP) when swapping the endpoint.
        # 
        # - **true**: The VIP is retained.
        # - **false** (default): The VIP is not retained.
        # 
        # > This parameter is applicable only to ApsaraDB RDS for PostgreSQL instances.
        self.retain_vip = retain_vip
        # The instance ID of the target ApsaraDB RDS for PostgreSQL instance with which you want to swap the endpoint.
        # 
        # > This parameter is applicable only to ApsaraDB RDS for PostgreSQL instances.
        self.target_dbinstance_id = target_dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.babelfish_port is not None:
            result['BabelfishPort'] = self.babelfish_port

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.general_group_name is not None:
            result['GeneralGroupName'] = self.general_group_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pgbouncer_port is not None:
            result['PGBouncerPort'] = self.pgbouncer_port

        if self.port is not None:
            result['Port'] = self.port

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retain_vip is not None:
            result['RetainVip'] = self.retain_vip

        if self.target_dbinstance_id is not None:
            result['TargetDBInstanceId'] = self.target_dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BabelfishPort') is not None:
            self.babelfish_port = m.get('BabelfishPort')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('GeneralGroupName') is not None:
            self.general_group_name = m.get('GeneralGroupName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PGBouncerPort') is not None:
            self.pgbouncer_port = m.get('PGBouncerPort')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetainVip') is not None:
            self.retain_vip = m.get('RetainVip')

        if m.get('TargetDBInstanceId') is not None:
            self.target_dbinstance_id = m.get('TargetDBInstanceId')

        return self

