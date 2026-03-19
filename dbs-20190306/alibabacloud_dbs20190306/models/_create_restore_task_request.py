# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRestoreTaskRequest(DaraModel):
    def __init__(
        self,
        auto_open_database: str = None,
        auto_shutdown_database: str = None,
        backup_gateway_id: int = None,
        backup_plan_id: str = None,
        backup_set_id: str = None,
        client_token: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        dest_database_instance_class: str = None,
        dest_database_instance_database_version: str = None,
        dest_database_instance_region: str = None,
        dest_database_instance_storage_size: str = None,
        dest_database_instance_type: str = None,
        dest_database_instance_vswitch: str = None,
        dest_database_instance_vpc: str = None,
        destination_endpoint_database_name: str = None,
        destination_endpoint_ip: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_password: str = None,
        destination_endpoint_port: int = None,
        destination_endpoint_region: str = None,
        destination_endpoint_user_name: str = None,
        duplicate_conflict: str = None,
        enable_destination_endpoint_ssl: bool = None,
        owner_id: str = None,
        restore_destination_mode: str = None,
        restore_dir: str = None,
        restore_home: str = None,
        restore_objects: str = None,
        restore_task_name: str = None,
        restore_time: int = None,
        ssl_ca_pem: str = None,
    ):
        self.auto_open_database = auto_open_database
        self.auto_shutdown_database = auto_shutdown_database
        # backup gateway ID.
        # 
        # > This parameter is required when **DestinationEndpointInstanceType** is agent.
        self.backup_gateway_id = backup_gateway_id
        # backup plan ID.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The ID of the full backup set used for restoration. Mutually exclusive with RestoreTime.
        self.backup_set_id = backup_set_id
        # Ensures request idempotence and prevents duplicate submissions.
        self.client_token = client_token
        # UID for cross-Alibaba Cloud account backup.
        self.cross_aliyun_id = cross_aliyun_id
        # RAM role name for cross-Alibaba Cloud account backup.
        self.cross_role_name = cross_role_name
        self.dest_database_instance_class = dest_database_instance_class
        self.dest_database_instance_database_version = dest_database_instance_database_version
        self.dest_database_instance_region = dest_database_instance_region
        self.dest_database_instance_storage_size = dest_database_instance_storage_size
        self.dest_database_instance_type = dest_database_instance_type
        self.dest_database_instance_vswitch = dest_database_instance_vswitch
        self.dest_database_instance_vpc = dest_database_instance_vpc
        # database name.
        # 
        # > This parameter is required when the database type is PostgreSQL or MongoDB.
        self.destination_endpoint_database_name = destination_endpoint_database_name
        # database endpoint.
        # 
        # > This parameter is required when **DestinationEndpointInstanceType** is express, agent, or other.
        self.destination_endpoint_ip = destination_endpoint_ip
        # database instance ID.
        # 
        # > This parameter is required when **DestinationEndpointInstanceType** is RDS, ECS, DDS, or Express.
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        # database location. Valid values:
        # 
        # - **RDS**
        # 
        # - **ECS**
        # 
        # - **Express**: databases accessed via leased line/VPN Gateway/Smart Gateway
        # 
        # - **Agent**: databases accessed via backup gateway
        # 
        # - **DDS**: Cloud MongoDB
        # 
        # - **Other**: databases directly connected via IP:Port
        # 
        # - **dg**: self-managed databases without public IP:Port (accessed via Database Gateway DG)
        # 
        # This parameter is required.
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        # Oracle SID name.
        # 
        # > This parameter is required when the database type is Oracle.
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        # password.
        # 
        # > This parameter is optional when the database type is Redis, or when the database location is agent and the database type is MSSQL. It is required in all other scenarios.
        self.destination_endpoint_password = destination_endpoint_password
        # database port.
        # 
        # > This parameter is required when **DestinationEndpointInstanceType** is express, agent, other, or ECS.
        self.destination_endpoint_port = destination_endpoint_port
        # region of the database instance.
        # 
        # > This parameter is required when **DestinationEndpointInstanceType** is RDS, ECS, DDS, Express, or Agent.
        self.destination_endpoint_region = destination_endpoint_region
        # database account.
        # 
        # > This parameter is optional when the database type is Redis, or when the database location is agent and the database type is MSSQL. It is required in all other scenarios.
        self.destination_endpoint_user_name = destination_endpoint_user_name
        # Conflict handling for objects with the same name. Currently supports:
        # 
        # **renamenew**: Rename objects if names conflict.
        self.duplicate_conflict = duplicate_conflict
        self.enable_destination_endpoint_ssl = enable_destination_endpoint_ssl
        self.owner_id = owner_id
        self.restore_destination_mode = restore_destination_mode
        # Required when **DestinationEndpointInstanceType** is agent and the backup plan is MySQL.
        self.restore_dir = restore_dir
        # database program directory.
        self.restore_home = restore_home
        # restore objects.
        # 
        # - For details, see the **RestoreObjects** parameter definition below. This parameter is optional when the database location is agent, and required in all other scenarios.
        # 
        # - Input template: `[{ "DBName": "database name to be restored", "NewDBName": "target database name to be restored" }]`
        # 
        # > This API only supports restoring objects at the database level. To configure table-level restoration, use the console. For details, see [Recover databases](https://help.aliyun.com/document_detail/85543.html).
        self.restore_objects = restore_objects
        # restore job name.
        # 
        # This parameter is required.
        self.restore_task_name = restore_task_name
        # restore time. Value: 1554560477000.
        self.restore_time = restore_time
        self.ssl_ca_pem = ssl_ca_pem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_open_database is not None:
            result['AutoOpenDatabase'] = self.auto_open_database

        if self.auto_shutdown_database is not None:
            result['AutoShutdownDatabase'] = self.auto_shutdown_database

        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id

        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name

        if self.dest_database_instance_class is not None:
            result['DestDatabaseInstanceClass'] = self.dest_database_instance_class

        if self.dest_database_instance_database_version is not None:
            result['DestDatabaseInstanceDatabaseVersion'] = self.dest_database_instance_database_version

        if self.dest_database_instance_region is not None:
            result['DestDatabaseInstanceRegion'] = self.dest_database_instance_region

        if self.dest_database_instance_storage_size is not None:
            result['DestDatabaseInstanceStorageSize'] = self.dest_database_instance_storage_size

        if self.dest_database_instance_type is not None:
            result['DestDatabaseInstanceType'] = self.dest_database_instance_type

        if self.dest_database_instance_vswitch is not None:
            result['DestDatabaseInstanceVSwitch'] = self.dest_database_instance_vswitch

        if self.dest_database_instance_vpc is not None:
            result['DestDatabaseInstanceVpc'] = self.dest_database_instance_vpc

        if self.destination_endpoint_database_name is not None:
            result['DestinationEndpointDatabaseName'] = self.destination_endpoint_database_name

        if self.destination_endpoint_ip is not None:
            result['DestinationEndpointIP'] = self.destination_endpoint_ip

        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id

        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type

        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid

        if self.destination_endpoint_password is not None:
            result['DestinationEndpointPassword'] = self.destination_endpoint_password

        if self.destination_endpoint_port is not None:
            result['DestinationEndpointPort'] = self.destination_endpoint_port

        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region

        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name

        if self.duplicate_conflict is not None:
            result['DuplicateConflict'] = self.duplicate_conflict

        if self.enable_destination_endpoint_ssl is not None:
            result['EnableDestinationEndpointSsl'] = self.enable_destination_endpoint_ssl

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.restore_destination_mode is not None:
            result['RestoreDestinationMode'] = self.restore_destination_mode

        if self.restore_dir is not None:
            result['RestoreDir'] = self.restore_dir

        if self.restore_home is not None:
            result['RestoreHome'] = self.restore_home

        if self.restore_objects is not None:
            result['RestoreObjects'] = self.restore_objects

        if self.restore_task_name is not None:
            result['RestoreTaskName'] = self.restore_task_name

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.ssl_ca_pem is not None:
            result['SslCaPem'] = self.ssl_ca_pem

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoOpenDatabase') is not None:
            self.auto_open_database = m.get('AutoOpenDatabase')

        if m.get('AutoShutdownDatabase') is not None:
            self.auto_shutdown_database = m.get('AutoShutdownDatabase')

        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')

        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')

        if m.get('DestDatabaseInstanceClass') is not None:
            self.dest_database_instance_class = m.get('DestDatabaseInstanceClass')

        if m.get('DestDatabaseInstanceDatabaseVersion') is not None:
            self.dest_database_instance_database_version = m.get('DestDatabaseInstanceDatabaseVersion')

        if m.get('DestDatabaseInstanceRegion') is not None:
            self.dest_database_instance_region = m.get('DestDatabaseInstanceRegion')

        if m.get('DestDatabaseInstanceStorageSize') is not None:
            self.dest_database_instance_storage_size = m.get('DestDatabaseInstanceStorageSize')

        if m.get('DestDatabaseInstanceType') is not None:
            self.dest_database_instance_type = m.get('DestDatabaseInstanceType')

        if m.get('DestDatabaseInstanceVSwitch') is not None:
            self.dest_database_instance_vswitch = m.get('DestDatabaseInstanceVSwitch')

        if m.get('DestDatabaseInstanceVpc') is not None:
            self.dest_database_instance_vpc = m.get('DestDatabaseInstanceVpc')

        if m.get('DestinationEndpointDatabaseName') is not None:
            self.destination_endpoint_database_name = m.get('DestinationEndpointDatabaseName')

        if m.get('DestinationEndpointIP') is not None:
            self.destination_endpoint_ip = m.get('DestinationEndpointIP')

        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')

        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')

        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')

        if m.get('DestinationEndpointPassword') is not None:
            self.destination_endpoint_password = m.get('DestinationEndpointPassword')

        if m.get('DestinationEndpointPort') is not None:
            self.destination_endpoint_port = m.get('DestinationEndpointPort')

        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')

        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')

        if m.get('DuplicateConflict') is not None:
            self.duplicate_conflict = m.get('DuplicateConflict')

        if m.get('EnableDestinationEndpointSsl') is not None:
            self.enable_destination_endpoint_ssl = m.get('EnableDestinationEndpointSsl')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RestoreDestinationMode') is not None:
            self.restore_destination_mode = m.get('RestoreDestinationMode')

        if m.get('RestoreDir') is not None:
            self.restore_dir = m.get('RestoreDir')

        if m.get('RestoreHome') is not None:
            self.restore_home = m.get('RestoreHome')

        if m.get('RestoreObjects') is not None:
            self.restore_objects = m.get('RestoreObjects')

        if m.get('RestoreTaskName') is not None:
            self.restore_task_name = m.get('RestoreTaskName')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('SslCaPem') is not None:
            self.ssl_ca_pem = m.get('SslCaPem')

        return self

