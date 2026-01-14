# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateDomainRequest(DaraModel):
    def __init__(
        self,
        accelerator_ids: List[str] = None,
        domain: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        # The ID of the GA instance.
        # 
        # You can enter up to 50 IDs.
        # 
        # This parameter is required.
        self.accelerator_ids = accelerator_ids
        # The accelerated domain name to be added.
        # 
        # Wildcard domain names are supported. A wildcard domain name must start with `*.`, such as `*.example.com`.
        # 
        # This parameter is required.
        self.domain = domain
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true:** performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, a 2xx HTTP status code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_ids is not None:
            result['AcceleratorIds'] = self.accelerator_ids

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorIds') is not None:
            self.accelerator_ids = m.get('AcceleratorIds')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

