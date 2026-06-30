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
        # The token that is used for the next query. Valid values:
        # 
        # - If **NextToken** is empty, it indicates that no next query is to be sent.
        # 
        # - If a value is returned for **NextToken**, the value is the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # A list of VPN connections.
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
        # Indicates whether the transit router automatically advertises routes to the IPsec-VPN connection. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The billing method of the VPN connection.
        # 
        # The value is set to POSTPAY, which indicates the pay-as-you-go billing method.
        self.charge_type = charge_type
        # The time when the VPN connection was created.
        # 
        # The time is displayed in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The party that pays for the network instance. Valid values:
        # 
        # - **PayByCenOwner**: The fees for the network instance are paid by the account that owns the CEN instance.
        # 
        # - **PayByResourceOwner**: The fees for the network instance are paid by the account that owns the network instance.
        self.order_type = order_type
        # The resource type of the VPN connection.
        # 
        # The value is set to **VPN**, which indicates that the transit router is connected to an IPsec-VPN connection.
        self.resource_type = resource_type
        # The status of the VPN connection.
        # 
        # - **Attached**: The VPN connection is attached.
        # 
        # - **Attaching**: The VPN connection is being attached.
        # 
        # - **Detaching**: The VPN connection is being detached.
        self.status = status
        # A list of tags.
        self.tags = tags
        # The description of the VPN connection.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The ID of the VPN connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The name of the VPN connection.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The ID of the transit router.
        self.transit_router_id = transit_router_id
        # The ID of the IPsec-VPN connection.
        self.vpn_id = vpn_id
        # The ID of the Alibaba Cloud account to which the IPsec-VPN connection belongs.
        self.vpn_owner_id = vpn_owner_id
        # The ID of the region where the IPsec-VPN connection is deployed.
        # 
        # For more information, see [DescribeRegions](https://help.aliyun.com/document_detail/36063.html).
        self.vpn_region_id = vpn_region_id
        # A list of zones where the VPN connection is deployed.
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
        # For more information, see [DescribeZones](https://help.aliyun.com/document_detail/36064.html).
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

