# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTransitRouterVbrAttachmentAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_publish_route_enabled: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_attachment_description: str = None,
        transit_router_attachment_id: str = None,
        transit_router_attachment_name: str = None,
    ):
        # Specifies whether to allow the Enterprise Edition transit router to automatically forward routing entries to the VBR instance. Valid values:
        # 
        # - **true**: allowed.
        # - **false**: not allowed.
        self.auto_publish_route_enabled = auto_publish_route_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform a dry run, including permission and instance status verification. Valid values:
        # 
        # - **false** (default): sends a normal request. If the request passes the check, the name and description of the VBR connection are modified.
        # - **true**: sends a check request. Only the check is performed. If the check passes, the error code `DryRunOperation` is returned. If the check fails, the corresponding error is returned.
        self.dry_run = dry_run
        # The payer of the network instance. Valid values:
        # 
        # - **PayByCenOwner**: the connection fee and data transfer fee of the VBR instance are paid by the account to which the transit router instance belongs.
        # - **PayByResourceOwner**: the connection fee and data transfer fee of the VBR instance are paid by the account to which the VBR instance belongs.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The new description of the VBR connection.
        # 
        # The description can be empty or 1 to 256 characters in length, and cannot start with http:// or https://.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The ID of the VBR connection.
        # 
        # This parameter is required.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The new name of the VBR connection.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        return self

