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
        # The information about the cluster.
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
        zone_id: str = None,
        zone_id_vswitch_map: Dict[str, Any] = None,
        zookeeper_class: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        self.appointment_elect_zookeeper_disable_write = appointment_elect_zookeeper_disable_write
        self.appointment_elect_zookeeper_time = appointment_elect_zookeeper_time
        self.appointment_restart_node_list = appointment_restart_node_list
        self.appointment_restart_node_time = appointment_restart_node_time
        # The scheduled restart time. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in Coordinated Universal Time (UTC).
        self.appointment_restart_time = appointment_restart_time
        # The major engine versions available for upgrades.
        self.available_upgrade_major_version = available_upgrade_major_version
        # The site ID. Valid values:
        # 
        # *   **26842**: the China site (aliyun.com)
        # *   **26888**: the international site (alibabacloud.com)
        self.bid = bid
        # The edition of the cluster. Valid values:
        # 
        # *   **Basic**: Single-replica Edition
        # *   **HighAvailability**: Double-replica Edition
        self.category = category
        # The commodity code of the cluster.
        self.commodity_code = commodity_code
        # The VPC endpoint of the cluster.
        self.connection_string = connection_string
        # The version of the ApsaraDB for ClickHouse console that is used to manage the cluster. Valid values:
        # 
        # *   **v1**
        # *   **v2**
        self.control_version = control_version
        # The time when the cluster was created. The value is in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the cluster.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The network type of the cluster. Only VPC is supported.
        self.dbcluster_network_type = dbcluster_network_type
        # The cluster state. Valid values:
        # 
        # *   **Preparing**: The cluster is being prepared.
        # *   **Creating**: The cluster is being created.
        # *   **Running**: The cluster is running.
        # *   **Deleting**: The cluster is being deleted.
        # *   **SCALING_OUT**: The storage capacity of the cluster is being expanded.
        self.dbcluster_status = dbcluster_status
        # The type of the cluster. Valid values:
        # 
        # *   **Common**: a common cluster
        # *   **Readonly**: a read-only cluster
        # *   **Guard**: a disaster recovery cluster
        self.dbcluster_type = dbcluster_type
        # The specifications of the cluster.
        # 
        # *   Valid values when the cluster is of Single-replica Edition:
        # 
        #     *   **S4-NEW**
        #     *   **S8**
        #     *   **S16**
        #     *   **S32**
        #     *   **S64**
        #     *   **S104**
        # 
        # *   Valid values when the cluster is of Double-replica Edition:
        # 
        #     *   **C4-NEW**
        #     *   **C8**
        #     *   **C16**
        #     *   **C32**
        #     *   **C64**
        #     *   **C104**
        self.dbnode_class = dbnode_class
        # The number of nodes.
        # 
        # *   Valid values when the cluster is of Single-replica Edition: 1 to 48.
        # *   Valid values when the cluster is of Double-replica Edition: 1 to 24.
        self.dbnode_count = dbnode_count
        # The storage capacity of a single node of the cluster. Unit: GB.
        # 
        # Valid values: 100 to 32000.
        # 
        # >  This value is a multiple of 100.
        self.dbnode_storage = dbnode_storage
        # The Key Management Service (KMS) key that is used to encrypt data.
        # 
        # >  If the value of the EncryptionType parameter is off, an empty string is returned for this parameter.
        self.encryption_key = encryption_key
        # The encryption type. Valid values:
        # 
        # *   **CloudDisk**: Disk encryption is enabled.
        # *   **off**: Data is not encrypted.
        self.encryption_type = encryption_type
        # The type of the database engine.
        self.engine = engine
        # The latest minor version to which the cluster can be updated.
        self.engine_latest_minor_version = engine_latest_minor_version
        # The current minor version.
        self.engine_minor_version = engine_minor_version
        # The engine version.
        self.engine_version = engine_version
        # The time when the cluster expired. The time is in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # >  Pay-as-you-go clusters never expire. If the cluster is a pay-as-you-go cluster, an empty string is returned for this parameter.
        self.expire_time = expire_time
        # The extended storage space. Unit: GB.
        self.ext_storage_size = ext_storage_size
        # The extended storage type. Valid values:
        # 
        # *   **CloudESSD**: The cluster uses an enhanced SSD (ESSD) of performance level (PL) 1.
        # *   **CloudESSD_PL2**: The cluster uses an ESSD of PL 2.
        # *   **CloudESSD_PL3**: The cluster uses an ESSD of PL 3.
        # *   **CloudEfficiency**: The cluster uses an ultra disk.
        self.ext_storage_type = ext_storage_type
        # Indicates whether the cluster has expired. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_expired = is_expired
        self.lb_kind = lb_kind
        # The lock mode of the cluster. Valid values:
        # 
        # *   **Unlock**: The cluster is not locked.
        # *   **ManualLock**: The cluster is manually locked.
        # *   **LockByExpiration**: The cluster is automatically locked due to cluster expiration.
        # *   **LockByRestoration**: The cluster is automatically locked because the cluster is about to be rolled back.
        # *   **LockByDiskQuota**: The cluster is automatically locked because the disk space is exhausted.
        self.lock_mode = lock_mode
        # The cause why the cluster was locked.
        # 
        # >  If the value of the LockMode parameter is Unlock, an empty string is returned for this parameter.
        self.lock_reason = lock_reason
        # The update type. If the value of the parameter is **false**, it indicates a manual update.
        self.maintain_auto_type = maintain_auto_type
        # The maintenance window of the cluster. The value is in the HH:mmZ-HH:mmZ format. The time is displayed in UTC.
        # 
        # For example, if you set the maintenance window to 00:00Z-01:00Z, the cluster can be maintained from 08:00 (UTC+8) to 09:00 (UTC+8).
        self.maintain_time = maintain_time
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: indicates the pay-as-you-go billing method.
        # *   **Prepaid**: indicates the subscription billing method.
        self.pay_type = pay_type
        # The HTTP port number.
        self.port = port
        # The public endpoint.
        self.public_connection_string = public_connection_string
        # The IP address that is used to connect to the cluster over the Internet.
        self.public_ip_addr = public_ip_addr
        # The TCP port number in the public endpoint.
        self.public_port = public_port
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the data migration task.
        self.scale_out_status = scale_out_status
        # The storage type of the cluster. Valid values:
        # 
        # *   **CloudESSD**: The cluster uses an enhanced SSD (ESSD) of performance level (PL) 1.
        # *   **CloudESSD_PL2**: The cluster uses an ESSD of PL 2.
        # *   **CloudESSD_PL3**: The cluster uses an ESSD of PL 3.
        # *   **CloudEfficiency**: The cluster uses an ultra disk.
        self.storage_type = storage_type
        # Indicates whether data backup is supported. Valid values:
        # 
        # *   **1**: Data backup is supported.
        # *   **2**: Data backup is not supported.
        self.support_backup = support_backup
        # Indicates whether HTTPS ports are supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.support_https_port = support_https_port
        # Indicates whether the cluster supports a MySQL port. Valid values:
        # 
        # *   **true**: A MySQL port is supported.
        # *   **false**: A MySQL port is not supported.
        self.support_mysql_port = support_mysql_port
        # Indicates whether tiered storage of hot data and cold data is supported. Valid values:
        # 
        # *   **1**: Tiered storage of hot data and cold data is supported.
        # *   **2**: Tiered storage of hot data and cold data is not supported.
        self.support_oss = support_oss
        # The tags.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the VPC in which the cluster is deployed.
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The IP address that is used to connect to the cluster over the VPC.
        self.vpc_ip_addr = vpc_ip_addr
        # The zone ID.
        self.zone_id = zone_id
        # The list of vSwitch IDs in multi-zone clusters.
        self.zone_id_vswitch_map = zone_id_vswitch_map
        # The ZooKeeper specifications.
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
        # The tag name.
        self.key = key
        # The tag value.
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
        # The progress of the data migration task in percentage.
        # 
        # >  This parameter is returned only when the cluster is in the SCALING_OUT state.
        self.progress = progress
        # The progress of the data migration task. This value is displayed in the following format: Data volume that has been migrated/Total data volume.
        # 
        # >  This parameter is returned only when the cluster is in the SCALING_OUT state.
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

