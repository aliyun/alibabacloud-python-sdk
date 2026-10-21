# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAgenticDataSourceRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        auth_account: str = None,
        auth_password: str = None,
        auth_type: int = None,
        catalog_name: str = None,
        create_mode: str = None,
        db_type: str = None,
        env_type: str = None,
        host: str = None,
        instance_resource_id: str = None,
        instance_source: str = None,
        kms_secret: str = None,
        policy_id: str = None,
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
        # The display name of the data source. If you do not specify this parameter, the server generates a name.
        self.alias = alias
        # The logon username. You can leave this parameter empty for authentication methods that do not require a username.
        self.auth_account = auth_account
        # The logon password. This is sensitive information. Do not record or disclose it.
        self.auth_password = auth_password
        # Optional. The authentication type. Valid values:
        # - -1: No authentication required.
        # - 0: Username and password.
        # - 1: Password only.
        # - 2: Password-free.
        self.auth_type = auth_type
        # The name of the metadata catalog. If you do not specify this parameter, the name is automatically generated. The name can be up to 128 characters in length. It must start with a Chinese character, a letter, or an underscore, and can contain digits and hyphens. It cannot contain only digits.
        self.catalog_name = catalog_name
        # The entry method. Valid values:
        # - INSTANCE_ID: Select an existing cloud instance.
        # - HOST_PORT: Enter the endpoint and port.
        # If you do not specify this parameter, HOST_PORT is used.
        self.create_mode = create_mode
        # The type of the data source. Use uppercase letters. Do not pass numbers. Valid values: MYSQL, POSTGRESQL, ORACLE, SQLSERVER, MARIADB, POLARDB, POLARDB_POSTGRESQL, POLARDB_ORACLE, OCEANBASEX, DRDS, ADB_MYSQL, ADB_POSTGRESQL, CLICKHOUSE, SELECTDB, STARROCKS, HOLOGRES, MAXCOMPUTE, ES_REST, and TRINO.
        # 
        # This parameter is required.
        self.db_type = db_type
        # The environment type. Valid values: product, pre, dev, test, sit, uat, pet, and stag.
        self.env_type = env_type
        # Optional. The domain name or IP address of the database. Do not include the protocol, path, or port. You can leave this parameter empty if you select an existing cloud instance and the address is automatically populated.
        self.host = host
        # The ID of the cloud resource instance. This parameter is required when you select an existing cloud instance. You can leave this parameter empty when you enter an endpoint.
        self.instance_resource_id = instance_resource_id
        # The source of the data source. Valid values:
        # - RDS: An ApsaraDB instance.
        # - PUBLIC_OWN: A self-managed database on the Internet.
        # - ECS_OWN: A self-managed database on an ECS instance.
        # - GATEWAY: A database accessed through Database Gateway.
        # - VPC_IDC: A database accessed through a VPC or data center.
        # 
        # This parameter is required.
        self.instance_source = instance_source
        # The name of the credential. Specify this parameter when you use Key Management Service (KMS) to manage database credentials. Leave this parameter empty in other scenarios.
        self.kms_secret = kms_secret
        # Optional. The ID of the data access security policy. This policy is used to control the access and protection rules for the data source.
        self.policy_id = policy_id
        # Optional. The service port of the database. You can leave this parameter empty if you select an existing cloud instance and the port is automatically populated.
        self.port = port
        # The complete ARN of the Resource Access Management (RAM) role. Specify this parameter when you use a RAM role to access the data source. Leave this parameter empty in other scenarios.
        self.role_arn = role_arn
        # Optional. For ADB_POSTGRESQL, DRDS, POSTGRESQL, and POLARDB_POSTGRESQL, enter the database name. For ORACLE, enter the SID or service name, and prefix the service name with a forward slash (/). For POLARDB_ORACLE, enter the SID. For MAXCOMPUTE, enter the project name. Leave this parameter empty for other types.
        self.schema = schema
        # The name of the Snowflake role. This parameter takes effect only when DbType is set to SNOWFLAKE.
        self.snowflake_role = snowflake_role
        # The name of the Snowflake compute warehouse. This parameter takes effect only when DbType is set to SNOWFLAKE.
        self.snowflake_warehouse = snowflake_warehouse
        # Specifies whether to use the cloud instance name as the data source name. Valid values:
        # - 1: Yes.
        # - 0: No.
        # This parameter takes effect only when you select a cloud database instance.
        self.sync_alias = sync_alias
        # Specifies whether to use SSL. Valid values:
        # - 1: Enable.
        # - 0: Disable.
        # - -1: Use the default setting.
        # Only ADB_MYSQL, CLICKHOUSE, MARIADB, MYSQL, OCEANBASEX, POLARDB, SELECTDB, and STARROCKS support SSL. Leave this parameter empty for other types.
        self.use_ssl = use_ssl
        # The ID of the destination vSwitch. Specify this parameter when you access MaxCompute through a VPC. Leave this parameter empty in other scenarios.
        self.v_switch_id = v_switch_id
        # The ID of the destination VPC. Specify this parameter when you access MaxCompute through a VPC. Leave this parameter empty in other scenarios.
        self.vpc_id = vpc_id
        # The ID of the destination zone. Specify this parameter when you access MaxCompute through a VPC. Leave this parameter empty in other scenarios.
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

        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode

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

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

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

        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')

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

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

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

