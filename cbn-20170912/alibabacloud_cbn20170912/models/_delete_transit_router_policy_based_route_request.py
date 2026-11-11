# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTransitRouterPolicyBasedRouteRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        policy_based_route_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, and you must ensure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the deletion request. The system checks items such as permissions and instance status. Valid values:
        # 
        # - **false** (default): sends a normal request. If the request passes the dry run, the policy-based routing rule is deleted.
        # - **true**: performs a dry run only and does not delete the policy-based routing rule. The system checks whether required parameters are specified and whether the request format is valid. If the request fails the dry run, an error is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        # The instance ID of the policy-based routing rule.
        # 
        # This parameter is required.
        self.policy_based_route_id = policy_based_route_id

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

        if self.policy_based_route_id is not None:
            result['PolicyBasedRouteId'] = self.policy_based_route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('PolicyBasedRouteId') is not None:
            self.policy_based_route_id = m.get('PolicyBasedRouteId')

        return self

