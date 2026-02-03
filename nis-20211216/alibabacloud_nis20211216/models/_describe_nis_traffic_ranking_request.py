# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNisTrafficRankingRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        nis_traffic_ranking_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.nis_traffic_ranking_id = nis_traffic_ranking_id

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

        if self.nis_traffic_ranking_id is not None:
            result['NisTrafficRankingId'] = self.nis_traffic_ranking_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NisTrafficRankingId') is not None:
            self.nis_traffic_ranking_id = m.get('NisTrafficRankingId')

        return self

