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
        # The remote regions to add to the list of supported regions.
        self.add_supported_region_set = add_supported_region_set
        # The IP version. Valid values:
        # 
        # - **IPv4**: IPv4.
        # 
        # - **DualStack**: dual-stack.
        # 
        # > Only endpoint services that use an NLB or GWLB instance as the service resource support the **DualStack** IP version.
        self.address_ip_version = address_ip_version
        # Specifies whether to automatically accept endpoint connections. Valid values:
        # 
        # - **true**: automatically accepts endpoint connections.
        # 
        # - **false**: does not automatically accept endpoint connections.
        self.auto_accept_enabled = auto_accept_enabled
        # A client-generated token that ensures the idempotence of the request.
        # 
        # Your client must generate a unique token for each request. **ClientToken** can contain only ASCII characters.
        self.client_token = client_token
        # The default maximum connection bandwidth. The default value is **3072**. Unit: Mbps.
        # 
        # Valid values: **100** to **10240**.
        # 
        # > You can set this parameter only if the service resource is a CLB or ALB instance, but not an NLB instance.
        self.connect_bandwidth = connect_bandwidth
        # The remote regions to remove from the list of supported regions.
        self.delete_supported_region_set = delete_supported_region_set
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the required parameters, request format, and service limits. If the request fails the dry run, the system returns an error message. If the request passes the dry run, the system returns the `DryRunOperation` error code.
        # 
        # - **false** (default): sends a normal request. If the request passes the check, the system returns a 2xx HTTP status code and performs the operation.
        self.dry_run = dry_run
        # The region ID of the endpoint service.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to get the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the endpoint service.
        self.service_description = service_description
        # The ID of the endpoint service.
        # 
        # This parameter is required.
        self.service_id = service_id
        # Specifies whether to enable IPv6 for the endpoint service. Valid values:
        # 
        # - **true**: Enables IPv6.
        # 
        # - **false** (default): Disables IPv6.
        self.service_support_ipv_6 = service_support_ipv_6
        # Specifies whether to enable zone affinity for the endpoint service. Valid values:
        # 
        # - **true** (default): Enables zone affinity.
        # 
        # - **false**: Disables zone affinity.
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

