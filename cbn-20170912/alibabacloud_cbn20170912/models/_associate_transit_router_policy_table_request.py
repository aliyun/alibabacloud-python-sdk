# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateTransitRouterPolicyTableRequest(DaraModel):
    def __init__(
        self,
        attachment_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        policy_table_id: str = None,
    ):
        # The ID of the network instance connection.
        # 
        # This parameter is required.
        self.attachment_id = attachment_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the value from your client. Make sure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the request. The dry run includes checks on permissions and instance status. Valid values:
        # 
        # - **false** (default): sends a normal request. The system performs the check and directly associates the policy route table if the check passes.
        # - **true**: sends a dry run request. The system only performs the check and does not associate the policy route table. Check items include whether required parameters are specified and the request format. If the check fails, an error is returned. If the check passes, the request ID is returned.
        self.dry_run = dry_run
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
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.policy_table_id is not None:
            result['PolicyTableId'] = self.policy_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('PolicyTableId') is not None:
            self.policy_table_id = m.get('PolicyTableId')

        return self

