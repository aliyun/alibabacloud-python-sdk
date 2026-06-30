# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTransitRouterVpcAttachmentAttributeShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        options_shrink: str = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_id: str = None,
        transit_router_attachment_name: str = None,
        transit_router_vpcattachment_options_shrink: str = None,
    ):
        # Specifies whether to allow the Enterprise Edition transit router to automatically advertise routes to the VPC.
        # 
        # - **false**: The transit router does not automatically advertise routes.
        # 
        # - **true**: The transit router automatically advertises routes.
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the token from your client, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **ClientToken**. The **RequestId** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run, which checks for issues such as permissions and instance status. Valid values:
        # 
        # - **false** (default): sends a normal request. After the request passes the check, the system modifies the name and description of the VPC connection.
        # 
        # - **true**: sends a check request. The system validates the request without modifying the VPC connection. If the check passes, the system returns the ID of the request. Otherwise, the system returns an error.
        self.dry_run = dry_run
        # The billing method.
        self.options_shrink = options_shrink
        # The billing method.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The new description of the VPC connection.
        # 
        # The description can be empty or 1 to 256 characters in length, and cannot start with http\\:// or https\\://.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The ID of the VPC connection.
        # 
        # This parameter is required.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The new name of the VPC connection.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http\\:// or https\\://.
        self.transit_router_attachment_name = transit_router_attachment_name
        # The feature properties of the VPC connection. This parameter is deprecated. We recommend that you use the `Options` parameter.
        self.transit_router_vpcattachment_options_shrink = transit_router_vpcattachment_options_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.options_shrink is not None:
            result['Options'] = self.options_shrink

        if self.order_type is not None:
            result['OrderType'] = self.order_type

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

        if self.transit_router_vpcattachment_options_shrink is not None:
            result['TransitRouterVPCAttachmentOptions'] = self.transit_router_vpcattachment_options_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Options') is not None:
            self.options_shrink = m.get('Options')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

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

        if m.get('TransitRouterVPCAttachmentOptions') is not None:
            self.transit_router_vpcattachment_options_shrink = m.get('TransitRouterVPCAttachmentOptions')

        return self

