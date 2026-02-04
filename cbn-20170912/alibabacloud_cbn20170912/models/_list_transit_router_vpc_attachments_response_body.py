# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterVpcAttachmentsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_attachments: List[main_models.ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachments] = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If **NextToken** is returned, it indicates that no additional results exist.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The ID of the region.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the VPC connection.
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
                temp_model = main_models.ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachments()
                self.transit_router_attachments.append(temp_model.from_map(k1))

        return self

class ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachments(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        cen_id: str = None,
        charge_type: str = None,
        creation_time: str = None,
        managed_service: str = None,
        order_type: str = None,
        resource_type: str = None,
        status: str = None,
        tags: List[main_models.ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsTags] = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_id: str = None,
        transit_router_attachment_name: str = None,
        transit_router_id: str = None,
        transit_router_vpcattachment_options: Dict[str, str] = None,
        vpc_id: str = None,
        vpc_owner_id: int = None,
        vpc_region_id: str = None,
        zone_mappings: List[main_models.ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsZoneMappings] = None,
    ):
        # Indicates whether the Enterprise Edition transit router can automatically advertise routes to the VPC. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The billing method of the VPC connection.
        # 
        # Only **POSTPAY** may be returned, which indicates the default pay-as-you-go billing method.
        self.charge_type = charge_type
        # The time when the VPC connection was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        self.managed_service = managed_service
        # The entity that pays the fees of the network instance. Valid values:
        # 
        # *   **PayByCenOwner**: the Alibaba Cloud account that owns the CEN instance.
        # *   **PayByResourceOwner**: the Alibaba Cloud account that owns the network instance.
        self.order_type = order_type
        # The type of resource to which the transit router is connected.
        # 
        # Only **VPC** may be returned, which indicates VPCs.
        self.resource_type = resource_type
        # The status of the VPC connection. Valid values:
        # 
        # *   **Attached**
        # *   **Attaching**
        # *   **Detaching**
        self.status = status
        # The tags.
        self.tags = tags
        # The description of the VPC connection.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The VPC connection ID.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The name of the VPC connection.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The description of the Enterprise Edition transit router.
        self.transit_router_id = transit_router_id
        # The features of the VPC connection.
        self.transit_router_vpcattachment_options = transit_router_vpcattachment_options
        # The VPC ID.
        self.vpc_id = vpc_id
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.vpc_owner_id = vpc_owner_id
        # The region ID of the VPC.
        self.vpc_region_id = vpc_region_id
        # The primary and secondary zones, vSwitches, and ENIs of the VPC.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.zone_mappings:
            for v1 in self.zone_mappings:
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

        if self.managed_service is not None:
            result['ManagedService'] = self.managed_service

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

        if self.transit_router_vpcattachment_options is not None:
            result['TransitRouterVPCAttachmentOptions'] = self.transit_router_vpcattachment_options

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k1 in self.zone_mappings:
                result['ZoneMappings'].append(k1.to_map() if k1 else None)

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

        if m.get('ManagedService') is not None:
            self.managed_service = m.get('ManagedService')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterVPCAttachmentOptions') is not None:
            self.transit_router_vpcattachment_options = m.get('TransitRouterVPCAttachmentOptions')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsZoneMappings(DaraModel):
    def __init__(
        self,
        network_interface_id: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the ENI created by the Enterprise Edition transit router in the vSwitch.
        self.network_interface_id = network_interface_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsTags(DaraModel):
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

