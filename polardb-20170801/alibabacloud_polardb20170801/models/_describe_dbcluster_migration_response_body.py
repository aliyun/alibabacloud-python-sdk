# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterMigrationResponseBody(DaraModel):
    def __init__(
        self,
        comment: str = None,
        dbcluster_endpoint_list: List[main_models.DescribeDBClusterMigrationResponseBodyDBClusterEndpointList] = None,
        dbcluster_id: str = None,
        dbcluster_read_write_mode: str = None,
        delayed_seconds: int = None,
        dts_instance_id: str = None,
        expired_time: str = None,
        migration_status: str = None,
        rds_endpoint_list: List[main_models.DescribeDBClusterMigrationResponseBodyRdsEndpointList] = None,
        rds_read_write_mode: str = None,
        request_id: str = None,
        source_rdsdbinstance_id: str = None,
        src_db_type: str = None,
        topologies: str = None,
    ):
        # The mode of the source ApsaraDB RDS instance. Valid values:
        # 
        # *   **rw**: read and write mode
        # *   **ro**: read-only mode
        self.comment = comment
        # The port number.
        self.dbcluster_endpoint_list = dbcluster_endpoint_list
        # The replication latency between the ApsaraDB RDS instance and the PolarDB cluster. Unit: seconds.
        self.dbcluster_id = dbcluster_id
        # Details about the endpoints.
        self.dbcluster_read_write_mode = dbcluster_read_write_mode
        # The vSwitch ID.
        self.delayed_seconds = delayed_seconds
        # The network type of the endpoint. Valid values:
        # 
        # *   **Public**: the public endpoint
        # *   **Private**: the internal endpoint (VPC)
        # *   **Inner**: the internal endpoint (classic network)
        self.dts_instance_id = dts_instance_id
        # The mode of the PolarDB cluster. Valid values:
        # 
        # *   **rw**: read and write mode
        # *   **ro**: read-only mode
        self.expired_time = expired_time
        # The endpoint.
        self.migration_status = migration_status
        # The endpoints of the ApsaraDB RDS instance.
        self.rds_endpoint_list = rds_endpoint_list
        # The ID of the synchronous task.
        self.rds_read_write_mode = rds_read_write_mode
        # The ID of the source ApsaraDB RDS instance.
        self.request_id = request_id
        # The endpoints of the ApsaraDB RDS instance.
        self.source_rdsdbinstance_id = source_rdsdbinstance_id
        # The type of the source database. Valid values:
        # 
        # - **PolarDBMySQL**: The source database is a PolarDB for MySQL database when the major version of your PolarDB cluster is upgraded.
        # - **RDS**: The source database is an ApsaraDB RDS database when data is migrated from ApsaraDB RDS to PolarDB for MySQL.
        self.src_db_type = src_db_type
        # The migration state of the PolarDB cluster. Valid values:
        # 
        # *   **NO_MIGRATION**: No migration task is running.
        # *   **RDS2POLARDB_CLONING**: Data is being replicated.
        # *   **RDS2POLARDB_SYNCING**: Data is being replicated. During the replication, the PolarDB cluster is running in read-only mode and the source ApsaraDB RDS instance is running in read and write mode.
        # *   **SWITCHING**: Databases are being switched.
        # *   **POLARDB2RDS_SYNCING**: Databases are switched. The PolarDB cluster is running in read and write mode and the source ApsaraDB RDS instance is running in read-only mode. In this state, you can modify the endpoints for your applications.
        # *   **ROLLBACK**: The migration is being rolled back. After the rollback is complete, the value **RDS2POLARDB_SYNCING** is returned.
        # *   **CLOSING_MIGRATION**: The migration task is being terminated.
        self.topologies = topologies

    def validate(self):
        if self.dbcluster_endpoint_list:
            for v1 in self.dbcluster_endpoint_list:
                 if v1:
                    v1.validate()
        if self.rds_endpoint_list:
            for v1 in self.rds_endpoint_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        result['DBClusterEndpointList'] = []
        if self.dbcluster_endpoint_list is not None:
            for k1 in self.dbcluster_endpoint_list:
                result['DBClusterEndpointList'].append(k1.to_map() if k1 else None)

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_read_write_mode is not None:
            result['DBClusterReadWriteMode'] = self.dbcluster_read_write_mode

        if self.delayed_seconds is not None:
            result['DelayedSeconds'] = self.delayed_seconds

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.migration_status is not None:
            result['MigrationStatus'] = self.migration_status

        result['RdsEndpointList'] = []
        if self.rds_endpoint_list is not None:
            for k1 in self.rds_endpoint_list:
                result['RdsEndpointList'].append(k1.to_map() if k1 else None)

        if self.rds_read_write_mode is not None:
            result['RdsReadWriteMode'] = self.rds_read_write_mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_rdsdbinstance_id is not None:
            result['SourceRDSDBInstanceId'] = self.source_rdsdbinstance_id

        if self.src_db_type is not None:
            result['SrcDbType'] = self.src_db_type

        if self.topologies is not None:
            result['Topologies'] = self.topologies

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        self.dbcluster_endpoint_list = []
        if m.get('DBClusterEndpointList') is not None:
            for k1 in m.get('DBClusterEndpointList'):
                temp_model = main_models.DescribeDBClusterMigrationResponseBodyDBClusterEndpointList()
                self.dbcluster_endpoint_list.append(temp_model.from_map(k1))

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterReadWriteMode') is not None:
            self.dbcluster_read_write_mode = m.get('DBClusterReadWriteMode')

        if m.get('DelayedSeconds') is not None:
            self.delayed_seconds = m.get('DelayedSeconds')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('MigrationStatus') is not None:
            self.migration_status = m.get('MigrationStatus')

        self.rds_endpoint_list = []
        if m.get('RdsEndpointList') is not None:
            for k1 in m.get('RdsEndpointList'):
                temp_model = main_models.DescribeDBClusterMigrationResponseBodyRdsEndpointList()
                self.rds_endpoint_list.append(temp_model.from_map(k1))

        if m.get('RdsReadWriteMode') is not None:
            self.rds_read_write_mode = m.get('RdsReadWriteMode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceRDSDBInstanceId') is not None:
            self.source_rdsdbinstance_id = m.get('SourceRDSDBInstanceId')

        if m.get('SrcDbType') is not None:
            self.src_db_type = m.get('SrcDbType')

        if m.get('Topologies') is not None:
            self.topologies = m.get('Topologies')

        return self

