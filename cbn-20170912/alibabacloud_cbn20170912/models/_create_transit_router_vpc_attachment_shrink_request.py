# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateTransitRouterVpcAttachmentShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        cen_id: str = None,
        charge_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateTransitRouterVpcAttachmentShrinkRequestTag] = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_name: str = None,
        transit_router_id: str = None,
        transit_router_vpcattachment_options_shrink: str = None,
        vpc_id: str = None,
        vpc_owner_id: int = None,
        zone_mappings: List[main_models.CreateTransitRouterVpcAttachmentShrinkRequestZoneMappings] = None,
    ):
        # Specifies whether to enable the Enterprise Edition transit router to automatically advertise routes to VPCs. Valid values:
        # 
        # *   **false:** (default)
        # *   **true**
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The billing method. The default value is **POSTPAY**, which specifies the pay-as-you-go billing method.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **false** (default): performs a dry run and sends the request.
        # *   **true**: performs a dry run. The system checks the required parameters and request syntax. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the VPC is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The information about the tags.
        # 
        # You can specify at most 20 tags in each call.
        self.tag = tag
        # The description of the VPC connection.
        # 
        # The description must be 1 to 256 characters in length, and cannot start with http:// or https://. You can also leave this parameter empty.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The name of the VPC connection.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with http:// or https://. You can also leave this parameter empty.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The ID of the Enterprise Edition transit router.
        self.transit_router_id = transit_router_id
        # Feature configurations of the VPC connection.
        self.transit_router_vpcattachment_options_shrink = transit_router_vpcattachment_options_shrink
        # The VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the Alibaba Cloud account to which the VPC belongs. The default value is the ID of the current Alibaba Cloud account.
        # 
        # > If the network instance and CEN instance belong to different Alibaba Cloud accounts, this parameter is required.
        self.vpc_owner_id = vpc_owner_id
        # A zone that supports Enterprise Edition transit routers.
        # 
        # You can specify at most 10 zones.
        # 
        # This parameter is required.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.tag:
            for v1 in self.tag:
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if self.transit_router_vpcattachment_options_shrink is not None:
            result['TransitRouterVPCAttachmentOptions'] = self.transit_router_vpcattachment_options_shrink

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTransitRouterVpcAttachmentShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')

        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterVPCAttachmentOptions') is not None:
            self.transit_router_vpcattachment_options_shrink = m.get('TransitRouterVPCAttachmentOptions')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.CreateTransitRouterVpcAttachmentShrinkRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class CreateTransitRouterVpcAttachmentShrinkRequestZoneMappings(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # A vSwitch that is deployed in the zone that supports Enterprise Edition transit routers.
        # 
        # You can specify vSwitches for at most 10 zones in each call.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the zone that supports Enterprise Edition transit routers.
        # 
        # You can call the [DescribeZones](https://help.aliyun.com/document_detail/36064.html) operation to query the most recent zone list.
        # 
        # You can specify at most 10 zones in each call.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateTransitRouterVpcAttachmentShrinkRequestTag(DaraModel):
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

