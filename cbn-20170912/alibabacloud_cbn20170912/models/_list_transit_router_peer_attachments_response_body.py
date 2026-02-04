# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterPeerAttachmentsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_attachments: List[main_models.ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachments] = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If the **NextToken** parameter is empty, no next page exists.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # A list of inter-region connections.
        self.transit_router_attachments = transit_router_attachments

    def validate(self):
        if self.transit_router_attachments:
            for v1 in self.transit_router_attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TransitRouterAttachments'] = []
        if self.transit_router_attachments is not None:
            for k1 in self.transit_router_attachments:
                result['TransitRouterAttachments'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.transit_router_attachments = []
        if m.get('TransitRouterAttachments') is not None:
            for k1 in m.get('TransitRouterAttachments'):
                temp_model = main_models.ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachments()
                self.transit_router_attachments.append(temp_model.from_map(k1))

        return self

class ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachments(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        bandwidth: int = None,
        bandwidth_type: str = None,
        cen_bandwidth_package_id: str = None,
        cen_id: str = None,
        creation_time: str = None,
        default_link_type: str = None,
        geographic_span_id: str = None,
        peer_transit_router_id: str = None,
        peer_transit_router_owner_id: int = None,
        peer_transit_router_region_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        status: str = None,
        tags: List[main_models.ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachmentsTags] = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_id: str = None,
        transit_router_attachment_name: str = None,
        transit_router_id: str = None,
    ):
        # Indicates whether the local Enterprise Edition transit router automatically advertises routes of the cross-region connection to the peer transit router. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The bandwidth value of the inter-region connection. Unit: Mbit/s.
        # 
        # *   This parameter specifies the maximum bandwidth value for the inter-region connection if you set **BandwidthType** to **BandwidthPackage**.
        # *   This parameter specifies the bandwidth throttling threshold for the inter-region connection if you set **BandwidthType** to **DataTransfer**.
        self.bandwidth = bandwidth
        # The bandwidth allocation method. Valid values:
        # 
        # *   **BandwidthPackage**: allocates bandwidth from a bandwidth plan.
        # *   **DataTransfer**: bandwidth is billed based on the pay-by-data-transfer metering method.
        self.bandwidth_type = bandwidth_type
        # The ID of the bandwidth plan that is used to allocate bandwidth to the inter-region connection.
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        # The CEN instance ID.
        self.cen_id = cen_id
        # The time when the inter-region connection was created.
        # 
        # The time follows the ISO8601 standard in the `YYYY-MM-DDThh:mmZ` format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The default line type.
        # 
        # *   **Gold** (default)
        # *   **Platinum**
        self.default_link_type = default_link_type
        # The areas that are connected by the bandwidth plan.
        self.geographic_span_id = geographic_span_id
        # The ID of the peer transit router.
        self.peer_transit_router_id = peer_transit_router_id
        # The ID of the Alibaba Cloud account to which the peer transit router belongs.
        self.peer_transit_router_owner_id = peer_transit_router_owner_id
        # The region ID of the peer transit router.
        self.peer_transit_router_region_id = peer_transit_router_region_id
        # The region ID of the Enterprise Edition transit router.
        self.region_id = region_id
        # The type of the resource to which the transit router is connected. Valid values:
        # 
        # *   **VPC**: virtual private cloud (VPC)
        # *   **CCN**: Cloud Connect Network (CCN) instance
        # *   **VBR**: virtual border router (VBR)
        # *   **TR**: transit router
        self.resource_type = resource_type
        # The status of the inter-region connection. Valid values:
        # 
        # *   **Attached**
        # *   **Attaching**
        # *   **Detaching**
        # *   **Detached**
        self.status = status
        # A list of tags.
        self.tags = tags
        # The description of the inter-region connection.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The ID of the inter-region connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The name of the inter-region connection.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The ID of the Enterprise Edition transit router.
        self.transit_router_id = transit_router_id

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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.default_link_type is not None:
            result['DefaultLinkType'] = self.default_link_type

        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id

        if self.peer_transit_router_id is not None:
            result['PeerTransitRouterId'] = self.peer_transit_router_id

        if self.peer_transit_router_owner_id is not None:
            result['PeerTransitRouterOwnerId'] = self.peer_transit_router_owner_id

        if self.peer_transit_router_region_id is not None:
            result['PeerTransitRouterRegionId'] = self.peer_transit_router_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

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

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DefaultLinkType') is not None:
            self.default_link_type = m.get('DefaultLinkType')

        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')

        if m.get('PeerTransitRouterId') is not None:
            self.peer_transit_router_id = m.get('PeerTransitRouterId')

        if m.get('PeerTransitRouterOwnerId') is not None:
            self.peer_transit_router_owner_id = m.get('PeerTransitRouterOwnerId')

        if m.get('PeerTransitRouterRegionId') is not None:
            self.peer_transit_router_region_id = m.get('PeerTransitRouterRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachmentsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachmentsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

