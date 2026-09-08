# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTransitRouterEcrAttachmentAttributeRequest(DaraModel):
    def __init__(
        self,
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
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run for this modification request, including permission and instance status checks. Valid values:
        # 
        # - **false** (default): Sends a normal request. If the request passes the check, the transit router instance information is directly modified.
        # - **true**: Sends a check request. Only the validation is performed, and the transit router instance information is not modified. The check items include whether required parameters are specified and the request format. If the check fails, the corresponding error is returned. If the check passes, the corresponding request ID is returned.
        self.dry_run = dry_run
        # The payer of the network instance. The payer of the ECR connection cannot be modified.
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The new description of the ECR connection.
        # 
        # The description can be empty or 1 to 256 characters in length and cannot start with http:// or https://.
        self.transit_router_attachment_description = transit_router_attachment_description
        # The ID of the ECR connection.
        # 
        # This parameter is required.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The new name of the ECR connection.
        # 
        # The name can be empty or 1 to 128 characters in length and cannot start with http:// or https://.
        self.transit_router_attachment_name = transit_router_attachment_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

