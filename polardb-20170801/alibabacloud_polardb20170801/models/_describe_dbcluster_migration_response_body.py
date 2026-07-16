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
        # The comments on the migration exception. If no exception occurs during the migration, an empty value is returned.
        self.comment = comment
        # The details of the PolarDB endpoints.
        self.dbcluster_endpoint_list = dbcluster_endpoint_list
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The read/write mode of the cluster. Valid values:
        # 
        # - **rw**: Read and write.
        # 
        # - **ro**: Read-only.
        self.dbcluster_read_write_mode = dbcluster_read_write_mode
        # The replication delay between the ApsaraDB RDS instance and the PolarDB cluster, in seconds.
        self.delayed_seconds = delayed_seconds
        # The ID of the sync task.
        self.dts_instance_id = dts_instance_id
        # The time when the replication relationship between the ApsaraDB RDS instance and the PolarDB cluster expires. The time is in the `YYYY-MM-DDThh:mm:ssZ` format and is displayed in UTC.
        self.expired_time = expired_time
        # The migration status of the PolarDB cluster. Valid values:
        # 
        # - **NO_MIGRATION**: No migration task is created.
        # 
        # - **RDS2POLARDB_CLONING**: Data is being cloned.
        # 
        # - **RDS2POLARDB_SYNCING**: Data is being synchronized. In this state, the PolarDB cluster is read-only, and the ApsaraDB RDS instance is read-write.
        # 
        # - **SWITCHING**: The database is being switched.
        # 
        # - **POLARDB2RDS_SYNCING**: The database switch is complete. In this state, the PolarDB cluster is read-write, and the ApsaraDB RDS instance is read-only. Change the endpoints in your application.
        # 
        # - **ROLLBACK**: The migration is being rolled back. After the rollback is complete, the migration status changes to **RDS2POLARDB_SYNCING**.
        # 
        # - **CLOSING_MIGRATION**: The migration task is being shut down.
        self.migration_status = migration_status
        # The details of the ApsaraDB RDS endpoints.
        self.rds_endpoint_list = rds_endpoint_list
        # The read/write mode of the source ApsaraDB RDS instance. Valid values:
        # 
        # - **rw**: Read and write.
        # 
        # - **ro**: Read-only.
        self.rds_read_write_mode = rds_read_write_mode
        # The request ID.
        self.request_id = request_id
        # The ID of the source ApsaraDB RDS instance.
        self.source_rdsdbinstance_id = source_rdsdbinstance_id
        # The type of the source database. Valid values:
        # 
        # - **PolarDBMySQL**: The source database for a major version upgrade of a PolarDB cluster.
        # 
        # - **RDS**: The source database for migrating data from an ApsaraDB RDS instance to a PolarDB for MySQL cluster.
        self.src_db_type = src_db_type
        # The data synchronization relationship. Valid values:
        # 
        # - **RDS2POLARDB**: Data is synchronized from the ApsaraDB RDS instance to the PolarDB cluster.
        # 
        # - **POLARDB2RDS**: Data is synchronized from the PolarDB cluster to the ApsaraDB RDS instance.
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
        # The details of the connection strings.
        self.address_items = address_items
        # The instance type.
        self.custins_type = custins_type
        # The endpoint ID.
        self.dbendpoint_id = dbendpoint_id
        # The type of the endpoint. Valid values:
        # 
        # - **Normal**: A regular endpoint.
        # 
        # - **ReadWriteSplitting**: A read/write splitting endpoint.
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
        # The connection string.
        self.connection_string = connection_string
        # The IP address.
        self.ipaddress = ipaddress
        # The network type of the endpoint. Valid values:
        # 
        # - **Public**: An endpoint for the Internet.
        # 
        # - **Private**: A private endpoint.
        # 
        # - **Inner**: A private endpoint in a classic network.
        self.net_type = net_type
        # The port.
        self.port = port
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **Enabled**: SSL encryption is enabled.
        # 
        # - **Disabled**: SSL encryption is disabled.
        self.sslenabled = sslenabled
        # The ID of the VPC.
        self.vpcid = vpcid
        # The ID of the vSwitch.
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
        # The details of the connection strings.
        self.address_items = address_items
        # The endpoint ID.
        self.dbendpoint_id = dbendpoint_id
        # The type of the endpoint. Valid values:
        # 
        # - **Cluster**: The default cluster endpoint.
        # 
        # - **Primary**: The primary endpoint.
        # 
        # - **Custom**: A custom cluster endpoint.
        self.endpoint_type = endpoint_type
        # The read/write mode. Valid values:
        # 
        # - ReadWrite: Read and write (automatic read/write splitting).
        # 
        # - ReadOnly (Default): Read-only.
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
        # The connection string.
        self.connection_string = connection_string
        # The IP address.
        self.ipaddress = ipaddress
        # The network type of the endpoint. Valid values:
        # 
        # - **Public**: An endpoint for the Internet.
        # 
        # - **Private**: A private endpoint.
        # 
        # - **Inner**: A private endpoint in a classic network.
        self.net_type = net_type
        # The port.
        self.port = port
        # Indicates whether Secure Sockets Layer (SSL) encryption is enabled. Valid values:
        # 
        # - **Enabled**: SSL encryption is enabled.
        # 
        # - **Disabled**: SSL encryption is disabled.
        self.sslenabled = sslenabled
        # The ID of the virtual private cloud (VPC).
        self.vpcid = vpcid
        # The ID of the virtual switch.
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

