# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDtsJobEndpointRequest(DaraModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        database: str = None,
        dry_run: bool = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        endpoint: str = None,
        endpoint_instance_id: str = None,
        endpoint_instance_type: str = None,
        endpoint_ip: str = None,
        endpoint_port: str = None,
        endpoint_primary_vsw_id: str = None,
        endpoint_region_id: str = None,
        endpoint_secondary_vsw_id: str = None,
        endpoint_vpc_id: str = None,
        modify_account: bool = None,
        password: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        role_name: str = None,
        shard_password: str = None,
        shard_username: str = None,
        synchronization_direction: str = None,
        username: str = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the Alibaba Cloud account that owns the database instance.
        # 
        # > Specifying this parameter indicates cross-account data synchronization. You must also specify the **RoleName** parameter.
        self.aliyun_uid = aliyun_uid
        # The database name when the database type is **PostgreSQL**, **PolarDB for PostgreSQL**, or **AnalyticDB PostgreSQL**. The authentication database name when the database type is **MongoDB**.
        # 
        # > This parameter is available and required only when the database type is **PostgreSQL**, **PolarDB for PostgreSQL**, **AnalyticDB PostgreSQL**, or **MongoDB**.
        self.database = database
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - **true**: Yes. After the dry run succeeds, the instance is not modified.
        # - **false** (default): No. After the dry run succeeds, the database instance of the DTS task is modified and the task runs.
        self.dry_run = dry_run
        # The ID of the DTS instance.
        # > If you do not specify this parameter, you must specify **DtsJobId**.
        self.dts_instance_id = dts_instance_id
        # The ID of the DTS task. You can call [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) to query the task ID.
        # 
        # > If you do not specify this parameter, you must specify **DtsInstanceId**.
        self.dts_job_id = dts_job_id
        # The database instance to be modified. Valid values:
        # 
        # - **src**: source instance.
        # - **dest**: destination instance.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The ID of the database instance.
        self.endpoint_instance_id = endpoint_instance_id
        # The type of the database instance. Valid values:
        # 
        # - **rds**: ApsaraDB RDS for MySQL or ApsaraDB RDS for PostgreSQL.
        # - **polardb**: PolarDB for MySQL or PolarDB for PostgreSQL.
        # - **mongodb**: when used as the source, ApsaraDB for MongoDB (replica set architecture). When used as the destination, ApsaraDB for MongoDB (replica set or sharded cluster architecture).
        # - **distributed_mongodb**: supported only as the source of a distributed instance. Indicates ApsaraDB for MongoDB (sharded cluster architecture).
        # 
        # > The incremental node of a distributed instance must obtain data changes from the source through Oplog.
        # 
        # - **greenplum**: cloud-native data warehouse AnalyticDB for PostgreSQL.
        # - **kafka**: ApsaraMQ for Kafka.
        # - **ecs**: self-managed database on an ECS instance (only supported database types).
        # - **express**: database connected over Express Connect (only supported database types).
        # - **other**: database connected over the Internet (only supported database types).
        # 
        # > - Currently supported database types include **MySQL**, **PolarDB for MySQL**, **PostgreSQL**, **PolarDB for PostgreSQL**, **MongoDB**, **Kafka**, and **AnalyticDB PostgreSQL**.
        # - If the database is MongoDB (sharded cluster), the number of shards in the new database must be the same as that in the original MongoDB (sharded cluster).
        # - If the source instance is to be modified and the database type is **PostgreSQL**, make sure that the latency of the DTS instance is less than 30 seconds and stop writing data to the source. Otherwise, inconsistent data may occur.
        # - The parameter values are case-insensitive.
        # 
        # This parameter is required.
        self.endpoint_instance_type = endpoint_instance_type
        # The IP address of the database instance.
        self.endpoint_ip = endpoint_ip
        # The port of the database instance.
        self.endpoint_port = endpoint_port
        # The primary vSwitch for Express Connect access.
        self.endpoint_primary_vsw_id = endpoint_primary_vsw_id
        # The region to which the database instance belongs.
        self.endpoint_region_id = endpoint_region_id
        # The secondary vSwitch for Express Connect access.
        self.endpoint_secondary_vsw_id = endpoint_secondary_vsw_id
        # The VPC ID for Express Connect access.
        self.endpoint_vpc_id = endpoint_vpc_id
        # Specifies whether to modify the account and password. Valid values:
        # 
        # - **true**: Yes.
        # - **false** (default): No.
        self.modify_account = modify_account
        # The database password.
        # 
        # > This parameter takes effect only when **ModifyAccount** is set to **true**.
        self.password = password
        # The region to which the DTS instance belongs.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The name of the RAM role for cross-account access.
        # 
        # > Specify this parameter when performing cross-account data synchronization. For the required permissions and authorization method of this role, see [Configure RAM authorization for cross-account data migration or synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.role_name = role_name
        # The password of the shard in the MongoDB sharded cluster instance.
        # 
        # > - This parameter is available and required only when the source database instance is ApsaraDB for MongoDB (sharded cluster architecture).
        # - This parameter takes effect only when **ModifyAccount** is set to **true**.
        self.shard_password = shard_password
        # The account of the shard in the MongoDB sharded cluster instance.
        # 
        # > - This parameter is available and required only when the source database instance is ApsaraDB for MongoDB (sharded cluster architecture).
        # - This parameter takes effect only when **ModifyAccount** is set to **true**.
        self.shard_username = shard_username
        # The synchronization direction. Valid values:
        # 
        # - **Forward** (default): forward.
        # - **Reverse**: reverse.
        self.synchronization_direction = synchronization_direction
        # The database account.
        # 
        # > This parameter takes effect only when **ModifyAccount** is set to **true**.
        self.username = username
        # Specifies whether this is a seamless integration (zero-ETL) node. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.database is not None:
            result['Database'] = self.database

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.endpoint_instance_id is not None:
            result['EndpointInstanceId'] = self.endpoint_instance_id

        if self.endpoint_instance_type is not None:
            result['EndpointInstanceType'] = self.endpoint_instance_type

        if self.endpoint_ip is not None:
            result['EndpointIp'] = self.endpoint_ip

        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port

        if self.endpoint_primary_vsw_id is not None:
            result['EndpointPrimaryVswId'] = self.endpoint_primary_vsw_id

        if self.endpoint_region_id is not None:
            result['EndpointRegionId'] = self.endpoint_region_id

        if self.endpoint_secondary_vsw_id is not None:
            result['EndpointSecondaryVswId'] = self.endpoint_secondary_vsw_id

        if self.endpoint_vpc_id is not None:
            result['EndpointVpcId'] = self.endpoint_vpc_id

        if self.modify_account is not None:
            result['ModifyAccount'] = self.modify_account

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.shard_password is not None:
            result['ShardPassword'] = self.shard_password

        if self.shard_username is not None:
            result['ShardUsername'] = self.shard_username

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        if self.username is not None:
            result['Username'] = self.username

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EndpointInstanceId') is not None:
            self.endpoint_instance_id = m.get('EndpointInstanceId')

        if m.get('EndpointInstanceType') is not None:
            self.endpoint_instance_type = m.get('EndpointInstanceType')

        if m.get('EndpointIp') is not None:
            self.endpoint_ip = m.get('EndpointIp')

        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')

        if m.get('EndpointPrimaryVswId') is not None:
            self.endpoint_primary_vsw_id = m.get('EndpointPrimaryVswId')

        if m.get('EndpointRegionId') is not None:
            self.endpoint_region_id = m.get('EndpointRegionId')

        if m.get('EndpointSecondaryVswId') is not None:
            self.endpoint_secondary_vsw_id = m.get('EndpointSecondaryVswId')

        if m.get('EndpointVpcId') is not None:
            self.endpoint_vpc_id = m.get('EndpointVpcId')

        if m.get('ModifyAccount') is not None:
            self.modify_account = m.get('ModifyAccount')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('ShardPassword') is not None:
            self.shard_password = m.get('ShardPassword')

        if m.get('ShardUsername') is not None:
            self.shard_username = m.get('ShardUsername')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

