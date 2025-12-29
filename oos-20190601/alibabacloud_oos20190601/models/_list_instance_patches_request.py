# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancePatchesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        patch_statuses: str = None,
        region_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The number of entries to return on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The status of the patches that you want to query. If you do not set this parameter, patches are not filtered.
        self.patch_statuses = patch_statuses
        # The ID of the region in which the instance whose patches you want to query resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.patch_statuses is not None:
            result['PatchStatuses'] = self.patch_statuses

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PatchStatuses') is not None:
            self.patch_statuses = m.get('PatchStatuses')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

