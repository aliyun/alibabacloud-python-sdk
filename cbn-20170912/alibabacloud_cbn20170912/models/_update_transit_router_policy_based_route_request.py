# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTransitRouterPolicyBasedRouteRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        name: str = None,
        policy_based_route_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the value of this parameter on the client side. Make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The description of the policy-based routing rule.
        # 
        # The description can be empty or 1 to 256 characters in length. It cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform only a dry run on the request. Valid values:
        # - **true**: Performs only a dry run and does not update the policy-based routing rule. The system checks whether the required parameters are specified, the request format is valid, and the service limits are met. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): Performs a dry run and updates the policy-based routing rule if the request passes the dry run.
        self.dry_run = dry_run
        # The name of the policy-based routing rule.
        # 
        # The name can be empty or 1 to 128 characters in length. It cannot start with http:// or https://.
        self.name = name
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

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_based_route_id is not None:
            result['PolicyBasedRouteId'] = self.policy_based_route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyBasedRouteId') is not None:
            self.policy_based_route_id = m.get('PolicyBasedRouteId')

        return self

