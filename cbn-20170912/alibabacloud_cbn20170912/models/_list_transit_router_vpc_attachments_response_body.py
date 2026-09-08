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
        # The number of entries per page for a paged query.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If **NextToken** is empty, no next query exists.
        # - If **NextToken** is returned, the value indicates the token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The list of VPC connections.
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
        options: main_models.ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsOptions = None,
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
        # Indicates whether the Enterprise Edition transit router automatically publishes route entries to the VPC instance.
        # 
        # - **false**: The forward router does not automatically publish route entries.
        # - **true**: The forward router automatically publishes route entries.
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The CEN instance ID.
        self.cen_id = cen_id
        # The billing type of the VPC connection.
        # 
        # The value is **POSTPAY**, which indicates pay-as-you-go.
        self.charge_type = charge_type
        # The time when the VPC connection was created.
        # 
        # The time is displayed in the ISO 8601 standard in UTC. Format: YYYY-MM-DDThh:mmZ.
        self.creation_time = creation_time
        # The cloud service to which the connection belongs.
        self.managed_service = managed_service
        # The collection of feature attributes.
        self.options = options
        # The payer of the network instance. Valid values:
        # 
        # - **PayByCenOwner**: The fees generated by the network instance are paid by the account that owns the CEN instance.
        # - **PayByResourceOwner**: The fees generated by the network instance are paid by the account that owns the network instance.
        self.order_type = order_type
        # The resource type of the connection.
        # 
        # The value is **VPC**, which indicates a VPC instance.
        self.resource_type = resource_type
        # The status of the VPC connection.
        # 
        # - **Attached**: attached.
        # - **Attaching**: being attached.
        # - **Detaching**: being detached.
        self.status = status
        # The tag information.
        self.tags = tags
        # The description of the VPC connection.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The VPC connection ID.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The name of the VPC connection.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The Enterprise Edition transit router instance ID.
        self.transit_router_id = transit_router_id
        # The list of feature attributes of the VPC connection (to be deprecated. Use the new parameter Options instead).
        self.transit_router_vpcattachment_options = transit_router_vpcattachment_options
        # The VPC instance ID.
        self.vpc_id = vpc_id
        # The ID of the account that owns the VPC instance.
        self.vpc_owner_id = vpc_owner_id
        # The region ID of the VPC instance.
        self.vpc_region_id = vpc_region_id
        # The zone information of the VPC connection and the vSwitch and network interface controller (NIC) information of the associated VPC instance that are active for forwarding and routing traffic.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.options:
            self.options.validate()
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

        if self.options is not None:
            result['Options'] = self.options.to_map()

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

        if m.get('Options') is not None:
            temp_model = main_models.ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsOptions()
            self.options = temp_model.from_map(m.get('Options'))

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
        # The ID of the network interface controller (NIC) that the Enterprise Edition transit router created in the vSwitch for forwarding and routing traffic.
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

class ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsOptions(DaraModel):
    def __init__(
        self,
        appliance_mode_support: str = None,
        ipv_6support: str = None,
    ):
        # Indicates whether the appliance mode is enabled.
        # 
        # - **disable** (default): No.
        # - **enable**: Yes.
        self.appliance_mode_support = appliance_mode_support
        # Indicates whether IPv6 is supported.
        # 
        # - **disable** (default): No.
        # - **enable**: Yes.
        self.ipv_6support = ipv_6support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appliance_mode_support is not None:
            result['ApplianceModeSupport'] = self.appliance_mode_support

        if self.ipv_6support is not None:
            result['Ipv6Support'] = self.ipv_6support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplianceModeSupport') is not None:
            self.appliance_mode_support = m.get('ApplianceModeSupport')

        if m.get('Ipv6Support') is not None:
            self.ipv_6support = m.get('Ipv6Support')

        return self

