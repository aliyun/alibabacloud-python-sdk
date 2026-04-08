# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class ConfigureSynchronizationJobRequest(DaraModel):
    def __init__(
        self,
        destination_endpoint: main_models.ConfigureSynchronizationJobRequestDestinationEndpoint = None,
        partition_key: main_models.ConfigureSynchronizationJobRequestPartitionKey = None,
        source_endpoint: main_models.ConfigureSynchronizationJobRequestSourceEndpoint = None,
        account_id: str = None,
        checkpoint: str = None,
        data_initialization: bool = None,
        migration_reserved: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        structure_initialization: bool = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_objects: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.partition_key = partition_key
        self.source_endpoint = source_endpoint
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.account_id = account_id
        # The synchronization checkpoint.
        self.checkpoint = checkpoint
        # Specifies whether to perform initial full data synchronization. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  Default value: **true**.
        # 
        # This parameter is required.
        self.data_initialization = data_initialization
        # The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet special requirements, for example, whether to automatically start a precheck. For more information, see [MigrationReserved](https://help.aliyun.com/document_detail/176470.html).
        # 
        # >  This parameter can be used for data synchronization between ApsaraDB for Redis Enterprise Edition instances. For more information, see [Use OpenAPI Explorer to configure one-way or two-way data synchronization between ApsaraDB for Redis Enterprise Edition instances](https://help.aliyun.com/document_detail/155967.html).
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id
        # The ID of the region where the data synchronization instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # 资源组ID。
        self.resource_group_id = resource_group_id
        # Specifies whether to perform initial schema synchronization. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  Default value: **true**.
        # 
        # This parameter is required.
        self.structure_initialization = structure_initialization
        # The synchronization direction. Valid values:
        # 
        # *   **Forward**
        # *   **Reverse**
        # 
        # > 
        # *   Default value: **Forward**.
        # *   The value **Reverse** takes effect only if the topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # The ID of the data synchronization instance. You can call the [DescribeSynchronizationJobs](https://help.aliyun.com/document_detail/49454.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.synchronization_job_id = synchronization_job_id
        # The name of the data synchronization task.
        # 
        # >  We recommend that you specify an informative name for easy identification. You do not need to use a unique task name.
        self.synchronization_job_name = synchronization_job_name
        # The objects that you want to synchronize. The value is a JSON string and can contain regular expressions. For more information, see [SynchronizationObjects](https://help.aliyun.com/document_detail/141901.html).
        # 
        # This parameter is required.
        self.synchronization_objects = synchronization_objects

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.partition_key:
            self.partition_key.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key.to_map()

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization

        if self.migration_reserved is not None:
            result['MigrationReserved'] = self.migration_reserved

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id

        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name

        if self.synchronization_objects is not None:
            result['SynchronizationObjects'] = self.synchronization_objects

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.ConfigureSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('PartitionKey') is not None:
            temp_model = main_models.ConfigureSynchronizationJobRequestPartitionKey()
            self.partition_key = temp_model.from_map(m.get('PartitionKey'))

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.ConfigureSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')

        if m.get('MigrationReserved') is not None:
            self.migration_reserved = m.get('MigrationReserved')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')

        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')

        if m.get('SynchronizationObjects') is not None:
            self.synchronization_objects = m.get('SynchronizationObjects')

        return self

class ConfigureSynchronizationJobRequestSourceEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: str = None,
        password: str = None,
        port: str = None,
        role: str = None,
        user_name: str = None,
    ):
        # The name of the database to which the synchronization object in the source instance belongs.
        self.database_name = database_name
        # The IP address of the source database.
        # 
        # >  You must specify this parameter only if the **SourceEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        self.ip = ip
        # The ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance. Valid values:
        # 
        # *   **RDS**: ApsaraDB RDS instance
        # *   **Redis**: ApsaraDB for Redis instance
        # *   **PolarDB**: PolarDB for MySQL cluster or PolarDB O Edition cluster
        # *   **ECS**: self-managed database that is hosted on Elastic Compute Service (ECS)
        # *   **Express**: self-managed database that is connected over Express Connect
        # *   **dg**: self-managed database that is connected over Database Gateway
        # *   **cen**: self-managed database that is connected over Cloud Enterprise Network (CEN)
        # 
        # >  The default value is **RDS**.
        self.instance_type = instance_type
        # The ID of the Alibaba Cloud account that owns the source RDS instance.
        # 
        # >  You can specify this parameter to synchronize data across different Alibaba Cloud accounts. In this case, you also need to specify the **SourceEndpoint.Role** parameter.
        self.owner_id = owner_id
        # The password of the source database account.
        # 
        # >  You must specify this parameter only if the **SourceEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        self.password = password
        # The service port number of the source database.
        # 
        # >  You must specify this parameter only if the **SourceEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        self.port = port
        # The name of the RAM role configured for the Alibaba Cloud account that owns the source instance.
        # 
        # >  You must specify this parameter when you synchronize data across different Alibaba Cloud accounts. For information about the permissions and authorization methods of the RAM role, see [Configure RAM authorization for cross-account data migration and synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.role = role
        # The database account of the source database.
        # 
        # > 
        # *   You must specify this parameter only if the **SourceEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        # *   If the **SourceEndpoint.InstanceType** parameter is set to **Redis**, you do not need to specify the database account.
        # *   The permissions that are required for database accounts vary with the synchronization scenario. For more information, see [Overview of data synchronization scenarios](https://help.aliyun.com/document_detail/140954.html).
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

        if self.ip is not None:
            result['IP'] = self.ip

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.role is not None:
            result['Role'] = self.role

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ConfigureSynchronizationJobRequestPartitionKey(DaraModel):
    def __init__(
        self,
        modify_time_day: bool = None,
        modify_time_hour: bool = None,
        modify_time_minute: bool = None,
        modify_time_month: bool = None,
        modify_time_year: bool = None,
    ):
        # Specifies whether the incremental data table contains partitions defined by the modifytime_day field. Valid values: **true** and **false**.
        # 
        # >  This parameter is available only if the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
        self.modify_time_day = modify_time_day
        # Specifies whether the incremental data table contains partitions defined by the modifytime_hour field. Valid values: **true** and **false**.
        # 
        # >  This parameter is available only if the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
        self.modify_time_hour = modify_time_hour
        # Specifies whether the incremental data table contains partitions defined by the modifytime_minute field. Valid values: **true** and **false**.
        # 
        # >  This parameter is available only if the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
        self.modify_time_minute = modify_time_minute
        # Specifies whether the incremental data table contains partitions defined by the modifytime_month field. Valid values: **true** and **false**.
        # 
        # >  This parameter is available only if the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
        self.modify_time_month = modify_time_month
        # Specifies whether the incremental data table contains partitions defined by the modifytime_year field. Valid values: **true** and **false**.
        # 
        # >  This parameter is available only if the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
        self.modify_time_year = modify_time_year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_time_day is not None:
            result['ModifyTime_Day'] = self.modify_time_day

        if self.modify_time_hour is not None:
            result['ModifyTime_Hour'] = self.modify_time_hour

        if self.modify_time_minute is not None:
            result['ModifyTime_Minute'] = self.modify_time_minute

        if self.modify_time_month is not None:
            result['ModifyTime_Month'] = self.modify_time_month

        if self.modify_time_year is not None:
            result['ModifyTime_Year'] = self.modify_time_year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime_Day') is not None:
            self.modify_time_day = m.get('ModifyTime_Day')

        if m.get('ModifyTime_Hour') is not None:
            self.modify_time_hour = m.get('ModifyTime_Hour')

        if m.get('ModifyTime_Minute') is not None:
            self.modify_time_minute = m.get('ModifyTime_Minute')

        if m.get('ModifyTime_Month') is not None:
            self.modify_time_month = m.get('ModifyTime_Month')

        if m.get('ModifyTime_Year') is not None:
            self.modify_time_year = m.get('ModifyTime_Year')

        return self

