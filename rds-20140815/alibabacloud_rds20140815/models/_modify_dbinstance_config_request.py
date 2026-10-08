# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        config_name: str = None,
        config_value: str = None,
        dbinstance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        switch_time_mode: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The name of the configuration item to modify. This parameter is used together with ConfigValue.
        # <details>
        # <summary>ApsaraDB RDS for PostgreSQL configuration items</summary>
        # 
        # - **pgbouncer**: Modifies the PgBouncer feature.
        # - **encryptionKey**: Modifies the cloud disk encryption feature.
        # - **duckdb_create_databases**: Configures databases of the primary instance as DuckDB column store databases in batches.
        # - **duckdb_prepare_dependency**: Configures the primary instance with one click so that its parameters and minor engine version meet the [prerequisites](https://help.aliyun.com/document_detail/2977241.html) for creating a DuckDB-based analytical instance. If the primary instance already has read-only instances, the read-only instances are also updated.
        # - **enable_db_visible_by_connect_rls**: Enables CONNECT RLS on the instance to control database visibility.
        # - **set_db_visible_by_connect_rls**: Enables CONNECT RLS on a database to control database visibility. This can be called only after CONNECT RLS is enabled on the instance.
        # 
        # </details>
        # 
        # <details>
        # <summary>ApsaraDB RDS for SQL Server configuration items</summary>
        # 
        # <props="intl">
        # 
        # - **clear_errorlog**: Clears error logs.
        # - **encryptionKey**: Modifies the cloud disk encryption feature. Serverless instances and shared instance types do not support this feature.
        # 
        # 
        # 
        # <props="china">
        # 
        # 
        # - **backup_recovery_model**: Enables the simple recovery model feature. Only Basic Edition instances support this feature. **This feature cannot be disabled after it is enabled**.
        # - **clear_errorlog**: Clears error logs.
        # - **encryptionKey**: Modifies the cloud disk encryption feature. Serverless instances and shared instance types do not support this feature.
        # 
        # 
        # </details>
        # 
        # This parameter is required.
        self.config_name = config_name
        # The value of the configuration item to modify. This parameter is used together with ConfigName.
        # 
        # <details>
        # <summary>ApsaraDB RDS for PostgreSQL configuration item values</summary>
        # 
        # - PgBouncer feature: **true** (enable) or **false** (disable).
        # - Cloud disk encryption feature:
        #   - **ServiceKey**: Uses an automatically generated key from Alibaba Cloud, which is the RDS-managed service key (Default Service CMK), to enable cloud disk encryption.
        #   - **<Key>**: Uses a custom key to enable cloud disk encryption or replaces the current key. Example: `494c98ce-f2b5-48ab-96ab-36c986b6****`.
        #   - **disabled**: Disables cloud disk encryption.
        # - One-click fix for prerequisites to create a DuckDB-based analytical instance: **duckdb_prepare_dependency**
        # - Configure databases of the primary instance as DuckDB column store databases in batches. The value is a JSON string. Example: `{"dbNames": "db1,db2,db3", "accountName": "yourSuperAccountName"}`, where:
        #   - **dbNames**: The names of databases to convert to DuckDB column store databases. Separate multiple database names with commas (,).
        #   - **accountName**: The privileged user. Specify only one privileged user.
        # - Enable CONNECT RLS on the instance to control database visibility: **true** to enable.
        # - Enable CONNECT RLS on a database to control database visibility: The **database names** managed by CONNECT RLS. Separate multiple database names with commas (,). Example: **testdb1,testdb2**. When a client connects to a database with CONNECT RLS enabled, the database list is displayed based on whether the client has CONNECT permissions on other databases.
        # </details>
        # <details>
        # <summary>ApsaraDB RDS for SQL Server configuration item values</summary>
        # 
        # <props="intl">
        # 
        # - Error log cleanup feature: **1** (confirm cleanup).
        # - Cloud disk encryption feature (**this feature cannot be disabled after it is enabled**):
        #   - **serviceKey**: Uses an automatically generated key from Alibaba Cloud, which is the RDS-managed service key (Default Service CMK), to enable cloud disk encryption.
        #   - **<Key>**: Uses a custom key to enable cloud disk encryption or replaces the current key. Example: `494c98ce-f2b5-48ab-96ab-36c986b6****`.
        # 
        # 
        # 
        # 
        # <props="china">
        # 
        # - Simple recovery feature: **simple** (enable simple recovery).
        # - Error log cleanup feature: **1** (confirm cleanup).
        # - Cloud disk encryption feature (**this feature cannot be disabled after it is enabled**):
        #   - **serviceKey**: Uses an automatically generated key from Alibaba Cloud, which is the RDS-managed service key (Default Service CMK), to enable cloud disk encryption.
        #   - **<Key>**: Uses a custom key to enable cloud disk encryption or replaces the current key. Example: `494c98ce-f2b5-48ab-96ab-36c986b6****`.
        # 
        # 
        # 
        # </details>
        # 
        # This parameter is required.
        self.config_value = config_value
        # The instance ID. You can call DescribeDBInstances to obtain the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The resource group ID. You can call DescribeDBInstanceAttribute to obtain the resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The time at which the modification takes effect. We recommend that you perform specification changes during off-peak hours. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.switch_time = switch_time
        # The switchover time. Valid values:
        # - **Immediate**: The modification takes effect immediately.
        # - **MaintainTime**: The modification takes effect during the maintenance window. You can call ModifyDBInstanceMaintainTime to modify the maintenance window.
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        return self

