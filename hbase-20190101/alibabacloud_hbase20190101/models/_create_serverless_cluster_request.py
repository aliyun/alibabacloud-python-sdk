# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServerlessClusterRequest(DaraModel):
    def __init__(
        self,
        auto_renew_period: int = None,
        client_token: str = None,
        client_type: str = None,
        cluster_name: str = None,
        disk_type: str = None,
        engine: str = None,
        engine_version: str = None,
        pay_type: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        serverless_capability: int = None,
        serverless_spec: str = None,
        serverless_storage: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The auto-renewal period of the instance. Unit: months.
        # 
        # > <ul><li>The default value of the auto-renewal period is 0, which indicates that the instance is not automatically renewed after the instance expires.</li>
        # <li>For example, if the auto-renewal period is set to 2, the instance is automatically renewed for two months after the instance expires.</li></ul>
        self.auto_renew_period = auto_renew_period
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can be up to 64 ASCII characters in length and cannot contain non-ASCII characters.
        self.client_token = client_token
        # The parameter that identifies the source of the creation request. For public cloud, leave this parameter empty.
        self.client_type = client_type
        # The name of the instance.
        self.cluster_name = cluster_name
        # The disk type of the instance. Valid values:
        # 
        # - **cloud_efficiency**: ultra cloud disk.
        # - **cloud_ssd**: standard SSD.
        # - **local_hdd_pro**: local HDD.
        # - **local_ssd_pro**: local SSD.
        # - **cloud_essd_pl1**: ESSD.
        self.disk_type = disk_type
        # The engine type of the HBase Serverless instance. Set the value to **serverlesshbase**.
        self.engine = engine
        # The DPI engine version.
        self.engine_version = engine_version
        # The billing method of the instance. Valid values:
        # 
        # - **Prepaid**: subscription.
        # - **Postpaid**: pay-as-you-go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription duration of the subscription instance. Valid values:
        # 
        # - If PeriodUnit is set to year, valid values are **1** to **3**.
        # - If PeriodUnit is set to month, valid values are **1** to **9**.
        # 
        # > This parameter is required only when the billing method of the instance is **Prepaid**.
        self.period = period
        # The unit of the subscription duration for the subscription instance. Valid values:
        # 
        # - **year**: year.
        # - **month**: month.
        # 
        # > This parameter is required only when the billing method of the instance is **Prepaid**.
        self.period_unit = period_unit
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/144489.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. For more information about resource groups, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The processing capability per unit. Unit: CU.
        self.serverless_capability = serverless_capability
        # The specification type. Valid values: leave empty or **serverless.small**.
        self.serverless_spec = serverless_spec
        # The storage size. Unit: GB.
        self.serverless_storage = serverless_storage
        # The vSwitch ID within the VPC.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        # 
        # > If both this parameter and the VswitchId parameter are left empty, the network type of the instance is classic network.
        self.vpc_id = vpc_id
        # The zone ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/144489.html) operation to query the zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.serverless_capability is not None:
            result['ServerlessCapability'] = self.serverless_capability

        if self.serverless_spec is not None:
            result['ServerlessSpec'] = self.serverless_spec

        if self.serverless_storage is not None:
            result['ServerlessStorage'] = self.serverless_storage

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServerlessCapability') is not None:
            self.serverless_capability = m.get('ServerlessCapability')

        if m.get('ServerlessSpec') is not None:
            self.serverless_spec = m.get('ServerlessSpec')

        if m.get('ServerlessStorage') is not None:
            self.serverless_storage = m.get('ServerlessStorage')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

