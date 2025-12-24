# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class AllocateDedicatedHostsRequest(DaraModel):
    def __init__(
        self,
        network_attributes: main_models.AllocateDedicatedHostsRequestNetworkAttributes = None,
        action_on_maintenance: str = None,
        auto_placement: str = None,
        auto_release_time: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        charge_type: str = None,
        client_token: str = None,
        cpu_over_commit_ratio: float = None,
        dedicated_host_cluster_id: str = None,
        dedicated_host_name: str = None,
        dedicated_host_type: str = None,
        description: str = None,
        min_quantity: int = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        quantity: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.AllocateDedicatedHostsRequestTag] = None,
        zone_id: str = None,
    ):
        self.network_attributes = network_attributes
        # The policy for migrating the instances deployed on the dedicated host when the dedicated host fails or needs to be repaired online. Valid values:
        # 
        # *   Migrate: The instances are migrated to another physical machine and then restarted.
        # 
        #     If cloud disks are attached to the dedicated host, the default value is Migrate.
        # 
        # *   Stop: The instances are stopped. If the dedicated host cannot be repaired, the instances are migrated to another physical machine and then restarted.
        # 
        #     If local disks are attached to the dedicated host, the default value is Stop.
        self.action_on_maintenance = action_on_maintenance
        # Specifies whether to add the dedicated host to the resource pool for automatic deployment. If you create an ECS instance on a dedicated host without specifying the **DedicatedHostId** parameter, Alibaba Cloud selects a dedicated host from the resource pool to host the instance. For more information, see [Automatic deployment](https://help.aliyun.com/document_detail/118938.html). Valid values:
        # 
        # *   on: adds the dedicated host to the resource pool for automatic deployment.
        # *   off: does not add the dedicated host to the resource pool for automatic deployment.
        # 
        # Default value: on.
        # 
        # > If you do not want to add the dedicated host to the resource pool for automatic deployment, set this parameter to off.
        self.auto_placement = auto_placement
        # The time when to automatically release the dedicated host. Specify the time in the `ISO 8601` standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > 
        # 
        # *   It must be at least half an hour later than the current time.
        # 
        # *   It must be at most three years later than the current time.
        # 
        # *   If the value of seconds (ss) is not 00, it is automatically set to 00.
        self.auto_release_time = auto_release_time
        # Specifies whether to automatically renew the subscription dedicated host.
        # 
        # > The **AutoRenew** parameter takes effect only when the **ChargeType** parameter is set to PrePaid.
        # 
        # Default value: false
        self.auto_renew = auto_renew
        # The auto-renewal duration of the dedicated host. The **AutoRenewPeriod** parameter takes effect and is required only when the **AutoRenew** parameter is set to true. Valid values:
        # 
        # Valid values when PeriodUnit is set to Month: 1, 2, 3, 6, and 12.
        self.auto_renew_period = auto_renew_period
        # The billing method of the dedicated host. Valid values:
        # 
        # *   PrePaid: subscription. If you set this parameter to PrePaid, make sure that you have sufficient account balance or credits. Otherwise, `InvalidPayMethod` is returned.
        # *   PostPaid: pay-as-you-go.
        # 
        # Default value: PostPaid.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The CPU overcommit ratio. You can configure CPU overcommit ratios only for the following dedicated host types: g6s, c6s, and r6s. Valid values: 1 to 5.
        # 
        # The CPU overcommit ratio affects the number of available vCPUs on a dedicated host. You can use the following formula to calculate the number of available vCPUs on a dedicated host: Number of available vCPUs = Number of physical CPU cores × 2 × CPU overcommit ratio. For example, the number of physical CPU cores on each g6s dedicated host is 52. If you set the CPU overcommit ratio of a g6s dedicated host to 4, the number of available vCPUs on the dedicated host is 416. For scenarios that have minimal requirements on CPU stability or where CPU load is not heavy, such as development and test environments, you can increase the number of available vCPUs on a dedicated host by increasing the CPU overcommit ratio. This way, you can deploy more ECS instances of the same specifications on the dedicated host and reduce the unit deployment cost.
        self.cpu_over_commit_ratio = cpu_over_commit_ratio
        # The ID of the dedicated host cluster in which to create the dedicated host.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The name of the dedicated host. The name must be 2 to 128 characters in length and can contain letters and digits. The name can contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.dedicated_host_name = dedicated_host_name
        # The dedicated host type. You can call the [DescribeDedicatedHostTypes](https://help.aliyun.com/document_detail/134240.html) operation to query the most recent list of dedicated host types.
        # 
        # This parameter is required.
        self.dedicated_host_type = dedicated_host_type
        # The description of the dedicated host. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The minimum number of dedicated hosts to create. Valid values: 1 to 100.
        # 
        # > If the number of available dedicated hosts is less than the minimum number of dedicated hosts to create, the dedicated hosts fail to be created.
        self.min_quantity = min_quantity
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration of the dedicated host. The `Period` parameter is required and takes effect only when the `ChargeType` parameter is set to `PrePaid`. Valid values:
        # 
        # *   Valid values when the PeriodUnit parameter is set to Month: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        # *   Valid values when the PeriodUnit parameter is set to Year: 1, 2, 3, 4, and 5.
        self.period = period
        # The unit of the subscription duration of the dedicated host. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # Default value: Month.
        self.period_unit = period_unit
        # The number of dedicated hosts that you want to create. Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.quantity = quantity
        # The ID of the region in which to create the dedicated host. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which to assign the dedicated host.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags to add to the dedicated host.
        self.tag = tag
        # The ID of the zone in which to create the dedicated host.
        # 
        # This parameter is empty by default. If you do not specify a zone, the system selects a zone.
        self.zone_id = zone_id

    def validate(self):
        if self.network_attributes:
            self.network_attributes.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_attributes is not None:
            result['NetworkAttributes'] = self.network_attributes.to_map()

        if self.action_on_maintenance is not None:
            result['ActionOnMaintenance'] = self.action_on_maintenance

        if self.auto_placement is not None:
            result['AutoPlacement'] = self.auto_placement

        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cpu_over_commit_ratio is not None:
            result['CpuOverCommitRatio'] = self.cpu_over_commit_ratio

        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name

        if self.dedicated_host_type is not None:
            result['DedicatedHostType'] = self.dedicated_host_type

        if self.description is not None:
            result['Description'] = self.description

        if self.min_quantity is not None:
            result['MinQuantity'] = self.min_quantity

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAttributes') is not None:
            temp_model = main_models.AllocateDedicatedHostsRequestNetworkAttributes()
            self.network_attributes = temp_model.from_map(m.get('NetworkAttributes'))

        if m.get('ActionOnMaintenance') is not None:
            self.action_on_maintenance = m.get('ActionOnMaintenance')

        if m.get('AutoPlacement') is not None:
            self.auto_placement = m.get('AutoPlacement')

        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CpuOverCommitRatio') is not None:
            self.cpu_over_commit_ratio = m.get('CpuOverCommitRatio')

        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')

        if m.get('DedicatedHostType') is not None:
            self.dedicated_host_type = m.get('DedicatedHostType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MinQuantity') is not None:
            self.min_quantity = m.get('MinQuantity')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.AllocateDedicatedHostsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class AllocateDedicatedHostsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the dedicated host. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with acs: or aliyun.
        self.key = key
        # The value of tag N to add to the dedicated host. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

class AllocateDedicatedHostsRequestNetworkAttributes(DaraModel):
    def __init__(
        self,
        slb_udp_timeout: int = None,
        udp_timeout: int = None,
    ):
        # The timeout period for a UDP session between a Server Load Balancer (SLB) instance and the dedicated host. Unit: seconds. Valid values: 15 to 310.
        self.slb_udp_timeout = slb_udp_timeout
        # The timeout period for a UDP session between a user and an Alibaba Cloud service on the dedicated host. Unit: seconds. Valid values: 15 to 310.
        self.udp_timeout = udp_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slb_udp_timeout is not None:
            result['SlbUdpTimeout'] = self.slb_udp_timeout

        if self.udp_timeout is not None:
            result['UdpTimeout'] = self.udp_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlbUdpTimeout') is not None:
            self.slb_udp_timeout = m.get('SlbUdpTimeout')

        if m.get('UdpTimeout') is not None:
            self.udp_timeout = m.get('UdpTimeout')

        return self

