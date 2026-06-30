# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTransitRouterPeerAttachmentRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        force: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_attachment_id: str = None,
    ):
        # A client token that is used to ensure the idempotence of the request.
        # 
        # Generate a token from your client to ensure that the token is unique among different requests. The ClientToken parameter can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the request as the **ClientToken**. The **RequestId** of each request is different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. A dry run checks permissions and the status of the instance. Valid values:
        # 
        # - **false** (default): sends the request. If the request passes the check, the inter-region connection is deleted.
        # 
        # - **true**: sends a check request. The system checks the required parameters and the request format. If the request fails the check, an error is returned. If the request passes the check, the corresponding request ID is returned. The inter-region connection is not deleted.
        self.dry_run = dry_run
        # Specifies whether to forcefully delete the inter-region connection. Valid values:
        # 
        # - **false** (default): checks for resource dependencies, such as associated forwarding and route learning, before deleting the inter-region connection. If dependencies exist, the deletion is not allowed and an error is returned.
        # 
        # - **true**: deletes all related dependencies when deleting the inter-region connection.
        self.force = force
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the inter-region connection.
        # 
        # This parameter is required.
        self.transit_router_attachment_id = transit_router_attachment_id

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

        if self.force is not None:
            result['Force'] = self.force

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        return self

