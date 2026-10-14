# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalDatabaseNetworkResponseBody(DaraModel):
    def __init__(
        self,
        connections: List[main_models.DescribeGlobalDatabaseNetworkResponseBodyConnections] = None,
        create_time: str = None,
        dbcluster_id: str = None,
        dbclusters: List[main_models.DescribeGlobalDatabaseNetworkResponseBodyDBClusters] = None,
        dbtype: str = None,
        dbversion: str = None,
        gdndescription: str = None,
        gdnid: str = None,
        gdnstatus: str = None,
        global_domain_name: str = None,
        labels: main_models.DescribeGlobalDatabaseNetworkResponseBodyLabels = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The connection information.
        self.connections = connections
        # The time when the GDN was created.
        # 
        # The time is in the ISO 8601 format in UTC (format: YYYY-MM-DDTHH:mm:ssZ).
        self.create_time = create_time
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The clusters in the GDN.
        self.dbclusters = dbclusters
        # The database engine type. Currently, only MySQL is supported.
        self.dbtype = dbtype
        # The database engine version. Currently, only version 8.0 is supported.
        self.dbversion = dbversion
        # The description of the GDN. The description must meet the following requirements:
        # 
        # - It cannot start with http:// or https://.
        # 
        # - It must start with an uppercase letter, a lowercase letter, or a Chinese character.
        # 
        # - It can contain uppercase letters, lowercase letters, Chinese characters, digits, underscores (_), or hyphens (-).
        # 
        # - It must be 2 to 126 characters in length.
        self.gdndescription = gdndescription
        # GDN ID。
        self.gdnid = gdnid
        # The status of the GDN. Valid values:
        # 
        # - **creating**: Being created.
        # 
        # - **active**: Running.
        # 
        # - **deleting**: Being deleted.
        # 
        # - **locked**: Locked. No operations can be performed on any cluster in the GDN.
        # 
        # - **removing_member**: A cluster is being removed from the GDN.
        self.gdnstatus = gdnstatus
        # The global domain name.
        self.global_domain_name = global_domain_name
        # The property labels.
        self.labels = labels
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.connections:
            for v1 in self.connections:
                 if v1:
                    v1.validate()
        if self.dbclusters:
            for v1 in self.dbclusters:
                 if v1:
                    v1.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Connections'] = []
        if self.connections is not None:
            for k1 in self.connections:
                result['Connections'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['DBClusters'] = []
        if self.dbclusters is not None:
            for k1 in self.dbclusters:
                result['DBClusters'].append(k1.to_map() if k1 else None)

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.gdndescription is not None:
            result['GDNDescription'] = self.gdndescription

        if self.gdnid is not None:
            result['GDNId'] = self.gdnid

        if self.gdnstatus is not None:
            result['GDNStatus'] = self.gdnstatus

        if self.global_domain_name is not None:
            result['GlobalDomainName'] = self.global_domain_name

        if self.labels is not None:
            result['Labels'] = self.labels.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k1 in m.get('Connections'):
                temp_model = main_models.DescribeGlobalDatabaseNetworkResponseBodyConnections()
                self.connections.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.dbclusters = []
        if m.get('DBClusters') is not None:
            for k1 in m.get('DBClusters'):
                temp_model = main_models.DescribeGlobalDatabaseNetworkResponseBodyDBClusters()
                self.dbclusters.append(temp_model.from_map(k1))

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('GDNDescription') is not None:
            self.gdndescription = m.get('GDNDescription')

        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')

        if m.get('GDNStatus') is not None:
            self.gdnstatus = m.get('GDNStatus')

        if m.get('GlobalDomainName') is not None:
            self.global_domain_name = m.get('GlobalDomainName')

        if m.get('Labels') is not None:
            temp_model = main_models.DescribeGlobalDatabaseNetworkResponseBodyLabels()
            self.labels = temp_model.from_map(m.get('Labels'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class DescribeGlobalDatabaseNetworkResponseBodyLabels(DaraModel):
    def __init__(
        self,
        gdnversion: str = None,
    ):
        # The GDN version.
        self.gdnversion = gdnversion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gdnversion is not None:
            result['GDNVersion'] = self.gdnversion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GDNVersion') is not None:
            self.gdnversion = m.get('GDNVersion')

        return self

class DescribeGlobalDatabaseNetworkResponseBodyDBClusters(DaraModel):
    def __init__(
        self,
        category: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        dbnode_class: str = None,
        dbnodes: List[main_models.DescribeGlobalDatabaseNetworkResponseBodyDBClustersDBNodes] = None,
        dbtype: str = None,
        dbversion: str = None,
        expire_time: str = None,
        expired: str = None,
        pay_type: str = None,
        region_id: str = None,
        replica_lag: str = None,
        role: str = None,
        serverless_type: str = None,
        storage_used: str = None,
    ):
        # The edition of the product. Valid values:
        # 
        # Normal: Cluster Edition
        # Basic: Single Node Edition
        # Archive: PolarDB X-Engine Edition
        # NormalMultimaster: Multi-master Cluster Edition
        # SENormal: PolarDB for MySQL Standard Edition
        # 
        # >- PolarDB for PostgreSQL 11 does not support Single Node Edition.
        # >- PolarDB for MySQL 8.0, PolarDB for MySQL 5.7, and PolarDB for PostgreSQL 14 support PolarDB for MySQL Standard Edition.
        # >- PolarDB for MySQL 8.0 supports PolarDB X-Engine Edition and Multi-master Cluster Edition.
        self.category = category
        # The cluster description.
        self.dbcluster_description = dbcluster_description
        # The cluster ID in the GDN.
        self.dbcluster_id = dbcluster_id
        # The status of the cluster in the GDN. For more information, see [Cluster status table](https://help.aliyun.com/document_detail/99286.html).
        self.dbcluster_status = dbcluster_status
        # The node specifications of the database node.
        self.dbnode_class = dbnode_class
        # The details of the database nodes.
        self.dbnodes = dbnodes
        # The database engine type. Currently, only MySQL is supported.
        self.dbtype = dbtype
        # The database engine version. Currently, only version 8.0 is supported.
        self.dbversion = dbversion
        # The expiration time of the cluster.
        # 
        # > This parameter is returned only for clusters whose billing method is **Prepaid** (subscription). An empty value is returned for **Postpaid** (pay-as-you-go) clusters.
        # 
        # The time is in the ISO 8601 format in UTC (format: YYYY-MM-DDTHH:mm:ssZ).
        self.expire_time = expire_time
        # Indicates whether the cluster has expired. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        # 
        # > This parameter is returned only for clusters whose billing method is **Prepaid** (subscription).
        self.expired = expired
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # 
        # - **Prepaid**: subscription.
        self.pay_type = pay_type
        # The region ID.
        self.region_id = region_id
        # The cross-region replication delay between the primary and secondary clusters. Unit: seconds.
        self.replica_lag = replica_lag
        # The role of the cluster. Valid values:
        # 
        # - **primary**: primary cluster
        # 
        # - **standby**: secondary cluster
        # 
        # > A GDN contains one primary cluster and up to four secondary clusters.
        self.role = role
        # The serverless type. The value is fixed as AgileServerless.
        # > This parameter is supported only for serverless clusters.
        self.serverless_type = serverless_type
        # The storage usage. Unit: bytes.
        self.storage_used = storage_used

    def validate(self):
        if self.dbnodes:
            for v1 in self.dbnodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k1 in self.dbnodes:
                result['DBNodes'].append(k1.to_map() if k1 else None)

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_lag is not None:
            result['ReplicaLag'] = self.replica_lag

        if self.role is not None:
            result['Role'] = self.role

        if self.serverless_type is not None:
            result['ServerlessType'] = self.serverless_type

        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k1 in m.get('DBNodes'):
                temp_model = main_models.DescribeGlobalDatabaseNetworkResponseBodyDBClustersDBNodes()
                self.dbnodes.append(temp_model.from_map(k1))

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaLag') is not None:
            self.replica_lag = m.get('ReplicaLag')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('ServerlessType') is not None:
            self.serverless_type = m.get('ServerlessType')

        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')

        return self

class DescribeGlobalDatabaseNetworkResponseBodyDBClustersDBNodes(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        dbnode_class: str = None,
        dbnode_id: str = None,
        dbnode_role: str = None,
        dbnode_status: str = None,
        failover_priority: int = None,
        max_connections: int = None,
        max_iops: int = None,
        zone_id: str = None,
    ):
        # The time when the database node was created.
        # 
        # The time is in the ISO 8601 format in UTC (format: YYYY-MM-DDTHH:mm:ssZ).
        self.creation_time = creation_time
        # The node specifications of the database node.
        self.dbnode_class = dbnode_class
        # The database node ID.
        self.dbnode_id = dbnode_id
        # The role of the database node. Valid values:
        # 
        # - **Writer**: primary node
        # 
        # - **Reader**: read-only node
        self.dbnode_role = dbnode_role
        # The status of the node. Valid values:
        # 
        # - **Creating**: Being created.
        # 
        # - **Running**: Running.
        # 
        # - **Deleting**: Being deleted.
        # 
        # - **Rebooting**: Being restarted.
        # 
        # - **ClassChanging**: The node specifications are being changed.
        # 
        # - **NetAddressCreating**: Network connectivity is being created.
        # 
        # - **NetAddressDeleting**: Network connectivity is being deleted.
        # 
        # - **NetAddressModifying**: Network connectivity is being modified.
        # 
        # - **MinorVersionUpgrading**: A minor engine version upgrade is in progress.
        # 
        # - **Maintaining**: The cluster is under maintenance.
        # 
        # - **Switching**: A failover is in progress.
        self.dbnode_status = dbnode_status
        # The failover priority. Each node has a failover priority that determines the likelihood of the node being elected as the primary node during a failover. A higher value indicates a higher priority. Valid values: 1 to 15.
        self.failover_priority = failover_priority
        # The maximum number of concurrent connections to the cluster.
        self.max_connections = max_connections
        # The maximum number of I/O requests per second (IOPS).
        self.max_iops = max_iops
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.dbnode_role is not None:
            result['DBNodeRole'] = self.dbnode_role

        if self.dbnode_status is not None:
            result['DBNodeStatus'] = self.dbnode_status

        if self.failover_priority is not None:
            result['FailoverPriority'] = self.failover_priority

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('DBNodeRole') is not None:
            self.dbnode_role = m.get('DBNodeRole')

        if m.get('DBNodeStatus') is not None:
            self.dbnode_status = m.get('DBNodeStatus')

        if m.get('FailoverPriority') is not None:
            self.failover_priority = m.get('FailoverPriority')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeGlobalDatabaseNetworkResponseBodyConnections(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        net_type: str = None,
        port: str = None,
    ):
        # The connection string.
        self.connection_string = connection_string
        # The network type.
        self.net_type = net_type
        # The port number of the connection string.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

