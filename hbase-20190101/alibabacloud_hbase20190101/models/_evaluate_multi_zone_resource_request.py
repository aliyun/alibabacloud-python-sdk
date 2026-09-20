# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EvaluateMultiZoneResourceRequest(DaraModel):
    def __init__(
        self,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arch_version: str = None,
        auto_renew_period: int = None,
        client_token: str = None,
        cluster_name: str = None,
        core_disk_size: int = None,
        core_disk_type: str = None,
        core_instance_type: str = None,
        core_node_count: int = None,
        engine: str = None,
        engine_version: str = None,
        log_disk_size: int = None,
        log_disk_type: str = None,
        log_instance_type: str = None,
        log_node_count: int = None,
        master_instance_type: str = None,
        multi_zone_combination: str = None,
        pay_type: str = None,
        period: int = None,
        period_unit: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        security_iplist: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        vpc_id: str = None,
    ):
        # The vSwitch ID of the arbitration zone. The vSwitch must be in the zone specified by **ArbiterZoneId**.
        # 
        # This parameter is required.
        self.arbiter_vswitch_id = arbiter_vswitch_id
        # The zone ID of the arbitration zone.
        # 
        # This parameter is required.
        self.arbiter_zone_id = arbiter_zone_id
        # The version of the deployment architecture. Currently, only the hbaseue engine type is supported. Set the value to **2.0**.
        # 
        # This parameter is required.
        self.arch_version = arch_version
        # The auto-renewal period of the instance. Unit: months.
        # 
        # > <ul><li>The default value is 0, which indicates that the instance is not automatically renewed after the instance expires.</li>
        # <li>For example, if the auto-renewal period is set to 2, the instance is automatically renewed for two months after the instance expires.</li></ul>
        self.auto_renew_period = auto_renew_period
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value. Make sure that the value is unique among different requests. The value cannot exceed 64 ASCII characters in length and cannot contain non-ASCII characters.
        self.client_token = client_token
        # The cluster name. The following rules apply:
        # 
        # - The name must be 2 to 128 characters in length.
        # - The name must start with an uppercase letter, a lowercase letter, or a Chinese character.
        # - The name can contain digits or special characters, including periods (.), hyphens (-), and underscores (_).
        self.cluster_name = cluster_name
        # The disk size of the node. Valid values: 400 to 64000. Unit: GB. The value must be a multiple of 40.
        # 
        # This parameter is required.
        self.core_disk_size = core_disk_size
        # The disk type of the core node. Valid values:
        # - **cloud_efficiency**: ultra cloud disk.
        # - **cloud_ssd**: standard SSD.
        # - **local_hdd_pro**: throughput-intensive local disk.
        # - **local_ssd_pro**: I/O-intensive local disk.
        # 
        # This parameter is required.
        self.core_disk_type = core_disk_type
        # The node specifications of the core node. You can invoke the [DescribeInstanceType](https://help.aliyun.com/document_detail/145796.html) operation to query the node specifications.
        # 
        # This parameter is required.
        self.core_instance_type = core_instance_type
        # The number of core nodes. Valid values: 2 to 20. The value must be an even number.
        # 
        # This parameter is required.
        self.core_node_count = core_node_count
        # The service type. Currently, only ApsaraDB for HBase Performance-enhanced Edition is supported. Set the value to **hbaseue**.
        # 
        # This parameter is required.
        self.engine = engine
        # The version of the engine type. Set the value to **2.0**.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The disk size of the log node. Valid values: 400 to 64000. Unit: GB. The value must be a multiple of 40.
        self.log_disk_size = log_disk_size
        # The disk type of the log node. Valid values:
        # - **cloud_efficiency**: ultra cloud disk.
        # - **cloud_ssd**: standard SSD.
        # - **local_hdd_pro**: throughput-intensive local disk.
        # - **local_ssd_pro**: I/O-intensive local disk.
        self.log_disk_type = log_disk_type
        # The node specifications of the log node. You can invoke the [DescribeInstanceType](https://help.aliyun.com/document_detail/145796.html) operation to query the node specifications.
        self.log_instance_type = log_instance_type
        # The number of log nodes. Valid values: 4 to 400. The value must be a multiple of 4.
        self.log_node_count = log_node_count
        # The node specifications of the master node. You can invoke the [DescribeInstanceType](https://help.aliyun.com/document_detail/145796.html) operation to query the node specifications.
        # 
        # This parameter is required.
        self.master_instance_type = master_instance_type
        # <props="china">The zone combination. The following combinations are supported. You can go to the buy page or call the [DescribeMultiZoneAvailableRegions](https://help.aliyun.com/document_detail/203039.html) operation to view the supported zone combinations.
        # <props="intl">The zone combination. The following combinations are supported. You can go to the buy page to view the supported zone combinations..
        # 
        # This parameter is required.
        self.multi_zone_combination = multi_zone_combination
        # The billing method of the instance. Valid values:
        # 
        # - **Prepaid**: subscription.
        # - **Postpaid**: pay-as-you-go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription duration of the subscription instance. Valid values:
        # 
        # - If PeriodUnit is set to year, valid values are 1 to 3.
        # - If PeriodUnit is set to month, valid values are 1 to 9.
        # 
        # > This parameter is required only when PayType is set to Prepaid.
        self.period = period
        # The unit of the subscription duration for the subscription instance. Valid values:
        # 
        # - **year**
        # - **month**
        # 
        # > This parameter is required only when PayType is set to Prepaid.
        self.period_unit = period_unit
        # The vSwitch ID of the primary zone instance. The vSwitch must be in the zone specified by **PrimaryZoneId**.
        # 
        # This parameter is required.
        self.primary_vswitch_id = primary_vswitch_id
        # The zone ID of the primary zone instance.
        # 
        # This parameter is required.
        self.primary_zone_id = primary_zone_id
        # The ID of the region in which the instance resides. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/144489.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IP addresses in the whitelist of the instance. Separate multiple IP addresses with commas (,).
        # 
        # > If the IP address is set to 127.0.0.1, all addresses are denied access to the instance. For example, 192.168.0.0/24 indicates that all IP addresses in the 192.168.0.XX range are allowed to access the instance.
        self.security_iplist = security_iplist
        # The vSwitch ID of the secondary zone instance. The vSwitch must be in the zone specified by **StandbyZoneId**.
        # 
        # This parameter is required.
        self.standby_vswitch_id = standby_vswitch_id
        # The zone ID of the secondary zone instance.
        # 
        # This parameter is required.
        self.standby_zone_id = standby_zone_id
        # The ID of the virtual private cloud (VPC). The VPC must be in the region specified by **RegionId**.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

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

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size

        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type

        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type

        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size

        if self.log_disk_type is not None:
            result['LogDiskType'] = self.log_disk_type

        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type

        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count

        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type

        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id

        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')

        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')

        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')

        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')

        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')

        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')

        if m.get('LogDiskType') is not None:
            self.log_disk_type = m.get('LogDiskType')

        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')

        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')

        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')

        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')

        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

