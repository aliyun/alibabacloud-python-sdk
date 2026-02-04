# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateTransitRouterPeerAttachmentRequest(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        bandwidth: int = None,
        bandwidth_type: str = None,
        cen_bandwidth_package_id: str = None,
        cen_id: str = None,
        client_token: str = None,
        default_link_type: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_transit_router_id: str = None,
        peer_transit_router_region_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateTransitRouterPeerAttachmentRequestTag] = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_name: str = None,
        transit_router_id: str = None,
    ):
        # Specifies whether to enable the local Enterprise Edition transit router to automatically advertise the routes of the inter-region connection to the peer transit router. Valid values:
        # 
        # *   **false** (default): no
        # *   **true**: yes
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The bandwidth value of the inter-region connection. Unit: Mbit/s.
        # 
        # *   This parameter specifies the maximum bandwidth value for the inter-region connection if you set **BandwidthType** to **BandwidthPackage**.
        # *   This parameter specifies the bandwidth throttling threshold for the inter-region connection if you set **BandwidthType** to **DataTransfer**.
        self.bandwidth = bandwidth
        # The method that is used to allocate bandwidth to the inter-region connection. Valid values:
        # 
        # *   **BandwidthPackage**: allocates bandwidth from a bandwidth plan.
        # *   **DataTransfer**: bandwidth is billed based on the pay-by-data-transfer metering method.
        self.bandwidth_type = bandwidth_type
        # The ID of the bandwidth plan that you want to associate with the inter-region connection.
        # 
        # >  If you set **BandwidthType** to **DataTransfer**, you can skip this parameter.
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The default line type.
        # 
        # Valid values: Platinum and Gold.
        # 
        # Platinum is supported only when BandwidthType is set to DataTransfer.
        self.default_link_type = default_link_type
        # Specifies whether to perform a dry run. Default values:
        # 
        # *   **false** (default): performs a dry run and sends the request.
        # *   **true**: performs a dry run. The system checks the required parameters and request syntax. If the request fails the dry run, an error message is returned. If the request passes the dry run, the system returns the ID of the request.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the peer transit router.
        # 
        # This parameter is required.
        self.peer_transit_router_id = peer_transit_router_id
        # The ID of the region where the peer transit router is deployed.
        self.peer_transit_router_region_id = peer_transit_router_region_id
        # The ID of the region where the local Enterprise Edition transit router is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The information about the tags.
        # 
        # You can specify at most 20 tags in each call.
        self.tag = tag
        # The description of the inter-region connection.
        # 
        # This parameter is optional. If you enter a description, it must be 1 to 256 characters in length, and cannot start with http:// or https://.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The name of the inter-region connection.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The ID of the local Enterprise Edition transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.default_link_type is not None:
            result['DefaultLinkType'] = self.default_link_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.peer_transit_router_id is not None:
            result['PeerTransitRouterId'] = self.peer_transit_router_id

        if self.peer_transit_router_region_id is not None:
            result['PeerTransitRouterRegionId'] = self.peer_transit_router_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description

        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DefaultLinkType') is not None:
            self.default_link_type = m.get('DefaultLinkType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeerTransitRouterId') is not None:
            self.peer_transit_router_id = m.get('PeerTransitRouterId')

        if m.get('PeerTransitRouterRegionId') is not None:
            self.peer_transit_router_region_id = m.get('PeerTransitRouterRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTransitRouterPeerAttachmentRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')

        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class CreateTransitRouterPeerAttachmentRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys.
        self.key = key
        # The tag value.
        # 
        # The tag value can be 0 to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # Each tag key must have a unique tag value. You can specify at most 20 tag values in each call.
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

