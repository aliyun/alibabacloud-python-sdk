# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisassociateTransitRouterPolicyTableRequest(DaraModel):
    def __init__(
        self,
        association_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
    ):
        # The ID of the association between the transit router policy table and the network instance connection.
        # 
        # This parameter is required.
        self.association_id = association_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the request. Checks include permissions and instance status. Valid values:
        # 
        # - **false** (default): sends a normal request. If the request passes the check, the transit router policy table association is removed.
        # - **true**: sends a dry run request. The system only performs the check and does not remove the transit router policy table association. The system checks whether required parameters are specified and whether the request format is valid. If the request fails the check, an error is returned. If the request passes the check, the corresponding request ID is returned.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_id is not None:
            result['AssociationId'] = self.association_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        return self

