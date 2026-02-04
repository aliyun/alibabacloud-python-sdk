# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterVpnAttachmentsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_attachments: List[main_models.ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachments] = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If **NextToken** is not returned, it indicates that no additional results exist.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the VPN attachment.
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
                temp_model = main_models.ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachments()
                self.transit_router_attachments.append(temp_model.from_map(k1))

        return self

class ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachments(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        cen_id: str = None,
        charge_type: str = None,
        creation_time: str = None,
        order_type: str = None,
        resource_type: str = None,
        status: str = None,
        tags: List[main_models.ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsTags] = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_id: str = None,
        transit_router_attachment_name: str = None,
        transit_router_id: str = None,
        vpn_id: str = None,
        vpn_owner_id: int = None,
        vpn_region_id: str = None,
        zones: List[main_models.ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsZones] = None,
    ):
        # Indicates the transit router can automatically advertise routes to the IPsec connection. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The billing method of the VPN attachment.
        # 
        # Only POSTPAY may be returned, which is the default pay-as-you-go billing method.
        self.charge_type = charge_type
        # The time when the VPN connection was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The entity that pays the fees of the network instance. Valid values:
        # 
        # *   **PayByCenOwner**: the Alibaba Cloud account that owns the CEN instance.
        # *   **PayByResourceOwner**: the Alibaba Cloud account that owns the network instance.
        self.order_type = order_type
        # The type of resource attached to the transit router.
        # 
        # Only **VPN** may be returned, which indicates that an IPsec-VPN connection is attached to the transit router.
        self.resource_type = resource_type
        # The status of the VPN connection. Valid values:
        # 
        # *   **Attached**
        # *   **Attaching**
        # *   **Detaching**
        self.status = status
        # A list of tags.
        self.tags = tags
        # The description of the IPsec-VPN connection.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The ID of the VPN attachment.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The name of the VPN attachment.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The ID of the transit router.
        self.transit_router_id = transit_router_id
        # The ID of the IPsec-VPN connection.
        self.vpn_id = vpn_id
        # The ID of the Alibaba Cloud account to which the IPsec-VPN connection belongs.
        self.vpn_owner_id = vpn_owner_id
        # The ID of the region to which the IPsec-VPN connection belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        self.vpn_region_id = vpn_region_id
        # The zones in which the VPN attachment is deployed.
        self.zones = zones

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.order_type is not None:
            result['OrderType'] = self.order_type

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

        if self.vpn_id is not None:
            result['VpnId'] = self.vpn_id

        if self.vpn_owner_id is not None:
            result['VpnOwnerId'] = self.vpn_owner_id

        if self.vpn_region_id is not None:
            result['VpnRegionId'] = self.vpn_region_id

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('VpnId') is not None:
            self.vpn_id = m.get('VpnId')

        if m.get('VpnOwnerId') is not None:
            self.vpn_owner_id = m.get('VpnOwnerId')

        if m.get('VpnRegionId') is not None:
            self.vpn_region_id = m.get('VpnRegionId')

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsZones(DaraModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        # The zone ID.
        # 
        # You can call the [DescribeZones](https://help.aliyun.com/document_detail/36064.html) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsTags(DaraModel):
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

