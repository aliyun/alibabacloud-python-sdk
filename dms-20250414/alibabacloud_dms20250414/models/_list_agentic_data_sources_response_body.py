# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListAgenticDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAgenticDataSourcesResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The data sources on the current page.
        self.data = data
        # The error code returned when the call fails. This parameter is empty if the call is successful.
        self.error_code = error_code
        # The error message returned when the call fails. This parameter is empty if the call is successful.
        self.error_message = error_message
        # The actual number of entries returned per page in this query.
        self.max_results = max_results
        # The cursor for the next page. An empty value indicates that no more pages are available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success
        # The total number of data sources that meet the filter conditions. This parameter may be empty in some scenarios.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAgenticDataSourcesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAgenticDataSourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        alias: str = None,
        auth_account: str = None,
        auth_password: str = None,
        auth_type: int = None,
        catalog_name: str = None,
        catalog_uuid: str = None,
        data_source_uuid: str = None,
        db_type: str = None,
        env_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        host: str = None,
        instance_resource_id: str = None,
        instance_source: str = None,
        kms_secret: str = None,
        port: int = None,
        region_id: str = None,
        resource_account_id: str = None,
        role_arn: str = None,
        schema: str = None,
        state: int = None,
        sync_alias: int = None,
        use_ssl: int = None,
    ):
        # The display name of the data source.
        self.alias = alias
        # The logon username of the data source. This parameter is empty if username authentication is not used.
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
        # The unique identifier of the data source.
        self.data_source_uuid = data_source_uuid
        # The data source type. Valid values: MYSQL, POSTGRESQL, ORACLE, SQLSERVER, MARIADB, POLARDB, POLARDB_POSTGRESQL, POLARDB_ORACLE, OCEANBASEX, DRDS, ADB_MYSQL, ADB_POSTGRESQL, CLICKHOUSE, SELECTDB, STARROCKS, HOLOGRES, MAXCOMPUTE, ES_REST, and TRINO.
        self.db_type = db_type
        # The environment type. Valid values: product, pre, dev, test, sit, uat, pet, and stag.
        self.env_type = env_type
        # The time when the data source was created. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_create = gmt_create
        # The time when the data source was last modified. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_modified = gmt_modified
        # The endpoint of the data source. A masked value may be returned in sensitive scenarios.
        self.host = host
        # The ID of the cloud resource instance. This parameter may be empty for data sources registered by endpoint.
        self.instance_resource_id = instance_resource_id
        # The source of the data source. Valid values:
        # - RDS: ApsaraDB instance
        # - PUBLIC_OWN: self-managed database on the public network
        # - ECS_OWN: self-managed database on an ECS instance
        # - GATEWAY: connected through Database Gateway
        # - VPC_IDC: connected over a VPC or IDC
        self.instance_source = instance_source
        # The name of the KMS managed credential. This parameter is empty if KMS is not used. This is sensitive information.
        self.kms_secret = kms_secret
        # The connection port of the data source.
        self.port = port
        # The region where the data source resides.
        self.region_id = region_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_account_id = resource_account_id
        # The ARN of the RAM role used to access the data source. This parameter is empty if role authorization is not used.
        self.role_arn = role_arn
        # The connection target name. For ADB_POSTGRESQL, DRDS, POSTGRESQL, and POLARDB_POSTGRESQL, this parameter indicates the database name. For ORACLE, this parameter indicates the SID or service name. For POLARDB_ORACLE, this parameter indicates the SID. For MAXCOMPUTE, this parameter indicates the project. For other types, this parameter is usually empty.
        self.schema = schema
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
        # - -1: default settings
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

        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

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

        if self.state is not None:
            result['State'] = self.state

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

        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

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

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('SyncAlias') is not None:
            self.sync_alias = m.get('SyncAlias')

        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')

        return self

