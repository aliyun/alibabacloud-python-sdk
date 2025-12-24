# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLindormInstanceResponseBody(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arch_version: str = None,
        archive_storage: int = None,
        auto_renew: bool = None,
        cold_storage: int = None,
        core_disk_category: str = None,
        core_num: int = None,
        core_single_storage: int = None,
        core_spec: str = None,
        create_milliseconds: int = None,
        create_time: str = None,
        deletion_protection: str = None,
        disk_category: str = None,
        disk_threshold: str = None,
        disk_usage: str = None,
        enable_blob: bool = None,
        enable_cdc: bool = None,
        enable_compute: bool = None,
        enable_kms: bool = None,
        enable_lproxy: bool = None,
        enable_lts: bool = None,
        enable_lsql_version_v3: bool = None,
        enable_mlctrl: bool = None,
        enable_ssl: bool = None,
        enable_shs: bool = None,
        enable_store_tde: bool = None,
        enable_stream: bool = None,
        engine_list: List[main_models.GetLindormInstanceResponseBodyEngineList] = None,
        engine_type: int = None,
        expire_time: str = None,
        expired_milliseconds: int = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_storage: str = None,
        log_disk_category: str = None,
        log_num: int = None,
        log_single_storage: int = None,
        log_spec: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        multi_zone_combination: str = None,
        network_type: str = None,
        pay_type: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        service_type: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # 16-digit AliUid of the Alibaba Cloud primary account (main account).
        self.ali_uid = ali_uid
        # Multi-AZ instance, coordinating Availability Zone virtual switch ID, which must be located in the Availability Zone corresponding to ArbiterZoneId.
        self.arbiter_vswitch_id = arbiter_vswitch_id
        # Multi-zone instance, coordinating Availability Zone ID.
        self.arbiter_zone_id = arbiter_zone_id
        # The architecture of the instance. Valid values:
        # 
        # *   **1.0**: The instance is deployed in a single zone.
        # *   **2.0**: The instance is deployed across multiple zones.
        self.arch_version = arch_version
        # The Archive storage size of the instance.
        self.archive_storage = archive_storage
        # Indicates whether auto-renewal is enabled, with the following returns:
        # - **true**: Enabled. 
        # - **false**: Disabled.
        # > This parameter is returned when the instance\\"s payment type is prepaid.
        self.auto_renew = auto_renew
        # The Capacity storage size of the instance.
        self.cold_storage = cold_storage
        # The disk type of the core nodes. This parameter is returned only for multi-zone instances. Valid values:
        # 
        # *   **cloud_efficiency**: This instance uses the Standard type of storage.
        # *   **cloud_ssd**: This instance uses the Performance type of storage.
        # *   **cloud_essd**: This instance uses ESSDs for storage.
        # *   **cloud_essd_pl0**: This instance uses PL0 ESSDs for storage.
        self.core_disk_category = core_disk_category
        # Multi-zone instance, number of core nodes.
        self.core_num = core_num
        # Multi-zone instance, core single-node disk capacity.
        self.core_single_storage = core_single_storage
        # Multi-zone instance, core node specification.
        self.core_spec = core_spec
        # The timestamp in milliseconds between the instance creation time and 1970-01-01 00:00:00.
        self.create_milliseconds = create_milliseconds
        # The storage capacity of the disk of a single log node. This parameter is returned only for multi-zone instances.
        self.create_time = create_time
        # Indicates whether deletion protection is enabled, returning:
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.deletion_protection = deletion_protection
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_efficiency**: This instance uses the Standard type of storage.
        # *   **cloud_ssd**: This instance uses the Performance type of storage.
        # *   **cloud_essd**: This instance uses ESSDs for storage.
        # *   **cloud_essd_pl0**: This instance uses PL0 ESSDs for storage.
        # *   **capacity_cloud_storage**: This instance uses the Capacity type of storage.
        # *   **local_ssd_pro**: This instance uses local SSDs for storage.
        # *   **local_hdd_pro**: This instance uses local HDDs for storage.
        self.disk_category = disk_category
        # The threshold for disk space.
        self.disk_threshold = disk_threshold
        # Disk space usage rate.
        self.disk_usage = disk_usage
        # Indicates whether LBlob is enabled for the instance. Valid values:
        # 
        # true: LBlob is enabled for the instance. false: LBlob is not enabled for the instance.
        self.enable_blob = enable_blob
        # Indicates whether the data subscription feature for the instance is enabled. Returns:
        # - **true**: Enabled. 
        # - **false**: Not enabled.
        self.enable_cdc = enable_cdc
        # Indicates whether the instance\\"s compute engine is enabled, returning:
        # - **true**: Enabled. 
        # - **false**: Not enabled.
        self.enable_compute = enable_compute
        # Indicates whether the Key Management Service (KMS) is enabled, returning:
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.enable_kms = enable_kms
        # Indicates whether LindormTable supports the Thrift and CQL protocols. If these protocols are not supported. You can call the SwitchLProxyService operation to enable or disable the support on these protocols for LindormTable.
        # 
        # True: LindormTable supports the Thrift and CQL protocols.
        # 
        # False: LindormTable does not support the Thrift and CQL protocols.
        self.enable_lproxy = enable_lproxy
        # Indicates whether the LTS engine is activated for the instance. Valid values:
        # 
        # *   **true**: The LTS engine is activated for the instance.
        # *   **false**: The LTS engine is not activated for the instance.
        self.enable_lts = enable_lts
        # Indicates whether LindormTable of the instance supports LindormSQL V3 that is compatible with MySQL. By default, LindormTable of instances that are purchased after October 24, 2023 supports LindormSQL V3. If your instance is purchased before this date and want to enable LindormSQL V3, contact the technical support.
        # 
        # *   True: LindormTable supports LindormSQL V3.
        # *   False: LindormTable does not support LindormSQL V3.
        self.enable_lsql_version_v3 = enable_lsql_version_v3
        # Indicates whether AI control nodes are enabled for the instance.
        # 
        # *   True: AI control nodes are enabled for the instance.
        # *   False: AI control nodes are not enabled for the instance.
        self.enable_mlctrl = enable_mlctrl
        # Indicates whether SSL link encryption is enabled, returning:
        # - **true**: Enabled. 
        # - **false**: Disabled.
        self.enable_ssl = enable_ssl
        # Whether to enable the Compute Engine History Server.
        self.enable_shs = enable_shs
        # Indicates whether the Transparent Data Encryption (TDE) is enabled, returning:
        # - **true**: Enabled. 
        # - **false**: Disabled.
        self.enable_store_tde = enable_store_tde
        # Indicates whether the instance has the stream engine enabled. Return values:
        # - **true**: Stream engine is enabled. 
        # - **false**: Stream engine is not enabled.
        self.enable_stream = enable_stream
        # The list of engines supported by the instance.
        self.engine_list = engine_list
        # Supported engine types, the return value is obtained by performing addition operations on the values of the following engine types.
        # - 1: Search Engine 
        # - 2: Time Series Engine
        # - 4: Wide Table Engine
        # - 8: File Engine
        # > For example: If EngineType is 15, where 15 = 8 + 4 + 2 + 1, it indicates that the instance supports Search Engine, Time Series Engine, Wide Table Engine, and File Engine. If EngineType is 6, where 6 = 4 + 2, it signifies that the instance supports Time Series Engine and Wide Table Engine.
        self.engine_type = engine_type
        # Expiration time of the instance, format: **yyyy-MM-dd HH:mm:ss**.
        # > This parameter is only returned when the payment type is pre-paid.
        self.expire_time = expire_time
        # The millisecond value between the instance expiration time and 1970-01-01 00:00:00.
        self.expired_milliseconds = expired_milliseconds
        # Instance name.
        self.instance_alias = instance_alias
        # Instance ID.
        self.instance_id = instance_id
        # The status of the instance. Valid values:
        # 
        # *   **CREATING**: The instance is being created.
        # *   **ACTIVATION**: The instance is running.
        # *   **COLD_EXPANDING**: The Capacity storage of the instance is being scaled up.
        # *   **MINOR_VERSION_TRANSING**: The minor version of the instance is being updated.
        # *   **RESIZING**: The nodes in the instance are being scaled up.
        # *   **SHRINKING**: The nodes in the instance are being scaled down.
        # *   **CLASS_CHANGING**: The specification of the instance is being changed.
        # *   **SSL_SWITCHING: SSL**: The SSL configurations of the instance are being changed.
        # *   **CDC_OPENING**: Data subscription is being enabled for the instance.
        # *   **TRANSFER**: The data of the instance is being transferred.
        # *   **DATABASE_TRANSFER**: The data of the instance is being transferred to databases.
        # *   **GUARD_CREATING**: A disaster recovery instance is being created.
        # *   **BACKUP_RECOVERING**: The data of the instance is being restored from a backup.
        # *   **DATABASE_IMPORTING**: Data is being imported to the instance.
        # *   **NET_MODIFYING**: The network configurations of the instance are being changed.
        # *   **NET_SWITCHING**: The network of the instance is being switched between a virtual private cloud (VPC) and the Internet.
        # *   **NET_CREATING**: The connection to the instance is being created.
        # *   **NET_DELETING**: The connection to the instance is being deleted.
        # *   **DELETING**: The instance is being deleted.
        # *   **RESTARTING**: The instance is restarting.
        # *   **LOCKED**: The instance is locked because it expires.
        self.instance_status = instance_status
        # Instance\\"s storage capacity.
        self.instance_storage = instance_storage
        # Multi-zone instance, log node disk type, returns:
        # - **cloud_efficiency**: Standard cloud storage. 
        # - **cloud_ssd**: Performance cloud storage.
        self.log_disk_category = log_disk_category
        # Multi-zone instance, number of log nodes.
        self.log_num = log_num
        # The storage capacity of the disk of a single log node. This parameter is returned only for multi-zone instances.
        self.log_single_storage = log_single_storage
        # Multi-zone instance, log node specification.
        self.log_spec = log_spec
        # Maintainable end time.
        self.maintain_end_time = maintain_end_time
        # Maintainable start time.
        self.maintain_start_time = maintain_start_time
        # Multi-zone combinations. For support details on zone combinations, please refer to the product page.
        # - **ap-southeast-5abc-aliyun**: Indonesia (Jakarta) A+B+C. 
        # - **cn-hangzhou-ehi-aliyun**: East China 1 (Hangzhou) E+H+I.
        # - **cn-beijing-acd-aliyun**: North China 2 (Beijing) A+C+D.
        # - **ap-southeast-1-abc-aliyun**: Singapore A+B+C.
        # - **cn-zhangjiakou-abc-aliyun**: North China 3 (Zhangjiakou) A+B+C.
        # - **cn-shanghai-efg-aliyun**: East China 2 (Shanghai) E+F+G.
        # - **cn-shanghai-abd-aliyun**: East China 2 (Shanghai) A+B+D.
        # - **cn-hangzhou-bef-aliyun**: East China 1 (Hangzhou) B+E+F.
        # - **cn-hangzhou-bce-aliyun**: East China 1 (Hangzhou) B+C+E.
        # - **cn-beijing-fgh-aliyun**: North China 2 (Beijing) F+G+H.
        # - **cn-shenzhen-abc-aliyun**: South China 1 (Shenzhen) A+B+C.
        self.multi_zone_combination = multi_zone_combination
        # Instance\\"s network type.
        self.network_type = network_type
        # The billing method of the instance. Valid values:
        # 
        # PREPAY: subscription.
        # POSTPAY: pay-as-you-go.
        self.pay_type = pay_type
        # Multi-zone instance, the virtual switch ID of the primary availability zone, which must be in the availability zone corresponding to PrimaryZoneId.
        self.primary_vswitch_id = primary_vswitch_id
        # Multi-zone instance, availability zone ID of the primary zone.
        self.primary_zone_id = primary_zone_id
        # Region ID.
        self.region_id = region_id
        # Request ID.
        self.request_id = request_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Instance type, valid values:
        # - **lindorm**: represents a Lindorm single-zone instance.
        # - **lindorm_multizone**: represents a Lindorm multi-zone instance.
        # - **serverless_lindorm**: represents a Lindorm Serverless instance.
        # - **lindorm_standalone**: represents a Lindorm standalone instance.
        # - **lts**: represents the Lindorm Data Channel Service type.
        self.service_type = service_type
        # Multi-zone instance, the virtual switch ID of the backup availability zone, which must be in the availability zone corresponding to StandbyZoneId.
        self.standby_vswitch_id = standby_vswitch_id
        # Multi-zone instance, backup availability zone\\"s availability zone ID.
        self.standby_zone_id = standby_zone_id
        # The type of the log nodes. This parameter is returned only for multi-zone instances.
        self.vpc_id = vpc_id
        # The number of the log nodes. This parameter is returned only for multi-zone instances.
        self.vswitch_id = vswitch_id
        # Availability Zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.engine_list:
            for v1 in self.engine_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id

        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id

        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version

        if self.archive_storage is not None:
            result['ArchiveStorage'] = self.archive_storage

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage

        if self.core_disk_category is not None:
            result['CoreDiskCategory'] = self.core_disk_category

        if self.core_num is not None:
            result['CoreNum'] = self.core_num

        if self.core_single_storage is not None:
            result['CoreSingleStorage'] = self.core_single_storage

        if self.core_spec is not None:
            result['CoreSpec'] = self.core_spec

        if self.create_milliseconds is not None:
            result['CreateMilliseconds'] = self.create_milliseconds

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_threshold is not None:
            result['DiskThreshold'] = self.disk_threshold

        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage

        if self.enable_blob is not None:
            result['EnableBlob'] = self.enable_blob

        if self.enable_cdc is not None:
            result['EnableCdc'] = self.enable_cdc

        if self.enable_compute is not None:
            result['EnableCompute'] = self.enable_compute

        if self.enable_kms is not None:
            result['EnableKms'] = self.enable_kms

        if self.enable_lproxy is not None:
            result['EnableLProxy'] = self.enable_lproxy

        if self.enable_lts is not None:
            result['EnableLTS'] = self.enable_lts

        if self.enable_lsql_version_v3 is not None:
            result['EnableLsqlVersionV3'] = self.enable_lsql_version_v3

        if self.enable_mlctrl is not None:
            result['EnableMLCtrl'] = self.enable_mlctrl

        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl

        if self.enable_shs is not None:
            result['EnableShs'] = self.enable_shs

        if self.enable_store_tde is not None:
            result['EnableStoreTDE'] = self.enable_store_tde

        if self.enable_stream is not None:
            result['EnableStream'] = self.enable_stream

        result['EngineList'] = []
        if self.engine_list is not None:
            for k1 in self.engine_list:
                result['EngineList'].append(k1.to_map() if k1 else None)

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired_milliseconds is not None:
            result['ExpiredMilliseconds'] = self.expired_milliseconds

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage

        if self.log_disk_category is not None:
            result['LogDiskCategory'] = self.log_disk_category

        if self.log_num is not None:
            result['LogNum'] = self.log_num

        if self.log_single_storage is not None:
            result['LogSingleStorage'] = self.log_single_storage

        if self.log_spec is not None:
            result['LogSpec'] = self.log_spec

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id

        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')

        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')

        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')

        if m.get('ArchiveStorage') is not None:
            self.archive_storage = m.get('ArchiveStorage')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')

        if m.get('CoreDiskCategory') is not None:
            self.core_disk_category = m.get('CoreDiskCategory')

        if m.get('CoreNum') is not None:
            self.core_num = m.get('CoreNum')

        if m.get('CoreSingleStorage') is not None:
            self.core_single_storage = m.get('CoreSingleStorage')

        if m.get('CoreSpec') is not None:
            self.core_spec = m.get('CoreSpec')

        if m.get('CreateMilliseconds') is not None:
            self.create_milliseconds = m.get('CreateMilliseconds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskThreshold') is not None:
            self.disk_threshold = m.get('DiskThreshold')

        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')

        if m.get('EnableBlob') is not None:
            self.enable_blob = m.get('EnableBlob')

        if m.get('EnableCdc') is not None:
            self.enable_cdc = m.get('EnableCdc')

        if m.get('EnableCompute') is not None:
            self.enable_compute = m.get('EnableCompute')

        if m.get('EnableKms') is not None:
            self.enable_kms = m.get('EnableKms')

        if m.get('EnableLProxy') is not None:
            self.enable_lproxy = m.get('EnableLProxy')

        if m.get('EnableLTS') is not None:
            self.enable_lts = m.get('EnableLTS')

        if m.get('EnableLsqlVersionV3') is not None:
            self.enable_lsql_version_v3 = m.get('EnableLsqlVersionV3')

        if m.get('EnableMLCtrl') is not None:
            self.enable_mlctrl = m.get('EnableMLCtrl')

        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')

        if m.get('EnableShs') is not None:
            self.enable_shs = m.get('EnableShs')

        if m.get('EnableStoreTDE') is not None:
            self.enable_store_tde = m.get('EnableStoreTDE')

        if m.get('EnableStream') is not None:
            self.enable_stream = m.get('EnableStream')

        self.engine_list = []
        if m.get('EngineList') is not None:
            for k1 in m.get('EngineList'):
                temp_model = main_models.GetLindormInstanceResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k1))

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpiredMilliseconds') is not None:
            self.expired_milliseconds = m.get('ExpiredMilliseconds')

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')

        if m.get('LogDiskCategory') is not None:
            self.log_disk_category = m.get('LogDiskCategory')

        if m.get('LogNum') is not None:
            self.log_num = m.get('LogNum')

        if m.get('LogSingleStorage') is not None:
            self.log_single_storage = m.get('LogSingleStorage')

        if m.get('LogSpec') is not None:
            self.log_spec = m.get('LogSpec')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')

        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetLindormInstanceResponseBodyEngineList(DaraModel):
    def __init__(
        self,
        arbiter_core_count: str = None,
        core_count: str = None,
        cpu_count: str = None,
        engine: str = None,
        is_last_version: bool = None,
        latest_version: str = None,
        memory_size: str = None,
        primary_core_count: str = None,
        specification: str = None,
        standby_core_count: str = None,
        version: str = None,
    ):
        self.arbiter_core_count = arbiter_core_count
        # The number of engine nodes.
        self.core_count = core_count
        # The number of CPU cores on the engine node.
        self.cpu_count = cpu_count
        # The engine type. Valid values:
        # 
        # *   **lindorm**: LindormTable.
        # *   **tsdb**: LindormTSDB.
        # *   **solr**: LindormSearch.
        # *   **store**: LindormDFS.
        # *   **bds**: Lindorm Tunnel Service (LTS).
        # *   **compute**: Lindorm Distributed Processing System (LDPS).
        self.engine = engine
        # Indicates whether the version of the engine is the latest. Valid values:
        # 
        # *   **true**: The version of the engine is the latest.
        # *   **false**: The version of the engine is not the latest.
        self.is_last_version = is_last_version
        # The latest version number of the engine.
        self.latest_version = latest_version
        # The memory size of the engine nodes.
        self.memory_size = memory_size
        self.primary_core_count = primary_core_count
        # The specification of the engine node.
        self.specification = specification
        self.standby_core_count = standby_core_count
        # The version of the engine.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arbiter_core_count is not None:
            result['ArbiterCoreCount'] = self.arbiter_core_count

        if self.core_count is not None:
            result['CoreCount'] = self.core_count

        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.is_last_version is not None:
            result['IsLastVersion'] = self.is_last_version

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.primary_core_count is not None:
            result['PrimaryCoreCount'] = self.primary_core_count

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.standby_core_count is not None:
            result['StandbyCoreCount'] = self.standby_core_count

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbiterCoreCount') is not None:
            self.arbiter_core_count = m.get('ArbiterCoreCount')

        if m.get('CoreCount') is not None:
            self.core_count = m.get('CoreCount')

        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('IsLastVersion') is not None:
            self.is_last_version = m.get('IsLastVersion')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('PrimaryCoreCount') is not None:
            self.primary_core_count = m.get('PrimaryCoreCount')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('StandbyCoreCount') is not None:
            self.standby_core_count = m.get('StandbyCoreCount')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

