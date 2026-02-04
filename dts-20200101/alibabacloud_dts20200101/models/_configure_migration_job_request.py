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
        # The objects that you want to migrate. The value is a JSON string and can contain regular expressions.
        # 
        # For more information, see [MigrationObject](https://help.aliyun.com/document_detail/141227.html).
        self.account_id = account_id
        # Specifies whether to perform incremental data migration. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  For more information about databases that support incremental data migration, see [Supported databases and migration types](https://help.aliyun.com/document_detail/26618.html).
        self.checkpoint = checkpoint
        # system
        # 
        # This parameter is required.
        self.migration_job_id = migration_job_id
        # The ID of the region where the data migration instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # >  The region ID of the data migration instance is the same as that of the destination database.
        # 
        # This parameter is required.
        self.migration_job_name = migration_job_name
        # Specifies whether to perform schema migration. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  For more information about databases that support schema migration, see [Supported databases and migration types](https://help.aliyun.com/document_detail/26618.html).
        # 
        # This parameter is required.
        self.migration_object = migration_object
        # Specifies whether to perform full data migration. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  For more information about databases that support full data migration, see [Supported databases and migration types](https://help.aliyun.com/document_detail/26618.html).
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id
        self.region_id = region_id
        # Resource GroupId
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
        # The endpoint of the source database.
        # 
        # >  You must specify the endpoint only if the **SourceEndpoint.InstanceType** parameter is set to **LocalInstance** or **Express**.
        self.database_name = database_name
        # The instance type of the source database. Valid values:
        # 
        # *   **RDS**: ApsaraDB RDS instance
        # *   **ECS**: self-managed database that is hosted on ECS
        # *   **LocalInstance**: self-managed database with a public IP address
        # *   **Express**: self-managed database that is connected over Express Connect, VPN Gateway, or Smart Access Gateway
        # *   **dg**: self-managed database that is connected over Database Gateway
        # *   **cen**: self-managed database that is connected over Cloud Enterprise Network (CEN)
        # *   **MongoDB**: ApsaraDB for MongoDB instance
        # *   **POLARDB**: PolarDB for MySQL cluster or PolarDB for PostgreSQL cluster
        # *   **PolarDB_o**: PolarDB O Edition cluster
        self.engine_name = engine_name
        # rm-bp1i99e8l7913****
        self.ip = ip
        # dtsl3m1213ye7l****
        self.instance_id = instance_id
        # The ID of the data migration instance. You can call the **DescribeMigrationJobs** operation to query the instance ID.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The region ID of the source database.
        # 
        # >  If the **SourceEndpoint.InstanceType** parameter is set to **LocalInstance**, you can enter **cn-hangzhou** or the ID of the region closest to the self-managed database. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.oracle_sid = oracle_sid
        # The name of the source database or the authentication database.
        # 
        # > 
        # *   You must specify the database name only if the **SourceEndpoint.EngineName** parameter is set to **PostgreSQL** or **MongoDB**.
        # *   If the **SourceEndpoint.EngineName** parameter is set to **PostgreSQL**, specify the name of the source database. If the SourceEndpoint.EngineName parameter is set to **MongoDB**, specify the name of the authentication database.
        self.owner_id = owner_id
        # The system ID (SID) of the Oracle database.
        # 
        # >  You must specify this parameter only if the **SourceEndpoint.EngineName** parameter is set to **Oracle** and the **Oracle** database is deployed in a non-RAC architecture.
        self.password = password
        # The engine type of the source database. Valid values: **MySQL**, **TiDB**, **SQLServer**, **PostgreSQL**, **Oracle**, **MongoDB**, **Redis**, **POLARDB**, and **polardb_pg**.
        # 
        # >  You must specify the engine type only if the **DestinationEndpoint.InstanceType** parameter is set to **RDS**, **POLARDB**, **ECS**, **LocalInstance**, or **Express**.
        self.port = port
        # The ID of the instance that hosts the source database.
        # 
        # > 
        # *   You must specify the instance ID only if the **SourceEndpoint.InstanceType** parameter is set to **RDS**, **ECS**, **Express**, **MongoDB**, **POLARDB**, or **PolarDB_o**. For example, if the SourceEndpoint.InstanceType parameter is set to **ECS**, you must specify the ID of the ECS instance.
        # *   If the **SourceEndpoint.InstanceType** parameter is set to **Express**, you must specify the ID of the virtual private cloud (VPC).
        self.region = region
        # The database account of the source database.
        # 
        # >  The permissions that are required for database accounts vary with the migration scenario. For more information, see [Overview of data migration scenarios](https://help.aliyun.com/document_detail/26618.html).
        self.role = role
        # The service port number of the source database.
        # 
        # >  You must specify the service port number only if the **SourceEndpoint.InstanceType** parameter is set to **ECS**, **LocalInstance**, or **Express**.
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
        # The database account of the destination database.
        # 
        # >  The permissions that are required for database accounts vary with the migration scenario. For more information, see [Overview of data migration scenarios](https://help.aliyun.com/document_detail/26618.html).
        # 
        # This parameter is required.
        self.data_intialization = data_intialization
        # The password of the destination database account.
        # 
        # This parameter is required.
        self.data_synchronization = data_synchronization
        # The name of the destination database or the authentication database.
        # 
        # > 
        # *   You must specify the database name only if the **DestinationEndpoint.EngineName** parameter is set to **PostgreSQL**, **DRDS**, or **MongoDB**.
        # *   If the **DestinationEndpoint.EngineName** parameter is set to **PostgreSQL** or **DRDS**, specify the name of the destination database. If the DestinationEndpoint.EngineName parameter is set to **MongoDB**, specify the name of the authentication database.
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
        # The region ID of the destination database.
        # 
        # >  If the **DestinationEndpoint.InstanceType** parameter is set to **LocalInstance**, you can enter **cn-hangzhou** or the ID of the region closest to the self-managed database. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.data_base_name = data_base_name
        # The authorized RAM role of the source instance. You must specify the RAM role only if the source instance and the destination instance belong to different Alibaba Cloud accounts. You can use the RAM role to allow the Alibaba Cloud account that owns the destination instance to access the source instance.
        # 
        # >  For information about the permissions and authorization methods of the RAM role, see [Configure RAM authorization for cross-account data migration and synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.engine_name = engine_name
        # The ID of the instance that hosts the destination database.
        # 
        # >  You must specify the instance ID only if the **DestinationEndpoint.InstanceType** parameter is set to **RDS**, **ECS**, **MongoDB**, **Redis**, **DRDS**, **PetaData**, **OceanBase**, **POLARDB**, **PolarDB_o**, **AnalyticDB**, or **Greenplum**. For example, if the DestinationEndpoint.InstanceType parameter is set to **ECS**, you must specify the ID of the ECS instance.
        self.ip = ip
        # The ID of the Alibaba Cloud account to which the source instance belongs.
        # 
        # >  You must specify this parameter only when you configure data migration across different Alibaba Cloud accounts.
        self.instance_id = instance_id
        # The password of the source database account.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet special requirements, for example, whether to automatically start a precheck. For more information, see [MigrationReserved](https://help.aliyun.com/document_detail/176470.html).
        self.oracle_sid = oracle_sid
        # The service port number of the destination database.
        # 
        # >  You must specify the service port number only if the **DestinationEndpoint.InstanceType** parameter is set to **ECS**, **LocalInstance**, or **Express**.
        self.password = password
        # The engine type of the destination database. Valid values: **MySQL**, **DRDS**, **SQLServer**, **PostgreSQL**, **PPAS**, **MongoDB**, **Redis**, **POLARDB**, and **polardb_pg**.
        # 
        # >  You must specify the engine type only if the **DestinationEndpoint.InstanceType** parameter is set to **RDS**, **POLARDB**, **ECS**, **LocalInstance**, or **Express**.
        self.port = port
        # The instance type of the destination database. Valid values:
        # 
        # *   **ECS**: self-managed database that is hosted on Elastic Compute Service (ECS)
        # *   **LocalInstance**: self-managed database with a public IP address
        # *   **RDS**: ApsaraDB RDS instance
        # *   **DRDS**: PolarDB-X instance
        # *   **MongoDB**: ApsaraDB for MongoDB instance
        # *   **Redis**: ApsaraDB for Redis instance
        # *   **PetaData**: HybridDB for MySQL instance
        # *   **POLARDB**: PolarDB for MySQL cluster or PolarDB for PostgreSQL cluster
        # *   **PolarDB_o**: PolarDB O Edition cluster
        # *   **AnalyticDB**: AnalyticDB for MySQL cluster V3.0 or V2.0
        # *   **Greenplum**: AnalyticDB for PostgreSQL instance
        self.region = region
        # The endpoint of the destination database.
        # 
        # >  You must specify the endpoint only if the **DestinationEndpoint.InstanceType** parameter is set to **LocalInstance** or **Express**.
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

