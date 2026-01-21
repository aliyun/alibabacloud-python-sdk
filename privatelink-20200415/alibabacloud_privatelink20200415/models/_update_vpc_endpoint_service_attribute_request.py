# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateVpcEndpointServiceAttributeRequest(DaraModel):
    def __init__(
        self,
        add_supported_region_set: List[str] = None,
        address_ip_version: str = None,
        auto_accept_enabled: bool = None,
        client_token: str = None,
        connect_bandwidth: int = None,
        delete_supported_region_set: List[str] = None,
        dry_run: bool = None,
        region_id: str = None,
        service_description: str = None,
        service_id: str = None,
        service_support_ipv_6: bool = None,
        zone_affinity_enabled: bool = None,
    ):
        self.add_supported_region_set = add_supported_region_set
        # The protocol. Valid values:
        # 
        # *   **IPv4**
        # *   **DualStack**
        # 
        # >  You can set the protocol to DualStack only for endpoint services whose backend resource type is NLB.
        self.address_ip_version = address_ip_version
        # Specifies whether to automatically accept endpoint connection requests. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_accept_enabled = auto_accept_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # The default maximum bandwidth of the endpoint connection. Unit: Mbit/s. Default value: **3072**.
        # 
        # Valid values: **100** to **10240**.
        # 
        # >  You can specify this parameter only if you specify Classic Load Balancer (CLB) instances or Application Load Balancer (ALB) instances as service resources.
        self.connect_bandwidth = connect_bandwidth
        self.delete_supported_region_set = delete_supported_region_set
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The region ID of the endpoint service.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the endpoint service.
        self.service_description = service_description
        # The endpoint service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # Specifies whether to enable IPv6. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.service_support_ipv_6 = service_support_ipv_6
        # Specifies whether to first resolve the domain name of the nearest endpoint that is associated with the endpoint service. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.zone_affinity_enabled = zone_affinity_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_supported_region_set is not None:
            result['AddSupportedRegionSet'] = self.add_supported_region_set

        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth

        if self.delete_supported_region_set is not None:
            result['DeleteSupportedRegionSet'] = self.delete_supported_region_set

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6

        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSupportedRegionSet') is not None:
            self.add_supported_region_set = m.get('AddSupportedRegionSet')

        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')

        if m.get('DeleteSupportedRegionSet') is not None:
            self.delete_supported_region_set = m.get('DeleteSupportedRegionSet')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')

        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')

        return self

