# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDisabledExpressConnectRouterRouteEntriesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        next_token: str = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the parameter value from your client to ensure that the value is unique across different requests. The ClientToken parameter supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether the request is a dry run. Valid values:
        # 
        # - **true**: performs a dry run on the request without modifying the EPS resources.
        # 
        # - **false** (default): sends a normal request.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The maximum number of entries to return. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If this is the first query or no next query is required, you do not need to specify this parameter.
        # - If a next query is required, set the value to the NextToken value returned by the previous API call.
        self.next_token = next_token
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