class DescribeDBClusterMigrationResponseBodyRdsEndpointList(DaraModel):
    def __init__(
        self,
        address_items: List[main_models.DescribeDBClusterMigrationResponseBodyRdsEndpointListAddressItems] = None,
        custins_type: str = None,
        dbendpoint_id: str = None,
        endpoint_type: str = None,
    ):
        # The VPC ID.
        self.address_items = address_items
        # The instance type.
        self.custins_type = custins_type
        # The ID of the endpoint.
        self.dbendpoint_id = dbendpoint_id
        # The type of the endpoint. Valid values:
        # 
        # - **Normal**: the standard endpoint
        # - **ReadWriteSplitting**: the read/write splitting endpoint
        self.endpoint_type = endpoint_type

    def validate(self):
        if self.address_items:
            for v1 in self.address_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddressItems'] = []
        if self.address_items is not None:
            for k1 in self.address_items:
                result['AddressItems'].append(k1.to_map() if k1 else None)

        if self.custins_type is not None:
            result['CustinsType'] = self.custins_type

        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_items = []
        if m.get('AddressItems') is not None:
            for k1 in m.get('AddressItems'):
                temp_model = main_models.DescribeDBClusterMigrationResponseBodyRdsEndpointListAddressItems()
                self.address_items.append(temp_model.from_map(k1))

        if m.get('CustinsType') is not None:
            self.custins_type = m.get('CustinsType')

        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        return self

class DescribeDBClusterMigrationResponseBodyRdsEndpointListAddressItems(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        ipaddress: str = None,
        net_type: str = None,
        port: str = None,
        sslenabled: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.connection_string = connection_string
        # The type of the source database. Valid values:
        # 
        # *   **PolarDBMySQL**: The source database is a PolarDB for MySQL database when the major version of your PolarDB cluster is upgraded.
        # *   **RDS**: The source database is an ApsaraDB RDS database when data is migrated from ApsaraDB RDS to PolarDB for MySQL.
        self.ipaddress = ipaddress
        # The ID of the endpoint.
        self.net_type = net_type
        # The type of the endpoint. Valid values:
        # 
        # *   **Normal**: the standard endpoint
        # *   **ReadWriteSplitting**: the read/write splitting endpoint
        self.port = port
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **Enabled**
        # - **Disabled**
        self.sslenabled = sslenabled
        # The instance type.
        self.vpcid = vpcid
        # The IP address of the endpoint.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeDBClusterMigrationResponseBodyDBClusterEndpointList(DaraModel):
    def __init__(
        self,
        address_items: List[main_models.DescribeDBClusterMigrationResponseBodyDBClusterEndpointListAddressItems] = None,
        dbendpoint_id: str = None,
        endpoint_type: str = None,
        read_write_mode: str = None,
    ):
        # The VPC ID.
        self.address_items = address_items
        # The expiration time of the replication between ApsaraDB RDS and PolarDB. The time is in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        self.dbendpoint_id = dbendpoint_id
        # The ID of the cluster.
        self.endpoint_type = endpoint_type
        # The synchronization direction. Valid values:
        # 
        # *   **RDS2POLARDB**: Data is replicated from an ApsaraDB RDS instance to a PolarDB cluster.
        # *   **POLARDB2RDS**: Data is replicated from a PolarDB cluster to an ApsaraDB RDS instance.
        self.read_write_mode = read_write_mode

    def validate(self):
        if self.address_items:
            for v1 in self.address_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddressItems'] = []
        if self.address_items is not None:
            for k1 in self.address_items:
                result['AddressItems'].append(k1.to_map() if k1 else None)

        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.read_write_mode is not None:
            result['ReadWriteMode'] = self.read_write_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_items = []
        if m.get('AddressItems') is not None:
            for k1 in m.get('AddressItems'):
                temp_model = main_models.DescribeDBClusterMigrationResponseBodyDBClusterEndpointListAddressItems()
                self.address_items.append(temp_model.from_map(k1))

        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('ReadWriteMode') is not None:
            self.read_write_mode = m.get('ReadWriteMode')

        return self

class DescribeDBClusterMigrationResponseBodyDBClusterEndpointListAddressItems(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        ipaddress: str = None,
        net_type: str = None,
        port: str = None,
        sslenabled: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.connection_string = connection_string
        # The description of a migration exception. If no exception occurs during the migration, an empty string is returned.
        self.ipaddress = ipaddress
        # The ID of the endpoint.
        self.net_type = net_type
        # The type of the endpoint. Valid values:
        # 
        # *   **Cluster**: the default cluster endpoint
        # *   **Primary**: the primary endpoint
        # *   **Custom**: the custom endpoint
        self.port = port
        # The ID of the request.
        self.sslenabled = sslenabled
        # The read/write mode. Valid values:
        # 
        # *   ReadWrite: receives and forwards read and write requests (automatic read-write splitting).
        # *   ReadOnly (default): receives and forwards read requests only.
        self.vpcid = vpcid
        # The IP address of the endpoint.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

