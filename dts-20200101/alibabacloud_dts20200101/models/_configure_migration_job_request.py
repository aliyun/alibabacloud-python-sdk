# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class ConfigureMigrationJobRequest(DaraModel):
    def __init__(
        self,
        destination_endpoint: main_models.ConfigureMigrationJobRequestDestinationEndpoint = None,
        migration_mode: main_models.ConfigureMigrationJobRequestMigrationMode = None,
        source_endpoint: main_models.ConfigureMigrationJobRequestSourceEndpoint = None,
        account_id: str = None,
        checkpoint: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_object: str = None,
        migration_reserved: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
        self.source_endpoint = source_endpoint
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter. This parameter is pending deprecation.
        self.account_id = account_id
        # The start checkpoint for incremental data migration. The value is a UNIX timestamp in seconds.
        self.checkpoint = checkpoint
        # The ID of the data migration instance. You can call the **DescribeMigrationJobs** operation to query the instance ID.
        # 
        # This parameter is required.
        self.migration_job_id = migration_job_id
        # The name of the migration task. The name can be up to 32 characters in length. Specify a descriptive name for easy identification. The name does not need to be unique.
        # 
        # This parameter is required.
        self.migration_job_name = migration_job_name
        # The objects to be migrated. The value is a JSON string and supports specific regular expressions. For more information, see [Configure migration objects](~141901~).
        # 
        # This parameter is required.
        self.migration_object = migration_object
        # The reserved parameters of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements, such as specifying whether to automatically start a precheck. For more information, see [MigrationReserved parameter description](https://help.aliyun.com/document_detail/176470.html).
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id
        # The ID of the region where the data migration instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > The region ID must be the same as the region ID of the destination database.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id

        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name

        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object

        if self.migration_reserved is not None:
            result['MigrationReserved'] = self.migration_reserved

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.ConfigureMigrationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('MigrationMode') is not None:
            temp_model = main_models.ConfigureMigrationJobRequestMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.ConfigureMigrationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')

        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')

        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')

        if m.get('MigrationReserved') is not None:
            self.migration_reserved = m.get('MigrationReserved')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class ConfigureMigrationJobRequestSourceEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        owner_id: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        role: str = None,
        user_name: str = None,
    ):
        # The name of the database to be migrated or the authentication database.
        # > - This parameter is available and required only when **SourceEndpoint.EngineName** is set to **PostgreSQL** or **MongoDB**.
        # - When **SourceEndpoint.EngineName** is set to **PostgreSQL**, specify the name of the database to be migrated. When it is set to **MongoDB**, specify the name of the authentication database for the database account.
        self.database_name = database_name
        # The database engine of the source database. Valid values: **MySQL**, **TiDB**, **SQLServer**, **PostgreSQL**, **Oracle**, **MongoDB**, **Redis**, **POLARDB**, and **polardb_pg**.
        # > This parameter is available and required only when **DestinationEndpoint.InstanceType** is set to **RDS**, **POLARDB**, **ECS**, **LocalInstance**, or **Express**.
        self.engine_name = engine_name
        # The endpoint of the source database.
        # > This parameter is available and required only when **SourceEndpoint.InstanceType** is set to **LocalInstance** or **Express**.
        self.ip = ip
        # The ID of the source instance.
        # > - This parameter is available and required only when **SourceEndpoint.InstanceType** is set to **RDS**, **ECS**, **Express**, **MongoDB**, **POLARDB**, or **PolarDB_o**. You must specify the corresponding instance ID. For example, if the value is **ECS**, specify the ID of the ECS instance.
        # - When **SourceEndpoint.InstanceType** is set to **Express**, specify the VPC ID.
        self.instance_id = instance_id
        # The instance type of the source database. Valid values:
        # - **RDS**: ApsaraDB RDS instance.
        # - **ECS**: Self-managed database hosted on Elastic Compute Service (ECS).
        # - **LocalInstance**: Self-managed database with a public IP address.
        # - **Express**: Self-managed database connected over Express Connect, VPN Gateway, or Smart Access Gateway.
        # - **dg**: Self-managed database connected over Database Gateway.
        # - **cen**: Self-managed database connected over Cloud Enterprise Network (CEN).
        # - **MongoDB**: ApsaraDB for MongoDB instance.
        # - **POLARDB**: PolarDB for MySQL or PolarDB for PostgreSQL cluster.
        # - **PolarDB_o**: PolarDB for Oracle cluster.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The system ID (SID) of the Oracle database.
        # > This parameter is available and required only when **SourceEndpoint.EngineName** is set to **Oracle** and the Oracle database is a non-Real Application Cluster instance.
        self.oracle_sid = oracle_sid
        # The Alibaba Cloud account ID to which the source instance belongs.
        # > This parameter is active and required only when you configure a cross-account data migration task.
        self.owner_id = owner_id
        # The password of the source database account.
        self.password = password
        # The service port number of the source database.
        # > This parameter is available and required only when **SourceEndpoint.InstanceType** is set to **ECS**, **LocalInstance**, or **Express**.
        self.port = port
        # The ID of the region where the source database resides.
        # > When **SourceEndpoint.InstanceType** is set to **LocalInstance**, you can specify **cn-hangzhou** or the ID of the region that is closest to your self-managed database. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # The RAM role that is authorized to the destination Alibaba Cloud account to access the source instance. This parameter is required when the source and destination instances belong to different Alibaba Cloud accounts.
        # > For more information about the required permissions and authorization method, see [Configure RAM authorization for cross-account data migration or synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.role = role
        # The database account of the source database.
        # 
        # Note: The required permissions vary based on the database engine. For more information, see the corresponding configuration examples in the migration overview.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.engine_name is not None:
            result['EngineName'] = self.engine_name

        if self.ip is not None:
            result['IP'] = self.ip

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.role is not None:
            result['Role'] = self.role

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ConfigureMigrationJobRequestMigrationMode(DaraModel):
    def __init__(
        self,
        data_intialization: bool = None,
        data_synchronization: bool = None,
        structure_intialization: bool = None,
    ):
        # Specifies whether to perform full data migration. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        # 
        # > The support for full data migration varies based on the database engine. For more information, see [Supported databases and migration types](https://help.aliyun.com/document_detail/26618.html).
        # 
        # This parameter is required.
        self.data_intialization = data_intialization
        # Specifies whether to perform incremental data migration. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        # 
        # > The support for incremental data migration varies based on the database engine. For more information, see [Supported databases and migration types](https://help.aliyun.com/document_detail/26618.html).
        # 
        # This parameter is required.
        self.data_synchronization = data_synchronization
        # Specifies whether to perform schema migration. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        # 
        # > The support for schema migration varies based on the database engine. For more information, see [Supported databases and migration types](https://help.aliyun.com/document_detail/26618.html).
        # 
        # This parameter is required.
        self.structure_intialization = structure_intialization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_intialization is not None:
            result['DataIntialization'] = self.data_intialization

        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization

        if self.structure_intialization is not None:
            result['StructureIntialization'] = self.structure_intialization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIntialization') is not None:
            self.data_intialization = m.get('DataIntialization')

        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')

        if m.get('StructureIntialization') is not None:
            self.structure_intialization = m.get('StructureIntialization')

        return self



