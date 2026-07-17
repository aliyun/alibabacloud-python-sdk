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
        backup_instance: str = None,
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
        # The UID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The ID of the vSwitch in the arbiter zone for the multi-zone instance. The vSwitch must be deployed in the zone that is specified by `ArbiterZoneId`.
        self.arbiter_vswitch_id = arbiter_vswitch_id
        # The arbiter zone ID of the multi-zone instance.
        self.arbiter_zone_id = arbiter_zone_id
        # The deployment architecture. Valid values:
        # 
        # - **1.0**: single-zone deployment.
        # 
        # - **2.0**: multi-zone deployment.
        self.arch_version = arch_version
        # The billable storage capacity of the archive storage. Unit: GB.
        self.archive_storage = archive_storage
        # Indicates whether auto-renewal is enabled for the instance. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        # 
        # > This parameter is returned only for subscription instances.
        self.auto_renew = auto_renew
        # The ID of the backup instance.
        self.backup_instance = backup_instance
        # The capacity of the cold storage.
        self.cold_storage = cold_storage
        # The disk type of the core nodes in a multi-zone instance. Valid values:
        # 
        # - **cloud_efficiency**: Standard.
        # 
        # - **cloud_ssd**: Performance.
        # 
        # - **cloud_essd**: ESSD.
        # 
        # - **cloud_essd_pl0**: ESSD PL0.
        self.core_disk_category = core_disk_category
        # The number of core nodes in the multi-zone instance.
        self.core_num = core_num
        # The storage capacity of a single core node in the multi-zone instance.
        self.core_single_storage = core_single_storage
        # The specification of the core nodes in the multi-zone instance.
        self.core_spec = core_spec
        # The time at which the instance was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_milliseconds = create_milliseconds
        # The time at which the instance was created. The time is displayed in the **yyyy-MM-dd HH:mm:ss** format.
        self.create_time = create_time
        # Indicates whether release protection is enabled for the instance. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.deletion_protection = deletion_protection
        # The storage type. Valid values:
        # 
        # - **cloud_efficiency**: Standard.
        # 
        # - **cloud_ssd**: Performance.
        # 
        # - **cloud_essd**: Enhanced SSD (ESSD).
        # 
        # - **cloud_essd_pl0**: ESSD PL0.
        # 
        # - **capacity_cloud_storage**: Capacity.
        # 
        # - **local_ssd_pro**: local SSD.
        # 
        # - **local_hdd_pro**: local HDD.
        self.disk_category = disk_category
        # The disk space threshold.
        self.disk_threshold = disk_threshold
        # The disk usage.
        self.disk_usage = disk_usage
        # Indicates whether LBlob is enabled. Valid values:
        # 
        # true: Enabled. false: Disabled.
        self.enable_blob = enable_blob
        # Indicates whether Change Data Capture (CDC) is enabled for the instance. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.enable_cdc = enable_cdc
        # Indicates whether the compute engine is enabled for the instance. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.enable_compute = enable_compute
        # Indicates whether Key Management Service (KMS) is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.enable_kms = enable_kms
        # Specifies whether the wide table engine supports the Thrift and CQL protocols. If this feature is disabled, you can call the SwitchLProxyService operation to enable it.
        # 
        # true: Supported.
        # 
        # false: Not supported.
        self.enable_lproxy = enable_lproxy
        # Indicates whether the LTS engine is enabled for the instance. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.enable_lts = enable_lts
        # Indicates whether LindormSQL V3.0, which is compatible with the MySQL protocol, is supported by the wide table engine.
        # This feature is supported by default on instances created after October 24, 2023. For existing instances, contact technical support to enable this feature.
        # 
        # - true: Supported.
        # 
        # - false: Not supported.
        self.enable_lsql_version_v3 = enable_lsql_version_v3
        # Indicates whether the ML node is enabled. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        self.enable_mlctrl = enable_mlctrl
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.enable_ssl = enable_ssl
        # Indicates whether the History Server is enabled for the compute engine.
        self.enable_shs = enable_shs
        # Indicates whether Transparent Data Encryption (TDE) is enabled. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        self.enable_store_tde = enable_store_tde
        # Indicates whether the stream engine is enabled for the instance. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.enable_stream = enable_stream
        # The information about the engines.
        self.engine_list = engine_list
        # The types of the engines that are supported by the instance. The value of this parameter is the sum of the values of all supported engine types.
        # 
        # - 1: search engine
        # 
        # - 2: time series engine
        # 
        # - 4: wide table engine
        # 
        # - 8: file engine
        # 
        # > For example, if the value of this parameter is 15, it indicates that the instance supports the search, time series, wide table, and file engines because 1 + 2 + 4 + 8 = 15. If the value of this parameter is 6, it indicates that the instance supports the time series and wide table engines because 2 + 4 = 6.
        self.engine_type = engine_type
        # The expiration time of the instance. The time is displayed in the **yyyy-MM-dd HH:mm:ss** format.
        # 
        # > This parameter is returned only for subscription instances.
        self.expire_time = expire_time
        # The expiration time of the instance. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expired_milliseconds = expired_milliseconds
        # The name of the instance.
        self.instance_alias = instance_alias
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the instance. Valid values:
        # 
        # - **CREATING**: The instance is being created.
        # 
        # - **ACTIVATION**: The instance is running.
        # 
        # - **COLD_EXPANDING**: The capacity of the cold storage is being expanded.
        # 
        # - **MINOR_VERSION_TRANSITIONING**: The minor version of the instance is being changed.
        # 
        # - **RESIZING**: The number of nodes is being changed.
        # 
        # - **SHRINKING**: The number of nodes is being changed.
        # 
        # - **CLASS_CHANGING**: The specification of the instance is being changed.
        # 
        # - **SSL_SWITCHING**: SSL is being enabled or disabled.
        # 
        # - **CDC_OPENING**: The CDC feature is being enabled.
        # 
        # - **TRANSFER**: Data is being migrated.
        # 
        # - **DATABASE_TRANSFER**: Data is being migrated.
        # 
        # - **GUARD_CREATING**: A disaster recovery instance is being created.
        # 
        # - **BACKUP_RECOVERING**: Data is being restored from a backup.
        # 
        # - **DATABASE_IMPORTING**: Data is being imported.
        # 
        # - **NET_MODIFYING**: The network type is being changed.
        # 
        # - **NET_SWITCHING**: The network is being switched.
        # 
        # - **NET_CREATING**: A network connection is being created.
        # 
        # - **NET_DELETING**: A network connection is being deleted.
        # 
        # - **DELETING**: The instance is being deleted.
        # 
        # - **RESTARTING**: The instance is being restarted.
        # 
        # - **LOCKED**: The instance is locked.
        self.instance_status = instance_status
        # The storage capacity of the instance.
        self.instance_storage = instance_storage
        # The disk type of the log nodes in the multi-zone instance. Valid values:
        # 
        # - **cloud_efficiency**: Standard.
        # 
        # - **cloud_ssd**: Performance.
        self.log_disk_category = log_disk_category
        # The number of log nodes in the multi-zone instance.
        self.log_num = log_num
        # The storage capacity of a single log node in the multi-zone instance.
        self.log_single_storage = log_single_storage
        # The specification of the log nodes in the multi-zone instance.
        self.log_spec = log_spec
        # The end time of the maintenance window.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window.
        self.maintain_start_time = maintain_start_time
        # The combination of zones. For more information about the supported zone combinations, see the instance buy page.
        # 
        # - **ap-southeast-5abc-aliyun**: Indonesia (Jakarta) Zone A, B, and C.
        # 
        # - **cn-hangzhou-ehi-aliyun**: China (Hangzhou) Zone E, H, and I.
        # 
        # - **cn-beijing-acd-aliyun**: China (Beijing) Zone A, C, and D.
        # 
        # - **ap-southeast-1-abc-aliyun**: Singapore Zone A, B, and C.
        # 
        # - **cn-zhangjiakou-abc-aliyun**: China (Zhangjiakou) Zone A, B, and C.
        # 
        # - **cn-shanghai-efg-aliyun**: China (Shanghai) Zone E, F, and G.
        # 
        # - **cn-shanghai-abd-aliyun**: China (Shanghai) Zone A, B, and D.
        # 
        # - **cn-hangzhou-bef-aliyun**: China (Hangzhou) Zone B, E, and F.
        # 
        # - **cn-hangzhou-bce-aliyun**: China (Hangzhou) Zone B, C, and E.
        # 
        # - **cn-beijing-fgh-aliyun**: China (Beijing) Zone F, G, and H.
        # 
        # - **cn-shenzhen-abc-aliyun**: China (Shenzhen) Zone A, B, and C.
        self.multi_zone_combination = multi_zone_combination
        # The network type of the instance.
        self.network_type = network_type
        # The billing method of the instance. Valid values:
        # 
        # - **PREPAY**: subscription
        # 
        # - **POSTPAY**: pay-as-you-go
        self.pay_type = pay_type
        # The ID of the vSwitch in the primary zone for the multi-zone instance. The vSwitch must be deployed in the zone that is specified by `PrimaryZoneId`.
        self.primary_vswitch_id = primary_vswitch_id
        # The primary zone ID of the multi-zone instance.
        self.primary_zone_id = primary_zone_id
        # The ID of the region.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The type of the instance. Valid values:
        # 
        # - **lindorm**: a single-zone instance.
        # 
        # - **lindorm_multizone**: a multi-zone instance.
        # 
        # - **serverless_lindorm**: a serverless instance.
        # 
        # - **lindorm_standalone**: a single-node instance.
        # 
        # - **lts**: a Lindorm Tunnel Service (LTS) instance.
        self.service_type = service_type
        # The ID of the vSwitch in the secondary zone for the multi-zone instance. The vSwitch must be deployed in the zone that is specified by `StandbyZoneId`.
        self.standby_vswitch_id = standby_vswitch_id
        # The secondary zone ID of the multi-zone instance.
        self.standby_zone_id = standby_zone_id
        # The ID of the virtual private cloud (VPC) to which the instance belongs.
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        self.vswitch_id = vswitch_id
        # The ID of the zone.
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

        if self.backup_instance is not None:
            result['BackupInstance'] = self.backup_instance

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

        if m.get('BackupInstance') is not None:
            self.backup_instance = m.get('BackupInstance')

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
        # The number of nodes in the arbiter zone.
        self.arbiter_core_count = arbiter_core_count
        # The number of engine nodes.
        self.core_count = core_count
        # The number of vCPUs for the engine node.
        self.cpu_count = cpu_count
        # The type of the engine. Valid values:
        # 
        # - **lindorm**: the wide table engine.
        # 
        # - **tsdb**: the time series engine.
        # 
        # - **solr**: the search engine.
        # 
        # - **store**: the file engine.
        # 
        # - **bds**: the LTS engine.
        # 
        # - **compute**: the compute engine.
        self.engine = engine
        # Indicates whether the engine is of the latest version. Valid values:
        # 
        # - **true**: The engine is of the latest version.
        # 
        # - **false**: The engine is not of the latest version.
        self.is_last_version = is_last_version
        # The latest version of the engine.
        self.latest_version = latest_version
        # The memory size of the engine node.
        self.memory_size = memory_size
        # The number of nodes in the primary zone.
        self.primary_core_count = primary_core_count
        # The specification of the engine nodes.
        self.specification = specification
        # The number of nodes in the secondary zone.
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

