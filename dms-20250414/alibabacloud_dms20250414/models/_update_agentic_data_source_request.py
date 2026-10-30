# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgenticDataSourceRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        auth_account: str = None,
        auth_password: str = None,
        auth_type: int = None,
        catalog_name: str = None,
        create_mode: str = None,
        data_source_uuid: str = None,
        db_type: str = None,
        env_type: str = None,
        host: str = None,
        instance_resource_id: str = None,
        kms_secret: str = None,
        policy_id: str = None,
        port: int = None,
        role_arn: str = None,
        schema: str = None,
        snowflake_role: str = None,
        snowflake_warehouse: str = None,
        sync_alias: int = None,
        use_ssl: int = None,
    ):
        # The new display name of the data source. If you do not specify this parameter, the alias is not updated.
        self.alias = alias
        # The new logon username. If you do not specify this parameter, the authentication account is not updated.
        self.auth_account = auth_account
        # The new logon password. If you do not specify this parameter, the authentication password is not updated. This is sensitive information. Do not record or disclose it.
        self.auth_password = auth_password
        # Optional. Valid values:
        # - -1: No authentication required.
        # - 0: Username and password.
        # - 1: Password only.
        # - 2: Password-free.
        # If you do not specify this parameter, the authentication type is not updated.
        self.auth_type = auth_type
        # The new name of the metadata catalog. If you do not specify this parameter, the catalog name is not updated. The name can be up to 128 characters in length. It must start with a Chinese character, a letter, or an underscore, and can contain digits and hyphens. It cannot contain only digits.
        self.catalog_name = catalog_name
        # The registration method. Valid values:
        # - INSTANCE_ID: Select an existing cloud instance.
        # - HOST_PORT: Register by endpoint and port.
        # If you do not specify this parameter, the creation mode is not updated.
        self.create_mode = create_mode
        # The UUID of the data source to be updated.
        # 
        # This parameter is required.
        self.data_source_uuid = data_source_uuid
        # Modifying the data source type is not supported. Do not specify this parameter.
        self.db_type = db_type
        # The environment type. Valid values: product, pre, dev, test, sit, uat, pet, and stag. If you do not specify this parameter, the environment type is not updated.
        self.env_type = env_type
        # Optional. The new domain name or IP address of the database. Do not include the protocol, path, or port. If you do not specify this parameter, the host is not updated.
        self.host = host
        # The new ID of the cloud resource instance. If you do not specify this parameter, the instance resource ID is not updated.
        self.instance_resource_id = instance_resource_id
        # The new name of the KMS-managed credential. If you do not specify this parameter, the KMS secret is not updated.
        self.kms_secret = kms_secret
        # Optional. The new ID of the data access security policy. If you do not specify this parameter, the policy ID is not updated.
        self.policy_id = policy_id
        # Optional. The new service port of the database. If you do not specify this parameter, the service port is not updated.
        self.port = port
        # The new ARN of the Alibaba Cloud RAM role. If you do not specify this parameter, the role ARN is not updated.
        self.role_arn = role_arn
        # Optional. For ADB_POSTGRESQL, DRDS, POSTGRESQL, and POLARDB_POSTGRESQL, specify the database name. For ORACLE, specify the SID or service name, and prefix the service name with a forward slash (/). For POLARDB_ORACLE, specify the SID. For MAXCOMPUTE, specify the project name. For other types, leave this parameter empty. If you do not specify this parameter, the schema is not updated.
        self.schema = schema
        # The name of the Snowflake role. This parameter takes effect only when DbType is set to SNOWFLAKE.
        self.snowflake_role = snowflake_role
        # The name of the Snowflake compute warehouse. This parameter takes effect only when DbType is set to SNOWFLAKE.
        self.snowflake_warehouse = snowflake_warehouse
        # Specifies whether to use the cloud instance name as the data source name. Valid values:
        # - 1: Yes.
        # - 0: No.
        # If you do not specify this parameter, the sync alias setting is not updated.
        self.sync_alias = sync_alias
        # The new SSL setting. Valid values:
        # - 1: Enable.
        # - 0: Disable.
        # - -1: Use default settings.
        # If you do not specify this parameter, the SSL setting is not updated. SSL is supported only for ADB_MYSQL, CLICKHOUSE, MARIADB, MYSQL, OCEANBASEX, POLARDB, SELECTDB, and STARROCKS.
        self.use_ssl = use_ssl

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

        return self

