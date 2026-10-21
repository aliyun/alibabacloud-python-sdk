# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TestAgenticDataSourceConnectionRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        auth_account: str = None,
        auth_password: str = None,
        auth_type: int = None,
        catalog_name: str = None,
        data_source_uuid: str = None,
        db_type: str = None,
        env_type: str = None,
        host: str = None,
        instance_resource_id: str = None,
        instance_source: str = None,
        kms_secret: str = None,
        port: int = None,
        role_arn: str = None,
        schema: str = None,
        snowflake_role: str = None,
        snowflake_warehouse: str = None,
        sync_alias: int = None,
        use_ssl: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The alias. You can leave this parameter empty when testing a connection. This parameter does not create or modify a data source.
        self.alias = alias
        # The logon username. You can leave this parameter empty for authentication methods that do not require a username.
        self.auth_account = auth_account
        # The logon password. When testing an existing data source, you can leave this parameter empty to reuse the saved password. If a new value is passed, the new value takes precedence.
        self.auth_password = auth_password
        # The authentication type. This parameter is optional. Valid values: -1 (no authentication required), 0 (username and password), 1 (password only), and 2 (password-free).
        self.auth_type = auth_type
        # The catalog name. You can leave this parameter empty when testing a connection. This parameter does not create a metadata catalog.
        self.catalog_name = catalog_name
        # The UUID of the data source. This parameter is required when testing an existing data source. If no new password is passed, the saved password is reused. Leave this parameter empty when testing a new data source.
        self.data_source_uuid = data_source_uuid
        # The type of the data source. Use uppercase letters. Do not pass numbers. Valid values: MYSQL, POSTGRESQL, ORACLE, SQLSERVER, MARIADB, POLARDB, POLARDB_POSTGRESQL, POLARDB_ORACLE, OCEANBASEX, DRDS, ADB_MYSQL, ADB_POSTGRESQL, CLICKHOUSE, SELECTDB, STARROCKS, HOLOGRES, MAXCOMPUTE, ES_REST, and TRINO.
        # 
        # This parameter is required.
        self.db_type = db_type
        # The environment type. This parameter is optional when testing a connection. Valid values: product, pre, dev, test, sit, uat, pet, and stag.
        self.env_type = env_type
        # The domain name or IP address of the database. Do not include the protocol, path, or port. This parameter is optional. You can leave this parameter empty when you select an existing cloud instance and the endpoint is automatically populated.
        self.host = host
        # The ID of the cloud resource instance. This parameter is required when you select an existing cloud instance. You can leave this parameter empty when you enter a connection endpoint.
        self.instance_resource_id = instance_resource_id
        # The source of the data source. Valid values:
        # - RDS: ApsaraDB instance.
        # - PUBLIC_OWN: self-managed database connected over the Internet.
        # - ECS_OWN: self-managed database hosted on an ECS instance.
        # - GATEWAY: database connected through Database Gateway.
        # - VPC_IDC: database connected over a VPC or data center.
        # 
        # This parameter is required.
        self.instance_source = instance_source
        # The name of the KMS secret. This parameter is required when you use KMS to manage database credentials. Leave this parameter empty in other scenarios.
        self.kms_secret = kms_secret
        # The service port of the database. This parameter is optional. You can leave this parameter empty when you select an existing cloud instance and the port is automatically populated.
        self.port = port
        # The complete ARN of the RAM role. This parameter is required when you use an Alibaba Cloud RAM role to access the data source. Leave this parameter empty in other scenarios.
        self.role_arn = role_arn
        # The schema name. This parameter is optional. For ADB_POSTGRESQL, DRDS, POSTGRESQL, and POLARDB_POSTGRESQL, enter the database name. For ORACLE, enter the SID or service name, and prefix the service name with a forward slash (/). For POLARDB_ORACLE, enter the SID. For MAXCOMPUTE, enter the project name. Leave this parameter empty for other types.
        self.schema = schema
        # The name of the Snowflake role. This parameter takes effect only when DbType is set to SNOWFLAKE.
        self.snowflake_role = snowflake_role
        # The name of the Snowflake compute warehouse. This parameter takes effect only when DbType is set to SNOWFLAKE.
        self.snowflake_warehouse = snowflake_warehouse
        # Specifies whether to synchronize the alias. This parameter is optional when testing a connection. This parameter does not modify the data source name.
        self.sync_alias = sync_alias
        # Specifies whether to enable SSL. Valid values:
        # - 1: Enable.
        # - 0: Disable.
        # - -1: Use the default setting.
        # SSL is supported only for ADB_MYSQL, CLICKHOUSE, MARIADB, MYSQL, OCEANBASEX, POLARDB, SELECTDB, and STARROCKS. Leave this parameter empty for other types.
        self.use_ssl = use_ssl
        # The ID of the vSwitch. This parameter is required when you access MaxCompute over a VPC. Leave this parameter empty in other scenarios.
        self.v_switch_id = v_switch_id
        # The ID of the VPC. This parameter is required when you access MaxCompute over a VPC. Leave this parameter empty in other scenarios.
        self.vpc_id = vpc_id
        # The zone ID. This parameter is required when you access MaxCompute over a VPC. Leave this parameter empty in other scenarios.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.auth_account is not None:
            result['AuthAccount'] = self.auth_account

        if self.auth_password is not None:
            result['AuthPassword'] = self.auth_password

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.data_source_uuid is not None:
            result['DataSourceUuid'] = self.data_source_uuid

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_resource_id is not None:
            result['InstanceResourceId'] = self.instance_resource_id

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.kms_secret is not None:
            result['KmsSecret'] = self.kms_secret

        if self.port is not None:
            result['Port'] = self.port

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.snowflake_role is not None:
            result['SnowflakeRole'] = self.snowflake_role

        if self.snowflake_warehouse is not None:
            result['SnowflakeWarehouse'] = self.snowflake_warehouse

        if self.sync_alias is not None:
            result['SyncAlias'] = self.sync_alias

        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('AuthAccount') is not None:
            self.auth_account = m.get('AuthAccount')

        if m.get('AuthPassword') is not None:
            self.auth_password = m.get('AuthPassword')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DataSourceUuid') is not None:
            self.data_source_uuid = m.get('DataSourceUuid')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceResourceId') is not None:
            self.instance_resource_id = m.get('InstanceResourceId')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('KmsSecret') is not None:
            self.kms_secret = m.get('KmsSecret')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('SnowflakeRole') is not None:
            self.snowflake_role = m.get('SnowflakeRole')

        if m.get('SnowflakeWarehouse') is not None:
            self.snowflake_warehouse = m.get('SnowflakeWarehouse')

        if m.get('SyncAlias') is not None:
            self.sync_alias = m.get('SyncAlias')

        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

