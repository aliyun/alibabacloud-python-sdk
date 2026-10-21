# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetAgenticDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAgenticDataSourceResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data source details. This parameter is empty if the data source does not exist.
        self.data = data
        # The error code returned when the call fails. This parameter is empty if the call is successful.
        self.error_code = error_code
        # The error message returned when the call fails. This parameter is empty if the call is successful.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetAgenticDataSourceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAgenticDataSourceResponseBodyData(DaraModel):
    def __init__(
        self,
        alias: str = None,
        auth_account: str = None,
        auth_password: str = None,
        auth_type: int = None,
        catalog_name: str = None,
        catalog_uuid: str = None,
        create_mode: str = None,
        data_source_uuid: str = None,
        db_type: str = None,
        env_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        host: str = None,
        instance_resource_id: str = None,
        instance_source: str = None,
        kms_secret: str = None,
        policy_id: str = None,
        port: int = None,
        region_id: str = None,
        resource_account_id: str = None,
        role_arn: str = None,
        schema: str = None,
        snowflake_role: str = None,
        snowflake_warehouse: str = None,
        state: int = None,
        sync_alias: int = None,
        use_ssl: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The display name of the data source.
        self.alias = alias
        # The logon username for the data source. This parameter is empty if username authentication is not used.
        self.auth_account = auth_account
        # The masked value of the password or token. The actual value is not returned.
        self.auth_password = auth_password
        # The authentication method. Valid values:
        # - -1: no authentication required
        # - 0: username and password
        # - 1: password only
        # - 2: password-free
        self.auth_type = auth_type
        # The name of the metadata catalog associated with the data source.
        self.catalog_name = catalog_name
        # The UUID of the metadata catalog associated with the data source.
        self.catalog_uuid = catalog_uuid
        # The method used to register the data source. Valid values:
        # - INSTANCE_ID: select an existing cloud instance
        # - HOST_PORT: register by endpoint and port
        self.create_mode = create_mode
        # The unique identifier of the data source.
        self.data_source_uuid = data_source_uuid
        # The type of the data source. Valid values: MYSQL, POSTGRESQL, ORACLE, SQLSERVER, MARIADB, POLARDB, POLARDB_POSTGRESQL, POLARDB_ORACLE, OCEANBASEX, DRDS, ADB_MYSQL, ADB_POSTGRESQL, CLICKHOUSE, SELECTDB, STARROCKS, HOLOGRES, MAXCOMPUTE, ES_REST, and TRINO.
        self.db_type = db_type
        # The environment type. Valid values: product, pre, dev, test, sit, uat, pet, and stag.
        self.env_type = env_type
        # The time when the data source was created. The format is yyyy-MM-dd HH:mm:ss.
        self.gmt_create = gmt_create
        # The time when the data source was last modified. The format is yyyy-MM-dd HH:mm:ss.
        self.gmt_modified = gmt_modified
        # The endpoint of the data source. A masked value may be returned in sensitive scenarios.
        self.host = host
        # The ID of the cloud resource instance. This parameter may be empty for data sources registered by endpoint.
        self.instance_resource_id = instance_resource_id
        # The source of the data source. Valid values:
        # - RDS: ApsaraDB instance
        # - PUBLIC_OWN: self-managed database on the Internet
        # - ECS_OWN: self-managed database on an ECS instance
        # - GATEWAY: connected through Database Gateway
        # - VPC_IDC: connected through a VPC or IDC
        self.instance_source = instance_source
        # The name of the KMS-managed credential. This parameter is empty if KMS is not used. This field contains sensitive information.
        self.kms_secret = kms_secret
        # The ID of the data access security policy currently in use. This parameter is empty if no policy is configured.
        self.policy_id = policy_id
        # The connection port of the data source.
        self.port = port
        # The region where the data source is located.
        self.region_id = region_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_account_id = resource_account_id
        # The ARN of the RAM role used to access the data source. This parameter is empty if role-based authorization is not used.
        self.role_arn = role_arn
        # The name of the connection target. For ADB_POSTGRESQL, DRDS, POSTGRESQL, and POLARDB_POSTGRESQL, this indicates the database name. For ORACLE, this indicates the SID or service name. For POLARDB_ORACLE, this indicates the SID. For MAXCOMPUTE, this indicates the project. For other types, this parameter is usually empty.
        self.schema = schema
        # The name of the Snowflake role. This parameter takes effect only when DbType is set to SNOWFLAKE.
        self.snowflake_role = snowflake_role
        # The name of the Snowflake compute warehouse. This parameter takes effect only when DbType is set to SNOWFLAKE.
        self.snowflake_warehouse = snowflake_warehouse
        # The status of the data source. Valid values:
        # - 0: normal
        # - -1: deleted
        # - -2: disabled
        self.state = state
        # Specifies whether to use the cloud instance name as the data source name. Valid values:
        # - 1: yes
        # - 0: no
        self.sync_alias = sync_alias
        # The SSL settings. Valid values:
        # - 1: enabled
        # - 0: disabled
        # - -1: use default settings
        self.use_ssl = use_ssl
        # The ID of the destination vSwitch used when accessing MaxCompute. This parameter is empty in other scenarios.
        self.v_switch_id = v_switch_id
        # The ID of the destination VPC used when accessing MaxCompute. This parameter is empty in other scenarios.
        self.vpc_id = vpc_id
        # The ID of the destination zone used when accessing MaxCompute. This parameter is empty in other scenarios.
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

        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode

        if self.data_source_uuid is not None:
            result['DataSourceUuid'] = self.data_source_uuid

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.snowflake_role is not None:
            result['SnowflakeRole'] = self.snowflake_role

        if self.snowflake_warehouse is not None:
            result['SnowflakeWarehouse'] = self.snowflake_warehouse

        if self.state is not None:
            result['State'] = self.state

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

        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')

        if m.get('DataSourceUuid') is not None:
            self.data_source_uuid = m.get('DataSourceUuid')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('SnowflakeRole') is not None:
            self.snowflake_role = m.get('SnowflakeRole')

        if m.get('SnowflakeWarehouse') is not None:
            self.snowflake_warehouse = m.get('SnowflakeWarehouse')

        if m.get('State') is not None:
            self.state = m.get('State')

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

