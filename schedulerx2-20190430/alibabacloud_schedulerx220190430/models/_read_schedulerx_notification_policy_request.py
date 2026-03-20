# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReadSchedulerxNotificationPolicyRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_name: str = None,
        region_id: str = None,
    ):
        # The maximum number of entries returned. Default value: 20.
        self.max_results = max_results
        # The cursor for pagination. Leave this parameter empty for the first request. When the returned value is empty, all data has been retrieved.
        self.next_token = next_token
        # The name of the notification policy. Supports fuzzy matching.
        self.policy_name = policy_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

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

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

