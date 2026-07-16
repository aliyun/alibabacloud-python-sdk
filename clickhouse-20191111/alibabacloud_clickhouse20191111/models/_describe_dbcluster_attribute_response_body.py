# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterAttributeResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster: main_models.DescribeDBClusterAttributeResponseBodyDBCluster = None,
        request_id: str = None,
    ):
        # Details about the cluster.
        self.dbcluster = dbcluster
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbcluster:
            self.dbcluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster is not None:
            result['DBCluster'] = self.dbcluster.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBCluster') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyDBCluster()
            self.dbcluster = temp_model.from_map(m.get('DBCluster'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterAttributeResponseBodyDBCluster(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        appointment_elect_zookeeper_disable_write: bool = None,
        appointment_elect_zookeeper_time: str = None,
        appointment_restart_node_list: str = None,
        appointment_restart_node_time: str = None,
        appointment_restart_time: str = None,
        available_upgrade_major_version: Dict[str, Any] = None,
        bid: str = None,
        category: str = None,
        commodity_code: str = None,
        connection_string: str = None,
        control_version: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_network_type: str = None,
        dbcluster_status: str = None,
        dbcluster_type: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dbnode_storage: int = None,
        encryption_key: str = None,
        encryption_type: str = None,
        engine: str = None,
        engine_latest_minor_version: str = None,
        engine_minor_version: str = None,
        engine_version: str = None,
        expire_time: str = None,
        ext_storage_size: int = None,
        ext_storage_type: str = None,
        is_expired: str = None,
        lb_kind: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        maintain_auto_type: bool = None,
        maintain_time: str = None,
        pay_type: str = None,
        port: int = None,
        public_connection_string: str = None,
        public_ip_addr: str = None,
        public_port: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        scale_out_status: main_models.DescribeDBClusterAttributeResponseBodyDBClusterScaleOutStatus = None,
        storage_type: str = None,
        support_backup: int = None,
        support_https_port: bool = None,
        support_mysql_port: bool = None,
        support_oss: int = None,
        tags: main_models.DescribeDBClusterAttributeResponseBodyDBClusterTags = None,
        v_switch_id: str = None,
        vpc_cloud_instance_id: str = None,
        vpc_id: str = None,
        vpc_ip_addr: str = None,
        web_uisnat_status: str = None,
        web_uistatus: str = None,
        zone_id: str = None,
        zone_id_vswitch_map: Dict[str, Any] = None,
        zookeeper_class: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # Specifies whether to stop write operations during a primary/secondary switchover. Valid values:
        # 
        # - `true`: Write operations are stopped for the instance during the switchover.
        # 
        # - `false`: Write operations are not stopped for the instance during the switchover.
        self.appointment_elect_zookeeper_disable_write = appointment_elect_zookeeper_disable_write
        # The scheduled time for a primary/secondary switchover. The time is in the `YYYY-MM-DDThh:mm:ssZ` format and is in UTC.
        self.appointment_elect_zookeeper_time = appointment_elect_zookeeper_time
        # A list of nodes that are scheduled for a restart.
        self.appointment_restart_node_list = appointment_restart_node_list
        # The scheduled time to restart specific nodes. The time is in the `YYYY-MM-DDThh:mm:ssZ` format and is in UTC.
        self.appointment_restart_node_time = appointment_restart_node_time
        # The scheduled restart time. The time is in the `YYYY-MM-DDThh:mm:ssZ` format and is in UTC.
        self.appointment_restart_time = appointment_restart_time
        # The available major versions to which the cluster can be upgraded, and their latest minor versions.
        self.available_upgrade_major_version = available_upgrade_major_version
        # The site ID. Valid values:
        # 
        # - `26842`: China site (aliyun.com).
        # 
        # - `26888`: international site (alibabacloud.com).
        self.bid = bid
        # The edition of the cluster. Valid values:
        # 
        # - `Basic`: single-replica edition.
        # 
        # - `HighAvailability`: dual-replica edition.
        self.category = category
        # The commodity code.
        self.commodity_code = commodity_code
        # The VPC endpoint.
        self.connection_string = connection_string
        # The version of the backend management system. Valid values:
        # 
        # - `v1`
        # 
        # - `v2`
        self.control_version = control_version
        # The creation time of the cluster, in `yyyy-MM-ddTHH:mm:ssZ` format (UTC).
        self.create_time = create_time
        # The cluster description.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The network type. Only VPC is supported.
        self.dbcluster_network_type = dbcluster_network_type
        # The cluster status. Valid values:
        # 
        # - `Preparing`: The cluster is being prepared.
        # 
        # - `Creating`: The cluster is being created.
        # 
        # - `Running`: The cluster is running.
        # 
        # - `Deleting`: The cluster is being deleted.
        # 
        # - `SCALING_OUT`: The cluster is being scaled out.
        self.dbcluster_status = dbcluster_status
        # The cluster type. Valid values:
        # 
        # - `Common`: a standard cluster.
        # 
        # - `Readonly`: a read-only cluster.
        # 
        # - `Guard`: a disaster recovery cluster.
        self.dbcluster_type = dbcluster_type
        # The instance type of the cluster nodes.
        # 
        # - Valid values for a single-replica edition:
        # 
        #   - `S4-NEW`
        # 
        #   - `S8`
        # 
        #   - `S16`
        # 
        #   - `S32`
        # 
        #   - `S64`
        # 
        #   - `S104`
        # 
        # - Valid values for a dual-replica edition:
        # 
        #   - `C4-NEW`
        # 
        #   - `C8`
        # 
        #   - `C16`
        # 
        #   - `C32`
        # 
        #   - `C64`
        # 
        #   - `C104`
        self.dbnode_class = dbnode_class
        # The number of nodes in the cluster.
        # 
        # - For a single-replica edition, the value range is 1 to 48.
        # 
        # - For a dual-replica edition, the value range is 1 to 24.
        self.dbnode_count = dbnode_count
        # The storage capacity per node, in GB.
        # 
        # The value can range from 100 to 32000.
        # 
        # > The value must be a multiple of 100.
        self.dbnode_storage = dbnode_storage
        # The Key Management Service (KMS) key ID.
        # 
        # > This parameter is empty if `EncryptionType` is set to `off`.
        self.encryption_key = encryption_key
        # The encryption type. Valid values:
        # 
        # - `CloudDisk`: disk encryption.
        # 
        # - `off`: Encryption is disabled.
        self.encryption_type = encryption_type
        # The database engine.
        self.engine = engine
        # The latest minor version to which the cluster can be upgraded.
        self.engine_latest_minor_version = engine_latest_minor_version
        # The engine\\"s current minor version.
        self.engine_minor_version = engine_minor_version
        # The engine version.
        self.engine_version = engine_version
        # The expiration time of the cluster, in `yyyy-MM-ddTHH:mm:ssZ` format (UTC).
        # 
        # > This parameter is empty for pay-as-you-go clusters.
        self.expire_time = expire_time
        # The extended storage capacity, in GB.
        self.ext_storage_size = ext_storage_size
        # The extended storage type. Valid values:
        # 
        # <props="china">
        # 
        # - `CloudESSD_PL0`: ESSD PL0 disk.
        # 
        # 
        # 
        # 
        # - `CloudESSD`: ESSD PL1 disk.
        # 
        # - `CloudESSD_PL2`: ESSD PL2 disk.
        # 
        # - `CloudESSD_PL3`: ESSD PL3 disk.
        # 
        # - `CloudEfficiency`: Ultra disk.
        self.ext_storage_type = ext_storage_type
        # Whether the cluster has expired. Valid values:
        # 
        # - `true`: The cluster has expired.
        # 
        # - `false`: The cluster has not expired.
        self.is_expired = is_expired
        # The type of the load balancer.
        self.lb_kind = lb_kind
        # The lock mode of the cluster. Valid values:
        # 
        # - `Unlock`: The cluster is not locked.
        # 
        # - `ManualLock`: The cluster is manually locked.
        # 
        # - `LockByExpiration`: The cluster is automatically locked upon expiration.
        # 
        # - `LockByRestoration`: The cluster is automatically locked before a rollback.
        # 
        # - `LockByDiskQuota`: The cluster is automatically locked because the storage is full.
        self.lock_mode = lock_mode
        # The reason the cluster was locked.
        # 
        # > This parameter is empty if `LockMode` is set to `Unlock`.
        self.lock_reason = lock_reason
        # The upgrade method. A value of `false` indicates that upgrades must be performed manually.
        self.maintain_auto_type = maintain_auto_type
        # The maintenance window of the cluster. The time is in the `HH:mmZ-HH:mmZ` format and is in UTC.
        # 
        # For example, `00:00Z-01:00Z` indicates that the maintenance window is from 00:00 to 01:00 (UTC), which corresponds to 08:00 to 09:00 in Beijing time (UTC+8).
        self.maintain_time = maintain_time
        # The billing method. Valid values:
        # 
        # - `Postpaid`: pay-as-you-go.
        # 
        # - `Prepaid`: subscription.
        self.pay_type = pay_type
        # The HTTP port.
        self.port = port
        # The public endpoint.
        self.public_connection_string = public_connection_string
        # The IP address of the public endpoint.
        self.public_ip_addr = public_ip_addr
        # The public TCP port.
        self.public_port = public_port
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The data migration status.
        self.scale_out_status = scale_out_status
        # The storage type. Valid values:
        # 
        # <props="china">
        # 
        # - `CloudESSD_PL0`: ESSD PL0 disk.
        # 
        # 
        # 
        # 
        # - `CloudESSD`: ESSD PL1 disk.
        # 
        # - `CloudESSD_PL2`: ESSD PL2 disk.
        # 
        # - `CloudESSD_PL3`: ESSD PL3 disk.
        # 
        # - `CloudEfficiency`: Ultra disk.
        self.storage_type = storage_type
        # Whether the cluster supports data backup. Valid values:
        # 
        # - `1`: Supported.
        # 
        # - `2`: Not supported.
        self.support_backup = support_backup
        # Whether the HTTPS port is supported. Valid values:
        # 
        # - `true`: Supported.
        # 
        # - `false`: Not supported.
        self.support_https_port = support_https_port
        # Whether the MySQL port is supported. Valid values:
        # 
        # - `true`: Supported.
        # 
        # - `false`: Not supported.
        self.support_mysql_port = support_mysql_port
        # Whether the cluster supports tiered storage for hot and cold data. Valid values:
        # 
        # - `1`: Supported.
        # 
        # - `2`: Not supported.
        self.support_oss = support_oss
        # The tags of the cluster.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The IP address of the VPC endpoint.
        self.vpc_ip_addr = vpc_ip_addr
        self.web_uisnat_status = web_uisnat_status
        self.web_uistatus = web_uistatus
        # The zone ID.
        self.zone_id = zone_id
        # A map of zone IDs to vSwitch IDs for a multi-zone cluster.
        self.zone_id_vswitch_map = zone_id_vswitch_map
        # The specifications of the ZooKeeper nodes.
        self.zookeeper_class = zookeeper_class

    def validate(self):
        if self.scale_out_status:
            self.scale_out_status.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.appointment_elect_zookeeper_disable_write is not None:
            result['AppointmentElectZookeeperDisableWrite'] = self.appointment_elect_zookeeper_disable_write

        if self.appointment_elect_zookeeper_time is not None:
            result['AppointmentElectZookeeperTime'] = self.appointment_elect_zookeeper_time

        if self.appointment_restart_node_list is not None:
            result['AppointmentRestartNodeList'] = self.appointment_restart_node_list

        if self.appointment_restart_node_time is not None:
            result['AppointmentRestartNodeTime'] = self.appointment_restart_node_time

        if self.appointment_restart_time is not None:
            result['AppointmentRestartTime'] = self.appointment_restart_time

        if self.available_upgrade_major_version is not None:
            result['AvailableUpgradeMajorVersion'] = self.available_upgrade_major_version

        if self.bid is not None:
            result['Bid'] = self.bid

        if self.category is not None:
            result['Category'] = self.category

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.control_version is not None:
            result['ControlVersion'] = self.control_version

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.dbcluster_type is not None:
            result['DBClusterType'] = self.dbcluster_type

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count

        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_latest_minor_version is not None:
            result['EngineLatestMinorVersion'] = self.engine_latest_minor_version

        if self.engine_minor_version is not None:
            result['EngineMinorVersion'] = self.engine_minor_version

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.ext_storage_size is not None:
            result['ExtStorageSize'] = self.ext_storage_size

        if self.ext_storage_type is not None:
            result['ExtStorageType'] = self.ext_storage_type

        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired

        if self.lb_kind is not None:
            result['LbKind'] = self.lb_kind

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.maintain_auto_type is not None:
            result['MaintainAutoType'] = self.maintain_auto_type

        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port is not None:
            result['Port'] = self.port

        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string

        if self.public_ip_addr is not None:
            result['PublicIpAddr'] = self.public_ip_addr

        if self.public_port is not None:
            result['PublicPort'] = self.public_port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scale_out_status is not None:
            result['ScaleOutStatus'] = self.scale_out_status.to_map()

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.support_backup is not None:
            result['SupportBackup'] = self.support_backup

        if self.support_https_port is not None:
            result['SupportHttpsPort'] = self.support_https_port

        if self.support_mysql_port is not None:
            result['SupportMysqlPort'] = self.support_mysql_port

        if self.support_oss is not None:
            result['SupportOss'] = self.support_oss

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_ip_addr is not None:
            result['VpcIpAddr'] = self.vpc_ip_addr

        if self.web_uisnat_status is not None:
            result['WebUISnatStatus'] = self.web_uisnat_status

        if self.web_uistatus is not None:
            result['WebUIStatus'] = self.web_uistatus

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_id_vswitch_map is not None:
            result['ZoneIdVswitchMap'] = self.zone_id_vswitch_map

        if self.zookeeper_class is not None:
            result['ZookeeperClass'] = self.zookeeper_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AppointmentElectZookeeperDisableWrite') is not None:
            self.appointment_elect_zookeeper_disable_write = m.get('AppointmentElectZookeeperDisableWrite')

        if m.get('AppointmentElectZookeeperTime') is not None:
            self.appointment_elect_zookeeper_time = m.get('AppointmentElectZookeeperTime')

        if m.get('AppointmentRestartNodeList') is not None:
            self.appointment_restart_node_list = m.get('AppointmentRestartNodeList')

        if m.get('AppointmentRestartNodeTime') is not None:
            self.appointment_restart_node_time = m.get('AppointmentRestartNodeTime')

        if m.get('AppointmentRestartTime') is not None:
            self.appointment_restart_time = m.get('AppointmentRestartTime')

        if m.get('AvailableUpgradeMajorVersion') is not None:
            self.available_upgrade_major_version = m.get('AvailableUpgradeMajorVersion')

        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ControlVersion') is not None:
            self.control_version = m.get('ControlVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('DBClusterType') is not None:
            self.dbcluster_type = m.get('DBClusterType')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')

        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineLatestMinorVersion') is not None:
            self.engine_latest_minor_version = m.get('EngineLatestMinorVersion')

        if m.get('EngineMinorVersion') is not None:
            self.engine_minor_version = m.get('EngineMinorVersion')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExtStorageSize') is not None:
            self.ext_storage_size = m.get('ExtStorageSize')

        if m.get('ExtStorageType') is not None:
            self.ext_storage_type = m.get('ExtStorageType')

        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')

        if m.get('LbKind') is not None:
            self.lb_kind = m.get('LbKind')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaintainAutoType') is not None:
            self.maintain_auto_type = m.get('MaintainAutoType')

        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')

        if m.get('PublicIpAddr') is not None:
            self.public_ip_addr = m.get('PublicIpAddr')

        if m.get('PublicPort') is not None:
            self.public_port = m.get('PublicPort')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScaleOutStatus') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyDBClusterScaleOutStatus()
            self.scale_out_status = temp_model.from_map(m.get('ScaleOutStatus'))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('SupportBackup') is not None:
            self.support_backup = m.get('SupportBackup')

        if m.get('SupportHttpsPort') is not None:
            self.support_https_port = m.get('SupportHttpsPort')

        if m.get('SupportMysqlPort') is not None:
            self.support_mysql_port = m.get('SupportMysqlPort')

        if m.get('SupportOss') is not None:
            self.support_oss = m.get('SupportOss')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDBClusterAttributeResponseBodyDBClusterTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcIpAddr') is not None:
            self.vpc_ip_addr = m.get('VpcIpAddr')

        if m.get('WebUISnatStatus') is not None:
            self.web_uisnat_status = m.get('WebUISnatStatus')

        if m.get('WebUIStatus') is not None:
            self.web_uistatus = m.get('WebUIStatus')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIdVswitchMap') is not None:
            self.zone_id_vswitch_map = m.get('ZoneIdVswitchMap')

        if m.get('ZookeeperClass') is not None:
            self.zookeeper_class = m.get('ZookeeperClass')

        return self

class DescribeDBClusterAttributeResponseBodyDBClusterTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDBClusterAttributeResponseBodyDBClusterTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDBClusterAttributeResponseBodyDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterAttributeResponseBodyDBClusterTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeDBClusterAttributeResponseBodyDBClusterScaleOutStatus(DaraModel):
    def __init__(
        self,
        progress: str = None,
        ratio: str = None,
    ):
        # The data migration progress, as a percentage.
        # 
        # > This parameter is returned only when the cluster is in the `SCALING_OUT` state.
        self.progress = progress
        # The data migration progress, displayed as `Amount of data migrated/Total data amount`.
        # 
        # > This parameter is returned only when the cluster is in the `SCALING_OUT` state.
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.progress is not None:
            result['Progress'] = self.progress

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        return self

