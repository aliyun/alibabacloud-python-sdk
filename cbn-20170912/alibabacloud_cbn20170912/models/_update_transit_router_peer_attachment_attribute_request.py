# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTransitRouterPeerAttachmentAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        bandwidth: int = None,
        bandwidth_type: str = None,
        cen_bandwidth_package_id: str = None,
        client_token: str = None,
        default_link_type: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_id: str = None,
        transit_router_attachment_name: str = None,
    ):
        # Specifies whether to allow the Enterprise Edition transit router to automatically advertise routes of the inter-region connection to the peer region.
        # 
        # - **false** (default): no.
        # - **true**: yes.
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The bandwidth value of the inter-region connection. Unit: Mbit/s.
        # 
        # - If **BandwidthType** is set to **BandwidthPackage**, this parameter specifies the bandwidth that the inter-region connection can use.
        # - If **BandwidthType** is set to **DataTransfer**, this parameter specifies the bandwidth limit of the inter-region connection.
        self.bandwidth = bandwidth
        # The bandwidth allocation method. Valid values:
        # 
        # - **BandwidthPackage**: allocates bandwidth from a bandwidth package.
        # - **DataTransfer**: does not allocate bandwidth to the inter-region connection. Billing is based on the traffic volume.
        self.bandwidth_type = bandwidth_type
        # The ID of the bandwidth package to be associated with the inter-region connection.
        # 
        # <props="china">If you do not specify a bandwidth package ID, the test bandwidth is used. The default test bandwidth is 1 Kbit/s and is intended only for testing (IPv4) network connectivity.
        # >If **BandwidthType** is set to **DataTransfer**, you do not need to configure this parameter.
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The default link type.
        # 
        # Valid values: Platinum and Gold. Default value: Gold.
        # 
        # The value can be set to Platinum only when the bandwidth allocation method is pay-by-data-transfer.
        self.default_link_type = default_link_type
        # Specifies whether to perform a dry run, including permission and instance status verification. Valid values:
        # 
        # - **false** (default): sends a normal request and directly modifies the configuration of the inter-region connection after the request passes the check.
        # - **true**: sends a check request. Only the check is performed and the configuration of the inter-region connection is not modified. The check items include whether required parameters are specified and the request format. If the check fails, the corresponding error is returned. If the check succeeds, the corresponding request ID is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The new description of the inter-region connection.
        # 
        # The description can be empty or 1 to 256 characters in length, and cannot start with http:// or https://.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The ID of the inter-region connection.
        # 
        # This parameter is required.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The new name of the inter-region connection.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.transit_router_attachment_name = transit_router_attachment_name

    def validate(self):
        pass

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')

        return self