class ConfigureMigrationJobRequestDestinationEndpoint(DaraModel):
    def __init__(
        self,
        data_base_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        user_name: str = None,
    ):
        # The name of the destination database or the authentication database. 
        # > - This parameter is available and required only when **DestinationEndpoint.EngineName** is set to **PostgreSQL**, **DRDS**, or **MongoDB**.
        # - When **DestinationEndpoint.EngineName** is set to **PostgreSQL** or **DRDS**, specify the name of the database to be migrated. When it is set to **MongoDB**, specify the name of the authentication database for the database account.
        self.data_base_name = data_base_name
        # The database engine of the destination database. Valid values: **MySQL**, **DRDS**, **SQLServer**, **PostgreSQL**, **PPAS**, **MongoDB**, **Redis**, **POLARDB**, and **polardb_pg**.
        # > This parameter is available and required only when **DestinationEndpoint.InstanceType** is set to **RDS**, **POLARDB**, **ECS**, **LocalInstance**, or **Express**.
        self.engine_name = engine_name
        # The endpoint of the destination database.
        # > This parameter is available and required only when **DestinationEndpoint.InstanceType** is set to **LocalInstance** or **Express**.
        self.ip = ip
        # The ID of the destination instance.
        # > This parameter is available and required only when **DestinationEndpoint.InstanceType** is set to **RDS**, **ECS**, **MongoDB**, **Redis**, **DRDS**, **PetaData**, **OceanBase**, **POLARDB**, **PolarDB_o**, **AnalyticDB**, or **Greenplum**. You must specify the corresponding instance ID. For example, if the value is **ECS**, specify the ID of the ECS instance.
        self.instance_id = instance_id
        # The instance type of the destination database. Valid values:
        # - **ECS**: Self-managed database hosted on ECS.
        # - **LocalInstance**: Self-managed database with a public IP address.
        # - **RDS**: ApsaraDB RDS instance.
        # - **DRDS**: PolarDB-X instance.
        # - **MongoDB**: ApsaraDB for MongoDB instance.
        # - **Redis**: ApsaraDB for Redis instance.
        # - **PetaData**: HybridDB for MySQL instance.
        # - **POLARDB**: PolarDB for MySQL or PolarDB for PostgreSQL cluster.
        # - **PolarDB_o**: PolarDB for Oracle cluster.
        # - **AnalyticDB**: AnalyticDB for MySQL 3.0 or 2.0 cluster.
        # - **Greenplum**: AnalyticDB for PostgreSQL cluster.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The SID of the Oracle database.
        # > This parameter is available and required only when **DestinationEndpoint.EngineName** is set to **Oracle** and the Oracle database is a non-Real Application Cluster instance.
        self.oracle_sid = oracle_sid
        # The password of the destination database account.
        self.password = password
        # The service port number of the destination database.
        # > This parameter is available and required only when **DestinationEndpoint.InstanceType** is set to **ECS**, **LocalInstance**, or **Express**.
        self.port = port
        # The ID of the region where the destination database resides.
        # > When **DestinationEndpoint.InstanceType** is set to **LocalInstance**, you can specify **cn-hangzhou** or the ID of the region that is closest to your self-managed database. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # The database account of the destination database.
        # 
        # Note: The required permissions vary based on the database engine. For more information, see the corresponding configuration examples in the migration overview.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_base_name is not None:
            result['DataBaseName'] = self.data_base_name

        if self.engine_name is not None:
            result['EngineName'] = self.engine_name

        if self.ip is not None:
            result['IP'] = self.ip

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

