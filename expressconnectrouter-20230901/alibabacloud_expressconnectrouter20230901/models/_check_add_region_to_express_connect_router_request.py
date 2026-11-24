# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAddRegionToExpressConnectRouterRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        fresh_region_id: str = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the parameter value on your client and ensure that the value is unique across different requests. The ClientToken parameter only supports ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform only a dry run on this request. Valid values:
        # 
        # - true: sends a check request and does not modify EPS resources.
        # 
        # - false: sends a normal request. This is the default value.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The region for which you want to check whether the Cloud Data Transfer (CDT) service is enabled for the Express Connect Router (ECR) feature.
        # 
        # This parameter is required.
        self.fresh_region_id = fresh_region_id
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

        if self.fresh_region_id is not None:
            result['FreshRegionId'] = self.fresh_region_id

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

        if m.get('FreshRegionId') is not None:
            self.fresh_region_id = m.get('FreshRegionId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

