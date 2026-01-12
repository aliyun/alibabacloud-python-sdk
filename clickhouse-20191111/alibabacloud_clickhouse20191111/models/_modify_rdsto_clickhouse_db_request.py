# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRDSToClickhouseDbRequest(DaraModel):
    def __init__(
        self,
        ck_password: str = None,
        ck_user_name: str = None,
        clickhouse_port: int = None,
        db_cluster_id: str = None,
        limit_upper: int = None,
        owner_account: str = None,
        owner_id: int = None,
        rds_id: str = None,
        rds_password: str = None,
        rds_port: int = None,
        rds_syn_db: str = None,
        rds_syn_tables: str = None,
        rds_user_name: str = None,
        rds_vpc_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        skip_unsupported: bool = None,
    ):
        # The password of the account that is used to log on to the database in the ApsaraDB for ClickHouse cluster.
        # 
        # This parameter is required.
        self.ck_password = ck_password
        # The account that is used to log on to the database in the ApsaraDB for ClickHouse cluster.
        # 
        # This parameter is required.
        self.ck_user_name = ck_user_name
        # The port number of the ApsaraDB for ClickHouse cluster.
        self.clickhouse_port = clickhouse_port
        # The ID of the ApsaraDB for ClickHouse cluster.
        # 
        # This parameter is required.
        self.db_cluster_id = db_cluster_id
        # The maximum number of rows that can be synchronized per second.
        self.limit_upper = limit_upper
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.rds_id = rds_id
        # The password of the account that is used to log on to the database in the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.rds_password = rds_password
        # The port number of the ApsaraDB RDS for MySQL instance.
        self.rds_port = rds_port
        # The database in the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.rds_syn_db = rds_syn_db
        # The table in the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.rds_syn_tables = rds_syn_tables
        # The account that is used to log on to the database in the ApsaraDB RDS for MySQL instance.
        # 
        # This parameter is required.
        self.rds_user_name = rds_user_name
        # The ID of the virtual private cloud (VPC) to which the ApsaraDB RDS for MySQL instance belongs.
        self.rds_vpc_id = rds_vpc_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to ignore databases that do not support synchronization. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # This parameter is required.
        self.skip_unsupported = skip_unsupported

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ck_password is not None:
            result['CkPassword'] = self.ck_password

        if self.ck_user_name is not None:
            result['CkUserName'] = self.ck_user_name

        if self.clickhouse_port is not None:
            result['ClickhousePort'] = self.clickhouse_port

        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id

        if self.limit_upper is not None:
            result['LimitUpper'] = self.limit_upper

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.rds_id is not None:
            result['RdsId'] = self.rds_id

        if self.rds_password is not None:
            result['RdsPassword'] = self.rds_password

        if self.rds_port is not None:
            result['RdsPort'] = self.rds_port

        if self.rds_syn_db is not None:
            result['RdsSynDb'] = self.rds_syn_db

        if self.rds_syn_tables is not None:
            result['RdsSynTables'] = self.rds_syn_tables

        if self.rds_user_name is not None:
            result['RdsUserName'] = self.rds_user_name

        if self.rds_vpc_id is not None:
            result['RdsVpcId'] = self.rds_vpc_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.skip_unsupported is not None:
            result['SkipUnsupported'] = self.skip_unsupported

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CkPassword') is not None:
            self.ck_password = m.get('CkPassword')

        if m.get('CkUserName') is not None:
            self.ck_user_name = m.get('CkUserName')

        if m.get('ClickhousePort') is not None:
            self.clickhouse_port = m.get('ClickhousePort')

        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('LimitUpper') is not None:
            self.limit_upper = m.get('LimitUpper')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')

        if m.get('RdsPassword') is not None:
            self.rds_password = m.get('RdsPassword')

        if m.get('RdsPort') is not None:
            self.rds_port = m.get('RdsPort')

        if m.get('RdsSynDb') is not None:
            self.rds_syn_db = m.get('RdsSynDb')

        if m.get('RdsSynTables') is not None:
            self.rds_syn_tables = m.get('RdsSynTables')

        if m.get('RdsUserName') is not None:
            self.rds_user_name = m.get('RdsUserName')

        if m.get('RdsVpcId') is not None:
            self.rds_vpc_id = m.get('RdsVpcId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SkipUnsupported') is not None:
            self.skip_unsupported = m.get('SkipUnsupported')

        return self

