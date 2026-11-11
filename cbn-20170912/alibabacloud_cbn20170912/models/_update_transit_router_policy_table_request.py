# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTransitRouterPolicyTableRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        name: str = None,
        policy_table_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The description of the policy route table.
        # 
        # The description can be empty or 1 to 256 characters in length. It cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform a dry run on the request, including checks on permissions and instance status. Valid values:
        # 
        # - **false** (default): sends a normal request. If the request passes the check, the policy route table is updated.
        # - **true**: sends a dry run request. Only the check is performed, and the policy route table is not updated. Check items include whether required parameters are specified and the request format. If the check fails, an error is returned. If the check passes, the request ID is returned.
        self.dry_run = dry_run
        # The name of the policy route table.
        # 
        # The name can be empty or 1 to 128 characters in length. It cannot start with http:// or https://.
        self.name = name
        # The instance ID of the policy routing table.
        # 
        # This parameter is required.
        self.policy_table_id = policy_table_id

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

        if self.policy_table_id is not None:
            result['PolicyTableId'] = self.policy_table_id

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

        if m.get('PolicyTableId') is not None:
            self.policy_table_id = m.get('PolicyTableId')

        return self

