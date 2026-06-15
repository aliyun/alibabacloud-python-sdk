# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRouterInterfaceRequest(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        auto_pay: bool = None,
        client_token: str = None,
        description: str = None,
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
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role: str = None,
        router_id: str = None,
        router_type: str = None,
        spec: str = None,
        user_cidr: str = None,
    ):
        # The access point ID.
        self.access_point_id = access_point_id
        # Specifies whether to enable automatic payment. Valid values are `true` and `false`. The default value is `true`.
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the router interface. The description must be 2 to 256 characters long, must start with a letter, and cannot start with `http://` or `https://`.
        self.description = description
        # The source IP address that is used for the health check.
        self.health_check_source_ip = health_check_source_ip
        # The destination IP address that is used for the health check.
        self.health_check_target_ip = health_check_target_ip
        # The billing method of the instance. Set the value to `PrePaid`. This parameter is required if you also specify `PricingCycle`.
        self.instance_charge_type = instance_charge_type
        # The name of the router interface. The name must be 2 to 128 characters long and start with a letter. It can contain letters, digits, underscores (_), and hyphens (-).
        self.name = name
        # The ID of the peer access point.
        self.opposite_access_point_id = opposite_access_point_id
        # The ID of the peer router interface.
        self.opposite_interface_id = opposite_interface_id
        # The ID of the account to which the peer router interface belongs.
        self.opposite_interface_owner_id = opposite_interface_owner_id
        # The ID of the peer region.
        # 
        # This parameter is required.
        self.opposite_region_id = opposite_region_id
        # The ID of the peer router. This parameter is available only when the local and peer router interfaces belong to the same account.
        self.opposite_router_id = opposite_router_id
        # The type of the peer router. Valid values:
        # 
        # - **VRouter**
        # - **VBR**
        # 
        # Default value: **VRouter**.
        self.opposite_router_type = opposite_router_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration. This parameter is required when `InstanceChargeType` is set to `PrePaid` and `PricingCycle` is set to `Month` or `Year`. Valid values:
        # 
        # - If `PricingCycle` is set to `Month`, the valid values are 1 to 9.
        # - If `PricingCycle` is set to `Year`, the valid values are 1 to 3.
        self.period = period
        # The billing cycle. This parameter is required if `InstanceChargeType` is set to `PrePaid`. Valid values are `Month` and `Year`.
        self.pricing_cycle = pricing_cycle
        # The region ID of the router interface.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role of the router interface in the peering connection. Valid values:
        # 
        # - **InitiatingSide**: The router interface is the initiator.
        # - **AcceptingSide**: The router interface is the acceptor.
        # 
        # This parameter is required.
        self.role = role
        # The router ID.
        # 
        # This parameter is required.
        self.router_id = router_id
        # The router type. Valid values:
        # 
        # - **VRouter**
        # - **VBR**
        # 
        # This parameter is required.
        self.router_type = router_type
        # The specification of the router interface. Valid values:
        # 
        # - **Mini.2**
        # - **Mini.5**
        # - **Small.1**
        # - **Small.2**
        # - **Small.5**
        # - **Middle.1**
        # - **Middle.2**
        # - **Middle.5**
        # - **Large.1**
        # - **Large.2**
        # - **Large.5**
        # - **Xlarge.1**
        # 
        # This parameter is required.
        self.spec = spec
        # The CIDR block of the user. This parameter is required when you create a router interface for a virtual border router (VBR) that is in the same region as the Express Connect circuit, or when both `RouterType` and `OppositeRouterType` are set to `VBR`.
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

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

        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

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

        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')

        return self

