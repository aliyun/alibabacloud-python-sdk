# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRouterInterfaceAttributeRequest(DaraModel):
    def __init__(
        self,
        delete_health_check_ip: bool = None,
        description: str = None,
        hc_rate: int = None,
        hc_threshold: int = None,
        health_check_source_ip: str = None,
        health_check_target_ip: str = None,
        name: str = None,
        opposite_interface_id: str = None,
        opposite_interface_owner_id: int = None,
        opposite_router_id: str = None,
        opposite_router_type: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        router_interface_id: str = None,
    ):
        # Specifies whether to delete the health check IP addresses configured on the router interface. Valid values:
        # 
        # - **true**: Deletes the health check IP addresses.
        #  
        # - **false** (default): Does not delete the health check IP addresses.
        self.delete_health_check_ip = delete_health_check_ip
        # The description of the router interface. 
        # 
        # The description must be 2 to 256 characters in length and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`.
        self.description = description
        # The health check rate. Unit: milliseconds. Recommended value: **2000**. This parameter specifies the interval between consecutive probe packets sent during a health check.
        # 
        # In this example, **HcThreshold** is set to **8** and **HcRate** is set to **2000**. This means that during a health check, a probe packet is sent from **HealthCheckSourceIp** (the source IP address for health checks) to **HealthCheckTargetIp** (the destination IP address for health checks) every 2000 milliseconds. If 8 consecutive probe packets receive no response, the health check fails.
        self.hc_rate = hc_rate
        # The health check threshold. Unit: packets. Recommended value: **8**. This parameter specifies the number of probe packets sent during a health check.
        self.hc_threshold = hc_threshold
        # The source IP address for health checks. The IP address must be an unused IP address in the local VPC.
        # 
        # > You can specify this parameter in Express Connect circuit scenarios.
        self.health_check_source_ip = health_check_source_ip
        # The destination IP address for health checks. 
        # 
        # > This parameter is required if **HealthCheckSourceIp** is specified.
        self.health_check_target_ip = health_check_target_ip
        # The name of the router interface.
        # 
        # The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, underscores (_), and hyphens (-).
        self.name = name
        # The ID of the peer router interface.
        self.opposite_interface_id = opposite_interface_id
        # The ID of the account to which the peer router interface belongs.
        self.opposite_interface_owner_id = opposite_interface_owner_id
        # The ID of the peer router.
        self.opposite_router_id = opposite_router_id
        # The type of the router to which the peer router interface belongs. Valid values:
        # 
        # - **VRouter**: vRouter.
        # 
        # - **VBR** (default): Virtual Border Router.
        self.opposite_router_type = opposite_router_type
        self.owner_id = owner_id
        # The region ID of the router interface.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the router interface.
        # 
        # This parameter is required.
        self.router_interface_id = router_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_health_check_ip is not None:
            result['DeleteHealthCheckIp'] = self.delete_health_check_ip

        if self.description is not None:
            result['Description'] = self.description

        if self.hc_rate is not None:
            result['HcRate'] = self.hc_rate

        if self.hc_threshold is not None:
            result['HcThreshold'] = self.hc_threshold

        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip

        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip

        if self.name is not None:
            result['Name'] = self.name

        if self.opposite_interface_id is not None:
            result['OppositeInterfaceId'] = self.opposite_interface_id

        if self.opposite_interface_owner_id is not None:
            result['OppositeInterfaceOwnerId'] = self.opposite_interface_owner_id

        if self.opposite_router_id is not None:
            result['OppositeRouterId'] = self.opposite_router_id

        if self.opposite_router_type is not None:
            result['OppositeRouterType'] = self.opposite_router_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteHealthCheckIp') is not None:
            self.delete_health_check_ip = m.get('DeleteHealthCheckIp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HcRate') is not None:
            self.hc_rate = m.get('HcRate')

        if m.get('HcThreshold') is not None:
            self.hc_threshold = m.get('HcThreshold')

        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')

        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OppositeInterfaceId') is not None:
            self.opposite_interface_id = m.get('OppositeInterfaceId')

        if m.get('OppositeInterfaceOwnerId') is not None:
            self.opposite_interface_owner_id = m.get('OppositeInterfaceOwnerId')

        if m.get('OppositeRouterId') is not None:
            self.opposite_router_id = m.get('OppositeRouterId')

        if m.get('OppositeRouterType') is not None:
            self.opposite_router_type = m.get('OppositeRouterType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')

        return self

