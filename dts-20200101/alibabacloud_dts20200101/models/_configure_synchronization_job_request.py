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
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter. This parameter will be deprecated soon.
        self.account_id = account_id
        # The synchronization checkpoint.
        self.checkpoint = checkpoint
        # Specifies whether to perform initial full data synchronization. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        # 
        # > Default value: **true**.
        # 
        # This parameter is required.
        self.data_initialization = data_initialization
        # The reserved parameter for DTS. The value is a JSON string. You can specify this parameter to meet specific requirements, such as whether to automatically start a precheck. For more information, see [MigrationReserved parameter description](https://help.aliyun.com/document_detail/176470.html).
        # > For example, you can use this parameter for data synchronization between Redis Enterprise instances. For more information, see [Call OpenAPI operations to configure one-way or two-way data synchronization between Redis Enterprise instances](https://help.aliyun.com/document_detail/155967.html).
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id
        # The ID of the region where the data synchronization instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to perform initial schema synchronization. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        # 
        # > Default value: **true**.
        # 
        # This parameter is required.
        self.structure_initialization = structure_initialization
        # The synchronization direction. Valid values:
        # - **Forward**: Forward synchronization.
        # - **Reverse**: Reverse synchronization.
        # 
        # > - Default value: **Forward**.
        # - This parameter takes effect only when the synchronization topology of the data synchronization instance is two-way synchronization and the value is set to **Reverse**.
        self.synchronization_direction = synchronization_direction
        # The ID of the data synchronization instance. You can call the [DescribeSynchronizationJobs](https://help.aliyun.com/document_detail/49454.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.synchronization_job_id = synchronization_job_id
        # The name of the synchronization task.
        # > Specify a descriptive name that is easy to identify. The name does not need to be unique.
        self.synchronization_job_name = synchronization_job_name
        # The objects to be synchronized. The value is a JSON string and supports specific regular expressions. For more information, see [Configure synchronization objects](https://help.aliyun.com/document_detail/141901.html).
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
        # The name of the database to which the synchronization objects in the source instance belong.
        self.database_name = database_name
        # The IP address of the source database.
        # > This parameter is available and required only when the **SourceEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        self.ip = ip
        # The instance ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance. Valid values:
        # 
        # - **RDS**: ApsaraDB RDS instance.
        # - **Redis**: Alibaba Cloud Redis instance.
        # - **PolarDB**: PolarDB cluster (only MySQL or Oracle-compatible engines are supported).
        # - **ECS**: Self-managed database hosted on Elastic Compute Service (ECS).
        # - **Express**: Self-managed database connected over Express Connect.
        # - **dg**: Self-managed database connected over Database Gateway.
        # - **cen**: Self-managed database connected over Cloud Enterprise Network (CEN).
        # 
        # > Default value: **RDS**.
        self.instance_type = instance_type
        # The Alibaba Cloud account ID to which the source ApsaraDB RDS instance belongs.
        # > Specifying this parameter indicates that cross-Alibaba Cloud account data synchronization is executed. You must also specify the **SourceEndpoint.Role** parameter.
        self.owner_id = owner_id
        # The password of the database account for the source database.
        # > This parameter is required only when the **SourceEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        self.password = password
        # The service port number of the source database.
        # > This parameter is available and required only when the **SourceEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        self.port = port
        # The name of the RAM role configured for the Alibaba Cloud account to which the source instance belongs.
        # > This parameter is required for cross-account data synchronization. For more information about the permissions required for the role and how to grant the permissions, see [Configure RAM authorization for cross-account data migration or synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.role = role
        # The database account of the source database.
        # > - This parameter is available and required only when the **SourceEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        # - This parameter is not required when the **SourceEndpoint.InstanceType** parameter is set to **Redis**.
        # - The permissions required for synchronizing different databases vary. For more information, see the corresponding configuration examples in [Overview of DTS data synchronization solutions](https://help.aliyun.com/document_detail/140954.html).
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
        # Specifies whether the incremental log table contains partitions defined by the day of the incremental update time. Valid values: **true** and **false**.
        # > This parameter is available only when the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
        self.modify_time_day = modify_time_day
        # Specifies whether the incremental log table contains partitions defined by the hour of the incremental update time. Valid values: **true** and **false**.
        # > This parameter is available only when the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
        self.modify_time_hour = modify_time_hour
        # Specifies whether the incremental log table contains partitions defined by the minute of the incremental update time. Valid values: **true** and **false**.
        # 
        # > This parameter is available only when the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
        self.modify_time_minute = modify_time_minute
        # Specifies whether the incremental log table contains partitions defined by the month of the incremental update time. Valid values: **true** and **false**.
        # > This parameter is available only when the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
        self.modify_time_month = modify_time_month
        # Specifies whether the incremental log table contains partitions defined by the year of the incremental update time. Valid values: **true** and **false**.
        # > This parameter is available only when the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute**.
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
        # The name of the database to which the synchronization objects in the destination instance belong.
        self.data_base_name = data_base_name
        # The IP address of the destination database.
        # > This parameter is available and required only when the **DestinationEndpoint.InstanceType** parameter is set to **Express**, **dg**, or **cen**.
        self.ip = ip
        # The instance ID of the destination instance for synchronization.
        # > When the **DestinationEndpoint.InstanceType** parameter is set to **MaxCompute** or **DataHub**, set this parameter to the name of the MaxCompute project or DataHub project.
        # If the destination instance is an Alibaba Cloud AnalyticDB for MySQL database, set this parameter to the cluster ID of the AnalyticDB for MySQL database.
        self.instance_id = instance_id
        # The destination instance type. Valid values:
        # 
        # - **Redis**: Alibaba Cloud Redis instance.
        # - **RDS**: ApsaraDB RDS instance.
        # - **PolarDB**: PolarDB cluster (only MySQL or Oracle-compatible engines are supported).
        # - **ECS**: Self-managed database hosted on ECS.
        # - **Express**: Self-managed database connected over Express Connect.
        # - **DataHub**: DataHub instance.
        # - **MaxCompute**: MaxCompute instance.
        # - **AnalyticDB**: AnalyticDB for MySQL 3.0 and 2.0.
        # - **Greenplum**: AnalyticDB for PostgreSQL.
        # 
        # > Default value: **RDS**.
        self.instance_type = instance_type
        # The password of the database account for the destination database.
        # 
        # > - This parameter is required when the **DestinationEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        self.password = password
        # The service port number of the destination database.
        # > This parameter is available and required only when the **DestinationEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        self.port = port
        # The database account of the destination database.
        # > - The permissions required for synchronizing different databases vary. For more information, see the corresponding configuration examples in [Overview of DTS data synchronization solutions](https://help.aliyun.com/document_detail/140954.html).
        # - This parameter is required when the **DestinationEndpoint.InstanceType** parameter is set to **ECS**, **Express**, **dg**, or **cen**.
        # - This parameter and the **DestinationEndpoint.Password** parameter are not required when the **DestinationEndpoint.InstanceType** parameter is set to **RDS** and the database engine version is MySQL 5.5 or MySQL 5.6.
        # - This parameter is not required when the **DestinationEndpoint.InstanceType** parameter is set to **Redis**.
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

