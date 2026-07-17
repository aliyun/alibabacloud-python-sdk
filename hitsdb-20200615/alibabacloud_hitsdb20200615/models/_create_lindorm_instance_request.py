# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class CreateLindormInstanceRequest(DaraModel):
    def __init__(
        self,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arch_version: str = None,
        auto_renew_duration: str = None,
        auto_renewal: bool = None,
        cold_storage: int = None,
        core_single_storage: int = None,
        core_spec: str = None,
        disk_category: str = None,
        duration: str = None,
        filestore_num: int = None,
        filestore_spec: str = None,
        instance_alias: str = None,
        instance_storage: str = None,
        lindorm_num: int = None,
        lindorm_spec: str = None,
        log_disk_category: str = None,
        log_num: int = None,
        log_single_storage: int = None,
        log_spec: str = None,
        lts_num: str = None,
        lts_spec: str = None,
        multi_zone_combination: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        solr_num: int = None,
        solr_spec: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        stream_num: int = None,
        stream_spec: str = None,
        tag: List[main_models.CreateLindormInstanceRequestTag] = None,
        tsdb_num: int = None,
        tsdb_spec: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the VSwitch for the arbiter zone of the multi-zone instance. The VSwitch must be in the zone specified by `ArbiterZoneId`. **This parameter is required for multi-zone instances.**
        self.arbiter_vswitch_id = arbiter_vswitch_id
        # The ID of the arbiter zone for the multi-zone instance. **This parameter is required for multi-zone instances.**
        self.arbiter_zone_id = arbiter_zone_id
        # The deployment architecture of the instance. Valid values:
        # 
        # - **1.0**: Single-zone deployment.
        # 
        # - **2.0**: Multi-zone deployment.
        # 
        # The default value is 1.0. To create a multi-zone instance, set this parameter to 2.0. **This parameter is required for multi-zone instances.**
        self.arch_version = arch_version
        # The auto-renewal duration, in months.
        # 
        # The value of this parameter ranges from **1** to **12**.
        # 
        # > This parameter takes effect only when **AutoRenewal** is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # Specifies whether to enable auto-renewal for the Subscription instance. Valid values:
        # 
        # - **true**: Auto-renewal is enabled.
        # 
        # - **false**: Auto-renewal is disabled.
        # 
        # Default value: false.
        # 
        # > This parameter takes effect only when the **PayType** parameter is set to **PREPAY**.
        self.auto_renewal = auto_renewal
        # The cold storage capacity of the instance, in GB. The value of this parameter ranges from **800** to **1,000,000**. If you do not specify this parameter, cold storage is not enabled.
        self.cold_storage = cold_storage
        # The storage capacity of a single core node in the multi-zone instance. Unit: GB. The value of this parameter ranges from 400 to 64,000. **This parameter is required for multi-zone instances.**
        self.core_single_storage = core_single_storage
        # The node specification for an instance that uses local disks.
        # 
        # If the storage type is **local_ssd_pro**, valid values include the following: Note that I3-family specifications are available only for Subscription instances.
        # 
        # - **lindorm.i4.xlarge**: 4 cores, 32 GB memory (I4).
        # 
        # - **lindorm.i4.2xlarge**: 8 cores, 64 GB memory (I4).
        # 
        # - **lindorm.i4.4xlarge**: 16 cores, 128 GB memory (I4).
        # 
        # - **lindorm.i4.8xlarge**: 32 cores, 256 GB memory (I4).
        # 
        # - **lindorm.i3.xlarge**: 4 cores, 32 GB memory (I3).
        # 
        # - **lindorm.i3.2xlarge**: 8 cores, 64 GB memory (I3).
        # 
        # - **lindorm.i3.4xlarge**: 16 cores, 128 GB memory (I3).
        # 
        # - **lindorm.i3.8xlarge**: 32 cores, 256 GB memory (I3).
        # 
        # - **lindorm.i2.xlarge**: 4 cores, 32 GB memory (I2).
        # 
        # - **lindorm.i2.2xlarge**: 8 cores, 64 GB memory (I2).
        # 
        # - **lindorm.i2.4xlarge**: 16 cores, 128 GB memory (I2).
        # 
        # - **lindorm.i2.8xlarge**: 32 cores, 256 GB memory (I2).
        # 
        # If the storage type is **local_hdd_pro**, valid values include:
        # 
        # - **lindorm.sd3c.3xlarge**: 14 cores, 56 GB memory (D3C PRO).
        # 
        # - **lindorm.sd3c.7xlarge**: 28 cores, 112 GB memory (D3C PRO).
        # 
        # - **lindorm.sd3c.14xlarge**: 56 cores, 224 GB memory (D3C PRO).
        # 
        # - **lindorm.d2c.6xlarge**: 24 cores, 88 GB memory (D2C).
        # 
        # - **lindorm.d2c.12xlarge**: 48 cores, 176 GB memory (D2C).
        # 
        # - **lindorm.d2c.24xlarge**: 96 cores, 352 GB memory (D2C).
        # 
        # - **lindorm.d2s.5xlarge**: 20 cores, 88 GB memory (D2S).
        # 
        # - **lindorm.d2s.10xlarge**: 40 cores, 176 GB memory (D2S).
        # 
        # - **lindorm.d1.2xlarge**: 8 cores, 32 GB memory (D1NE).
        # 
        # - **lindorm.d1.4xlarge**: 16 cores, 64 GB memory (D1NE).
        # 
        # - **lindorm.d1.6xlarge**: 24 cores, 96 GB memory (D1NE).
        self.core_spec = core_spec
        # The storage type of the instance. Valid values:
        # 
        # - **cloud_efficiency**: Efficiency cloud disk.
        # 
        # - **cloud_ssd**: Performance cloud disk.
        # 
        # - **cloud_essd**: Enhanced SSD (ESSD).
        # 
        # - **cloud_essd_pl0**: ESSD PL0.
        # 
        # - **capacity_cloud_storage**: Capacity-optimized cloud storage. (Not available for multi-zone instances.)
        # 
        # - **local_ssd_pro**: Local SSD. (Not available for multi-zone instances.)
        # 
        # - **local_hdd_pro**: Local HDD. (Not available for multi-zone instances.)
        # 
        # This parameter is required.
        self.disk_category = disk_category
        # The subscription duration for the instance. Valid values:
        # 
        # - If **PricingCycle** is set to **Month**, the value can range from **1** to **9**.
        # 
        # - If **PricingCycle** is set to **Year**, the value can range from **1** to **3**.
        # 
        # > This parameter is required if you set **PayType** to **PREPAY**.
        self.duration = duration
        # The number of nodes in the file engine. Valid values:
        # 
        # - For a Subscription instance, the value of this parameter ranges from **0** to **60**.
        # 
        # - For a Pay-As-You-Go instance, the value of this parameter ranges from **0** to **8**.
        self.filestore_num = filestore_num
        # The specification of the file engine nodes. Valid values:
        # 
        # - **lindorm.c.xlarge**: 4 cores, 8 GB memory (standard).
        self.filestore_spec = filestore_spec
        # The name of the instance.
        self.instance_alias = instance_alias
        # The storage capacity of the instance, in GB.
        self.instance_storage = instance_storage
        # The number of nodes in the wide table engine.
        # 
        # For a single-zone instance, the value of this parameter ranges from **0** to **90**.
        # 
        # **This parameter is required for multi-zone instances.** For an instance that uses cloud disks, the value ranges from **4** to **400**. For an instance that uses local disks, the value ranges from **6** to **400**.
        self.lindorm_num = lindorm_num
        # The specification of the wide table engine nodes. Valid values:
        # 
        # - **lindorm.g.xlarge**: 4 cores, 16 GB memory (dedicated).
        # 
        # - **lindorm.c.2xlarge**: 8 cores, 16 GB memory (dedicated).
        # 
        # - **lindorm.g.2xlarge**: 8 cores, 32 GB memory (dedicated).
        # 
        # - **lindorm.c.4xlarge**: 16 cores, 32 GB memory (dedicated).
        # 
        # - **lindorm.g.4xlarge**: 16 cores, 64 GB memory (dedicated).
        # 
        # - **lindorm.c.8xlarge**: 32 cores, 64 GB memory (dedicated).
        # 
        # - **lindorm.g.8xlarge**: 32 cores, 128 GB memory (dedicated).
        self.lindorm_spec = lindorm_spec
        # The storage type of the log nodes for the multi-zone instance. Valid values:
        # 
        # - **cloud_efficiency**: Efficiency cloud disk.
        # 
        # - **cloud_ssd**: Performance cloud disk.
        # 
        # **This parameter is required for multi-zone instances.**
        self.log_disk_category = log_disk_category
        # The number of log nodes for the multi-zone instance. The value of this parameter ranges from 4 to 400. **This parameter is required for multi-zone instances.**
        self.log_num = log_num
        # The storage capacity of a single log node in the multi-zone instance. Unit: GB. The value of this parameter ranges from 400 to 64,000. **This parameter is required for multi-zone instances.**
        self.log_single_storage = log_single_storage
        # The specification of the log nodes for the multi-zone instance. Valid values:
        # 
        # - **lindorm.sn1.large**: 4 cores, 8 GB memory (dedicated).
        # 
        # - **lindorm.sn1.2xlarge**: 8 cores, 16 GB memory (dedicated).
        # 
        # **This parameter is required for multi-zone instances.**
        self.log_spec = log_spec
        # The number of nodes in the LTS engine. The value of this parameter ranges from **0** to **60**.
        self.lts_num = lts_num
        # The specification of the LTS engine nodes. Valid values:
        # 
        # - **lindorm.c.xlarge**: 4 cores, 8 GB memory (dedicated).
        # 
        # - **lindorm.g.xlarge**: 4 cores, 16 GB memory (dedicated).
        # 
        # - **lindorm.c.2xlarge**: 8 cores, 16 GB memory (dedicated).
        # 
        # - **lindorm.g.2xlarge**: 8 cores, 32 GB memory (dedicated).
        # 
        # - **lindorm.c.4xlarge**: 16 cores, 32 GB memory (dedicated).
        # 
        # - **lindorm.g.4xlarge**: 16 cores, 64 GB memory (dedicated).
        # 
        # - **lindorm.c.8xlarge**: 32 cores, 64 GB memory (dedicated).
        # 
        # - **lindorm.g.8xlarge**: 32 cores, 128 GB memory (dedicated).
        self.lts_spec = lts_spec
        # The combination of zones for the multi-zone instance. For a list of supported combinations, refer to the instance purchase page.
        # 
        # - **ap-southeast-5abc-aliyun**: Indonesia (Jakarta) A+B+C.
        # 
        # - **cn-hangzhou-ehi-aliyun**: China (Hangzhou) E+H+I.
        # 
        # - **cn-beijing-acd-aliyun**: China (Beijing) A+C+D.
        # 
        # - **ap-southeast-1-abc-aliyun**: Singapore A+B+C.
        # 
        # - **cn-zhangjiakou-abc-aliyun**: China (Zhangjiakou) A+B+C.
        # 
        # - **cn-shanghai-efg-aliyun**: China (Shanghai) E+F+G.
        # 
        # - **cn-shanghai-abd-aliyun**: China (Shanghai) A+B+D.
        # 
        # - **cn-hangzhou-bef-aliyun**: China (Hangzhou) B+E+F.
        # 
        # - **cn-hangzhou-bce-aliyun**: China (Hangzhou) B+C+E.
        # 
        # - **cn-beijing-fgh-aliyun**: China (Beijing) F+G+H.
        # 
        # - **cn-shenzhen-abc-aliyun**: China (Shenzhen) A+B+C.
        # 
        # **This parameter is required for multi-zone instances.**
        self.multi_zone_combination = multi_zone_combination
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the instance. Valid values:
        # 
        # - **PREPAY**: Subscription.
        # 
        # - **POSTPAY**: Pay-As-You-Go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The billing cycle for the Subscription instance. Valid values:
        # 
        # - **Month**
        # 
        # - **Year**
        # 
        # > This parameter is required if you set **PayType** to **PREPAY**.
        self.pricing_cycle = pricing_cycle
        # The ID of the VSwitch for the primary zone of the multi-zone instance. The VSwitch must be in the zone specified by `PrimaryZoneId`. **This parameter is required for multi-zone instances.**
        self.primary_vswitch_id = primary_vswitch_id
        # The ID of the primary zone for the multi-zone instance. **This parameter is required for multi-zone instances.**
        self.primary_zone_id = primary_zone_id
        # The ID of the region in which to create the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to query the latest region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The number of search engine nodes. The value of this parameter ranges from **0** to **60**.
        self.solr_num = solr_num
        # The specification of the search engine nodes. Valid values:
        # 
        # - **lindorm.g.xlarge**: 4 cores, 16 GB memory (dedicated).
        # 
        # - **lindorm.c.2xlarge**: 8 cores, 16 GB memory (dedicated).
        # 
        # - **lindorm.g.2xlarge**: 8 cores, 32 GB memory (dedicated).
        # 
        # - **lindorm.c.4xlarge**: 16 cores, 32 GB memory (dedicated).
        # 
        # - **lindorm.g.4xlarge**: 16 cores, 64 GB memory (dedicated).
        # 
        # - **lindorm.c.8xlarge**: 32 cores, 64 GB memory (dedicated).
        # 
        # - **lindorm.g.8xlarge**: 32 cores, 128 GB memory (dedicated).
        self.solr_spec = solr_spec
        # The ID of the VSwitch for the standby zone of the multi-zone instance. The VSwitch must be in the zone specified by `StandbyZoneId`. **This parameter is required for multi-zone instances.**
        self.standby_vswitch_id = standby_vswitch_id
        # The ID of the standby zone for the multi-zone instance. **This parameter is required for multi-zone instances.**
        self.standby_zone_id = standby_zone_id
        # The number of nodes in the stream engine. The value of this parameter ranges from **0** to **60**.
        self.stream_num = stream_num
        # The specification of the stream engine nodes. Valid values:
        # 
        # - **lindorm.g.xlarge**: 4 cores, 16 GB memory (dedicated).
        # 
        # - **lindorm.c.2xlarge**: 8 cores, 16 GB memory (dedicated).
        # 
        # - **lindorm.g.2xlarge**: 8 cores, 32 GB memory (dedicated).
        # 
        # - **lindorm.c.4xlarge**: 16 cores, 32 GB memory (dedicated).
        # 
        # - **lindorm.g.4xlarge**: 16 cores, 64 GB memory (dedicated).
        # 
        # - **lindorm.c.8xlarge**: 32 cores, 64 GB memory (dedicated).
        # 
        # - **lindorm.g.8xlarge**: 32 cores, 128 GB memory (dedicated).
        self.stream_spec = stream_spec
        # The tags to add to the instance. You can add up to 20 tags.
        self.tag = tag
        # The number of nodes in the time series engine. Valid values:
        # 
        # - For a Subscription instance, the value of this parameter ranges from **0** to **24**.
        # 
        # - For a Pay-As-You-Go instance, the value of this parameter ranges from **0** to **32**.
        self.tsdb_num = tsdb_num
        # The specification of the time series engine nodes. Valid values:
        # 
        # - **lindorm.g.xlarge**: 4 cores, 16 GB memory (dedicated).
        # 
        # - **lindorm.g.2xlarge**: 8 cores, 32 GB memory (dedicated).
        # 
        # - **lindorm.g.4xlarge**: 16 cores, 64 GB memory (dedicated).
        # 
        # - **lindorm.g.8xlarge**: 32 cores, 128 GB memory (dedicated).
        self.tsdb_spec = tsdb_spec
        # The ID of the VPC where you want to create the instance.
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The ID of the VSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the zone where you want to create the instance.
        # 
        # This parameter is required.
        self.zone_id = zone_id

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
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id

        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id

        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage

        if self.core_single_storage is not None:
            result['CoreSingleStorage'] = self.core_single_storage

        if self.core_spec is not None:
            result['CoreSpec'] = self.core_spec

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.filestore_num is not None:
            result['FilestoreNum'] = self.filestore_num

        if self.filestore_spec is not None:
            result['FilestoreSpec'] = self.filestore_spec

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage

        if self.lindorm_num is not None:
            result['LindormNum'] = self.lindorm_num

        if self.lindorm_spec is not None:
            result['LindormSpec'] = self.lindorm_spec

        if self.log_disk_category is not None:
            result['LogDiskCategory'] = self.log_disk_category

        if self.log_num is not None:
            result['LogNum'] = self.log_num

        if self.log_single_storage is not None:
            result['LogSingleStorage'] = self.log_single_storage

        if self.log_spec is not None:
            result['LogSpec'] = self.log_spec

        if self.lts_num is not None:
            result['LtsNum'] = self.lts_num

        if self.lts_spec is not None:
            result['LtsSpec'] = self.lts_spec

        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id

        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.solr_num is not None:
            result['SolrNum'] = self.solr_num

        if self.solr_spec is not None:
            result['SolrSpec'] = self.solr_spec

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num

        if self.stream_spec is not None:
            result['StreamSpec'] = self.stream_spec

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tsdb_num is not None:
            result['TsdbNum'] = self.tsdb_num

        if self.tsdb_spec is not None:
            result['TsdbSpec'] = self.tsdb_spec

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')

        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')

        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')

        if m.get('CoreSingleStorage') is not None:
            self.core_single_storage = m.get('CoreSingleStorage')

        if m.get('CoreSpec') is not None:
            self.core_spec = m.get('CoreSpec')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FilestoreNum') is not None:
            self.filestore_num = m.get('FilestoreNum')

        if m.get('FilestoreSpec') is not None:
            self.filestore_spec = m.get('FilestoreSpec')

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')

        if m.get('LindormNum') is not None:
            self.lindorm_num = m.get('LindormNum')

        if m.get('LindormSpec') is not None:
            self.lindorm_spec = m.get('LindormSpec')

        if m.get('LogDiskCategory') is not None:
            self.log_disk_category = m.get('LogDiskCategory')

        if m.get('LogNum') is not None:
            self.log_num = m.get('LogNum')

        if m.get('LogSingleStorage') is not None:
            self.log_single_storage = m.get('LogSingleStorage')

        if m.get('LogSpec') is not None:
            self.log_spec = m.get('LogSpec')

        if m.get('LtsNum') is not None:
            self.lts_num = m.get('LtsNum')

        if m.get('LtsSpec') is not None:
            self.lts_spec = m.get('LtsSpec')

        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')

        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SolrNum') is not None:
            self.solr_num = m.get('SolrNum')

        if m.get('SolrSpec') is not None:
            self.solr_spec = m.get('SolrSpec')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')

        if m.get('StreamSpec') is not None:
            self.stream_spec = m.get('StreamSpec')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateLindormInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TsdbNum') is not None:
            self.tsdb_num = m.get('TsdbNum')

        if m.get('TsdbSpec') is not None:
            self.tsdb_spec = m.get('TsdbSpec')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateLindormInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of a tag.
        # 
        # > You can specify the keys of multiple tags. For example, `Tag.1.Key` specifies the key of the first tag and `Tag.2.Key` specifies the key of the second tag.
        self.key = key
        # The value of a tag.
        # 
        # > You can specify the values of multiple tags. For example, `Tag.1.Value` specifies the value of the first tag and `Tag.2.Value` specifies the value of the second tag.
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

