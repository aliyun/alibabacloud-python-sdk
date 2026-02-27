# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        charge_type: str = None,
        cold_storage_size: int = None,
        cpu: int = None,
        duration: int = None,
        enable_serverless_computing: bool = None,
        gateway_count: int = None,
        initial_databases: str = None,
        instance_name: str = None,
        instance_type: str = None,
        leader_instance_id: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_size: int = None,
        storage_type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable auto-payment. Default value: true. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  The default value is true. If the balance of your account is insufficient, you can set this parameter to false. In this case, an unpaid order is generated. You can log on to the Expenses and Costs console to pay for the order.
        self.auto_pay = auto_pay
        # Specifies whether to enable monthly auto-renewal. The default value is false. Valid values:
        # 
        # *   true
        # *   false
        self.auto_renew = auto_renew
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        # 
        # >  This parameter is invalid for Hologres Shared Cluster instances. Hologres Shared Cluster instances have fixed specifications and are pay-as-you-go instances.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The infrequent access (IA) storage space of the instance. Unit: GB.
        # 
        # >  This parameter is invalid for pay-as-you-go instances.
        self.cold_storage_size = cold_storage_size
        # The instance specifications. Valid values:
        # 
        # *   8-core 32GB (number of compute nodes: 1)
        # *   32-core 128GB (number of compute nodes: 2)
        # *   64-core 256GB (number of compute nodes: 4)
        # *   96-core 384GB (number of compute nodes: 6)
        # *   128-core 512GB (number of compute nodes: 8)
        # *   Others
        # 
        # > 
        # 
        # *   Set this parameter to the number of cores.
        # 
        # *   If you want to set this parameter to specifications with more than 1,024 GB, you must submit a ticket.
        # 
        # *   This parameter is invalid for Hologres Shared Cluster instances.
        # 
        # *   The specifications of 8-core 32GB (number of compute nodes: 1) are for trial use only and cannot be used for production.
        self.cpu = cpu
        # The validity period of the instance that you want to purchase. For example, you can specify a validity period of two months.
        # 
        # >  You do not need to configure this parameter for pay-as-you-go instances.
        self.duration = duration
        # Specifies whether to enable the Serverless Computing feature.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.enable_serverless_computing = enable_serverless_computing
        # The number of gateways. Valid values: 2 to 50.
        # 
        # >  This parameter is required only for virtual warehouse instances.
        self.gateway_count = gateway_count
        # The initial database.
        self.initial_databases = initial_databases
        # The name of the instance. The name must be 2 to 64 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The category of the instance. Valid values:
        # 
        # *   Standard: general-purpose instance
        # *   Follower: read-only secondary instance
        # *   Warehouse: virtual warehouse instance
        # *   Shared: Hologres Shared Cluster instance
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The ID of the primary instance. This parameter is required for read-only secondary instances.
        # 
        # >  The primary and secondary instances must meet the following requirements:
        # 
        # *   The primary instance is in the Running state.
        # 
        # *   The primary instance and secondary instances are deployed in the same region.
        # 
        # *   The primary instance and secondary instances are deployed in the same zone.
        # 
        # *   Less than 10 secondary instances are associated with the primary instance.
        # 
        # *   The primary instance and secondary instances belong to the same Alibaba Cloud account.
        self.leader_instance_id = leader_instance_id
        # The billing cycle. Valid values:
        # 
        # *   Month
        # *   Hour
        # 
        # > 
        # 
        # *   This parameter can only be set to Month for subscription instances.
        # 
        # *   This parameter can only be set to Hour for pay-as-you-go instances.
        # 
        # *   By default, this parameter is set to Hour for Hologres Shared Cluster instances.
        self.pricing_cycle = pricing_cycle
        # The ID of the region. You can obtain region IDs in [Endpoints](https://www.alibabacloud.com/help/en/maxcompute/user-guide/endpoints).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. If you do not specify this parameter, the default resource group of the account is used.
        self.resource_group_id = resource_group_id
        # The standard storage space of the instance. Unit: GB.
        # 
        # >  This parameter is invalid for pay-as-you-go instances.
        self.storage_size = storage_size
        self.storage_type = storage_type
        # The ID of the vSwitch. The zone in which the vSwitch resides must be the same as the zone in which the Hologres instance resides.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC). The region in which the VPC resides must be the same as the region in which the Hologres instance resides.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the zone. For more information, see the "Operation description" section in this topic.
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
        if self.auto_pay is not None:
            result['autoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.cold_storage_size is not None:
            result['coldStorageSize'] = self.cold_storage_size

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.duration is not None:
            result['duration'] = self.duration

        if self.enable_serverless_computing is not None:
            result['enableServerlessComputing'] = self.enable_serverless_computing

        if self.gateway_count is not None:
            result['gatewayCount'] = self.gateway_count

        if self.initial_databases is not None:
            result['initialDatabases'] = self.initial_databases

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.leader_instance_id is not None:
            result['leaderInstanceId'] = self.leader_instance_id

        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        if self.storage_type is not None:
            result['storageType'] = self.storage_type

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoPay') is not None:
            self.auto_pay = m.get('autoPay')

        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('coldStorageSize') is not None:
            self.cold_storage_size = m.get('coldStorageSize')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('enableServerlessComputing') is not None:
            self.enable_serverless_computing = m.get('enableServerlessComputing')

        if m.get('gatewayCount') is not None:
            self.gateway_count = m.get('gatewayCount')

        if m.get('initialDatabases') is not None:
            self.initial_databases = m.get('initialDatabases')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('leaderInstanceId') is not None:
            self.leader_instance_id = m.get('leaderInstanceId')

        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

