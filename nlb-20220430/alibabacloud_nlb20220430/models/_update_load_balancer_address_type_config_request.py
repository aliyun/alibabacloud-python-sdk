# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class UpdateLoadBalancerAddressTypeConfigRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
        zone_mappings: List[main_models.UpdateLoadBalancerAddressTypeConfigRequestZoneMappings] = None,
    ):
        # The new network type. Valid values:
        # 
        # *   **Internet**: The nodes of an Internet-facing NLB instance have public IP addresses. The DNS name of an Internet-facing NLB instance is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing NLB instances can route requests from clients over the Internet.
        # *   **Intranet**: The nodes of an internal-facing NLB instance have only private IP addresses. The DNS name of an internal-facing NLB instance is publicly resolvable to the private IP addresses of the nodes. Therefore, internal-facing NLB instances can route requests only from clients with access to the virtual private cloud (VPC) for the NLB instance.
        # 
        # This parameter is required.
        self.address_type = address_type
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate this value. Ensure that the value is unique among all requests. Only ASCII characters are allowed.
        # 
        # >  If you do not specify this parameter, the value of **RequestId** is used.**** **RequestId** of each request is different.
        self.client_token = client_token
        # Perform a dry run without actually making the request. Valid values are:
        # 
        # *   **true**: Perform only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the check, an error message specifying the issue is returned. If the request passes, the `DryRunOperation` error code is returned.
        # *   **false** (default): Check the request and perform the operation. If the request passes the check, a 2xx HTTP status code is returned, and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # The mappings between zones and vSwitches. You can specify up to 10 zones.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.zone_mappings:
            for v1 in self.zone_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k1 in self.zone_mappings:
                result['ZoneMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.UpdateLoadBalancerAddressTypeConfigRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class UpdateLoadBalancerAddressTypeConfigRequestZoneMappings(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        eip_type: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the elastic IP address (EIP).
        self.allocation_id = allocation_id
        # The type of the EIP. Valid values:
        # 
        # *   **Common**: an EIP
        # *   **Anycast**: an Anycast EIP
        # 
        # >  This parameter is required only if **AddressType** is set to **Internet**.
        self.eip_type = eip_type
        # The ID of the vSwitch in the zone. You can specify only one vSwitch (subnet) in each zone of an NLB instance.
        self.v_switch_id = v_switch_id
        # The zone ID of the NLB instance.
        # 
        # You can call the [DescribeZones](https://help.aliyun.com/document_detail/443890.html) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.eip_type is not None:
            result['EipType'] = self.eip_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('EipType') is not None:
            self.eip_type = m.get('EipType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

