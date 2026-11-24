# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ActivateFlowLogRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_id: str = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the value from your client to ensure that the value is unique among different requests. The ClientToken parameter supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId of each API request may be different.
        self.client_token = client_token
        # Specifies whether it is a dry run for this request. Valid values:
        # - **true**: sends a check request without modifying any EPS resource.
        # - **false** (default): sends a normal request.
        self.dry_run = dry_run
        # The Express Connect Router (ECR) instance ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The flow log instance ID.
        # > The flow log must be in the DEACTIVATE state. After you invoke the DeactivateFlowLog operation, the flow log enters the DEACTIVATING transitional state. You must invoke the DescribeFlowLogs operation for polling and wait until the state changes to DEACTIVATE before you invoke this operation.
        # 
        # This parameter is required.
        self.flow_log_id = flow_log_id
        self.version = version

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

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

