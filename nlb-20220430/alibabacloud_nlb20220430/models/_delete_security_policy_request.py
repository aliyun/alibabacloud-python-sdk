# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecurityPolicyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        security_policy_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a value for this parameter on your client to ensure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether to perform a dry run only. Valid values:
        # - **true**: sends a check request and does not delete the custom security policy. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the check fails, the system returns an error. If the check succeeds, the system returns the `DryRunOperation` error code.
        # - **false** (default): sends a regular request. If the check succeeds, the system returns an HTTP 2xx status code and performs the operation.
        self.dry_run = dry_run
        # The ID of the region where the Network Load Balancer (NLB) instance is deployed. 
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to obtain region IDs.
        self.region_id = region_id
        # The ID of the TLS security policy.
        # 
        # This parameter is required.
        self.security_policy_id = security_policy_id

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        return self

