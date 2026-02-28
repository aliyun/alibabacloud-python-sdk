# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class GetErResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.GetErResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # Information returned when the call fails
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.GetErResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetErResponseBodyContent(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        er_attachments: List[main_models.GetErResponseBodyContentErAttachments] = None,
        er_id: str = None,
        er_name: str = None,
        er_route_entrys: List[main_models.GetErResponseBodyContentErRouteEntrys] = None,
        er_route_maps: List[main_models.GetErResponseBodyContentErRouteMaps] = None,
        gmt_modified: str = None,
        master_zone_id: str = None,
        message: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.GetErResponseBodyContentTags] = None,
        tenant_id: str = None,
    ):
        # The time when the data address was created.
        self.create_time = create_time
        # Description
        self.description = description
        # Network instance information list
        self.er_attachments = er_attachments
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # Lingjun HUB Instance Name
        self.er_name = er_name
        # The list of route entry information.
        self.er_route_entrys = er_route_entrys
        # routing policy information list
        self.er_route_maps = er_route_maps
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # Primary Zone
        self.master_zone_id = master_zone_id
        # The message that is returned.
        self.message = message
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The status of the intervention entry. Valid value:
        self.status = status
        # List of Tags
        self.tags = tags
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        if self.er_attachments:
            for v1 in self.er_attachments:
                 if v1:
                    v1.validate()
        if self.er_route_entrys:
            for v1 in self.er_route_entrys:
                 if v1:
                    v1.validate()
        if self.er_route_maps:
            for v1 in self.er_route_maps:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        result['ErAttachments'] = []
        if self.er_attachments is not None:
            for k1 in self.er_attachments:
                result['ErAttachments'].append(k1.to_map() if k1 else None)

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.er_name is not None:
            result['ErName'] = self.er_name

        result['ErRouteEntrys'] = []
        if self.er_route_entrys is not None:
            for k1 in self.er_route_entrys:
                result['ErRouteEntrys'].append(k1.to_map() if k1 else None)

        result['ErRouteMaps'] = []
        if self.er_route_maps is not None:
            for k1 in self.er_route_maps:
                result['ErRouteMaps'].append(k1.to_map() if k1 else None)

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id

        if self.message is not None:
            result['Message'] = self.message

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.er_attachments = []
        if m.get('ErAttachments') is not None:
            for k1 in m.get('ErAttachments'):
                temp_model = main_models.GetErResponseBodyContentErAttachments()
                self.er_attachments.append(temp_model.from_map(k1))

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')

        self.er_route_entrys = []
        if m.get('ErRouteEntrys') is not None:
            for k1 in m.get('ErRouteEntrys'):
                temp_model = main_models.GetErResponseBodyContentErRouteEntrys()
                self.er_route_entrys.append(temp_model.from_map(k1))

        self.er_route_maps = []
        if m.get('ErRouteMaps') is not None:
            for k1 in m.get('ErRouteMaps'):
                temp_model = main_models.GetErResponseBodyContentErRouteMaps()
                self.er_route_maps.append(temp_model.from_map(k1))

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetErResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class GetErResponseBodyContentTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class GetErResponseBodyContentErRouteMaps(DaraModel):
    def __init__(
        self,
        action: str = None,
        create_time: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_map_id: str = None,
        er_route_map_name: str = None,
        gmt_modified: str = None,
        message: str = None,
        reception_instance_id: str = None,
        reception_instance_name: str = None,
        reception_instance_owner: str = None,
        reception_instance_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_map_num: int = None,
        status: str = None,
        tenant_id: str = None,
        transmission_instance_id: str = None,
        transmission_instance_name: str = None,
        transmission_instance_owner: str = None,
        transmission_instance_type: str = None,
    ):
        # Policy behavior
        # 
        # Valid value:
        # 
        # *   deny: rejects the.
        # *   permit: The allows.
        self.action = action
        # The time when the data address was created.
        self.create_time = create_time
        # Policy description
        self.description = description
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB ID
        self.er_id = er_id
        # routing policy ID
        self.er_route_map_id = er_route_map_id
        # The name of the routing policy.
        self.er_route_map_name = er_route_map_name
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The message that is returned.
        self.message = message
        # The ID of the destination instance.
        self.reception_instance_id = reception_instance_id
        # The name of the destination instance.
        self.reception_instance_name = reception_instance_name
        # The tenant to which the destination instance belongs.
        self.reception_instance_owner = reception_instance_owner
        # The type of the destination instance.
        self.reception_instance_type = reception_instance_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Policy sequence number (1001-2000)
        self.route_map_num = route_map_num
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The ID of the source instance.
        self.transmission_instance_id = transmission_instance_id
        # Source instance name
        self.transmission_instance_name = transmission_instance_name
        # The tenant to which the source instance belongs.
        self.transmission_instance_owner = transmission_instance_owner
        # The type of the source instance.
        self.transmission_instance_type = transmission_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id

        if self.er_route_map_name is not None:
            result['ErRouteMapName'] = self.er_route_map_name

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.message is not None:
            result['Message'] = self.message

        if self.reception_instance_id is not None:
            result['ReceptionInstanceId'] = self.reception_instance_id

        if self.reception_instance_name is not None:
            result['ReceptionInstanceName'] = self.reception_instance_name

        if self.reception_instance_owner is not None:
            result['ReceptionInstanceOwner'] = self.reception_instance_owner

        if self.reception_instance_type is not None:
            result['ReceptionInstanceType'] = self.reception_instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_map_num is not None:
            result['RouteMapNum'] = self.route_map_num

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.transmission_instance_id is not None:
            result['TransmissionInstanceId'] = self.transmission_instance_id

        if self.transmission_instance_name is not None:
            result['TransmissionInstanceName'] = self.transmission_instance_name

        if self.transmission_instance_owner is not None:
            result['TransmissionInstanceOwner'] = self.transmission_instance_owner

        if self.transmission_instance_type is not None:
            result['TransmissionInstanceType'] = self.transmission_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')

        if m.get('ErRouteMapName') is not None:
            self.er_route_map_name = m.get('ErRouteMapName')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ReceptionInstanceId') is not None:
            self.reception_instance_id = m.get('ReceptionInstanceId')

        if m.get('ReceptionInstanceName') is not None:
            self.reception_instance_name = m.get('ReceptionInstanceName')

        if m.get('ReceptionInstanceOwner') is not None:
            self.reception_instance_owner = m.get('ReceptionInstanceOwner')

        if m.get('ReceptionInstanceType') is not None:
            self.reception_instance_type = m.get('ReceptionInstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteMapNum') is not None:
            self.route_map_num = m.get('RouteMapNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TransmissionInstanceId') is not None:
            self.transmission_instance_id = m.get('TransmissionInstanceId')

        if m.get('TransmissionInstanceName') is not None:
            self.transmission_instance_name = m.get('TransmissionInstanceName')

        if m.get('TransmissionInstanceOwner') is not None:
            self.transmission_instance_owner = m.get('TransmissionInstanceOwner')

        if m.get('TransmissionInstanceType') is not None:
            self.transmission_instance_type = m.get('TransmissionInstanceType')

        return self

