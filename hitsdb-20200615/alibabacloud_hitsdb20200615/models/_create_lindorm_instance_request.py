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
        # The ID of the vSwitch that is specified for the zone for the coordinate node of the instance. The vSwitch must be deployed in the zone specified by the ArbiterZoneId parameter. **This parameter is required if you want to create a multi-zone instance**.
        self.arbiter_vswitch_id = arbiter_vswitch_id
        # The ID of the zone for the coordinate node of the instance. **This parameter is required if you want to create a multi-zone instance**.
        self.arbiter_zone_id = arbiter_zone_id
        # The architecture of the instance. Valid values:
        # 
        # *   **1.0**: The instance that you want to create is a single-zone instance.
        # *   **2.0**: The instance that you want to create is a multi-zone instance.
        # 
        # By default, the value of this parameter is 1.0. To create a multi-zone instance, set this parameter to 2.0. **This parameter is required if you want to create a multi-zone instance**.
        self.arch_version = arch_version
        # The auto-renewal duration. Unit: month.
        # 
        # Valid values: **1** to **12**.
        # 
        # >  This parameter is available only when the **AutoRenewal** parameter is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false**: disables auto-renewal.
        # 
        # Default value: false.
        # 
        # >  This parameter is available only when the **PayType** parameter is set to **PREPAY**.
        self.auto_renewal = auto_renewal
        # The cold storage capacity of the instance. By default, if you leave this parameter unspecified, cold storage is not enabled for the instance. Unit: GB. Valid values: **800** to **1000000**.
        self.cold_storage = cold_storage
        # The storage capacity of the disk of a single core node. Valid values: 400 to 64000. Unit: GB. **This parameter is required if you want to create a multi-zone instance**.
        self.core_single_storage = core_single_storage
        # The specification of the nodes in the instance if you set DiskCategory to local_ssd_pro or local_hdd_pro.
        # 
        # Valid values when DiskCategory is set to local_ssd_pro (i3 instance types support only subscription instances):
        # 
        # *   **lindorm.i4.xlarge**: Each node has 4 CPU cores and 32 GB of memory.
        # *   **lindorm.i4.2xlarge**: Each node has 8 CPU cores and 64 GB of memory.
        # *   **lindorm.i4.4xlarge**: Each node has 16 CPU cores and 128 GB of memory.
        # *   **lindorm.i4.8xlarge**: Each node has 32 CPU cores and 256 GB of memory.
        # *   **lindorm.i3.xlarge**: Each node has 4 CPU cores and 32 GB of memory.
        # *   **lindorm.i3.2xlarge**: Each node has 8 CPU cores and 64 GB of memory.
        # *   **lindorm.i3.4xlarge**: Each node has 16 CPU cores and 128 GB of memory.
        # *   **lindorm.i3.8xlarge**: Each node has 32 CPU cores and 256 GB of memory.
        # *   **lindorm.i2.xlarge**: Each node has 4 CPU cores and 32 GB of memory.
        # *   **lindorm.i2.2xlarge**: Each node has 8 CPU cores and 64 GB of memory.
        # *   **lindorm.i2.4xlarge**: Each node has 16 CPU cores and 128 GB of memory.
        # *   **lindorm.i2.8xlarge**: Each node has 32 CPU cores and 256 GB of memory.
        # 
        # Valid values when DiskCategory is set to local_hhd_pro:
        # 
        # *   **lindorm.sd3c.3xlarge**: Each node has 14 CPU cores and 56 GB of memory.
        # *   **lindorm.sd3c.7xlarge**: Each node has 28 CPU cores and 112 GB of memory.
        # *   **lindorm.sd3c.14xlarge**: Each node has 56 CPU cores and 224 GB of memory.
        # *   **lindorm.d2c.6xlarge**: Each node has 24 CPU cores and 88 GB of memory.
        # *   **lindorm.d2c.12xlarge**: Each node has 48 CPU cores and 176 GB of memory.
        # *   **lindorm.d2c.24xlarge**: Each node has 96 CPU cores and 352 GB of memory.
        # *   **lindorm.d2s.5xlarge**: Each node has 20 CPU cores and 88 GB of memory.
        # *   **lindorm.d2s.10xlarge**: Each node has 40 CPU cores and 176 GB of memory.
        # *   **lindorm.d1.2xlarge**: Each node has 8 CPU cores and 32 GB of memory.
        # *   **lindorm.d1.4xlarge**: Each node has 16 CPU cores and 64 GB of memory.
        # *   **lindorm.d1.6xlarge**: Each node has 24 CPU cores and 96 GB of memory.
        self.core_spec = core_spec
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_efficiency**: This instance uses the Standard type of storage.
        # *   **cloud_ssd**: This instance uses the Performance type of storage.
        # *   **capacity_cloud_storage**: This instance uses the Capacity type of storage.
        # *   **local_ssd_pro**: This instance uses local SSDs.
        # *   **local_hdd_pro**: This instance uses local HDDs.
        # 
        # This parameter is required.
        self.disk_category = disk_category
        # The subscription period of the instance. The valid values of this parameter depend on the value of the PricingCycle parameter.
        # 
        # *   If PricingCycle is set to **Month**, set this parameter to an integer that ranges from **1** to **9**.
        # *   If PricingCycle is set to **Year**, set this parameter to an integer that ranges from **1** to **3**.
        # 
        # > This parameter is available and required when the PayType parameter is set to **PREPAY**.
        self.duration = duration
        # The number of LindormDFS nodes in the instance. The valid values of this parameter depend on the value of the PayType parameter.
        # 
        # *   If the PayType parameter is set to **PREPAY**, set this parameter to an integer that ranges from **0** to **60**.
        # *   If the PayType parameter is set to **POSTPAY**, set this parameter to an integer that ranges from **0** to **8**.
        self.filestore_num = filestore_num
        # The specification of LindormDFS nodes in the instance. Set the value of this parameter to **lindorm.c.xlarge**, which indicates that each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        self.filestore_spec = filestore_spec
        # The name of the instance that you want to create.
        self.instance_alias = instance_alias
        # The storage capacity of the instance you want to create. Unit: GB.
        self.instance_storage = instance_storage
        # The number of LindormTable nodes in the instance. The valid values of this parameter depend on the value of the PayType parameter.
        # 
        # *   If the PayType parameter is set to **PREPAY**, set this parameter to an integer that ranges from **0** to **90**.
        # *   If the PayType parameter is set to **POSTPAY**, set this parameter to an integer that ranges from **0** to **400**.
        # 
        # **This parameter is required if you want to create a multi-zone instance**.  The valid values of this parameter range from 4 to 400 if you want to create a multi-zone instance.
        self.lindorm_num = lindorm_num
        # The specification of LindormTable nodes in the instance. Valid values:
        # 
        # *   **lindorm.c.xlarge**: Each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        # *   **lindorm.c.2xlarge**: Each node has 8 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.c.4xlarge**: Each node has 16 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.c.8xlarge**: Each node has 32 dedicated CPU cores and 64 GB of dedicated memory.
        self.lindorm_spec = lindorm_spec
        # The disk type of the log nodes. Valid values:
        # 
        # *   **cloud_efficiency**: This instance uses the Standard type of storage.
        # *   **cloud_ssd**: This instance uses the Performance type of storage.
        # 
        # **This parameter is required if you want to create a multi-zone instance**.
        self.log_disk_category = log_disk_category
        # The number of the log nodes. Valid values: 4 to 400. **This parameter is required if you want to create a multi-zone instance**.
        self.log_num = log_num
        # The storage capacity of the disk of a single log node. Valid values: 400 to 64000. Unit: GB. **This parameter is required if you want to create a multi-zone instance**.
        self.log_single_storage = log_single_storage
        # The type of the log nodes. Valid values:
        # 
        # *   **lindorm.sn1.xlarge**: Each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        # *   **lindorm.sn1.2xlarge**: Each node has 8 dedicated CPU cores and 16 GB of dedicated memory.
        # 
        # **This parameter is required if you want to create a multi-zone instance**.
        self.log_spec = log_spec
        # The number of LTS nodes in the instance. Valid values: **0** to **60**.
        self.lts_num = lts_num
        # The specification of LTS nodes in the instance. Valid values:
        # 
        # *   **lindorm.c.xlarge**: Each node has 4 dedicated CPU cores and 8 GB of dedicated memory.
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.c.2xlarge**: Each node has 8 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.c.4xlarge**: Each node has 16 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.c.8xlarge**: Each node has 32 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.lts_spec = lts_spec
        # The combinations of zones that are available for the multi-zone instance. You can go to the purchase page of Lindorm to view the supported zone combinations.
        # 
        # *   **ap-southeast-5abc-aliyun**: Zone A+B+C in the Indonesia (Jakarta) region.
        # *   **cn-hangzhou-ehi-aliyun**: Zone E+H+I in the China (Hangzhou) region.
        # *   **cn-beijing-acd-aliyun**: Zone A+C+D in the China (Beijing) region.
        # *   **ap-southeast-1-abc-aliyun**: Zone A+B+C in the Singapore region.
        # *   **cn-zhangjiakou-abc-aliyun**: Zone A+B+C in the China (Zhangjiakou) region.
        # *   **cn-shanghai-efg-aliyun**: Zone E+F+G in the China (Shanghai) region.
        # *   **cn-shanghai-abd-aliyun**: Zone A+B+D in the China (Shanghai) region.
        # *   **cn-hangzhou-bef-aliyun**: Zone B+E+F in the China (Hangzhou) region.
        # *   **cn-hangzhou-bce-aliyun**: Zone B+C+E in the China (Hangzhou) region.
        # *   **cn-beijing-fgh-aliyun**: Zone F+G+H in the China (Beijing) region.
        # *   **cn-shenzhen-abc-aliyun**: Zone A+B+C in the China (Shenzhen) region.
        # 
        # **This parameter is required if you want to create a multi-zone instance**.
        self.multi_zone_combination = multi_zone_combination
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the instance you want to create. Valid values:
        # 
        # *   **PREPAY**: subscription.
        # *   **POSTPAY**: pay-as-you-go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The period based on which you are charged for the instance. Valid values:
        # 
        # *   **Month**: You are charged for the instance on a monthly basis.
        # *   **Year**: You are charged for the instance on a yearly basis.
        # 
        # > This parameter is available and required when the PayType parameter is set to **PREPAY**.
        self.pricing_cycle = pricing_cycle
        # The ID of the vSwitch that is specified for the secondary zone of the instance. The vSwitch must be deployed in the zone specified by the StandbyZoneId parameter. **This parameter is required if you want to create a multi-zone instance**.
        self.primary_vswitch_id = primary_vswitch_id
        # Multi-zone instance, availability zone ID of the primary zone. **This parameter is required if you need to create a multi-zone instance.**
        self.primary_zone_id = primary_zone_id
        # The ID of the region in which you want to create the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/426062.html) operation to query the region in which you can create the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Lindorm instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The number of LindormSearch nodes in the instance. Valid values: integers from **0** to **60**.
        self.solr_num = solr_num
        # The specification of the LindormSearch nodes in the instance. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.c.2xlarge**: Each node has 8 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.c.4xlarge**: Each node has 16 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.c.8xlarge**: Each node has 32 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.solr_spec = solr_spec
        # The ID of the vSwitch that is specified for the secondary zone of the instance. The vSwitch must be deployed in the zone specified by the StandbyZoneId parameter. **This parameter is required if you want to create a multi-zone instance**.
        self.standby_vswitch_id = standby_vswitch_id
        # The ID of the secondary zone of the instance. **This parameter is required if you want to create a multi-zone instance**.
        self.standby_zone_id = standby_zone_id
        # The number of LindormStream nodes in the instance. Valid values: integers from **0** to **60**.
        self.stream_num = stream_num
        # The specification of the LindormStream nodes in the instance. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.stream_spec = stream_spec
        # The tags that are added to instances.
        self.tag = tag
        # The number of the LindormTSDB nodes in the instance. The valid values of this parameter depend on the value of the PayType parameter.
        # 
        # *   If the PayType parameter is set to **PREPAY**, set this parameter to an integer that ranges from **0** to **24**.
        # *   If the PayType parameter is set to **POSTPAY**, set this parameter to an integer that ranges from **0** to **32**.
        self.tsdb_num = tsdb_num
        # The specification of the LindormTSDB nodes in the instance. Valid values:
        # 
        # *   **lindorm.g.xlarge**: Each node has 4 dedicated CPU cores and 16 GB of dedicated memory.
        # *   **lindorm.g.2xlarge**: Each node has 8 dedicated CPU cores and 32 GB of dedicated memory.
        # *   **lindorm.g.4xlarge**: Each node has 16 dedicated CPU cores and 64 GB of dedicated memory.
        # *   **lindorm.g.8xlarge**: Each node has 32 dedicated CPU cores and 128 GB of dedicated memory.
        self.tsdb_spec = tsdb_spec
        # The ID of the VPC in which you want to create the instance.
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The ID of the vSwitch to which you want the instance to connect.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the zone in which you want to create the instance.
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
        # The tag key. Valid values of N: 1 to 20.
        # 
        # >  You can specify the keys of multiple tags. For example, you can specify the key of the first tag in the first key-value pair contained in the value of this parameter and specify the key of the second tag in the second key-value pair.
        self.key = key
        # The tag value. Valid values of N: 1 to 20.
        # 
        # >  You can specify the values of multiple tags. For example, you can specify the value of the first tag in the first key-value pair contained in the value of this parameter and specify the value of the second tag in the second key-value pair.
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

