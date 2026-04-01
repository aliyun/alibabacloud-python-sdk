# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateInstancePublicConnectionRequest(DaraModel):
    def __init__(
        self,
        babelfish_port: str = None,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        general_group_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pgbouncer_port: str = None,
        port: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The Tabular Data Stream (TDS) port of the instance for which Babelfish is enabled.
        # 
        # > This parameter applies only to ApsaraDB RDS for PostgreSQL instances. For more information about Babelfish for ApsaraDB RDS for PostgreSQL, see [Introduction to Babelfish](https://help.aliyun.com/document_detail/428613.html).
        self.babelfish_port = babelfish_port
        # The prefix of the public endpoint. A valid public endpoint is in the following format: `Prefix.Database engine.rds.aliyuncs.com`. Example: `test1234.mysql.rds.aliyuncs.com`.
        # 
        # > The value can be 5 to 40 characters in length and can contain letters, digits, and hyphens (-). The value cannot contain any of the following characters: ~ ! # % ^ & \\* = + | {} ; : \\" " , <> / ?
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the dedicated cluster to which the instance belongs. This parameter is available only when the instance is created in an ApsaraDB MyBase cluster that runs MySQL on Standard Edition.
        self.general_group_name = general_group_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The PgBouncer port.
        # 
        # > This parameter is available only for instances that run PostgreSQL.
        self.pgbouncer_port = pgbouncer_port
        # The public port of the instance. Valid values: **1000 to 5999**.
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
        if self.babelfish_port is not None:
            result['BabelfishPort'] = self.babelfish_port

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BabelfishPort') is not None:
            self.babelfish_port = m.get('BabelfishPort')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

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

        return self

