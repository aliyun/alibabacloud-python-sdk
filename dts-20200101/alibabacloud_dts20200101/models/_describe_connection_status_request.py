# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConnectionStatusRequest(DaraModel):
    def __init__(
        self,
        destination_endpoint_architecture: str = None,
        destination_endpoint_database_name: str = None,
        destination_endpoint_engine_name: str = None,
        destination_endpoint_ip: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_password: str = None,
        destination_endpoint_port: str = None,
        destination_endpoint_region: str = None,
        destination_endpoint_user_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_endpoint_architecture: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_engine_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: str = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
    ):
        # This parameter is required only when **SourceEndpointEngineName** is set to **Oracle**. Valid values:
        # - **SID**: non-cluster architecture.
        # - **RAC**: Real Application Cluster architecture.
        # 
        # > The type of this parameter is String, and this parameter is optional.
        self.destination_endpoint_architecture = destination_endpoint_architecture
        # The name of the database to be migrated to or the name of the authentication database.
        # > - This parameter is available and required only when **DestinationEndpointEngineName** is set to **PostgreSQL**, **DRDS**, or **MongoDB**, or when **DestinationEndpointInstanceType** is set to **PolarDB_o**.
        # - When **DestinationEndpointEngineName** is set to **PostgreSQL** or **DRDS**, specify the name of the database to be migrated. When the value is **MongoDB**, specify the name of the authentication database for the database account.
        # - When **DestinationEndpointInstanceType** is set to **PolarDB_o**, specify the name of the database to be migrated.
        self.destination_endpoint_database_name = destination_endpoint_database_name
        # The database type of the destination database. Valid values: **MySQL**, **DRDS**, **SQLServer**, **PostgreSQL**, **PPAS**, **MongoDB**, and **Redis**.
        # > This parameter is available and required only when **DestinationEndpointInstanceType** is set to **RDS**, **DRDS**, **ECS**, **LocalInstance**, or **Express**.
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        # The endpoint of the destination database.
        # > This parameter is available and required only when **DestinationEndpointInstanceType** is set to **LocalInstance** or **Express**.
        self.destination_endpoint_ip = destination_endpoint_ip
        # The instance ID of the destination instance.
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        # The type of the destination instance. Valid values:
        # > - **ECS**: self-managed database hosted on an ECS instance.
        # - **LocalInstance**: self-managed database with a public IP address.
        # - **RDS**: ApsaraDB RDS instance.
        # - **DRDS**: PolarDB-X instance.
        # - **MongoDB**: ApsaraDB for MongoDB instance.
        # - **Redis**: ApsaraDB for Redis instance.
        # - **PetaData**: HybridDB for MySQL instance.
        # - **POLARDB**: PolarDB for MySQL cluster.
        # - **PolarDB_o**: PolarDB for PostgreSQL (Oracle-Compatible) cluster.
        # - **AnalyticDB**: AnalyticDB for MySQL V3.0 or V2.0.
        # - **Greenplum**: AnalyticDB for PostgreSQL.
        # 
        # This parameter is required.
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        # This parameter is required only when **DestinationEndpointEngineName** is set to **Oracle**. Valid values:
        # 
        # - **SID**: non-cluster architecture.
        # - **RAC**: Real Application Cluster architecture.
        # 
        # 
        # > The type of this parameter is String, and this parameter is optional.
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        # The password of the destination database account.
        self.destination_endpoint_password = destination_endpoint_password
        # The service port of the source database.
        # > This parameter is available and required only when **SourceEndpointInstanceType** is set to **ECS**, **LocalInstance**, or **Express**.
        self.destination_endpoint_port = destination_endpoint_port
        # The region in which the destination instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.destination_endpoint_region = destination_endpoint_region
        # The database account of the destination database.
        self.destination_endpoint_user_name = destination_endpoint_user_name
        # The region in which the DTS instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # This parameter is required only when **SourceEndpointEngineName** is set to **Oracle**. Valid values:
        # 
        # - **SID**: non-cluster architecture.
        # - **RAC**: Real Application Cluster architecture.
        # 
        # 
        # > This parameter is optional.
        self.source_endpoint_architecture = source_endpoint_architecture
        # The name of the database to be migrated or the name of the authentication database.
        # >- This parameter is available and required only when **SourceEndpointEngineName** is set to **PostgreSQL** or **MongoDB**, or when **SourceEndpointInstanceType** is set to **PolarDB_o**.
        # - When **SourceEndpointEngineName** is set to **PostgreSQL** or **DRDS**, specify the name of the database to be migrated. When the value is **MongoDB**, specify the name of the authentication database for the database account.
        # - When **SourceEndpointInstanceType** is set to **PolarDB_o**, specify the name of the database to be migrated.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The database engine type of the source instance. Valid values: **MySQL**, **TiDB**, **SQLServer**, **PostgreSQL**, **Oracle**, **MongoDB**, and **Redis**.
        # 
        # > Default value: **MySQL**.
        self.source_endpoint_engine_name = source_endpoint_engine_name
        # The endpoint of the source database.
        # > This parameter is available and required only when **SourceEndpointInstanceType** is set to **LocalInstance** or **Express**.
        self.source_endpoint_ip = source_endpoint_ip
        # The instance ID of the source instance.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The type of the source instance. Valid values:
        # - **RDS**: ApsaraDB RDS instance.
        # - **LocalInstance**: self-managed database with a public IP address.
        # - **ECS**: self-managed database hosted on an ECS instance.
        # - **Express**: self-managed database connected over Express Connect.
        # - **dg**: self-managed database connected over Database Gateway.
        # - **MongoDB**: ApsaraDB for MongoDB instance.
        # - **POLARDB**: PolarDB for MySQL cluster.
        # - **PolarDB_o**: PolarDB for PostgreSQL (Oracle-Compatible) cluster.
        # 
        # This parameter is required.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # The SID of the Oracle database.
        # > This parameter is available and required only when **SourceEndpointEngineName** is set to **Oracle** and the Oracle database is a non-RAC instance.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The password of the source database account.
        self.source_endpoint_password = source_endpoint_password
        # The service port of the source database.
        # > This parameter is available and required only when **SourceEndpointInstanceType** is set to **ECS**, **LocalInstance**, or **Express**.
        self.source_endpoint_port = source_endpoint_port
        # The region in which the source instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.source_endpoint_region = source_endpoint_region
        # The database account of the source database.
        self.source_endpoint_user_name = source_endpoint_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_endpoint_architecture is not None:
            result['DestinationEndpointArchitecture'] = self.destination_endpoint_architecture

        if self.destination_endpoint_database_name is not None:
            result['DestinationEndpointDatabaseName'] = self.destination_endpoint_database_name

        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_endpoint_architecture is not None:
            result['SourceEndpointArchitecture'] = self.source_endpoint_architecture

        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name

        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name

        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id

        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpointArchitecture') is not None:
            self.destination_endpoint_architecture = m.get('DestinationEndpointArchitecture')

        if m.get('DestinationEndpointDatabaseName') is not None:
            self.destination_endpoint_database_name = m.get('DestinationEndpointDatabaseName')

        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceEndpointArchitecture') is not None:
            self.source_endpoint_architecture = m.get('SourceEndpointArchitecture')

        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')

        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')

        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')

        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')

        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')

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

        return self

