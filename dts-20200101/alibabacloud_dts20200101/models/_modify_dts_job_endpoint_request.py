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
        endpoint_region_id: str = None,
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
        # The ID of the Alibaba Cloud account (primary account) to which the database instance belongs.
        # >  Passing this parameter indicates that cross-Alibaba Cloud account data synchronization will be performed, and you also need to pass the **RoleName** parameter.
        self.aliyun_uid = aliyun_uid
        # When the database type is **PostgreSQL**, **PolarDB for PostgreSQL**, or **AnalyticDB PostgreSQL**, it represents the database name; when the database type is **MongoDB**, it represents the authentication database name.
        # > This parameter is only available and must be provided when the database type is **PostgreSQL**, **PolarDB for PostgreSQL**, **AnalyticDB PostgreSQL**, or **MongoDB**.
        self.database = database
        # Specifies whether to perform only a precheck. Valid values:
        # 
        # *   **true**: Yes. After the precheck is passed, the database is not changed.
        # *   **false** (default): No. After the precheck is passed, the system changes the original database of the DTS task and runs the task.
        self.dry_run = dry_run
        # The ID of the DTS instance. If this parameter is not provided, **DtsJobId** must be specified.
        self.dts_instance_id = dts_instance_id
        # DTS job ID, which can be queried by calling [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html).
        # > If this parameter is not provided, **DtsInstanceId** must be filled in.
        self.dts_job_id = dts_job_id
        # The database instance to be modified, with values:
        # - **src**: Source database instance. - **dest**: Target database instance.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # ID of the database instance.
        self.endpoint_instance_id = endpoint_instance_id
        # The type of the database. Valid values:
        # 
        # *   **rds**: ApsaraDB RDS for MySQL instance, ApsaraDB RDS for SQL Server instance, or ApsaraDB RDS for PostgreSQL instance.
        # *   **polardb**: PolarDB for MySQL cluster or PolarDB for PostgreSQL cluster.
        # *   **mongodb**: ApsaraDB for MongoDB replica set instance.
        # *   **distributed_mongodb**: ApsaraDB for MongoDB sharded cluster instance.
        # *   **greenplum**: AnalyticDB for PostgreSQL instance.
        # *   **kafka**: ApsaraMQ for Kafka instance.
        # *   **ecs**: self-managed database that is hosted on an Elastic Compute Service (ECS) instance. If you set this parameter to ecs, the database must be the supported one.
        # *   **express**: database that is connected over Express Connect. If you set this parameter to express, the database must be the supported one.
        # *   **other**: database that is connected over Internet. If you set this parameter to other, the database must be the supported one.
        # 
        # > 
        # 
        # *   The following types of databases are supported: **MySQL**, **PolarDB for MySQL**, **PostgreSQL**, **PolarDB for PostgreSQL**, **MongoDB**, **SQL Server**, **Kafka**, and **AnalyticDB for PostgreSQL**.
        # 
        # *   If the original database is an ApsaraDB for MongoDB sharded cluster instance, the new database must have the same number of shards as the original database.
        # *   If the database that you want to change is a source **PostgreSQL** database, you must make sure that the latency of the DTS instance is less than 30 seconds and no data is written to the source database during the change. Otherwise, data inconsistency may occur.
        # *   The value of this parameter is case-insensitive.
        # 
        # This parameter is required.
        self.endpoint_instance_type = endpoint_instance_type
        # The IP of the database instance.
        self.endpoint_ip = endpoint_ip
        # port of the database instance.
        self.endpoint_port = endpoint_port
        # The ID of the region in which the database resides.
        self.endpoint_region_id = endpoint_region_id
        # Specifies whether to change the password of the database account. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.modify_account = modify_account
        # The password of the database account.
        # 
        # >  This parameter is valid only if **ModifyAccount** is set to **true**.
        self.password = password
        # The ID of the region in which the DTS instance resides.
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Cross Alibaba Cloud account role name. When performing data synchronization across Alibaba Cloud accounts, this parameter must be passed. For the required permissions and authorization methods for this role, please refer to [How to Configure RAM Authorization for Cross-Account Data Migration or Synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.role_name = role_name
        # The account password of the shard of the ApsaraDB for MongoDB sharded cluster instance.
        # 
        # > 
        # 
        # *   This parameter is valid and required only if the source database is an ApsaraDB for MongoDB sharded cluster instance.
        # 
        # *   This parameter is valid only if **ModifyAccount** is set to **true**.
        self.shard_password = shard_password
        # The account username of the shard of the ApsaraDB for MongoDB sharded cluster instance.
        # 
        # > 
        # 
        # *   This parameter is valid and required only if the source database is an ApsaraDB for MongoDB sharded cluster instance.
        # 
        # *   This parameter is valid only if **ModifyAccount** is set to **true**.
        self.shard_username = shard_username
        # Synchronization direction, with values:
        # - **Forward** (default): Forward. - **Reverse**: Reverse.
        self.synchronization_direction = synchronization_direction
        # The database account.
        # 
        # >  This parameter is valid only if **ModifyAccount** is set to **true**.
        self.username = username
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

        if self.endpoint_region_id is not None:
            result['EndpointRegionId'] = self.endpoint_region_id

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

        if m.get('EndpointRegionId') is not None:
            self.endpoint_region_id = m.get('EndpointRegionId')

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