class GetErResponseBodyContentErRouteEntrys(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_entry_id: str = None,
        gmt_modified: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        route_type: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # The ID of the route entry.
        self.er_route_entry_id = er_route_entry_id
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # Route type
        self.route_type = route_type
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.er_route_entry_id is not None:
            result['ErRouteEntryId'] = self.er_route_entry_id

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id

        if self.route_type is not None:
            result['RouteType'] = self.route_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErRouteEntryId') is not None:
            self.er_route_entry_id = m.get('ErRouteEntryId')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')

        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class GetErResponseBodyContentErAttachments(DaraModel):
    def __init__(
        self,
        across: bool = None,
        auto_receive_all_route: bool = None,
        create_time: str = None,
        er_attachment_id: str = None,
        er_attachment_name: str = None,
        er_id: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        message: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Cross-account
        self.across = across
        # Receive all routes automatically
        self.auto_receive_all_route = auto_receive_all_route
        # The time when the data address was created.
        self.create_time = create_time
        # The connection ID of the Lingjun HUB network instance.
        self.er_attachment_id = er_attachment_id
        # Network Instance Name
        self.er_attachment_name = er_attachment_name
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The instance ID.
        self.instance_id = instance_id
        # The name of the ECU.
        self.instance_name = instance_name
        # Instance type: VPD and VCC
        # 
        # Valid value:
        # 
        # *   VCC: Lingjun Connection.
        # *   VPD: Lingjun network segment.
        self.instance_type = instance_type
        # The returned message.
        self.message = message
        # The synchronized region where the ECS instances are deployed.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.across is not None:
            result['Across'] = self.across

        if self.auto_receive_all_route is not None:
            result['AutoReceiveAllRoute'] = self.auto_receive_all_route

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.er_attachment_id is not None:
            result['ErAttachmentId'] = self.er_attachment_id

        if self.er_attachment_name is not None:
            result['ErAttachmentName'] = self.er_attachment_name

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.message is not None:
            result['Message'] = self.message

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Across') is not None:
            self.across = m.get('Across')

        if m.get('AutoReceiveAllRoute') is not None:
            self.auto_receive_all_route = m.get('AutoReceiveAllRoute')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErAttachmentId') is not None:
            self.er_attachment_id = m.get('ErAttachmentId')

        if m.get('ErAttachmentName') is not None:
            self.er_attachment_name = m.get('ErAttachmentName')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

