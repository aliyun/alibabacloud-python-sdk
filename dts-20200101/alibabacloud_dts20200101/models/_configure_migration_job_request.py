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
        # The Alibaba Cloud account ID. You do not need to specify this parameter because it will be deprecated.
        self.account_id = account_id
        # The start position of incremental data migration. The value is a UNIX timestamp in seconds.
        self.checkpoint = checkpoint
        # The ID of the data migration instance. You can call the **DescribeMigrationJobs** operation to query the instance ID.
        # 
        # This parameter is required.
        self.migration_job_id = migration_job_id
        # The name of the migration task. The name can be up to 32 characters in length. Specify a descriptive name for easy identification. Uniqueness is not required.
        # 
        # This parameter is required.
        self.migration_job_name = migration_job_name
        # The objects to be migrated. The value is a JSON string that supports regular expressions. For more information, see [Migration object configuration](~141901~).
        # 
        # This parameter is required.
        self.migration_object = migration_object
        # The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet special requirements, such as whether to automatically start the precheck. For more information, see [MigrationReserved parameter description](https://help.aliyun.com/document_detail/176470.html).
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id
        # The region ID of the data migration instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > The region ID must be the same as the region ID of the destination database.
        self.region_id = region_id
        # The resource group ID.
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
        # 待迁移的数据库名称或鉴权数据库名称。
        # > - 当**SourceEndpoint.EngineName**取值为**PostgreSQL**或**MongoDB**时，本参数才可用且必须传入。
        # - 当**SourceEndpoint.EngineName**取值为**PostgreSQL**时，传入待迁移的数据库名称；取值为**MongoDB**时，传入数据库账号的鉴权数据库名称。
        self.database_name = database_name
        # 源库的数据库类型，取值：**MySQL**、**TiDB**、**SQLServer**、**PostgreSQL**、**Oracle**、**MongoDB**、**Redis**、**POLARDB**、**polardb_pg**。
        # > 当**DestinationEndpoint.InstanceType**取值为**RDS**、**POLARDB**、**ECS**、**LocalInstance**或**Express**时，本参数才可用且必须传入。
        self.engine_name = engine_name
        # 源库的连接地址。
        # > 当**SourceEndpoint.InstanceType**取值为**LocalInstance**或**Express**时，本参数才可用且必须传入。
        self.ip = ip
        # 源库的实例ID。
        # > - 当**SourceEndpoint.InstanceType**取值为**RDS**、**ECS**、**Express**、**MongoDB**、**POLARDB**或**PolarDB_o**时，本参数才可用且必须传入对应的实例ID（例如取值为**ECS**，则本参数传入ECS实例的ID）。
        # - 当**SourceEndpoint.InstanceType**取值为**Express**时，本参数传入VPC ID（即专有网络ID）。
        self.instance_id = instance_id
        # 源库的实例类型，取值：
        # - **RDS**：阿里云RDS实例。
        # - **ECS**：ECS上的自建数据库。
        # - **LocalInstance**：有公网IP的自建数据库。
        # - **Express**：通过专线/VPN网关/智能接入网关接入的自建数据库。
        # - **dg**：通过数据库网关DG接入的自建数据库。
        # - **cen**：通过云企业网CEN接入的自建数据库。
        # - **MongoDB**：阿里云MongoDB实例。
        # - **POLARDB**：阿里云PolarDB MySQL、PolarDB PostgreSQL。
        # - **PolarDB_o**：阿里云PolarDB O引擎集群。
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Oracle数据库的SID信息。
        # > 当**SourceEndpoint.EngineName**取值为**Oracle**，且Oracle数据库为非RAC实例时，本参数才可用且必须传入。
        self.oracle_sid = oracle_sid
        # 源实例所属的阿里云账号ID。
        # > 仅在配置跨阿里云账号的数据迁移时本参数才可用，且必须传入。
        self.owner_id = owner_id
        # 源库数据库账号对应的密码。
        self.password = password
        # 源库的服务端口。
        # > 当**SourceEndpoint.InstanceType**取值为**ECS**、**LocalInstance**或**Express**时，本参数才可用且必须传入。
        self.port = port
        # 源库所属的地域ID。
        # > 当**SourceEndpoint.InstanceType**取值为**LocalInstance**时，您可以传入**cn-hangzhou**或者离自建数据库地物理距离最近的地域ID，详情请参见[支持的地域列表](https://help.aliyun.com/document_detail/141033.html)。
        self.region = region
        # 当源实例与目标实例所属阿里云账号不同时，需传入该参数，来指定源实例的授权角色，以允许目标实例阿里云账号访问源实例的实例信息。
        # > 角色所需的权限及授权方式，请参见[跨阿里云账号数据迁移或同步时如何配置RAM授权](https://help.aliyun.com/document_detail/48468.html)。
        self.role = role
        # 源库的数据库账号。
        # 
        # 说明 迁移不同的数据库所需的权限有所差异，详情请参见迁移方案概览中对应的配置案例。
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
        # 是否进行全量数据迁移，取值：
        # - **true**：是。
        # - **false**：否。
        # 
        # > DTS对全量数据迁移的支持情况因数据库类型不同而有所差异，详情请参见[支持的数据库和迁移类型](https://help.aliyun.com/document_detail/26618.html)。
        # 
        # This parameter is required.
        self.data_intialization = data_intialization
        # 是否进行增量数据迁移，取值：
        # - **true**：是。
        # - **false**：否。
        # 
        # > DTS对增量数据迁移的支持情况因数据库类型不同而有所差异，详情请参见[支持的数据库和迁移类型](https://help.aliyun.com/document_detail/26618.html)。
        # 
        # This parameter is required.
        self.data_synchronization = data_synchronization
        # 是否进行结构迁移，取值：
        # - **true**：是。
        # - **false**：否。
        # 
        # > DTS对结构迁移的支持情况因数据库类型不同而有所差异，详情请参见[支持的数据库和迁移类型](https://help.aliyun.com/document_detail/26618.html)。
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
        # 待迁入的数据库名称或鉴权数据库名称。 
        # > - 当**DestinationEndpoint.EngineName**取值为**PostgreSQL**、**DRDS**或**MongoDB**时，本参数才可用且必须传入。
        # - 当**DestinationEndpoint.EngineName**取值为**PostgreSQL**或**DRDS**时，传入待迁移的数据库名称；取值为**MongoDB**时，传入数据库账号的鉴权数据库名称。
        self.data_base_name = data_base_name
        # 目标库的数据库类型。取值：**MySQL**、**DRDS**、**SQLServer**、**PostgreSQL**、**PPAS**、**MongoDB**、**Redis**、**POLARDB**、**polardb_pg**
        # > 当**DestinationEndpoint.InstanceType**取值为**RDS**、**POLARDB**、**ECS**、**LocalInstance**或**Express**时，本参数才可用且必须传入。
        self.engine_name = engine_name
        # 目标库的连接地址。
        # > 当**DestinationEndpoint.InstanceType**取值为**LocalInstance**或**Express**时，本参数才可用且必须传入。
        self.ip = ip
        # 目标实例ID。
        # > 当**DestinationEndpoint.InstanceType**取值为**RDS**、**ECS**、**MongoDB**、**Redis**、**DRDS**、**PetaData**、**OceanBase**、**POLARDB**、**PolarDB_o**、**AnalyticDB**或**Greenplum**时，本参数才可用且必须传入对应的实例ID（例如取值为**ECS**，则需要传入ECS实例ID）。
        self.instance_id = instance_id
        # 目标库的实例类型，取值：
        # - **ECS**：ECS上的自建数据库。
        # - **LocalInstance**：有公网IP的自建数据库。
        # - **RDS**：阿里云RDS实例。
        # - **DRDS**：阿里云PolarDB-X实例。
        # - **MongoDB**：阿里云MongoDB实例。
        # - **Redis**：阿里云Redis实例。
        # - **PetaData**：阿里云HybridDB for MySQL实例。
        # - **POLARDB**：阿里云PolarDB MySQL、PolarDB PostgreSQL。
        # - **PolarDB_o**：阿里云PolarDB O引擎集群。
        # - **AnalyticDB**：阿里云云原生数据仓库AnalyticDB MySQL 3.0和2.0版本。
        # - **Greenplum**：阿里云云原生数据仓库AnalyticDB PostgreSQL。
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Oracle数据库的SID信息。
        # > 当**DestinationEndpoint.EngineName**取值为**Oracle**，且**Oracle**数据库为非RAC实例时，本参数才可用且必须传入。
        self.oracle_sid = oracle_sid
        # 目标库数据库账号的密码。
        self.password = password
        # 目标库的服务端口。
        # > 当**DestinationEndpoint.InstanceType**取值为**ECS**、**LocalInstance**或**Express**时，本参数才可用且必须传入。
        self.port = port
        # 目标库所属的地域ID。
        # > 当**DestinationEndpoint.InstanceType**取值为**LocalInstance**时，您可以传入**cn-hangzhou**或者离自建数据库地物理距离最近的地域ID，详情请参见[支持的地域列表](https://help.aliyun.com/document_detail/141033.html)。
        self.region = region
        # 目标库的数据库账号。
        # 
        # 说明 迁移不同的数据库所需的权限有所差异，详情请参见迁移方案概览中对应的配置案例。
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

