# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListStackResourceDriftsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_drift_status: List[str] = None,
        stack_id: str = None,
    ):
        # The time when the resource drift detection operation was initiated.
        self.max_results = max_results
        # The type of the resource.
        self.next_token = next_token
        # The physical ID of the resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource properties as defined in the template, in JSON format.
        self.resource_drift_status = resource_drift_status
        # The ID of the stack.
        # 
        # This parameter is required.
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