class ConfigureSynchronizationJobRequestDestinationEndpoint(DaraModel):
    def __init__(
        self,
        data_base_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        password: str = None,
        port: str = None,
        user_name: str = None,
    ):
        # The name of the database to which the synchronization object in the destination instance belongs.
        self.data_base_name = data_base_name
        # The IP address of the destination database.
        # 
        # >  You must specify this parameter only if the **DestinationEndpoint.InstanceType** parameter is set to **Express**, **dg**, or **cen**.
        self.ip = ip
        # The ID of the destination instance.
        # 
        # >  If the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute** or **DataHub**, you must specify the name of the MaxCompute project or the DataHub project.
        # 
        # If the destination instance is an AnalyticDB for MySQL cluster, specify the ID of the AnalyticDB for MySQL cluster.
        self.instance_id = instance_id
        # The type of the destination instance. Valid values:
        # 
        # *   **Redis**: ApsaraDB for Redis instance
        # *   **RDS**: ApsaraDB RDS instance
        # *   **PolarDB**: PolarDB for MySQL cluster or PolarDB O Edition cluster
        # *   **ECS**: self-managed database that is hosted on ECS
        # *   **Express**: self-managed database that is connected over Express Connect
        # *   **DataHub**: DataHub project
        # *   **MaxCompute**: MaxCompute project
        # *   **AnalyticDB**: AnalyticDB for MySQL cluster V3.0 or V2.0
        # *   **Greenplum**: AnalyticDB for PostgreSQL instance
        # 
        # >  The default value is **RDS**.
        self.instance_type = instance_type
        # The password of the destination database account.
        # 
        # > 
        # *   If the **DestinationEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**, you must specify the DestinationEndpoint.Password parameter.
        self.password = password
        # The service port number of the destination database.
        # 
        # >  You must specify this parameter only if the **DestinationEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        self.port = port
        # The database account of the destination database.
        # 
        # > 
        # *   The permissions that are required for database accounts vary with the synchronization scenario. For more information, see [Overview of data synchronization scenarios](https://help.aliyun.com/document_detail/140954.html).
        # *   If the **DestinationEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**, you must specify the DestinationEndpoint.UserName parameter.
        # *   If the **DestinationEndpoint.InstanceType** parameter is set to RDS and the database version is MySQL 5.5 or MySQL 5.6, you do not need to specify the DestinationEndpoint.UserName and **DestinationEndpoint.Password** parameters.
        # *   If the **DestinationEndpoint.InstanceType** parameter is set to **Redis**, you do not need to specify the DestinationEndpoint.UserName parameter.
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

        if self.ip is not None:
            result['IP'] = self.ip

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

