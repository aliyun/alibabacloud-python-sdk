# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateRouterInterfaceRequest(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        client_token: str = None,
        description: str = None,
        fast_link_mode: bool = None,
        health_check_source_ip: str = None,
        health_check_target_ip: str = None,
        instance_charge_type: str = None,
        name: str = None,
        opposite_access_point_id: str = None,
        opposite_interface_id: str = None,
        opposite_interface_owner_id: str = None,
        opposite_region_id: str = None,
        opposite_router_id: str = None,
        opposite_router_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role: str = None,
        router_id: str = None,
        router_type: str = None,
        spec: str = None,
        tags: List[main_models.CreateRouterInterfaceRequestTags] = None,
    ):
        # The ID of the access point to which the VBR belongs.
        # 
        # You can call the [DescribeAccessPoints](https://help.aliyun.com/document_detail/36062.html) operation to obtain the IDs of access points.
        # 
        # >  This parameter is required if the VBR is connected to an Express Connect circuit.
        self.access_point_id = access_point_id
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **false** (default): The automatic payment is disabled. If you select this option, you must go to the Order Center to complete the payment after an order is generated.
        # *   **true**: The automatic payment is enabled. Payments are automatically complete after an order is generated.
        # 
        # >  This parameter is required if **InstanceChargeType** is set to **PrePaid**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.auto_renew = auto_renew
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description of the router interface.
        # 
        # The description must be 2 to 256 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether the VBR that is created in the Fast Link mode is uplinked to the router interface. The Fast Link mode helps automatically connect router interfaces that are created for the VBR and its peer VPC. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > 
        # 
        # *   This parameter takes effect only if **RouterType** is set to **VBR** and **OppositeRouterType** is set to **VRouter**.
        # 
        # *   If **FastLinkMode** is set to **true**, **Role** must be set to **InitiatingSide**. In this case, **AccessPointId**, **OppositeRouterType**, **OpppsiteRouterId**, and **OppositeInterfaceOwnerId** are required.
        self.fast_link_mode = fast_link_mode
        # The source IP address that is used to perform health checks. The source IP address must be an idle IP address of the local virtual private cloud (VPC).
        # 
        # >  You can set this parameter when an Express Connect circuit is used.
        self.health_check_source_ip = health_check_source_ip
        # The destination IP address that is used to perform health checks.
        # 
        # >  This parameter is required if you specify **HealthCheckSourceIp**
        self.health_check_target_ip = health_check_target_ip
        # The billing method of the router interface. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The name of the router interface.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The ID of the access point to which the peer belongs.
        # 
        # >  This parameter is required if the peer router interface is associated with a VBR. The specified value cannot be changed after the router interface is created.
        self.opposite_access_point_id = opposite_access_point_id
        # The ID of the peer router interface.
        self.opposite_interface_id = opposite_interface_id
        # The ID of the Alibaba Cloud account to which the peer router interface belongs.
        self.opposite_interface_owner_id = opposite_interface_owner_id
        # The ID of the region in which the acceptor is deployed.
        # 
        # This parameter is required.
        self.opposite_region_id = opposite_region_id
        # The ID of the peer router.
        self.opposite_router_id = opposite_router_id
        # The type of router that is associated with the peer router interface. Valid values:
        # 
        # *   **VRouter**
        # *   **VBR**
        self.opposite_router_type = opposite_router_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration. Valid values:
        # 
        # *   Valid values when PricingCycle is set to Month: **1 to 9**.
        # *   Valid values when PricingCycle is set to Year: **1 to 3**.
        # 
        # >  This parameter is required if **InstanceChargeType** is set to **PrePaid**.
        self.period = period
        # The billing cycle of the subscription. Valid values:
        # 
        # *   **Month** (default)
        # *   **Year**
        # 
        # >  This parameter is required if **InstanceChargeType** is set to **PrePaid**.
        self.pricing_cycle = pricing_cycle
        # The ID of the region to which the router interface belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # For more information about resource group, see [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html)
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role of the router interface. Valid values:
        # 
        # *   **InitiatingSide**: requester
        # *   **AcceptingSide**: acceptor
        # 
        # This parameter is required.
        self.role = role
        # The ID of the router that is associated with the router interface.
        # 
        # This parameter is required.
        self.router_id = router_id
        # The type of router that is associated with the router interface. Valid values:
        # 
        # *   **VRouter**
        # *   **VBR**
        # 
        # This parameter is required.
        self.router_type = router_type
        # The specification of the router interface and the corresponding bandwidth. Valid values:
        # 
        # *   **Mini.2**: 2 Mbit/s
        # *   **Mini.5**: 5 Mbit/s
        # *   **Small.1**: 10 Mbit/s
        # *   **Small.2**: 20 Mbit/s
        # *   **Small.5**: 50 Mbit/s
        # *   **Middle.1**: 100 Mbit/s
        # *   **Middle.2**: 200 Mbit/s
        # *   **Middle.5**: 500 Mbit/s
        # *   **Large.1**: 1,000 Mbit/s
        # *   **Large.2**: 2,000 Mbit/s
        # *   **Large.5**: 5,000 Mbit/s
        # *   **Xlarge.1**: 10,000 Mbit/s
        # 
        # >  If **Role** is set to **AcceptingSide**, set **Spec** to **Negative**. This indicates that you do not need to specify the specification when you create an acceptor router interface.
        # 
        # This parameter is required.
        self.spec = spec
        # The tag to add to the resource.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.fast_link_mode is not None:
            result['FastLinkMode'] = self.fast_link_mode

        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip

        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.name is not None:
            result['Name'] = self.name

        if self.opposite_access_point_id is not None:
            result['OppositeAccessPointId'] = self.opposite_access_point_id

        if self.opposite_interface_id is not None:
            result['OppositeInterfaceId'] = self.opposite_interface_id

        if self.opposite_interface_owner_id is not None:
            result['OppositeInterfaceOwnerId'] = self.opposite_interface_owner_id

        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id

        if self.opposite_router_id is not None:
            result['OppositeRouterId'] = self.opposite_router_id

        if self.opposite_router_type is not None:
            result['OppositeRouterType'] = self.opposite_router_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role is not None:
            result['Role'] = self.role

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.router_type is not None:
            result['RouterType'] = self.router_type

        if self.spec is not None:
            result['Spec'] = self.spec

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FastLinkMode') is not None:
            self.fast_link_mode = m.get('FastLinkMode')

        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')

        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OppositeAccessPointId') is not None:
            self.opposite_access_point_id = m.get('OppositeAccessPointId')

        if m.get('OppositeInterfaceId') is not None:
            self.opposite_interface_id = m.get('OppositeInterfaceId')

        if m.get('OppositeInterfaceOwnerId') is not None:
            self.opposite_interface_owner_id = m.get('OppositeInterfaceOwnerId')

        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')

        if m.get('OppositeRouterId') is not None:
            self.opposite_router_id = m.get('OppositeRouterId')

        if m.get('OppositeRouterType') is not None:
            self.opposite_router_type = m.get('OppositeRouterType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('RouterType') is not None:
            self.router_type = m.get('RouterType')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateRouterInterfaceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateRouterInterfaceRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key to add to the resource. You must enter at least one tag key. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be at most 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value to add to the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
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

