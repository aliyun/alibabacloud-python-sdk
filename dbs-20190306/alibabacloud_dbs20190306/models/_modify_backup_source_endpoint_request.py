# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupSourceEndpointRequest(DaraModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_objects: str = None,
        backup_plan_id: str = None,
        client_token: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        enable_source_endpoint_ssl: str = None,
        owner_id: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_home: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: int = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
        ssl_ca_pem: str = None,
    ):
        # The backup gateway ID. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # > You must specify this parameter when **SourceEndpointInstanceType** is Agent.
        self.backup_gateway_id = backup_gateway_id
        # The backup objects. This parameter is optional when SourceEndpointInstanceType is Agent. For all other cases, you must specify it. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        self.backup_objects = backup_objects
        # The backup plan ID. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # A unique string that ensures idempotence and prevents duplicate requests.
        self.client_token = client_token
        # The UID of the Alibaba Cloud account used for cross-account backup. Call [DescribeRestoreTaskList](https://help.aliyun.com/document_detail/2869838.html) to get this value.
        self.cross_aliyun_id = cross_aliyun_id
        # The RAM role name used for cross-account backup. Call [DescribeRestoreTaskList](https://help.aliyun.com/document_detail/2869838.html) to get this value.
        self.cross_role_name = cross_role_name
        self.enable_source_endpoint_ssl = enable_source_endpoint_ssl
        self.owner_id = owner_id
        # The database name.
        # 
        # - You must specify this parameter for PostgreSQL or MongoDB databases.
        # 
        # - You must specify this parameter for Microsoft SQL Server databases connected through a backup gateway.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The database endpoint. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # > You must specify this parameter when **SourceEndpointInstanceType** is Express, Agent, or Other.
        self.source_endpoint_ip = source_endpoint_ip
        # The database instance ID. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # > You must specify this parameter when **SourceEndpointInstanceType** is RDS, ECS, DDS, or Express.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The location of the database. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value. Valid values:
        # 
        # - **RDS**
        # 
        # - **ECS**
        # 
        # - **Express**: A database connected through a leased line, VPN Gateway, or Smart Access Gateway
        # 
        # - **Agent**: A database connected through a backup gateway
        # 
        # - **DDS**: A MongoDB instance on Alibaba Cloud
        # 
        # - **Other**: A database connected directly using an IP address and port
        # 
        # This parameter is required.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_oracle_home = source_endpoint_oracle_home
        # The Oracle system ID (SID). You must specify this parameter for Oracle databases.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The password.
        # 
        # This parameter is optional for Redis databases or for Microsoft SQL Server databases connected through a backup gateway. For all other cases, you must specify it.
        self.source_endpoint_password = source_endpoint_password
        # The database port. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # > You must specify this parameter when **SourceEndpointInstanceType** is Express, Agent, Other, or ECS.
        self.source_endpoint_port = source_endpoint_port
        # The region where the database is located. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # > You must specify this parameter when **SourceEndpointInstanceType** is RDS, ECS, DDS, Express, or Agent.
        self.source_endpoint_region = source_endpoint_region
        # The database account. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # This parameter is optional for Redis databases or for Microsoft SQL Server databases connected through a backup gateway. For all other cases, you must specify it.
        self.source_endpoint_user_name = source_endpoint_user_name
        self.ssl_ca_pem = ssl_ca_pem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id

        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id

        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name

        if self.enable_source_endpoint_ssl is not None:
            result['EnableSourceEndpointSsl'] = self.enable_source_endpoint_ssl

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name

        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id

        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type

        if self.source_endpoint_oracle_home is not None:
            result['SourceEndpointOracleHome'] = self.source_endpoint_oracle_home

        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid

        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password

        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name

        if self.ssl_ca_pem is not None:
            result['SslCaPem'] = self.ssl_ca_pem

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')

        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')

        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')

        if m.get('EnableSourceEndpointSsl') is not None:
            self.enable_source_endpoint_ssl = m.get('EnableSourceEndpointSsl')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')

        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')

        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')

        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')

        if m.get('SourceEndpointOracleHome') is not None:
            self.source_endpoint_oracle_home = m.get('SourceEndpointOracleHome')

        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')

        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')

        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')

        if m.get('SslCaPem') is not None:
            self.ssl_ca_pem = m.get('SslCaPem')

        return self

