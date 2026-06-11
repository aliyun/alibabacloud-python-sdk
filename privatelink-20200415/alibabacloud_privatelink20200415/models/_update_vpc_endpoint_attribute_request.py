# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVpcEndpointAttributeRequest(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        client_token: str = None,
        cross_region_bandwidth: int = None,
        dry_run: bool = None,
        endpoint_description: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        policy_document: str = None,
        region_id: str = None,
        reset_policy: bool = None,
        zone_affinity_enabled: bool = None,
    ):
        # The protocol version. Valid values:
        # 
        # - **IPv4**: IPv4.
        # 
        # - **DualStack**: dual-stack.
        # 
        # > To enable dual-stack for an endpoint, the associated endpoint service and the endpoint\\"s VPC must also support dual-stack.
        self.address_ip_version = address_ip_version
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You must generate a unique value for this parameter. The token can contain only ASCII characters.
        self.client_token = client_token
        # The cross-region bandwidth in Mbps. This parameter applies only when the endpoint and its associated endpoint service are in different regions. Valid values:
        # 
        # - **Minimum value**: 100.
        # 
        # - **Maximum value**: The value is limited by your account quota. For more information, see [Quotas and limits](https://help.aliyun.com/zh/privatelink/quotas-and-limits?spm=a2c4g.11174283.help-menu-search-120462.d_0).
        # 
        # > You can specify this parameter only for cross-region endpoints.
        self.cross_region_bandwidth = cross_region_bandwidth
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Performs a dry run. The system checks the required parameters, request format, and service limits. If the request fails the check, the system returns an error message. If the request passes the check, the system returns the `DryRunOperation` error code.
        # 
        # - **false** (Default): Sends a normal request. If the request passes the check, the system performs the operation and returns a 2xx HTTP status code.
        self.dry_run = dry_run
        # The new description for the endpoint.
        # 
        # The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.endpoint_description = endpoint_description
        # The ID of the endpoint to modify.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The new name for the endpoint.
        # 
        # The name must be 2 to 128 characters in length, start with a letter or a Chinese character, and can contain digits, hyphens (-), and underscores (_).
        self.endpoint_name = endpoint_name
        # The RAM access policy. For more information, see [Basic elements of a RAM policy](https://help.aliyun.com/document_detail/93738.html).
        self.policy_document = policy_document
        # The region ID of the endpoint. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reset_policy = reset_policy
        # Specifies whether to enable zone affinity for domain name resolution of the endpoint service. Valid values:
        # 
        # - **true**: Enables zone affinity.
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
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cross_region_bandwidth is not None:
            result['CrossRegionBandwidth'] = self.cross_region_bandwidth

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reset_policy is not None:
            result['ResetPolicy'] = self.reset_policy

        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CrossRegionBandwidth') is not None:
            self.cross_region_bandwidth = m.get('CrossRegionBandwidth')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResetPolicy') is not None:
            self.reset_policy = m.get('ResetPolicy')

        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')

        return self

