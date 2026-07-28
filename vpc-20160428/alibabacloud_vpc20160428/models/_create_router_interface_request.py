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
        # You can call the [DescribeAccessPoints](https://help.aliyun.com/document_detail/36062.html) operation to query the access point ID of the Express Connect circuit.  
        #           
        # > This parameter is required in Express Connect circuit scenarios.
        self.access_point_id = access_point_id
        # Specifies whether to enable automatic payment. Valid values: 
        #           
        # - **false** (default): Automatic payment is disabled. After an order is generated, go to the Order Center to complete the payment.   
        # 
        # - **true**: Automatic payment is enabled. The order is automatically paid.   
        # 
        # > This parameter is required when **InstanceChargeType** is set to **PrePaid**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **false** (default): Auto-renewal is disabled.
        # - **true**: Auto-renewal is enabled.
        self.auto_renew = auto_renew
        # The client token that is used to ensure the idempotence of the request. 
        # 
        # The client generates the value of this parameter. Ensure that the value is unique among different requests. 
        # 
        # > If you do not specify this parameter, the system uses the RequestId of the API request as the ClientToken. The RequestId may be different for each API request.
        self.client_token = client_token
        # The description of the router interface.  
        # 
        # The description must be 2 to 256 characters in length and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether the router interface on the VBR is created in fast link mode. Fast link mode allows the router interfaces on the VBR and VPC to be automatically connected after they are created. Valid values:
        # 
        # - **true**: yes.
        # - **false** (default): no.
        # 
        # > - This parameter takes effect only when **RouterType** is set to **VBR** and **OppositeRouterType** is set to **VRouter**.
        # > - When **FastLinkMode** is set to **true**, **Role** must be set to **InitiatingSide**, and **AccessPointId**, **OppositeRouterType**, **OppositeRouterId**, and **OppositeInterfaceOwnerId** are required.
        self.fast_link_mode = fast_link_mode
        # The source IP address for health checks. The IP address must be an unused IP address in the local VPC. 
        # 
        # > You can specify this parameter in Express Connect circuit scenarios.
        self.health_check_source_ip = health_check_source_ip
        # The destination IP address for health checks. 
        # 
        # > This parameter is required when **HealthCheckSourceIp** is specified.
        self.health_check_target_ip = health_check_target_ip
        # The billing method of the router interface. Valid values: 
        # 
        # - **PrePaid**: subscription.
        # 
        # - **PostPaid**: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The name of the router interface.  
        # 
        # The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The ID of the access point to which the peer belongs.
        # 
        # > This parameter is required when the peer router interface is on a VBR. This parameter cannot be modified after the router interface is created.
        self.opposite_access_point_id = opposite_access_point_id
        # The ID of the peer router interface.
        self.opposite_interface_id = opposite_interface_id
        # The Alibaba Cloud account ID of the owner of the peer router interface.
        self.opposite_interface_owner_id = opposite_interface_owner_id
        # The region ID of the accepter.
        # 
        # This parameter is required.
        self.opposite_region_id = opposite_region_id
        # The ID of the peer router.
        self.opposite_router_id = opposite_router_id
        # The type of the router associated with the peer router interface. Valid values: 
        # 
        # - **VRouter**: vRouter.
        # 
        # - **VBR**: Virtual Border Router.
        self.opposite_router_type = opposite_router_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration. Valid values: 
        # 
        # - If you select monthly billing, the valid values are **1** to **9**.
        # 
        # - If you select yearly billing, the valid values are **1** to **3**.
        # 
        # > This parameter is required when **InstanceChargeType** is set to **PrePaid**.
        self.period = period
        # The billing cycle of the subscription. Valid values:
        # 
        # - **Month** (default): monthly billing.
        # 
        # - **Year**: yearly billing.
        # 
        # > This parameter is required when **InstanceChargeType** is set to **PrePaid**.
        self.pricing_cycle = pricing_cycle
        # The region ID of the router interface.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # For more information about resource groups, see [What is a resource group?](https://help.aliyun.com/document_detail/2381067.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role of the router interface. Valid values: 
        #   
        # - **InitiatingSide**: requester.   
        # 
        # - **AcceptingSide**: accepter.
        # 
        # This parameter is required.
        self.role = role
        # The ID of the router associated with the router interface.
        # 
        # This parameter is required.
        self.router_id = router_id
        # The type of the router associated with the router interface. Valid values: 
        # 
        # - **VRouter**: vRouter.
        # 
        # - **VBR**: Virtual Border Router.
        # 
        # This parameter is required.
        self.router_type = router_type
        # The specification of the router interface. The available specifications and corresponding bandwidth values are as follows: 
        #           
        # - **Mini.2**: 2 Mbps   
        # 
        # - **Mini.5**: 5 Mbps   
        # 
        # - **Small.1**: 10 Mbps   
        # 
        # - **Small.2**: 20 Mbps   
        #  
        # - **Small.5**: 50 Mbps   
        # 
        # - **Middle.1**: 100 Mbps   
        # 
        # - **Middle.2**: 200 Mbps   
        # 
        # - **Middle.5**: 500 Mbps   
        # 
        # - **Large.1**: 1000 Mbps   
        # 
        # - **Large.2**: 2000 Mbps   
        # 
        # - **Large.5**: 5000 Mbps   
        # 
        # - **Xlarge.1**: 10000 Mbps  
        # 
        # > When **Role** is set to **AcceptingSide** (accepter), set **Spec** to **Negative**. No specification is required when you create an accepter router interface.
        # 
        # This parameter is required.
        self.spec = spec
        # The tags of the resource.
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
        # The tag key of the resource. You must specify at least 1 and can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

