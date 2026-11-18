# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteMetricRulesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        id: List[str] = None,
        region_id: str = None,
    ):
        # Ensures the idempotence of the request. Generate a parameter value on your client to ensure that the value is unique across different requests. ClientToken supports only ASCII characters and can be up to 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # Specifies whether to perform a dry run only. Valid values:
        # - **true**: Sends a check request and does not bind the security group to the instance. The check items include whether required parameters are specified, the request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # - **false** (default): Sends a normal request. If the check succeeds, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The IDs of the alert rules to delete.
        # 
        # This parameter is required.
        self.id = id
        self.region_id = region_id

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

        if self.id is not None:
            result['Id'] = self.id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

