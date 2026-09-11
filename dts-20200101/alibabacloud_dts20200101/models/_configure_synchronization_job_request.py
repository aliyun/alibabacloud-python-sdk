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
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because it will be discontinued.
        self.account_id = account_id
        # The synchronization checkpoint.
        self.checkpoint = checkpoint
        # Specifies whether to perform initial full data synchronization. Valid values:
        # 
        # - **true**: yes.
        # - **false**: no.
        # 
        # > Default value: **true**.
        # 
        # This parameter is required.
        self.data_initialization = data_initialization
        # The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet special requirements, such as specifying whether to automatically start the precheck. For more information, see [MigrationReserved parameter description](https://help.aliyun.com/document_detail/176470.html).
        # > For example, you can use this parameter for data synchronization between ApsaraDB for Redis Enhanced Edition (Tair) instances. For more information, see [Use OpenAPI to configure one-way or bidirectional data synchronization between ApsaraDB for Redis Enhanced Edition instances](https://help.aliyun.com/document_detail/155967.html).
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id
        # The ID of the region where the data synchronization instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to perform initial schema synchronization. Valid values:
        # - **true**: yes.
        # - **false**: no.
        # 
        # > Default value: **true**.
        # 
        # This parameter is required.
        self.structure_initialization = structure_initialization
        # The synchronization direction. Valid values:
        # - **Forward**: forward.
        # - **Reverse**: reverse.
        # 
        # > - Default value: **Forward**.
        # - This parameter takes effect only if you set it to **Reverse** and the synchronization topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # The ID of the data synchronization instance. You can call the [DescribeSynchronizationJobs](https://help.aliyun.com/document_detail/49454.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.synchronization_job_id = synchronization_job_id
        # The name of the synchronization task.
        # > Specify a descriptive name that makes it easy to identify the task. It does not need to be unique.
        self.synchronization_job_name = synchronization_job_name
        # The objects to be synchronized. The value is a JSON string and supports certain regular expressions. For more information, see [Synchronization object configuration](https://help.aliyun.com/document_detail/141901.html).
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
        # 源实例中的同步对象所属数据库名称。
        self.database_name = database_name
        # 源库的IP地址。
        # > 当**SourceEndpoint.InstanceType**取值为**ECS**、**Express**、**dg**或**cen**时，本参数才可用且必须传入。
        self.ip = ip
        # 源实例ID。
        self.instance_id = instance_id
        # 源实例类型，取值为：
        # 
        # - **RDS**：阿里云RDS实例。
        # - **Redis**：阿里云Redis实例。
        # - **PolarDB**：阿里云PolarDB集群（仅支持MySQL或兼容Oracle语法的引擎）。
        # - **ECS**：ECS上的自建数据库。
        # - **Express**：通过专线接入的自建数据库。
        # - **dg**：通过数据库网关DG接入的自建数据库。
        # - **cen**：通过云企业网CEN接入的自建数据库。
        # 
        # > 默认取值为**RDS**。
        self.instance_type = instance_type
        # 源RDS实例所属的阿里云账号ID。
        # > 传入本参数即代表执行跨阿里云账号的数据同步，同时您还需要传入**SourceEndpoint.Role**参数。
        self.owner_id = owner_id
        # 源库数据库账号密码。
        # > 当**SourceEndpoint.InstanceType**取值为**ECS**、**Express**、**dg**或**cen**时，本参数必须传入。
        self.password = password
        # 源库的数据库服务端口。
        # > 当**SourceEndpoint.InstanceType**取值为**ECS**、**Express**、**dg**或**cen**时，本参数才可用且必须传入。
        self.port = port
        # 源实例所属云账号配置的角色名称。
        # > 执行跨阿里云账号的数据同步时须传入本参数，该角色所需的权限及授权方式请参见[跨阿里云账号数据迁移或同步时如何配置RAM授权](https://help.aliyun.com/document_detail/48468.html)。
        self.role = role
        # 源库的数据库账号。
        # > - 当**SourceEndpoint.InstanceType**取值为**ECS**、**Express**、**dg**或**cen**时，本参数才可用且必须传入。
        # - 当**SourceEndpoint.InstanceType**取值为**Redis**时，本参数无需传入。
        # - 同步不同的数据库所需的权限有所差异，详情请参见[DTS数据同步方案概览](https://help.aliyun.com/document_detail/140954.html)中对应的配置案例。
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
        # 设置增量日志表是否包含以增量更新时间对应日期信息定义的分区，取值：**true**或**false**。
        # > 当**DestinationEndpoint.InstanceType**参数取值为**Maxcompute**时，本参数才可用。
        self.modify_time_day = modify_time_day
        # 设置增量日志表是否包含以增量更新时间对应小时信息定义的分区，取值：**true**或**false**。
        # > 当**DestinationEndpoint.InstanceType**参数取值为**Maxcompute**时，本参数才可用。
        self.modify_time_hour = modify_time_hour
        # 设置增量日志表是否包含以增量更新时间对应分钟信息定义的分区，取值：**true**或**false**。
        # 
        # > 当**DestinationEndpoint.InstanceType**参数取值为**Maxcompute**时，本参数才可用。
        self.modify_time_minute = modify_time_minute
        # 设置增量日志表是否包含以增量更新时间对应月份信息定义的分区，取值：**true**或**false**。
        # > 当**DestinationEndpoint.InstanceType**参数取值为**Maxcompute**时，本参数才可用。
        self.modify_time_month = modify_time_month
        # 设置增量日志表是否包含以增量更新时间对应年份信息定义的分区，取值：**true**或**false**。
        # > 当**DestinationEndpoint.InstanceType**参数取值为**Maxcompute**时，本参数才可用。
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
        # 目标实例中的同步对象所属数据库名称。
        self.data_base_name = data_base_name
        # 目标库的IP地址。
        # > 当**DestinationEndpoint.InstanceType**取值为**Express**、**dg**或**cen**时，本参数必须传入本参数才可用且必须传入。
        self.ip = ip
        # 同步目标实例的实例ID
        # > 当**DestinationEndpoint.InstanceType**取值为**MaxCompute**或**DataHub**时，本参数传入MaxCompute实例或DataHub的Project名称。
        # 当目标实例为阿里云分析型数据库MySQL版时，传入分析型数据库MySQL版的集群ID。
        self.instance_id = instance_id
        # 目标实例类型，取值为：
        # 
        # - **Redis**：阿里云Redis实例。
        # - **RDS**：阿里云RDS实例。
        # - **PolarDB**：阿里云PolarDB集群（仅支持MySQL或兼容Oracle语法的引擎）。
        # - **ECS**：ECS上的自建数据库。
        # - **Express**：通过专线接入的本地数据库。
        # - **DataHub**：阿里云DataHub实例。
        # - **MaxCompute**：阿里云MaxCompute实例。
        # - **AnalyticDB**：云原生数据仓库AnalyticDB MySQL  3.0和2.0版本。
        # - **Greenplum**：云原生数据仓库ADB PostgreSQL版（原分析型数据库PostgreSQL版）。
        # 
        # > 默认取值为**RDS**。
        self.instance_type = instance_type
        # 目标库数据库账号密码。
        # 
        # > - 当**DestinationEndpoint.InstanceType**取值为**ECS**、**Express**、**dg**或**cen**时，本参数必须传入。
        self.password = password
        # 目标库的数据库服务端口。
        # > 当**DestinationEndpoint.InstanceType**取值为**ECS**、**Express**、**dg**或**cen**时，本参数才可用且必须传入。
        self.port = port
        # 目标库的数据库账号。
        # > - 同步不同的数据库所需的权限有所差异，详情请参见[DTS数据同步方案概览](https://help.aliyun.com/document_detail/140954.html)中对应的配置案例。
        # - 当**DestinationEndpoint.InstanceType**取值为**ECS**、**Express**、**dg**或**cen**时，本参数必须传入。
        # - 当**DestinationEndpoint.InstanceType**取值为RDS且数据库版本为MySQL 5.5或MySQL 5.6，无需传入本参数和**DestinationEndpoint.Password**参数。
        # - 当**DestinationEndpoint.InstanceType**取值为**Redis**时，无需传入本参数。
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

